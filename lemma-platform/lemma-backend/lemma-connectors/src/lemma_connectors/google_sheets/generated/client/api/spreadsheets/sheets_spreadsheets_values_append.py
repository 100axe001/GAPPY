from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.append_values_response import AppendValuesResponse
from ...models.sheets_spreadsheets_values_append_alt import SheetsSpreadsheetsValuesAppendAlt
from ...models.sheets_spreadsheets_values_append_insert_data_option import SheetsSpreadsheetsValuesAppendInsertDataOption
from ...models.sheets_spreadsheets_values_append_response_date_time_render_option import SheetsSpreadsheetsValuesAppendResponseDateTimeRenderOption
from ...models.sheets_spreadsheets_values_append_response_value_render_option import SheetsSpreadsheetsValuesAppendResponseValueRenderOption
from ...models.sheets_spreadsheets_values_append_value_input_option import SheetsSpreadsheetsValuesAppendValueInputOption
from ...models.sheets_spreadsheets_values_append_xgafv import SheetsSpreadsheetsValuesAppendXgafv
from ...models.value_range import ValueRange
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    spreadsheet_id: str,
    range_: str,
    *,
    body: ValueRange | Unset = UNSET,
    include_values_in_response: bool | Unset = UNSET,
    insert_data_option: SheetsSpreadsheetsValuesAppendInsertDataOption | Unset = UNSET,
    response_date_time_render_option: SheetsSpreadsheetsValuesAppendResponseDateTimeRenderOption | Unset = UNSET,
    response_value_render_option: SheetsSpreadsheetsValuesAppendResponseValueRenderOption | Unset = UNSET,
    value_input_option: SheetsSpreadsheetsValuesAppendValueInputOption | Unset = UNSET,
    xgafv: SheetsSpreadsheetsValuesAppendXgafv | Unset = UNSET,
    access_token: str | Unset = UNSET,
    alt: SheetsSpreadsheetsValuesAppendAlt | Unset = UNSET,
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

    params["includeValuesInResponse"] = include_values_in_response

    json_insert_data_option: str | Unset = UNSET
    if not isinstance(insert_data_option, Unset):
        json_insert_data_option = insert_data_option.value

    params["insertDataOption"] = json_insert_data_option

    json_response_date_time_render_option: str | Unset = UNSET
    if not isinstance(response_date_time_render_option, Unset):
        json_response_date_time_render_option = response_date_time_render_option.value

    params["responseDateTimeRenderOption"] = json_response_date_time_render_option

    json_response_value_render_option: str | Unset = UNSET
    if not isinstance(response_value_render_option, Unset):
        json_response_value_render_option = response_value_render_option.value

    params["responseValueRenderOption"] = json_response_value_render_option

    json_value_input_option: str | Unset = UNSET
    if not isinstance(value_input_option, Unset):
        json_value_input_option = value_input_option.value

    params["valueInputOption"] = json_value_input_option

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
        "url": "/v4/spreadsheets/{spreadsheet_id}/values/{range_}:append".format(spreadsheet_id=quote(str(spreadsheet_id), safe=""),range_=quote(str(range_), safe=""),),
        "params": params,
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AppendValuesResponse | None:
    if response.status_code == 200:
        response_200 = AppendValuesResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AppendValuesResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    spreadsheet_id: str,
    range_: str,
    *,
    client: AuthenticatedClient,
    body: ValueRange | Unset = UNSET,
    include_values_in_response: bool | Unset = UNSET,
    insert_data_option: SheetsSpreadsheetsValuesAppendInsertDataOption | Unset = UNSET,
    response_date_time_render_option: SheetsSpreadsheetsValuesAppendResponseDateTimeRenderOption | Unset = UNSET,
    response_value_render_option: SheetsSpreadsheetsValuesAppendResponseValueRenderOption | Unset = UNSET,
    value_input_option: SheetsSpreadsheetsValuesAppendValueInputOption | Unset = UNSET,
    xgafv: SheetsSpreadsheetsValuesAppendXgafv | Unset = UNSET,
    access_token: str | Unset = UNSET,
    alt: SheetsSpreadsheetsValuesAppendAlt | Unset = UNSET,
    callback: str | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    upload_protocol: str | Unset = UNSET,
    upload_type: str | Unset = UNSET,

) -> Response[AppendValuesResponse]:
    r"""  Appends values to a spreadsheet. The input range is used to search for existing data and find a
    \"table\" within that range. Values will be appended to the next row of the table, starting with the
    first column of the table. See the [guide](/sheets/api/guides/values#appending_values) and [sample
    code](/sheets/api/samples/writing#append_values) for specific details of how tables are detected and
    data is appended. The caller must specify the spreadsheet ID, range, and a valueInputOption. The
    `valueInputOption` only controls how the input data will be added to the sheet (column-wise or row-
    wise), it does not influence what cell the data starts being written to.

    Args:
        spreadsheet_id (str):
        range_ (str):
        include_values_in_response (bool | Unset):
        insert_data_option (SheetsSpreadsheetsValuesAppendInsertDataOption | Unset):
        response_date_time_render_option
            (SheetsSpreadsheetsValuesAppendResponseDateTimeRenderOption | Unset):
        response_value_render_option (SheetsSpreadsheetsValuesAppendResponseValueRenderOption |
            Unset):
        value_input_option (SheetsSpreadsheetsValuesAppendValueInputOption | Unset):
        xgafv (SheetsSpreadsheetsValuesAppendXgafv | Unset):
        access_token (str | Unset):
        alt (SheetsSpreadsheetsValuesAppendAlt | Unset):
        callback (str | Unset):
        fields (str | Unset):
        key (str | Unset):
        oauth_token (str | Unset):
        pretty_print (bool | Unset):
        quota_user (str | Unset):
        upload_protocol (str | Unset):
        upload_type (str | Unset):
        body (ValueRange | Unset): Data within a range of the spreadsheet.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppendValuesResponse]
     """


    kwargs = _get_kwargs(
        spreadsheet_id=spreadsheet_id,
range_=range_,
body=body,
include_values_in_response=include_values_in_response,
insert_data_option=insert_data_option,
response_date_time_render_option=response_date_time_render_option,
response_value_render_option=response_value_render_option,
value_input_option=value_input_option,
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
    range_: str,
    *,
    client: AuthenticatedClient,
    body: ValueRange | Unset = UNSET,
    include_values_in_response: bool | Unset = UNSET,
    insert_data_option: SheetsSpreadsheetsValuesAppendInsertDataOption | Unset = UNSET,
    response_date_time_render_option: SheetsSpreadsheetsValuesAppendResponseDateTimeRenderOption | Unset = UNSET,
    response_value_render_option: SheetsSpreadsheetsValuesAppendResponseValueRenderOption | Unset = UNSET,
    value_input_option: SheetsSpreadsheetsValuesAppendValueInputOption | Unset = UNSET,
    xgafv: SheetsSpreadsheetsValuesAppendXgafv | Unset = UNSET,
    access_token: str | Unset = UNSET,
    alt: SheetsSpreadsheetsValuesAppendAlt | Unset = UNSET,
    callback: str | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    upload_protocol: str | Unset = UNSET,
    upload_type: str | Unset = UNSET,

) -> AppendValuesResponse | None:
    r"""  Appends values to a spreadsheet. The input range is used to search for existing data and find a
    \"table\" within that range. Values will be appended to the next row of the table, starting with the
    first column of the table. See the [guide](/sheets/api/guides/values#appending_values) and [sample
    code](/sheets/api/samples/writing#append_values) for specific details of how tables are detected and
    data is appended. The caller must specify the spreadsheet ID, range, and a valueInputOption. The
    `valueInputOption` only controls how the input data will be added to the sheet (column-wise or row-
    wise), it does not influence what cell the data starts being written to.

    Args:
        spreadsheet_id (str):
        range_ (str):
        include_values_in_response (bool | Unset):
        insert_data_option (SheetsSpreadsheetsValuesAppendInsertDataOption | Unset):
        response_date_time_render_option
            (SheetsSpreadsheetsValuesAppendResponseDateTimeRenderOption | Unset):
        response_value_render_option (SheetsSpreadsheetsValuesAppendResponseValueRenderOption |
            Unset):
        value_input_option (SheetsSpreadsheetsValuesAppendValueInputOption | Unset):
        xgafv (SheetsSpreadsheetsValuesAppendXgafv | Unset):
        access_token (str | Unset):
        alt (SheetsSpreadsheetsValuesAppendAlt | Unset):
        callback (str | Unset):
        fields (str | Unset):
        key (str | Unset):
        oauth_token (str | Unset):
        pretty_print (bool | Unset):
        quota_user (str | Unset):
        upload_protocol (str | Unset):
        upload_type (str | Unset):
        body (ValueRange | Unset): Data within a range of the spreadsheet.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppendValuesResponse
     """


    return sync_detailed(
        spreadsheet_id=spreadsheet_id,
range_=range_,
client=client,
body=body,
include_values_in_response=include_values_in_response,
insert_data_option=insert_data_option,
response_date_time_render_option=response_date_time_render_option,
response_value_render_option=response_value_render_option,
value_input_option=value_input_option,
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
    range_: str,
    *,
    client: AuthenticatedClient,
    body: ValueRange | Unset = UNSET,
    include_values_in_response: bool | Unset = UNSET,
    insert_data_option: SheetsSpreadsheetsValuesAppendInsertDataOption | Unset = UNSET,
    response_date_time_render_option: SheetsSpreadsheetsValuesAppendResponseDateTimeRenderOption | Unset = UNSET,
    response_value_render_option: SheetsSpreadsheetsValuesAppendResponseValueRenderOption | Unset = UNSET,
    value_input_option: SheetsSpreadsheetsValuesAppendValueInputOption | Unset = UNSET,
    xgafv: SheetsSpreadsheetsValuesAppendXgafv | Unset = UNSET,
    access_token: str | Unset = UNSET,
    alt: SheetsSpreadsheetsValuesAppendAlt | Unset = UNSET,
    callback: str | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    upload_protocol: str | Unset = UNSET,
    upload_type: str | Unset = UNSET,

) -> Response[AppendValuesResponse]:
    r"""  Appends values to a spreadsheet. The input range is used to search for existing data and find a
    \"table\" within that range. Values will be appended to the next row of the table, starting with the
    first column of the table. See the [guide](/sheets/api/guides/values#appending_values) and [sample
    code](/sheets/api/samples/writing#append_values) for specific details of how tables are detected and
    data is appended. The caller must specify the spreadsheet ID, range, and a valueInputOption. The
    `valueInputOption` only controls how the input data will be added to the sheet (column-wise or row-
    wise), it does not influence what cell the data starts being written to.

    Args:
        spreadsheet_id (str):
        range_ (str):
        include_values_in_response (bool | Unset):
        insert_data_option (SheetsSpreadsheetsValuesAppendInsertDataOption | Unset):
        response_date_time_render_option
            (SheetsSpreadsheetsValuesAppendResponseDateTimeRenderOption | Unset):
        response_value_render_option (SheetsSpreadsheetsValuesAppendResponseValueRenderOption |
            Unset):
        value_input_option (SheetsSpreadsheetsValuesAppendValueInputOption | Unset):
        xgafv (SheetsSpreadsheetsValuesAppendXgafv | Unset):
        access_token (str | Unset):
        alt (SheetsSpreadsheetsValuesAppendAlt | Unset):
        callback (str | Unset):
        fields (str | Unset):
        key (str | Unset):
        oauth_token (str | Unset):
        pretty_print (bool | Unset):
        quota_user (str | Unset):
        upload_protocol (str | Unset):
        upload_type (str | Unset):
        body (ValueRange | Unset): Data within a range of the spreadsheet.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AppendValuesResponse]
     """


    kwargs = _get_kwargs(
        spreadsheet_id=spreadsheet_id,
range_=range_,
body=body,
include_values_in_response=include_values_in_response,
insert_data_option=insert_data_option,
response_date_time_render_option=response_date_time_render_option,
response_value_render_option=response_value_render_option,
value_input_option=value_input_option,
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
    range_: str,
    *,
    client: AuthenticatedClient,
    body: ValueRange | Unset = UNSET,
    include_values_in_response: bool | Unset = UNSET,
    insert_data_option: SheetsSpreadsheetsValuesAppendInsertDataOption | Unset = UNSET,
    response_date_time_render_option: SheetsSpreadsheetsValuesAppendResponseDateTimeRenderOption | Unset = UNSET,
    response_value_render_option: SheetsSpreadsheetsValuesAppendResponseValueRenderOption | Unset = UNSET,
    value_input_option: SheetsSpreadsheetsValuesAppendValueInputOption | Unset = UNSET,
    xgafv: SheetsSpreadsheetsValuesAppendXgafv | Unset = UNSET,
    access_token: str | Unset = UNSET,
    alt: SheetsSpreadsheetsValuesAppendAlt | Unset = UNSET,
    callback: str | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    upload_protocol: str | Unset = UNSET,
    upload_type: str | Unset = UNSET,

) -> AppendValuesResponse | None:
    r"""  Appends values to a spreadsheet. The input range is used to search for existing data and find a
    \"table\" within that range. Values will be appended to the next row of the table, starting with the
    first column of the table. See the [guide](/sheets/api/guides/values#appending_values) and [sample
    code](/sheets/api/samples/writing#append_values) for specific details of how tables are detected and
    data is appended. The caller must specify the spreadsheet ID, range, and a valueInputOption. The
    `valueInputOption` only controls how the input data will be added to the sheet (column-wise or row-
    wise), it does not influence what cell the data starts being written to.

    Args:
        spreadsheet_id (str):
        range_ (str):
        include_values_in_response (bool | Unset):
        insert_data_option (SheetsSpreadsheetsValuesAppendInsertDataOption | Unset):
        response_date_time_render_option
            (SheetsSpreadsheetsValuesAppendResponseDateTimeRenderOption | Unset):
        response_value_render_option (SheetsSpreadsheetsValuesAppendResponseValueRenderOption |
            Unset):
        value_input_option (SheetsSpreadsheetsValuesAppendValueInputOption | Unset):
        xgafv (SheetsSpreadsheetsValuesAppendXgafv | Unset):
        access_token (str | Unset):
        alt (SheetsSpreadsheetsValuesAppendAlt | Unset):
        callback (str | Unset):
        fields (str | Unset):
        key (str | Unset):
        oauth_token (str | Unset):
        pretty_print (bool | Unset):
        quota_user (str | Unset):
        upload_protocol (str | Unset):
        upload_type (str | Unset):
        body (ValueRange | Unset): Data within a range of the spreadsheet.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AppendValuesResponse
     """


    return (await asyncio_detailed(
        spreadsheet_id=spreadsheet_id,
range_=range_,
client=client,
body=body,
include_values_in_response=include_values_in_response,
insert_data_option=insert_data_option,
response_date_time_render_option=response_date_time_render_option,
response_value_render_option=response_value_render_option,
value_input_option=value_input_option,
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
