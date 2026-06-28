from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.batch_get_values_by_data_filter_request import BatchGetValuesByDataFilterRequest
from ...models.batch_get_values_by_data_filter_response import BatchGetValuesByDataFilterResponse
from ...models.sheets_spreadsheets_values_batch_get_by_data_filter_alt import SheetsSpreadsheetsValuesBatchGetByDataFilterAlt
from ...models.sheets_spreadsheets_values_batch_get_by_data_filter_xgafv import SheetsSpreadsheetsValuesBatchGetByDataFilterXgafv
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    spreadsheet_id: str,
    *,
    body: BatchGetValuesByDataFilterRequest | Unset = UNSET,
    xgafv: SheetsSpreadsheetsValuesBatchGetByDataFilterXgafv | Unset = UNSET,
    access_token: str | Unset = UNSET,
    alt: SheetsSpreadsheetsValuesBatchGetByDataFilterAlt | Unset = UNSET,
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
        "url": "/v4/spreadsheets/{spreadsheet_id}/values:batchGetByDataFilter".format(spreadsheet_id=quote(str(spreadsheet_id), safe=""),),
        "params": params,
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BatchGetValuesByDataFilterResponse | None:
    if response.status_code == 200:
        response_200 = BatchGetValuesByDataFilterResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BatchGetValuesByDataFilterResponse]:
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
    body: BatchGetValuesByDataFilterRequest | Unset = UNSET,
    xgafv: SheetsSpreadsheetsValuesBatchGetByDataFilterXgafv | Unset = UNSET,
    access_token: str | Unset = UNSET,
    alt: SheetsSpreadsheetsValuesBatchGetByDataFilterAlt | Unset = UNSET,
    callback: str | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    upload_protocol: str | Unset = UNSET,
    upload_type: str | Unset = UNSET,

) -> Response[BatchGetValuesByDataFilterResponse]:
    """  Returns one or more ranges of values that match the specified data filters. The caller must specify
    the spreadsheet ID and one or more DataFilters. Ranges that match any of the data filters in the
    request will be returned.

    Args:
        spreadsheet_id (str):
        xgafv (SheetsSpreadsheetsValuesBatchGetByDataFilterXgafv | Unset):
        access_token (str | Unset):
        alt (SheetsSpreadsheetsValuesBatchGetByDataFilterAlt | Unset):
        callback (str | Unset):
        fields (str | Unset):
        key (str | Unset):
        oauth_token (str | Unset):
        pretty_print (bool | Unset):
        quota_user (str | Unset):
        upload_protocol (str | Unset):
        upload_type (str | Unset):
        body (BatchGetValuesByDataFilterRequest | Unset): The request for retrieving a range of
            values in a spreadsheet selected by a set of DataFilters.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BatchGetValuesByDataFilterResponse]
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
    body: BatchGetValuesByDataFilterRequest | Unset = UNSET,
    xgafv: SheetsSpreadsheetsValuesBatchGetByDataFilterXgafv | Unset = UNSET,
    access_token: str | Unset = UNSET,
    alt: SheetsSpreadsheetsValuesBatchGetByDataFilterAlt | Unset = UNSET,
    callback: str | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    upload_protocol: str | Unset = UNSET,
    upload_type: str | Unset = UNSET,

) -> BatchGetValuesByDataFilterResponse | None:
    """  Returns one or more ranges of values that match the specified data filters. The caller must specify
    the spreadsheet ID and one or more DataFilters. Ranges that match any of the data filters in the
    request will be returned.

    Args:
        spreadsheet_id (str):
        xgafv (SheetsSpreadsheetsValuesBatchGetByDataFilterXgafv | Unset):
        access_token (str | Unset):
        alt (SheetsSpreadsheetsValuesBatchGetByDataFilterAlt | Unset):
        callback (str | Unset):
        fields (str | Unset):
        key (str | Unset):
        oauth_token (str | Unset):
        pretty_print (bool | Unset):
        quota_user (str | Unset):
        upload_protocol (str | Unset):
        upload_type (str | Unset):
        body (BatchGetValuesByDataFilterRequest | Unset): The request for retrieving a range of
            values in a spreadsheet selected by a set of DataFilters.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BatchGetValuesByDataFilterResponse
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
    body: BatchGetValuesByDataFilterRequest | Unset = UNSET,
    xgafv: SheetsSpreadsheetsValuesBatchGetByDataFilterXgafv | Unset = UNSET,
    access_token: str | Unset = UNSET,
    alt: SheetsSpreadsheetsValuesBatchGetByDataFilterAlt | Unset = UNSET,
    callback: str | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    upload_protocol: str | Unset = UNSET,
    upload_type: str | Unset = UNSET,

) -> Response[BatchGetValuesByDataFilterResponse]:
    """  Returns one or more ranges of values that match the specified data filters. The caller must specify
    the spreadsheet ID and one or more DataFilters. Ranges that match any of the data filters in the
    request will be returned.

    Args:
        spreadsheet_id (str):
        xgafv (SheetsSpreadsheetsValuesBatchGetByDataFilterXgafv | Unset):
        access_token (str | Unset):
        alt (SheetsSpreadsheetsValuesBatchGetByDataFilterAlt | Unset):
        callback (str | Unset):
        fields (str | Unset):
        key (str | Unset):
        oauth_token (str | Unset):
        pretty_print (bool | Unset):
        quota_user (str | Unset):
        upload_protocol (str | Unset):
        upload_type (str | Unset):
        body (BatchGetValuesByDataFilterRequest | Unset): The request for retrieving a range of
            values in a spreadsheet selected by a set of DataFilters.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BatchGetValuesByDataFilterResponse]
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
    body: BatchGetValuesByDataFilterRequest | Unset = UNSET,
    xgafv: SheetsSpreadsheetsValuesBatchGetByDataFilterXgafv | Unset = UNSET,
    access_token: str | Unset = UNSET,
    alt: SheetsSpreadsheetsValuesBatchGetByDataFilterAlt | Unset = UNSET,
    callback: str | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    upload_protocol: str | Unset = UNSET,
    upload_type: str | Unset = UNSET,

) -> BatchGetValuesByDataFilterResponse | None:
    """  Returns one or more ranges of values that match the specified data filters. The caller must specify
    the spreadsheet ID and one or more DataFilters. Ranges that match any of the data filters in the
    request will be returned.

    Args:
        spreadsheet_id (str):
        xgafv (SheetsSpreadsheetsValuesBatchGetByDataFilterXgafv | Unset):
        access_token (str | Unset):
        alt (SheetsSpreadsheetsValuesBatchGetByDataFilterAlt | Unset):
        callback (str | Unset):
        fields (str | Unset):
        key (str | Unset):
        oauth_token (str | Unset):
        pretty_print (bool | Unset):
        quota_user (str | Unset):
        upload_protocol (str | Unset):
        upload_type (str | Unset):
        body (BatchGetValuesByDataFilterRequest | Unset): The request for retrieving a range of
            values in a spreadsheet selected by a set of DataFilters.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BatchGetValuesByDataFilterResponse
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
