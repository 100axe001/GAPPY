from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.draft import Draft
from ...models.gmail_users_drafts_update_alt import GmailUsersDraftsUpdateAlt
from ...models.gmail_users_drafts_update_xgafv import GmailUsersDraftsUpdateXgafv
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    user_id: str,
    id: str,
    *,
    body:    Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  | Unset = UNSET,
    xgafv: GmailUsersDraftsUpdateXgafv | Unset = UNSET,
    access_token: str | Unset = UNSET,
    alt: GmailUsersDraftsUpdateAlt | Unset = UNSET,
    callback: str | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    upload_protocol: str | Unset = UNSET,
    upload_type: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    json_xgafv: str | Unset = UNSET
    if not isinstance(xgafv, Unset):
        json_xgafv = xgafv.value

    params["$.xgafv"] = json_xgafv

    params["access_token"] = access_token

    json_alt: str | Unset = UNSET
    if not isinstance(alt, Unset):
        json_alt = alt.value

    params["alt"] = json_alt

    params["callback"] = callback

    params["fields"] = fields

    params["key"] = key

    params["oauth_token"] = oauth_token

    params["prettyPrint"] = pretty_print

    params["quotaUser"] = quota_user

    params["upload_protocol"] = upload_protocol

    params["uploadType"] = upload_type


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/gmail/v1/users/{user_id}/drafts/{id}".format(user_id=quote(str(user_id), safe=""),id=quote(str(id), safe=""),),
        "params": params,
    }

    if isinstance(body, Draft):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "message/cpim"
    if isinstance(body, Draft):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "message/delivery-status"
    if isinstance(body, Draft):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "message/disposition-notification"
    if isinstance(body, Draft):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "message/external-body"
    if isinstance(body, Draft):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "message/feedback-report"
    if isinstance(body, Draft):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "message/global"
    if isinstance(body, Draft):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "message/global-delivery-status"
    if isinstance(body, Draft):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "message/global-disposition-notification"
    if isinstance(body, Draft):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "message/global-headers"
    if isinstance(body, Draft):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "message/http"
    if isinstance(body, Draft):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "message/imdn+xml"
    if isinstance(body, Draft):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "message/news"
    if isinstance(body, Draft):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "message/partial"
    if isinstance(body, Draft):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "message/rfc822"
    if isinstance(body, Draft):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "message/s-http"
    if isinstance(body, Draft):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "message/sip"
    if isinstance(body, Draft):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "message/sipfrag"
    if isinstance(body, Draft):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "message/tracking-status"
    if isinstance(body, Draft):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "message/vnd.si.simp"
    if isinstance(body, Draft):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "message/vnd.wfa.wsc"
    if isinstance(body, Draft):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Draft | None:
    if response.status_code == 200:
        response_200 = Draft.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Draft]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body:    Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  | Unset = UNSET,
    xgafv: GmailUsersDraftsUpdateXgafv | Unset = UNSET,
    access_token: str | Unset = UNSET,
    alt: GmailUsersDraftsUpdateAlt | Unset = UNSET,
    callback: str | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    upload_protocol: str | Unset = UNSET,
    upload_type: str | Unset = UNSET,

) -> Response[Draft]:
    """  Replaces a draft's content.

    Args:
        user_id (str):
        id (str):
        xgafv (GmailUsersDraftsUpdateXgafv | Unset):
        access_token (str | Unset):
        alt (GmailUsersDraftsUpdateAlt | Unset):
        callback (str | Unset):
        fields (str | Unset):
        key (str | Unset):
        oauth_token (str | Unset):
        pretty_print (bool | Unset):
        quota_user (str | Unset):
        upload_protocol (str | Unset):
        upload_type (str | Unset):
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Draft]
     """


    kwargs = _get_kwargs(
        user_id=user_id,
id=id,
body=body,
xgafv=xgafv,
access_token=access_token,
alt=alt,
callback=callback,
fields=fields,
key=key,
oauth_token=oauth_token,
pretty_print=pretty_print,
quota_user=quota_user,
upload_protocol=upload_protocol,
upload_type=upload_type,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    user_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body:    Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  | Unset = UNSET,
    xgafv: GmailUsersDraftsUpdateXgafv | Unset = UNSET,
    access_token: str | Unset = UNSET,
    alt: GmailUsersDraftsUpdateAlt | Unset = UNSET,
    callback: str | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    upload_protocol: str | Unset = UNSET,
    upload_type: str | Unset = UNSET,

) -> Draft | None:
    """  Replaces a draft's content.

    Args:
        user_id (str):
        id (str):
        xgafv (GmailUsersDraftsUpdateXgafv | Unset):
        access_token (str | Unset):
        alt (GmailUsersDraftsUpdateAlt | Unset):
        callback (str | Unset):
        fields (str | Unset):
        key (str | Unset):
        oauth_token (str | Unset):
        pretty_print (bool | Unset):
        quota_user (str | Unset):
        upload_protocol (str | Unset):
        upload_type (str | Unset):
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Draft
     """


    return sync_detailed(
        user_id=user_id,
id=id,
client=client,
body=body,
xgafv=xgafv,
access_token=access_token,
alt=alt,
callback=callback,
fields=fields,
key=key,
oauth_token=oauth_token,
pretty_print=pretty_print,
quota_user=quota_user,
upload_protocol=upload_protocol,
upload_type=upload_type,

    ).parsed

async def asyncio_detailed(
    user_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body:    Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  | Unset = UNSET,
    xgafv: GmailUsersDraftsUpdateXgafv | Unset = UNSET,
    access_token: str | Unset = UNSET,
    alt: GmailUsersDraftsUpdateAlt | Unset = UNSET,
    callback: str | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    upload_protocol: str | Unset = UNSET,
    upload_type: str | Unset = UNSET,

) -> Response[Draft]:
    """  Replaces a draft's content.

    Args:
        user_id (str):
        id (str):
        xgafv (GmailUsersDraftsUpdateXgafv | Unset):
        access_token (str | Unset):
        alt (GmailUsersDraftsUpdateAlt | Unset):
        callback (str | Unset):
        fields (str | Unset):
        key (str | Unset):
        oauth_token (str | Unset):
        pretty_print (bool | Unset):
        quota_user (str | Unset):
        upload_protocol (str | Unset):
        upload_type (str | Unset):
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Draft]
     """


    kwargs = _get_kwargs(
        user_id=user_id,
id=id,
body=body,
xgafv=xgafv,
access_token=access_token,
alt=alt,
callback=callback,
fields=fields,
key=key,
oauth_token=oauth_token,
pretty_print=pretty_print,
quota_user=quota_user,
upload_protocol=upload_protocol,
upload_type=upload_type,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    user_id: str,
    id: str,
    *,
    client: AuthenticatedClient,
    body:    Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  |     Draft  | Unset = UNSET,
    xgafv: GmailUsersDraftsUpdateXgafv | Unset = UNSET,
    access_token: str | Unset = UNSET,
    alt: GmailUsersDraftsUpdateAlt | Unset = UNSET,
    callback: str | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    upload_protocol: str | Unset = UNSET,
    upload_type: str | Unset = UNSET,

) -> Draft | None:
    """  Replaces a draft's content.

    Args:
        user_id (str):
        id (str):
        xgafv (GmailUsersDraftsUpdateXgafv | Unset):
        access_token (str | Unset):
        alt (GmailUsersDraftsUpdateAlt | Unset):
        callback (str | Unset):
        fields (str | Unset):
        key (str | Unset):
        oauth_token (str | Unset):
        pretty_print (bool | Unset):
        quota_user (str | Unset):
        upload_protocol (str | Unset):
        upload_type (str | Unset):
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.
        body (Draft | Unset): A draft email in the user's mailbox.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Draft
     """


    return (await asyncio_detailed(
        user_id=user_id,
id=id,
client=client,
body=body,
xgafv=xgafv,
access_token=access_token,
alt=alt,
callback=callback,
fields=fields,
key=key,
oauth_token=oauth_token,
pretty_print=pretty_print,
quota_user=quota_user,
upload_protocol=upload_protocol,
upload_type=upload_type,

    )).parsed
