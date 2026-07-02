#input_type_name: SendGmailInput
#output_type_name: SendGmailResult
#function_name: send_gmail

import base64
from email.message import EmailMessage
from typing import Optional
from pydantic import BaseModel
from lemma_sdk import FunctionContext, Pod

# Auth-config name provisioned for the native Gmail connector (see pod README / provision.py).
GMAIL_AUTH_CONFIG = "gmail-lifeos"


class SendGmailInput(BaseModel):
    to: str
    subject: str
    body: str
    auth_config: Optional[str] = None


class SendGmailResult(BaseModel):
    sent: bool
    detail: str


def _raw_mime(to: str, subject: str, body: str) -> str:
    msg = EmailMessage()
    msg["To"] = to
    msg["Subject"] = subject
    msg.set_content(body)
    return base64.urlsafe_b64encode(msg.as_bytes()).decode()


async def send_gmail(ctx: FunctionContext, data: SendGmailInput) -> SendGmailResult:
    """Send an approved email draft via the user's connected Gmail account.

    The native Gmail `messages_send` operation accepts either high-level fields or a raw
    RFC-822 message. We try the high-level shape first and fall back to a raw MIME payload.
    """
    pod = Pod.from_env()
    auth_config = data.auth_config or GMAIL_AUTH_CONFIG

    attempts = [
        {"recipient_email": data.to, "subject": data.subject, "body": data.body},
        {"to": data.to, "subject": data.subject, "body": data.body},
        {"raw": _raw_mime(data.to, data.subject, data.body)},
    ]

    last_err = ""
    for payload in attempts:
        try:
            res = pod.connectors.execute(auth_config, "messages_send", payload).to_dict()
            return SendGmailResult(sent=True, detail=str(res.get("result", res))[:500])
        except Exception as exc:  # noqa: BLE001 - surface the reason to the workflow
            last_err = str(exc)
            continue

    return SendGmailResult(sent=False, detail=f"send failed: {last_err}"[:500])
