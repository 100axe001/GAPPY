from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.docs_documents_get_alt import DocsDocumentsGetAlt
from ...models.docs_documents_get_suggestions_view_mode import DocsDocumentsGetSuggestionsViewMode
from ...models.docs_documents_get_xgafv import DocsDocumentsGetXgafv
from ...models.document import Document
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    document_id: str,
    *,
    suggestions_view_mode: DocsDocumentsGetSuggestionsViewMode | Unset = UNSET,
    xgafv: DocsDocumentsGetXgafv | Unset = UNSET,
    access_token: str | Unset = UNSET,
    alt: DocsDocumentsGetAlt | Unset = UNSET,
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

    json_suggestions_view_mode: str | Unset = UNSET
    if not isinstance(suggestions_view_mode, Unset):
        json_suggestions_view_mode = suggestions_view_mode.value

    params["suggestionsViewMode"] = json_suggestions_view_mode

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
        "url": "/v1/documents/{document_id}".format(document_id=quote(str(document_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Document | None:
    if response.status_code == 200:
        response_200 = Document.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Document]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    document_id: str,
    *,
    client: AuthenticatedClient,
    suggestions_view_mode: DocsDocumentsGetSuggestionsViewMode | Unset = UNSET,
    xgafv: DocsDocumentsGetXgafv | Unset = UNSET,
    access_token: str | Unset = UNSET,
    alt: DocsDocumentsGetAlt | Unset = UNSET,
    callback: str | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    upload_protocol: str | Unset = UNSET,
    upload_type: str | Unset = UNSET,

) -> Response[Document]:
    """  Gets the latest version of the specified document.

    Args:
        document_id (str):
        suggestions_view_mode (DocsDocumentsGetSuggestionsViewMode | Unset):
        xgafv (DocsDocumentsGetXgafv | Unset):
        access_token (str | Unset):
        alt (DocsDocumentsGetAlt | Unset):
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
        Response[Document]
     """


    kwargs = _get_kwargs(
        document_id=document_id,
suggestions_view_mode=suggestions_view_mode,
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
    document_id: str,
    *,
    client: AuthenticatedClient,
    suggestions_view_mode: DocsDocumentsGetSuggestionsViewMode | Unset = UNSET,
    xgafv: DocsDocumentsGetXgafv | Unset = UNSET,
    access_token: str | Unset = UNSET,
    alt: DocsDocumentsGetAlt | Unset = UNSET,
    callback: str | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    upload_protocol: str | Unset = UNSET,
    upload_type: str | Unset = UNSET,

) -> Document | None:
    """  Gets the latest version of the specified document.

    Args:
        document_id (str):
        suggestions_view_mode (DocsDocumentsGetSuggestionsViewMode | Unset):
        xgafv (DocsDocumentsGetXgafv | Unset):
        access_token (str | Unset):
        alt (DocsDocumentsGetAlt | Unset):
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
        Document
     """


    return sync_detailed(
        document_id=document_id,
client=client,
suggestions_view_mode=suggestions_view_mode,
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
    document_id: str,
    *,
    client: AuthenticatedClient,
    suggestions_view_mode: DocsDocumentsGetSuggestionsViewMode | Unset = UNSET,
    xgafv: DocsDocumentsGetXgafv | Unset = UNSET,
    access_token: str | Unset = UNSET,
    alt: DocsDocumentsGetAlt | Unset = UNSET,
    callback: str | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    upload_protocol: str | Unset = UNSET,
    upload_type: str | Unset = UNSET,

) -> Response[Document]:
    """  Gets the latest version of the specified document.

    Args:
        document_id (str):
        suggestions_view_mode (DocsDocumentsGetSuggestionsViewMode | Unset):
        xgafv (DocsDocumentsGetXgafv | Unset):
        access_token (str | Unset):
        alt (DocsDocumentsGetAlt | Unset):
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
        Response[Document]
     """


    kwargs = _get_kwargs(
        document_id=document_id,
suggestions_view_mode=suggestions_view_mode,
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
    document_id: str,
    *,
    client: AuthenticatedClient,
    suggestions_view_mode: DocsDocumentsGetSuggestionsViewMode | Unset = UNSET,
    xgafv: DocsDocumentsGetXgafv | Unset = UNSET,
    access_token: str | Unset = UNSET,
    alt: DocsDocumentsGetAlt | Unset = UNSET,
    callback: str | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    upload_protocol: str | Unset = UNSET,
    upload_type: str | Unset = UNSET,

) -> Document | None:
    """  Gets the latest version of the specified document.

    Args:
        document_id (str):
        suggestions_view_mode (DocsDocumentsGetSuggestionsViewMode | Unset):
        xgafv (DocsDocumentsGetXgafv | Unset):
        access_token (str | Unset):
        alt (DocsDocumentsGetAlt | Unset):
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
        Document
     """


    return (await asyncio_detailed(
        document_id=document_id,
client=client,
suggestions_view_mode=suggestions_view_mode,
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
