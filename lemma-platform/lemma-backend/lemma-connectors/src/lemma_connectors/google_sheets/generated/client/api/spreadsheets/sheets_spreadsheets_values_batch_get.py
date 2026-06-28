from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.batch_get_values_response import BatchGetValuesResponse
from ...models.sheets_spreadsheets_values_batch_get_alt import SheetsSpreadsheetsValuesBatchGetAlt
from ...models.sheets_spreadsheets_values_batch_get_date_time_render_option import SheetsSpreadsheetsValuesBatchGetDateTimeRenderOption
from ...models.sheets_spreadsheets_values_batch_get_major_dimension import SheetsSpreadsheetsValuesBatchGetMajorDimension
from ...models.sheets_spreadsheets_values_batch_get_value_render_option import SheetsSpreadsheetsValuesBatchGetValueRenderOption
from ...models.sheets_spreadsheets_values_batch_get_xgafv import SheetsSpreadsheetsValuesBatchGetXgafv
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    spreadsheet_id: str,
    *,
    date_time_render_option: SheetsSpreadsheetsValuesBatchGetDateTimeRenderOption | Unset = UNSET,
    major_dimension: SheetsSpreadsheetsValuesBatchGetMajorDimension | Unset = UNSET,
    ranges: list[str] | Unset = UNSET,
    value_render_option: SheetsSpreadsheetsValuesBatchGetValueRenderOption | Unset = UNSET,
    xgafv: SheetsSpreadsheetsValuesBatchGetXgafv | Unset = UNSET,
    access_token: str | Unset = UNSET,
    alt: SheetsSpreadsheetsValuesBatchGetAlt | Unset = UNSET,
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

    json_date_time_render_option: str | Unset = UNSET
    if not isinstance(date_time_render_option, Unset):
        json_date_time_render_option = date_time_render_option.value

    params["dateTimeRenderOption"] = json_date_time_render_option

    json_major_dimension: str | Unset = UNSET
    if not isinstance(major_dimension, Unset):
        json_major_dimension = major_dimension.value

    params["majorDimension"] = json_major_dimension

    json_ranges: list[str] | Unset = UNSET
    if not isinstance(ranges, Unset):
        json_ranges = ranges


    params["ranges"] = json_ranges

    json_value_render_option: str | Unset = UNSET
    if not isinstance(value_render_option, Unset):
        json_value_render_option = value_render_option.value

    params["valueRenderOption"] = json_value_render_option

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
        "url": "/v4/spreadsheets/{spreadsheet_id}/values:batchGet".format(spreadsheet_id=quote(str(spreadsheet_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BatchGetValuesResponse | None:
    if response.status_code == 200:
        response_200 = BatchGetValuesResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BatchGetValuesResponse]:
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
    date_time_render_option: SheetsSpreadsheetsValuesBatchGetDateTimeRenderOption | Unset = UNSET,
    major_dimension: SheetsSpreadsheetsValuesBatchGetMajorDimension | Unset = UNSET,
    ranges: list[str] | Unset = UNSET,
    value_render_option: SheetsSpreadsheetsValuesBatchGetValueRenderOption | Unset = UNSET,
    xgafv: SheetsSpreadsheetsValuesBatchGetXgafv | Unset = UNSET,
    access_token: str | Unset = UNSET,
    alt: SheetsSpreadsheetsValuesBatchGetAlt | Unset = UNSET,
    callback: str | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    upload_protocol: str | Unset = UNSET,
    upload_type: str | Unset = UNSET,

) -> Response[BatchGetValuesResponse]:
    """  Returns one or more ranges of values from a spreadsheet. The caller must specify the spreadsheet ID
    and one or more ranges.

    Args:
        spreadsheet_id (str):
        date_time_render_option (SheetsSpreadsheetsValuesBatchGetDateTimeRenderOption | Unset):
        major_dimension (SheetsSpreadsheetsValuesBatchGetMajorDimension | Unset):
        ranges (list[str] | Unset):
        value_render_option (SheetsSpreadsheetsValuesBatchGetValueRenderOption | Unset):
        xgafv (SheetsSpreadsheetsValuesBatchGetXgafv | Unset):
        access_token (str | Unset):
        alt (SheetsSpreadsheetsValuesBatchGetAlt | Unset):
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
        Response[BatchGetValuesResponse]
     """


    kwargs = _get_kwargs(
        spreadsheet_id=spreadsheet_id,
date_time_render_option=date_time_render_option,
major_dimension=major_dimension,
ranges=ranges,
value_render_option=value_render_option,
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
    date_time_render_option: SheetsSpreadsheetsValuesBatchGetDateTimeRenderOption | Unset = UNSET,
    major_dimension: SheetsSpreadsheetsValuesBatchGetMajorDimension | Unset = UNSET,
    ranges: list[str] | Unset = UNSET,
    value_render_option: SheetsSpreadsheetsValuesBatchGetValueRenderOption | Unset = UNSET,
    xgafv: SheetsSpreadsheetsValuesBatchGetXgafv | Unset = UNSET,
    access_token: str | Unset = UNSET,
    alt: SheetsSpreadsheetsValuesBatchGetAlt | Unset = UNSET,
    callback: str | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    upload_protocol: str | Unset = UNSET,
    upload_type: str | Unset = UNSET,

) -> BatchGetValuesResponse | None:
    """  Returns one or more ranges of values from a spreadsheet. The caller must specify the spreadsheet ID
    and one or more ranges.

    Args:
        spreadsheet_id (str):
        date_time_render_option (SheetsSpreadsheetsValuesBatchGetDateTimeRenderOption | Unset):
        major_dimension (SheetsSpreadsheetsValuesBatchGetMajorDimension | Unset):
        ranges (list[str] | Unset):
        value_render_option (SheetsSpreadsheetsValuesBatchGetValueRenderOption | Unset):
        xgafv (SheetsSpreadsheetsValuesBatchGetXgafv | Unset):
        access_token (str | Unset):
        alt (SheetsSpreadsheetsValuesBatchGetAlt | Unset):
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
        BatchGetValuesResponse
     """


    return sync_detailed(
        spreadsheet_id=spreadsheet_id,
client=client,
date_time_render_option=date_time_render_option,
major_dimension=major_dimension,
ranges=ranges,
value_render_option=value_render_option,
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
    date_time_render_option: SheetsSpreadsheetsValuesBatchGetDateTimeRenderOption | Unset = UNSET,
    major_dimension: SheetsSpreadsheetsValuesBatchGetMajorDimension | Unset = UNSET,
    ranges: list[str] | Unset = UNSET,
    value_render_option: SheetsSpreadsheetsValuesBatchGetValueRenderOption | Unset = UNSET,
    xgafv: SheetsSpreadsheetsValuesBatchGetXgafv | Unset = UNSET,
    access_token: str | Unset = UNSET,
    alt: SheetsSpreadsheetsValuesBatchGetAlt | Unset = UNSET,
    callback: str | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    upload_protocol: str | Unset = UNSET,
    upload_type: str | Unset = UNSET,

) -> Response[BatchGetValuesResponse]:
    """  Returns one or more ranges of values from a spreadsheet. The caller must specify the spreadsheet ID
    and one or more ranges.

    Args:
        spreadsheet_id (str):
        date_time_render_option (SheetsSpreadsheetsValuesBatchGetDateTimeRenderOption | Unset):
        major_dimension (SheetsSpreadsheetsValuesBatchGetMajorDimension | Unset):
        ranges (list[str] | Unset):
        value_render_option (SheetsSpreadsheetsValuesBatchGetValueRenderOption | Unset):
        xgafv (SheetsSpreadsheetsValuesBatchGetXgafv | Unset):
        access_token (str | Unset):
        alt (SheetsSpreadsheetsValuesBatchGetAlt | Unset):
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
        Response[BatchGetValuesResponse]
     """


    kwargs = _get_kwargs(
        spreadsheet_id=spreadsheet_id,
date_time_render_option=date_time_render_option,
major_dimension=major_dimension,
ranges=ranges,
value_render_option=value_render_option,
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
    date_time_render_option: SheetsSpreadsheetsValuesBatchGetDateTimeRenderOption | Unset = UNSET,
    major_dimension: SheetsSpreadsheetsValuesBatchGetMajorDimension | Unset = UNSET,
    ranges: list[str] | Unset = UNSET,
    value_render_option: SheetsSpreadsheetsValuesBatchGetValueRenderOption | Unset = UNSET,
    xgafv: SheetsSpreadsheetsValuesBatchGetXgafv | Unset = UNSET,
    access_token: str | Unset = UNSET,
    alt: SheetsSpreadsheetsValuesBatchGetAlt | Unset = UNSET,
    callback: str | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    upload_protocol: str | Unset = UNSET,
    upload_type: str | Unset = UNSET,

) -> BatchGetValuesResponse | None:
    """  Returns one or more ranges of values from a spreadsheet. The caller must specify the spreadsheet ID
    and one or more ranges.

    Args:
        spreadsheet_id (str):
        date_time_render_option (SheetsSpreadsheetsValuesBatchGetDateTimeRenderOption | Unset):
        major_dimension (SheetsSpreadsheetsValuesBatchGetMajorDimension | Unset):
        ranges (list[str] | Unset):
        value_render_option (SheetsSpreadsheetsValuesBatchGetValueRenderOption | Unset):
        xgafv (SheetsSpreadsheetsValuesBatchGetXgafv | Unset):
        access_token (str | Unset):
        alt (SheetsSpreadsheetsValuesBatchGetAlt | Unset):
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
        BatchGetValuesResponse
     """


    return (await asyncio_detailed(
        spreadsheet_id=spreadsheet_id,
client=client,
date_time_render_option=date_time_render_option,
major_dimension=major_dimension,
ranges=ranges,
value_render_option=value_render_option,
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
