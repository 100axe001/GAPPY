from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.sheets_spreadsheets_get_alt import SheetsSpreadsheetsGetAlt
from ...models.sheets_spreadsheets_get_xgafv import SheetsSpreadsheetsGetXgafv
from ...models.spreadsheet import Spreadsheet
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    spreadsheet_id: str,
    *,
    include_grid_data: bool | Unset = UNSET,
    ranges: list[str] | Unset = UNSET,
    xgafv: SheetsSpreadsheetsGetXgafv | Unset = UNSET,
    access_token: str | Unset = UNSET,
    alt: SheetsSpreadsheetsGetAlt | Unset = UNSET,
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

    params["includeGridData"] = include_grid_data

    json_ranges: list[str] | Unset = UNSET
    if not isinstance(ranges, Unset):
        json_ranges = ranges


    params["ranges"] = json_ranges

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
        "url": "/v4/spreadsheets/{spreadsheet_id}".format(spreadsheet_id=quote(str(spreadsheet_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Spreadsheet | None:
    if response.status_code == 200:
        response_200 = Spreadsheet.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Spreadsheet]:
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
    include_grid_data: bool | Unset = UNSET,
    ranges: list[str] | Unset = UNSET,
    xgafv: SheetsSpreadsheetsGetXgafv | Unset = UNSET,
    access_token: str | Unset = UNSET,
    alt: SheetsSpreadsheetsGetAlt | Unset = UNSET,
    callback: str | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    upload_protocol: str | Unset = UNSET,
    upload_type: str | Unset = UNSET,

) -> Response[Spreadsheet]:
    """  Returns the spreadsheet at the given ID. The caller must specify the spreadsheet ID. By default,
    data within grids is not returned. You can include grid data in one of 2 ways: * Specify a [field
    mask](https://developers.google.com/sheets/api/guides/field-masks) listing your desired fields using
    the `fields` URL parameter in HTTP * Set the includeGridData URL parameter to true. If a field mask
    is set, the `includeGridData` parameter is ignored For large spreadsheets, as a best practice,
    retrieve only the specific spreadsheet fields that you want. To retrieve only subsets of spreadsheet
    data, use the ranges URL parameter. Ranges are specified using [A1
    notation](/sheets/api/guides/concepts#cell). You can define a single cell (for example, `A1`) or
    multiple cells (for example, `A1:D5`). You can also get cells from other sheets within the same
    spreadsheet (for example, `Sheet2!A1:C4`) or retrieve multiple ranges at once (for example,
    `?ranges=A1:D5&ranges=Sheet2!A1:C4`). Limiting the range returns only the portions of the
    spreadsheet that intersect the requested ranges.

    Args:
        spreadsheet_id (str):
        include_grid_data (bool | Unset):
        ranges (list[str] | Unset):
        xgafv (SheetsSpreadsheetsGetXgafv | Unset):
        access_token (str | Unset):
        alt (SheetsSpreadsheetsGetAlt | Unset):
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
        Response[Spreadsheet]
     """


    kwargs = _get_kwargs(
        spreadsheet_id=spreadsheet_id,
include_grid_data=include_grid_data,
ranges=ranges,
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
    include_grid_data: bool | Unset = UNSET,
    ranges: list[str] | Unset = UNSET,
    xgafv: SheetsSpreadsheetsGetXgafv | Unset = UNSET,
    access_token: str | Unset = UNSET,
    alt: SheetsSpreadsheetsGetAlt | Unset = UNSET,
    callback: str | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    upload_protocol: str | Unset = UNSET,
    upload_type: str | Unset = UNSET,

) -> Spreadsheet | None:
    """  Returns the spreadsheet at the given ID. The caller must specify the spreadsheet ID. By default,
    data within grids is not returned. You can include grid data in one of 2 ways: * Specify a [field
    mask](https://developers.google.com/sheets/api/guides/field-masks) listing your desired fields using
    the `fields` URL parameter in HTTP * Set the includeGridData URL parameter to true. If a field mask
    is set, the `includeGridData` parameter is ignored For large spreadsheets, as a best practice,
    retrieve only the specific spreadsheet fields that you want. To retrieve only subsets of spreadsheet
    data, use the ranges URL parameter. Ranges are specified using [A1
    notation](/sheets/api/guides/concepts#cell). You can define a single cell (for example, `A1`) or
    multiple cells (for example, `A1:D5`). You can also get cells from other sheets within the same
    spreadsheet (for example, `Sheet2!A1:C4`) or retrieve multiple ranges at once (for example,
    `?ranges=A1:D5&ranges=Sheet2!A1:C4`). Limiting the range returns only the portions of the
    spreadsheet that intersect the requested ranges.

    Args:
        spreadsheet_id (str):
        include_grid_data (bool | Unset):
        ranges (list[str] | Unset):
        xgafv (SheetsSpreadsheetsGetXgafv | Unset):
        access_token (str | Unset):
        alt (SheetsSpreadsheetsGetAlt | Unset):
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
        Spreadsheet
     """


    return sync_detailed(
        spreadsheet_id=spreadsheet_id,
client=client,
include_grid_data=include_grid_data,
ranges=ranges,
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
    include_grid_data: bool | Unset = UNSET,
    ranges: list[str] | Unset = UNSET,
    xgafv: SheetsSpreadsheetsGetXgafv | Unset = UNSET,
    access_token: str | Unset = UNSET,
    alt: SheetsSpreadsheetsGetAlt | Unset = UNSET,
    callback: str | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    upload_protocol: str | Unset = UNSET,
    upload_type: str | Unset = UNSET,

) -> Response[Spreadsheet]:
    """  Returns the spreadsheet at the given ID. The caller must specify the spreadsheet ID. By default,
    data within grids is not returned. You can include grid data in one of 2 ways: * Specify a [field
    mask](https://developers.google.com/sheets/api/guides/field-masks) listing your desired fields using
    the `fields` URL parameter in HTTP * Set the includeGridData URL parameter to true. If a field mask
    is set, the `includeGridData` parameter is ignored For large spreadsheets, as a best practice,
    retrieve only the specific spreadsheet fields that you want. To retrieve only subsets of spreadsheet
    data, use the ranges URL parameter. Ranges are specified using [A1
    notation](/sheets/api/guides/concepts#cell). You can define a single cell (for example, `A1`) or
    multiple cells (for example, `A1:D5`). You can also get cells from other sheets within the same
    spreadsheet (for example, `Sheet2!A1:C4`) or retrieve multiple ranges at once (for example,
    `?ranges=A1:D5&ranges=Sheet2!A1:C4`). Limiting the range returns only the portions of the
    spreadsheet that intersect the requested ranges.

    Args:
        spreadsheet_id (str):
        include_grid_data (bool | Unset):
        ranges (list[str] | Unset):
        xgafv (SheetsSpreadsheetsGetXgafv | Unset):
        access_token (str | Unset):
        alt (SheetsSpreadsheetsGetAlt | Unset):
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
        Response[Spreadsheet]
     """


    kwargs = _get_kwargs(
        spreadsheet_id=spreadsheet_id,
include_grid_data=include_grid_data,
ranges=ranges,
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
    include_grid_data: bool | Unset = UNSET,
    ranges: list[str] | Unset = UNSET,
    xgafv: SheetsSpreadsheetsGetXgafv | Unset = UNSET,
    access_token: str | Unset = UNSET,
    alt: SheetsSpreadsheetsGetAlt | Unset = UNSET,
    callback: str | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    upload_protocol: str | Unset = UNSET,
    upload_type: str | Unset = UNSET,

) -> Spreadsheet | None:
    """  Returns the spreadsheet at the given ID. The caller must specify the spreadsheet ID. By default,
    data within grids is not returned. You can include grid data in one of 2 ways: * Specify a [field
    mask](https://developers.google.com/sheets/api/guides/field-masks) listing your desired fields using
    the `fields` URL parameter in HTTP * Set the includeGridData URL parameter to true. If a field mask
    is set, the `includeGridData` parameter is ignored For large spreadsheets, as a best practice,
    retrieve only the specific spreadsheet fields that you want. To retrieve only subsets of spreadsheet
    data, use the ranges URL parameter. Ranges are specified using [A1
    notation](/sheets/api/guides/concepts#cell). You can define a single cell (for example, `A1`) or
    multiple cells (for example, `A1:D5`). You can also get cells from other sheets within the same
    spreadsheet (for example, `Sheet2!A1:C4`) or retrieve multiple ranges at once (for example,
    `?ranges=A1:D5&ranges=Sheet2!A1:C4`). Limiting the range returns only the portions of the
    spreadsheet that intersect the requested ranges.

    Args:
        spreadsheet_id (str):
        include_grid_data (bool | Unset):
        ranges (list[str] | Unset):
        xgafv (SheetsSpreadsheetsGetXgafv | Unset):
        access_token (str | Unset):
        alt (SheetsSpreadsheetsGetAlt | Unset):
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
        Spreadsheet
     """


    return (await asyncio_detailed(
        spreadsheet_id=spreadsheet_id,
client=client,
include_grid_data=include_grid_data,
ranges=ranges,
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
