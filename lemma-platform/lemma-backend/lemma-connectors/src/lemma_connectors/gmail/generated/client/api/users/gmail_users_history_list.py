from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.gmail_users_history_list_alt import GmailUsersHistoryListAlt
from ...models.gmail_users_history_list_history_types_item import GmailUsersHistoryListHistoryTypesItem
from ...models.gmail_users_history_list_xgafv import GmailUsersHistoryListXgafv
from ...models.list_history_response import ListHistoryResponse
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    user_id: str,
    *,
    history_types: list[GmailUsersHistoryListHistoryTypesItem] | Unset = UNSET,
    label_id: str | Unset = UNSET,
    max_results: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    start_history_id: str | Unset = UNSET,
    xgafv: GmailUsersHistoryListXgafv | Unset = UNSET,
    access_token: str | Unset = UNSET,
    alt: GmailUsersHistoryListAlt | Unset = UNSET,
    callback: str | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    upload_protocol: str | Unset = UNSET,
    upload_type: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_history_types: list[str] | Unset = UNSET
    if not isinstance(history_types, Unset):
        json_history_types = []
        for history_types_item_data in history_types:
            history_types_item = history_types_item_data.value
            json_history_types.append(history_types_item)


    params["historyTypes"] = json_history_types

    params["labelId"] = label_id

    params["maxResults"] = max_results

    params["pageToken"] = page_token

    params["startHistoryId"] = start_history_id

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
        "method": "get",
        "url": "/gmail/v1/users/{user_id}/history".format(user_id=quote(str(user_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ListHistoryResponse | None:
    if response.status_code == 200:
        response_200 = ListHistoryResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ListHistoryResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
    history_types: list[GmailUsersHistoryListHistoryTypesItem] | Unset = UNSET,
    label_id: str | Unset = UNSET,
    max_results: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    start_history_id: str | Unset = UNSET,
    xgafv: GmailUsersHistoryListXgafv | Unset = UNSET,
    access_token: str | Unset = UNSET,
    alt: GmailUsersHistoryListAlt | Unset = UNSET,
    callback: str | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    upload_protocol: str | Unset = UNSET,
    upload_type: str | Unset = UNSET,

) -> Response[ListHistoryResponse]:
    """  Lists the history of all changes to the given mailbox. History results are returned in chronological
    order (increasing `historyId`).

    Args:
        user_id (str):
        history_types (list[GmailUsersHistoryListHistoryTypesItem] | Unset):
        label_id (str | Unset):
        max_results (int | Unset):
        page_token (str | Unset):
        start_history_id (str | Unset):
        xgafv (GmailUsersHistoryListXgafv | Unset):
        access_token (str | Unset):
        alt (GmailUsersHistoryListAlt | Unset):
        callback (str | Unset):
        fields (str | Unset):
        key (str | Unset):
        oauth_token (str | Unset):
        pretty_print (bool | Unset):
        quota_user (str | Unset):
        upload_protocol (str | Unset):
        upload_type (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListHistoryResponse]
     """


    kwargs = _get_kwargs(
        user_id=user_id,
history_types=history_types,
label_id=label_id,
max_results=max_results,
page_token=page_token,
start_history_id=start_history_id,
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
    *,
    client: AuthenticatedClient,
    history_types: list[GmailUsersHistoryListHistoryTypesItem] | Unset = UNSET,
    label_id: str | Unset = UNSET,
    max_results: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    start_history_id: str | Unset = UNSET,
    xgafv: GmailUsersHistoryListXgafv | Unset = UNSET,
    access_token: str | Unset = UNSET,
    alt: GmailUsersHistoryListAlt | Unset = UNSET,
    callback: str | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    upload_protocol: str | Unset = UNSET,
    upload_type: str | Unset = UNSET,

) -> ListHistoryResponse | None:
    """  Lists the history of all changes to the given mailbox. History results are returned in chronological
    order (increasing `historyId`).

    Args:
        user_id (str):
        history_types (list[GmailUsersHistoryListHistoryTypesItem] | Unset):
        label_id (str | Unset):
        max_results (int | Unset):
        page_token (str | Unset):
        start_history_id (str | Unset):
        xgafv (GmailUsersHistoryListXgafv | Unset):
        access_token (str | Unset):
        alt (GmailUsersHistoryListAlt | Unset):
        callback (str | Unset):
        fields (str | Unset):
        key (str | Unset):
        oauth_token (str | Unset):
        pretty_print (bool | Unset):
        quota_user (str | Unset):
        upload_protocol (str | Unset):
        upload_type (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListHistoryResponse
     """


    return sync_detailed(
        user_id=user_id,
client=client,
history_types=history_types,
label_id=label_id,
max_results=max_results,
page_token=page_token,
start_history_id=start_history_id,
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
    *,
    client: AuthenticatedClient,
    history_types: list[GmailUsersHistoryListHistoryTypesItem] | Unset = UNSET,
    label_id: str | Unset = UNSET,
    max_results: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    start_history_id: str | Unset = UNSET,
    xgafv: GmailUsersHistoryListXgafv | Unset = UNSET,
    access_token: str | Unset = UNSET,
    alt: GmailUsersHistoryListAlt | Unset = UNSET,
    callback: str | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    upload_protocol: str | Unset = UNSET,
    upload_type: str | Unset = UNSET,

) -> Response[ListHistoryResponse]:
    """  Lists the history of all changes to the given mailbox. History results are returned in chronological
    order (increasing `historyId`).

    Args:
        user_id (str):
        history_types (list[GmailUsersHistoryListHistoryTypesItem] | Unset):
        label_id (str | Unset):
        max_results (int | Unset):
        page_token (str | Unset):
        start_history_id (str | Unset):
        xgafv (GmailUsersHistoryListXgafv | Unset):
        access_token (str | Unset):
        alt (GmailUsersHistoryListAlt | Unset):
        callback (str | Unset):
        fields (str | Unset):
        key (str | Unset):
        oauth_token (str | Unset):
        pretty_print (bool | Unset):
        quota_user (str | Unset):
        upload_protocol (str | Unset):
        upload_type (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ListHistoryResponse]
     """


    kwargs = _get_kwargs(
        user_id=user_id,
history_types=history_types,
label_id=label_id,
max_results=max_results,
page_token=page_token,
start_history_id=start_history_id,
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
    *,
    client: AuthenticatedClient,
    history_types: list[GmailUsersHistoryListHistoryTypesItem] | Unset = UNSET,
    label_id: str | Unset = UNSET,
    max_results: int | Unset = UNSET,
    page_token: str | Unset = UNSET,
    start_history_id: str | Unset = UNSET,
    xgafv: GmailUsersHistoryListXgafv | Unset = UNSET,
    access_token: str | Unset = UNSET,
    alt: GmailUsersHistoryListAlt | Unset = UNSET,
    callback: str | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    upload_protocol: str | Unset = UNSET,
    upload_type: str | Unset = UNSET,

) -> ListHistoryResponse | None:
    """  Lists the history of all changes to the given mailbox. History results are returned in chronological
    order (increasing `historyId`).

    Args:
        user_id (str):
        history_types (list[GmailUsersHistoryListHistoryTypesItem] | Unset):
        label_id (str | Unset):
        max_results (int | Unset):
        page_token (str | Unset):
        start_history_id (str | Unset):
        xgafv (GmailUsersHistoryListXgafv | Unset):
        access_token (str | Unset):
        alt (GmailUsersHistoryListAlt | Unset):
        callback (str | Unset):
        fields (str | Unset):
        key (str | Unset):
        oauth_token (str | Unset):
        pretty_print (bool | Unset):
        quota_user (str | Unset):
        upload_protocol (str | Unset):
        upload_type (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ListHistoryResponse
     """


    return (await asyncio_detailed(
        user_id=user_id,
client=client,
history_types=history_types,
label_id=label_id,
max_results=max_results,
page_token=page_token,
start_history_id=start_history_id,
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
