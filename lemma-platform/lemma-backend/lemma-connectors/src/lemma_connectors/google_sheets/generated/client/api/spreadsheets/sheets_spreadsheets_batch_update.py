from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.batch_update_spreadsheet_request import BatchUpdateSpreadsheetRequest
from ...models.batch_update_spreadsheet_response import BatchUpdateSpreadsheetResponse
from ...models.sheets_spreadsheets_batch_update_alt import SheetsSpreadsheetsBatchUpdateAlt
from ...models.sheets_spreadsheets_batch_update_xgafv import SheetsSpreadsheetsBatchUpdateXgafv
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    spreadsheet_id: str,
    *,
    body: BatchUpdateSpreadsheetRequest | Unset = UNSET,
    xgafv: SheetsSpreadsheetsBatchUpdateXgafv | Unset = UNSET,
    access_token: str | Unset = UNSET,
    alt: SheetsSpreadsheetsBatchUpdateAlt | Unset = UNSET,
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
        "method": "post",
        "url": "/v4/spreadsheets/{spreadsheet_id}:batchUpdate".format(spreadsheet_id=quote(str(spreadsheet_id), safe=""),),
        "params": params,
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BatchUpdateSpreadsheetResponse | None:
    if response.status_code == 200:
        response_200 = BatchUpdateSpreadsheetResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BatchUpdateSpreadsheetResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    spreadsheet_id: str,
    *,
    client: AuthenticatedClient,
    body: BatchUpdateSpreadsheetRequest | Unset = UNSET,
    xgafv: SheetsSpreadsheetsBatchUpdateXgafv | Unset = UNSET,
    access_token: str | Unset = UNSET,
    alt: SheetsSpreadsheetsBatchUpdateAlt | Unset = UNSET,
    callback: str | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    upload_protocol: str | Unset = UNSET,
    upload_type: str | Unset = UNSET,

) -> Response[BatchUpdateSpreadsheetResponse]:
    """  Applies one or more updates to the spreadsheet. Each request is validated before being applied. If
    any request is not valid then the entire request will fail and nothing will be applied. Some
    requests have replies to give you some information about how they are applied. The replies will
    mirror the requests. For example, if you applied 4 updates and the 3rd one had a reply, then the
    response will have 2 empty replies, the actual reply, and another empty reply, in that order. Due to
    the collaborative nature of spreadsheets, it is not guaranteed that the spreadsheet will reflect
    exactly your changes after this completes, however it is guaranteed that the updates in the request
    will be applied together atomically. Your changes may be altered with respect to collaborator
    changes. If there are no collaborators, the spreadsheet should reflect your changes.

    Args:
        spreadsheet_id (str):
        xgafv (SheetsSpreadsheetsBatchUpdateXgafv | Unset):
        access_token (str | Unset):
        alt (SheetsSpreadsheetsBatchUpdateAlt | Unset):
        callback (str | Unset):
        fields (str | Unset):
        key (str | Unset):
        oauth_token (str | Unset):
        pretty_print (bool | Unset):
        quota_user (str | Unset):
        upload_protocol (str | Unset):
        upload_type (str | Unset):
        body (BatchUpdateSpreadsheetRequest | Unset): The request for updating any aspect of a
            spreadsheet.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BatchUpdateSpreadsheetResponse]
     """


    kwargs = _get_kwargs(
        spreadsheet_id=spreadsheet_id,
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
    spreadsheet_id: str,
    *,
    client: AuthenticatedClient,
    body: BatchUpdateSpreadsheetRequest | Unset = UNSET,
    xgafv: SheetsSpreadsheetsBatchUpdateXgafv | Unset = UNSET,
    access_token: str | Unset = UNSET,
    alt: SheetsSpreadsheetsBatchUpdateAlt | Unset = UNSET,
    callback: str | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    upload_protocol: str | Unset = UNSET,
    upload_type: str | Unset = UNSET,

) -> BatchUpdateSpreadsheetResponse | None:
    """  Applies one or more updates to the spreadsheet. Each request is validated before being applied. If
    any request is not valid then the entire request will fail and nothing will be applied. Some
    requests have replies to give you some information about how they are applied. The replies will
    mirror the requests. For example, if you applied 4 updates and the 3rd one had a reply, then the
    response will have 2 empty replies, the actual reply, and another empty reply, in that order. Due to
    the collaborative nature of spreadsheets, it is not guaranteed that the spreadsheet will reflect
    exactly your changes after this completes, however it is guaranteed that the updates in the request
    will be applied together atomically. Your changes may be altered with respect to collaborator
    changes. If there are no collaborators, the spreadsheet should reflect your changes.

    Args:
        spreadsheet_id (str):
        xgafv (SheetsSpreadsheetsBatchUpdateXgafv | Unset):
        access_token (str | Unset):
        alt (SheetsSpreadsheetsBatchUpdateAlt | Unset):
        callback (str | Unset):
        fields (str | Unset):
        key (str | Unset):
        oauth_token (str | Unset):
        pretty_print (bool | Unset):
        quota_user (str | Unset):
        upload_protocol (str | Unset):
        upload_type (str | Unset):
        body (BatchUpdateSpreadsheetRequest | Unset): The request for updating any aspect of a
            spreadsheet.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BatchUpdateSpreadsheetResponse
     """


    return sync_detailed(
        spreadsheet_id=spreadsheet_id,
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
    spreadsheet_id: str,
    *,
    client: AuthenticatedClient,
    body: BatchUpdateSpreadsheetRequest | Unset = UNSET,
    xgafv: SheetsSpreadsheetsBatchUpdateXgafv | Unset = UNSET,
    access_token: str | Unset = UNSET,
    alt: SheetsSpreadsheetsBatchUpdateAlt | Unset = UNSET,
    callback: str | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    upload_protocol: str | Unset = UNSET,
    upload_type: str | Unset = UNSET,

) -> Response[BatchUpdateSpreadsheetResponse]:
    """  Applies one or more updates to the spreadsheet. Each request is validated before being applied. If
    any request is not valid then the entire request will fail and nothing will be applied. Some
    requests have replies to give you some information about how they are applied. The replies will
    mirror the requests. For example, if you applied 4 updates and the 3rd one had a reply, then the
    response will have 2 empty replies, the actual reply, and another empty reply, in that order. Due to
    the collaborative nature of spreadsheets, it is not guaranteed that the spreadsheet will reflect
    exactly your changes after this completes, however it is guaranteed that the updates in the request
    will be applied together atomically. Your changes may be altered with respect to collaborator
    changes. If there are no collaborators, the spreadsheet should reflect your changes.

    Args:
        spreadsheet_id (str):
        xgafv (SheetsSpreadsheetsBatchUpdateXgafv | Unset):
        access_token (str | Unset):
        alt (SheetsSpreadsheetsBatchUpdateAlt | Unset):
        callback (str | Unset):
        fields (str | Unset):
        key (str | Unset):
        oauth_token (str | Unset):
        pretty_print (bool | Unset):
        quota_user (str | Unset):
        upload_protocol (str | Unset):
        upload_type (str | Unset):
        body (BatchUpdateSpreadsheetRequest | Unset): The request for updating any aspect of a
            spreadsheet.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BatchUpdateSpreadsheetResponse]
     """


    kwargs = _get_kwargs(
        spreadsheet_id=spreadsheet_id,
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
    spreadsheet_id: str,
    *,
    client: AuthenticatedClient,
    body: BatchUpdateSpreadsheetRequest | Unset = UNSET,
    xgafv: SheetsSpreadsheetsBatchUpdateXgafv | Unset = UNSET,
    access_token: str | Unset = UNSET,
    alt: SheetsSpreadsheetsBatchUpdateAlt | Unset = UNSET,
    callback: str | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    upload_protocol: str | Unset = UNSET,
    upload_type: str | Unset = UNSET,

) -> BatchUpdateSpreadsheetResponse | None:
    """  Applies one or more updates to the spreadsheet. Each request is validated before being applied. If
    any request is not valid then the entire request will fail and nothing will be applied. Some
    requests have replies to give you some information about how they are applied. The replies will
    mirror the requests. For example, if you applied 4 updates and the 3rd one had a reply, then the
    response will have 2 empty replies, the actual reply, and another empty reply, in that order. Due to
    the collaborative nature of spreadsheets, it is not guaranteed that the spreadsheet will reflect
    exactly your changes after this completes, however it is guaranteed that the updates in the request
    will be applied together atomically. Your changes may be altered with respect to collaborator
    changes. If there are no collaborators, the spreadsheet should reflect your changes.

    Args:
        spreadsheet_id (str):
        xgafv (SheetsSpreadsheetsBatchUpdateXgafv | Unset):
        access_token (str | Unset):
        alt (SheetsSpreadsheetsBatchUpdateAlt | Unset):
        callback (str | Unset):
        fields (str | Unset):
        key (str | Unset):
        oauth_token (str | Unset):
        pretty_print (bool | Unset):
        quota_user (str | Unset):
        upload_protocol (str | Unset):
        upload_type (str | Unset):
        body (BatchUpdateSpreadsheetRequest | Unset): The request for updating any aspect of a
            spreadsheet.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BatchUpdateSpreadsheetResponse
     """


    return (await asyncio_detailed(
        spreadsheet_id=spreadsheet_id,
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
