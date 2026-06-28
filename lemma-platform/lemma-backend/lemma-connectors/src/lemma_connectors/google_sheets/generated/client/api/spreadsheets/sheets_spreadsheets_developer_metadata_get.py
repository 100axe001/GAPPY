from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.developer_metadata import DeveloperMetadata
from ...models.sheets_spreadsheets_developer_metadata_get_alt import SheetsSpreadsheetsDeveloperMetadataGetAlt
from ...models.sheets_spreadsheets_developer_metadata_get_xgafv import SheetsSpreadsheetsDeveloperMetadataGetXgafv
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    spreadsheet_id: str,
    metadata_id: int,
    *,
    xgafv: SheetsSpreadsheetsDeveloperMetadataGetXgafv | Unset = UNSET,
    access_token: str | Unset = UNSET,
    alt: SheetsSpreadsheetsDeveloperMetadataGetAlt | Unset = UNSET,
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
        "url": "/v4/spreadsheets/{spreadsheet_id}/developerMetadata/{metadata_id}".format(spreadsheet_id=quote(str(spreadsheet_id), safe=""),metadata_id=quote(str(metadata_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> DeveloperMetadata | None:
    if response.status_code == 200:
        response_200 = DeveloperMetadata.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[DeveloperMetadata]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    spreadsheet_id: str,
    metadata_id: int,
    *,
    client: AuthenticatedClient,
    xgafv: SheetsSpreadsheetsDeveloperMetadataGetXgafv | Unset = UNSET,
    access_token: str | Unset = UNSET,
    alt: SheetsSpreadsheetsDeveloperMetadataGetAlt | Unset = UNSET,
    callback: str | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    upload_protocol: str | Unset = UNSET,
    upload_type: str | Unset = UNSET,

) -> Response[DeveloperMetadata]:
    """  Returns the developer metadata with the specified ID. The caller must specify the spreadsheet ID and
    the developer metadata's unique metadataId.

    Args:
        spreadsheet_id (str):
        metadata_id (int):
        xgafv (SheetsSpreadsheetsDeveloperMetadataGetXgafv | Unset):
        access_token (str | Unset):
        alt (SheetsSpreadsheetsDeveloperMetadataGetAlt | Unset):
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
        Response[DeveloperMetadata]
     """


    kwargs = _get_kwargs(
        spreadsheet_id=spreadsheet_id,
metadata_id=metadata_id,
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
    metadata_id: int,
    *,
    client: AuthenticatedClient,
    xgafv: SheetsSpreadsheetsDeveloperMetadataGetXgafv | Unset = UNSET,
    access_token: str | Unset = UNSET,
    alt: SheetsSpreadsheetsDeveloperMetadataGetAlt | Unset = UNSET,
    callback: str | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    upload_protocol: str | Unset = UNSET,
    upload_type: str | Unset = UNSET,

) -> DeveloperMetadata | None:
    """  Returns the developer metadata with the specified ID. The caller must specify the spreadsheet ID and
    the developer metadata's unique metadataId.

    Args:
        spreadsheet_id (str):
        metadata_id (int):
        xgafv (SheetsSpreadsheetsDeveloperMetadataGetXgafv | Unset):
        access_token (str | Unset):
        alt (SheetsSpreadsheetsDeveloperMetadataGetAlt | Unset):
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
        DeveloperMetadata
     """


    return sync_detailed(
        spreadsheet_id=spreadsheet_id,
metadata_id=metadata_id,
client=client,
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
    metadata_id: int,
    *,
    client: AuthenticatedClient,
    xgafv: SheetsSpreadsheetsDeveloperMetadataGetXgafv | Unset = UNSET,
    access_token: str | Unset = UNSET,
    alt: SheetsSpreadsheetsDeveloperMetadataGetAlt | Unset = UNSET,
    callback: str | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    upload_protocol: str | Unset = UNSET,
    upload_type: str | Unset = UNSET,

) -> Response[DeveloperMetadata]:
    """  Returns the developer metadata with the specified ID. The caller must specify the spreadsheet ID and
    the developer metadata's unique metadataId.

    Args:
        spreadsheet_id (str):
        metadata_id (int):
        xgafv (SheetsSpreadsheetsDeveloperMetadataGetXgafv | Unset):
        access_token (str | Unset):
        alt (SheetsSpreadsheetsDeveloperMetadataGetAlt | Unset):
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
        Response[DeveloperMetadata]
     """


    kwargs = _get_kwargs(
        spreadsheet_id=spreadsheet_id,
metadata_id=metadata_id,
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
    metadata_id: int,
    *,
    client: AuthenticatedClient,
    xgafv: SheetsSpreadsheetsDeveloperMetadataGetXgafv | Unset = UNSET,
    access_token: str | Unset = UNSET,
    alt: SheetsSpreadsheetsDeveloperMetadataGetAlt | Unset = UNSET,
    callback: str | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    upload_protocol: str | Unset = UNSET,
    upload_type: str | Unset = UNSET,

) -> DeveloperMetadata | None:
    """  Returns the developer metadata with the specified ID. The caller must specify the spreadsheet ID and
    the developer metadata's unique metadataId.

    Args:
        spreadsheet_id (str):
        metadata_id (int):
        xgafv (SheetsSpreadsheetsDeveloperMetadataGetXgafv | Unset):
        access_token (str | Unset):
        alt (SheetsSpreadsheetsDeveloperMetadataGetAlt | Unset):
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
        DeveloperMetadata
     """


    return (await asyncio_detailed(
        spreadsheet_id=spreadsheet_id,
metadata_id=metadata_id,
client=client,
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
