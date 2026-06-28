from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.drive_replies_update_alt import DriveRepliesUpdateAlt
from ...models.reply import Reply
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    file_id: str,
    comment_id: str,
    reply_id: str,
    *,
    body: Reply | Unset = UNSET,
    alt: DriveRepliesUpdateAlt | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    user_ip: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    json_alt: str | Unset = UNSET
    if not isinstance(alt, Unset):
        json_alt = alt.value

    params["alt"] = json_alt

    params["fields"] = fields

    params["key"] = key

    params["oauth_token"] = oauth_token

    params["prettyPrint"] = pretty_print

    params["quotaUser"] = quota_user

    params["userIp"] = user_ip


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/files/{file_id}/comments/{comment_id}/replies/{reply_id}".format(file_id=quote(str(file_id), safe=""),comment_id=quote(str(comment_id), safe=""),reply_id=quote(str(reply_id), safe=""),),
        "params": params,
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Reply | None:
    if response.status_code == 200:
        response_200 = Reply.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Reply]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    file_id: str,
    comment_id: str,
    reply_id: str,
    *,
    client: AuthenticatedClient,
    body: Reply | Unset = UNSET,
    alt: DriveRepliesUpdateAlt | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    user_ip: str | Unset = UNSET,

) -> Response[Reply]:
    """  Updates a reply with patch semantics.

    Args:
        file_id (str):
        comment_id (str):
        reply_id (str):
        alt (DriveRepliesUpdateAlt | Unset):
        fields (str | Unset):
        key (str | Unset):
        oauth_token (str | Unset):
        pretty_print (bool | Unset):
        quota_user (str | Unset):
        user_ip (str | Unset):
        body (Reply | Unset): A reply to a comment on a file.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Reply]
     """


    kwargs = _get_kwargs(
        file_id=file_id,
comment_id=comment_id,
reply_id=reply_id,
body=body,
alt=alt,
fields=fields,
key=key,
oauth_token=oauth_token,
pretty_print=pretty_print,
quota_user=quota_user,
user_ip=user_ip,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    file_id: str,
    comment_id: str,
    reply_id: str,
    *,
    client: AuthenticatedClient,
    body: Reply | Unset = UNSET,
    alt: DriveRepliesUpdateAlt | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    user_ip: str | Unset = UNSET,

) -> Reply | None:
    """  Updates a reply with patch semantics.

    Args:
        file_id (str):
        comment_id (str):
        reply_id (str):
        alt (DriveRepliesUpdateAlt | Unset):
        fields (str | Unset):
        key (str | Unset):
        oauth_token (str | Unset):
        pretty_print (bool | Unset):
        quota_user (str | Unset):
        user_ip (str | Unset):
        body (Reply | Unset): A reply to a comment on a file.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Reply
     """


    return sync_detailed(
        file_id=file_id,
comment_id=comment_id,
reply_id=reply_id,
client=client,
body=body,
alt=alt,
fields=fields,
key=key,
oauth_token=oauth_token,
pretty_print=pretty_print,
quota_user=quota_user,
user_ip=user_ip,

    ).parsed

async def asyncio_detailed(
    file_id: str,
    comment_id: str,
    reply_id: str,
    *,
    client: AuthenticatedClient,
    body: Reply | Unset = UNSET,
    alt: DriveRepliesUpdateAlt | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    user_ip: str | Unset = UNSET,

) -> Response[Reply]:
    """  Updates a reply with patch semantics.

    Args:
        file_id (str):
        comment_id (str):
        reply_id (str):
        alt (DriveRepliesUpdateAlt | Unset):
        fields (str | Unset):
        key (str | Unset):
        oauth_token (str | Unset):
        pretty_print (bool | Unset):
        quota_user (str | Unset):
        user_ip (str | Unset):
        body (Reply | Unset): A reply to a comment on a file.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Reply]
     """


    kwargs = _get_kwargs(
        file_id=file_id,
comment_id=comment_id,
reply_id=reply_id,
body=body,
alt=alt,
fields=fields,
key=key,
oauth_token=oauth_token,
pretty_print=pretty_print,
quota_user=quota_user,
user_ip=user_ip,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    file_id: str,
    comment_id: str,
    reply_id: str,
    *,
    client: AuthenticatedClient,
    body: Reply | Unset = UNSET,
    alt: DriveRepliesUpdateAlt | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    user_ip: str | Unset = UNSET,

) -> Reply | None:
    """  Updates a reply with patch semantics.

    Args:
        file_id (str):
        comment_id (str):
        reply_id (str):
        alt (DriveRepliesUpdateAlt | Unset):
        fields (str | Unset):
        key (str | Unset):
        oauth_token (str | Unset):
        pretty_print (bool | Unset):
        quota_user (str | Unset):
        user_ip (str | Unset):
        body (Reply | Unset): A reply to a comment on a file.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Reply
     """


    return (await asyncio_detailed(
        file_id=file_id,
comment_id=comment_id,
reply_id=reply_id,
client=client,
body=body,
alt=alt,
fields=fields,
key=key,
oauth_token=oauth_token,
pretty_print=pretty_print,
quota_user=quota_user,
user_ip=user_ip,

    )).parsed
