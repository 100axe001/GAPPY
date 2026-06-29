"""
Gmail (and any IMAP/SMTP host) email access using an App Password.

Uses the Python standard library (imaplib / smtplib / email) so no extra
dependencies are needed. All blocking socket calls are run in a thread so they
don't block the FastAPI event loop.
"""
import imaplib
import smtplib
import email
import asyncio
import logging
from email.header import decode_header, make_header
from email.message import EmailMessage
from typing import Dict, Any, List

logger = logging.getLogger("lifeos.email")


class EmailNotConfigured(Exception):
    pass


def _require_creds(settings: Dict[str, str]):
    addr = settings.get("email_address") or ""
    pw = settings.get("email_app_password") or ""
    if not addr or not pw:
        raise EmailNotConfigured(
            "Email isn't configured. Add your address and a Gmail App Password in Settings."
        )
    return addr, pw


def _decode(value) -> str:
    if not value:
        return ""
    try:
        return str(make_header(decode_header(value)))
    except Exception:
        return str(value)


# ---- blocking implementations (run via asyncio.to_thread) ----

def _imap_search(settings: Dict[str, str], query: str, max_results: int) -> List[Dict[str, str]]:
    addr, pw = _require_creds(settings)
    host = settings.get("imap_host") or "imap.gmail.com"
    conn = imaplib.IMAP4_SSL(host)
    try:
        conn.login(addr, pw)
        conn.select("INBOX")
        if query and query.strip():
            safe = query.replace('"', "")
            typ, data = conn.search(None, "TEXT", f'"{safe}"')
        else:
            typ, data = conn.search(None, "ALL")
        ids = data[0].split() if data and data[0] else []
        ids = ids[-max_results:][::-1]  # newest first
        out: List[Dict[str, str]] = []
        for mid in ids:
            typ, msg_data = conn.fetch(mid, "(RFC822.HEADER)")
            if typ != "OK" or not msg_data or not msg_data[0]:
                continue
            msg = email.message_from_bytes(msg_data[0][1])
            out.append({
                "from": _decode(msg.get("From")),
                "subject": _decode(msg.get("Subject")) or "(no subject)",
                "date": _decode(msg.get("Date")),
            })
        return out
    finally:
        try:
            conn.logout()
        except Exception:
            pass


def _smtp_send(settings: Dict[str, str], to: str, subject: str, body: str) -> bool:
    addr, pw = _require_creds(settings)
    host = settings.get("smtp_host") or "smtp.gmail.com"
    port = int(settings.get("smtp_port") or 587)

    msg = EmailMessage()
    msg["From"] = addr
    msg["To"] = to
    msg["Subject"] = subject
    msg.set_content(body)

    server = smtplib.SMTP(host, port, timeout=30)
    try:
        server.starttls()
        server.login(addr, pw)
        server.send_message(msg)
        return True
    finally:
        try:
            server.quit()
        except Exception:
            pass


def _imap_test(settings: Dict[str, str]) -> bool:
    addr, pw = _require_creds(settings)
    host = settings.get("imap_host") or "imap.gmail.com"
    conn = imaplib.IMAP4_SSL(host)
    try:
        conn.login(addr, pw)
        return True
    finally:
        try:
            conn.logout()
        except Exception:
            pass


# ---- async wrappers ----

async def search_emails(settings: Dict[str, str], query: str = "", max_results: int = 8) -> List[Dict[str, str]]:
    return await asyncio.to_thread(_imap_search, settings, query, max_results)


async def send_email(settings: Dict[str, str], to: str, subject: str, body: str) -> bool:
    return await asyncio.to_thread(_smtp_send, settings, to, subject, body)


async def test_email(settings: Dict[str, str]) -> bool:
    try:
        return await asyncio.to_thread(_imap_test, settings)
    except Exception as e:
        logger.warning(f"Email connection test failed: {e}")
        return False
