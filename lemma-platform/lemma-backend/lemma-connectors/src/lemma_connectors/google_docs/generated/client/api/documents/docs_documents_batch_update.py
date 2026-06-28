from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.batch_update_document_request import BatchUpdateDocumentRequest
from ...models.batch_update_document_response import BatchUpdateDocumentResponse
from ...models.docs_documents_batch_update_alt import DocsDocumentsBatchUpdateAlt
from ...models.docs_documents_batch_update_xgafv import DocsDocumentsBatchUpdateXgafv
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    document_id: str,
    *,
    body: BatchUpdateDocumentRequest | Unset = UNSET,
    xgafv: DocsDocumentsBatchUpdateXgafv | Unset = UNSET,
    access_token: str | Unset = UNSET,
    alt: DocsDocumentsBatchUpdateAlt | Unset = UNSET,
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
        "url": "/v1/documents/{document_id}:batchUpdate".format(document_id=quote(str(document_id), safe=""),),
        "params": params,
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> BatchUpdateDocumentResponse | None:
    if response.status_code == 200:
        response_200 = BatchUpdateDocumentResponse.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[BatchUpdateDocumentResponse]:
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
    body: BatchUpdateDocumentRequest | Unset = UNSET,
    xgafv: DocsDocumentsBatchUpdateXgafv | Unset = UNSET,
    access_token: str | Unset = UNSET,
    alt: DocsDocumentsBatchUpdateAlt | Unset = UNSET,
    callback: str | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    upload_protocol: str | Unset = UNSET,
    upload_type: str | Unset = UNSET,

) -> Response[BatchUpdateDocumentResponse]:
    """  Applies one or more updates to the document. Each request is validated before being applied. If any
    request is not valid, then the entire request will fail and nothing will be applied. Some requests
    have replies to give you some information about how they are applied. Other requests do not need to
    return information; these each return an empty reply. The order of replies matches that of the
    requests. For example, suppose you call batchUpdate with four updates, and only the third one
    returns information. The response would have two empty replies, the reply to the third request, and
    another empty reply, in that order. Because other users may be editing the document, the document
    might not exactly reflect your changes: your changes may be altered with respect to collaborator
    changes. If there are no collaborators, the document should reflect your changes. In any case, the
    updates in your request are guaranteed to be applied together atomically.

    Args:
        document_id (str):
        xgafv (DocsDocumentsBatchUpdateXgafv | Unset):
        access_token (str | Unset):
        alt (DocsDocumentsBatchUpdateAlt | Unset):
        callback (str | Unset):
        fields (str | Unset):
        key (str | Unset):
        oauth_token (str | Unset):
        pretty_print (bool | Unset):
        quota_user (str | Unset):
        upload_protocol (str | Unset):
        upload_type (str | Unset):
        body (BatchUpdateDocumentRequest | Unset): Request message for BatchUpdateDocument.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BatchUpdateDocumentResponse]
     """


    kwargs = _get_kwargs(
        document_id=document_id,
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
    document_id: str,
    *,
    client: AuthenticatedClient,
    body: BatchUpdateDocumentRequest | Unset = UNSET,
    xgafv: DocsDocumentsBatchUpdateXgafv | Unset = UNSET,
    access_token: str | Unset = UNSET,
    alt: DocsDocumentsBatchUpdateAlt | Unset = UNSET,
    callback: str | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    upload_protocol: str | Unset = UNSET,
    upload_type: str | Unset = UNSET,

) -> BatchUpdateDocumentResponse | None:
    """  Applies one or more updates to the document. Each request is validated before being applied. If any
    request is not valid, then the entire request will fail and nothing will be applied. Some requests
    have replies to give you some information about how they are applied. Other requests do not need to
    return information; these each return an empty reply. The order of replies matches that of the
    requests. For example, suppose you call batchUpdate with four updates, and only the third one
    returns information. The response would have two empty replies, the reply to the third request, and
    another empty reply, in that order. Because other users may be editing the document, the document
    might not exactly reflect your changes: your changes may be altered with respect to collaborator
    changes. If there are no collaborators, the document should reflect your changes. In any case, the
    updates in your request are guaranteed to be applied together atomically.

    Args:
        document_id (str):
        xgafv (DocsDocumentsBatchUpdateXgafv | Unset):
        access_token (str | Unset):
        alt (DocsDocumentsBatchUpdateAlt | Unset):
        callback (str | Unset):
        fields (str | Unset):
        key (str | Unset):
        oauth_token (str | Unset):
        pretty_print (bool | Unset):
        quota_user (str | Unset):
        upload_protocol (str | Unset):
        upload_type (str | Unset):
        body (BatchUpdateDocumentRequest | Unset): Request message for BatchUpdateDocument.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BatchUpdateDocumentResponse
     """


    return sync_detailed(
        document_id=document_id,
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
    document_id: str,
    *,
    client: AuthenticatedClient,
    body: BatchUpdateDocumentRequest | Unset = UNSET,
    xgafv: DocsDocumentsBatchUpdateXgafv | Unset = UNSET,
    access_token: str | Unset = UNSET,
    alt: DocsDocumentsBatchUpdateAlt | Unset = UNSET,
    callback: str | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    upload_protocol: str | Unset = UNSET,
    upload_type: str | Unset = UNSET,

) -> Response[BatchUpdateDocumentResponse]:
    """  Applies one or more updates to the document. Each request is validated before being applied. If any
    request is not valid, then the entire request will fail and nothing will be applied. Some requests
    have replies to give you some information about how they are applied. Other requests do not need to
    return information; these each return an empty reply. The order of replies matches that of the
    requests. For example, suppose you call batchUpdate with four updates, and only the third one
    returns information. The response would have two empty replies, the reply to the third request, and
    another empty reply, in that order. Because other users may be editing the document, the document
    might not exactly reflect your changes: your changes may be altered with respect to collaborator
    changes. If there are no collaborators, the document should reflect your changes. In any case, the
    updates in your request are guaranteed to be applied together atomically.

    Args:
        document_id (str):
        xgafv (DocsDocumentsBatchUpdateXgafv | Unset):
        access_token (str | Unset):
        alt (DocsDocumentsBatchUpdateAlt | Unset):
        callback (str | Unset):
        fields (str | Unset):
        key (str | Unset):
        oauth_token (str | Unset):
        pretty_print (bool | Unset):
        quota_user (str | Unset):
        upload_protocol (str | Unset):
        upload_type (str | Unset):
        body (BatchUpdateDocumentRequest | Unset): Request message for BatchUpdateDocument.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[BatchUpdateDocumentResponse]
     """


    kwargs = _get_kwargs(
        document_id=document_id,
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
    document_id: str,
    *,
    client: AuthenticatedClient,
    body: BatchUpdateDocumentRequest | Unset = UNSET,
    xgafv: DocsDocumentsBatchUpdateXgafv | Unset = UNSET,
    access_token: str | Unset = UNSET,
    alt: DocsDocumentsBatchUpdateAlt | Unset = UNSET,
    callback: str | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    upload_protocol: str | Unset = UNSET,
    upload_type: str | Unset = UNSET,

) -> BatchUpdateDocumentResponse | None:
    """  Applies one or more updates to the document. Each request is validated before being applied. If any
    request is not valid, then the entire request will fail and nothing will be applied. Some requests
    have replies to give you some information about how they are applied. Other requests do not need to
    return information; these each return an empty reply. The order of replies matches that of the
    requests. For example, suppose you call batchUpdate with four updates, and only the third one
    returns information. The response would have two empty replies, the reply to the third request, and
    another empty reply, in that order. Because other users may be editing the document, the document
    might not exactly reflect your changes: your changes may be altered with respect to collaborator
    changes. If there are no collaborators, the document should reflect your changes. In any case, the
    updates in your request are guaranteed to be applied together atomically.

    Args:
        document_id (str):
        xgafv (DocsDocumentsBatchUpdateXgafv | Unset):
        access_token (str | Unset):
        alt (DocsDocumentsBatchUpdateAlt | Unset):
        callback (str | Unset):
        fields (str | Unset):
        key (str | Unset):
        oauth_token (str | Unset):
        pretty_print (bool | Unset):
        quota_user (str | Unset):
        upload_protocol (str | Unset):
        upload_type (str | Unset):
        body (BatchUpdateDocumentRequest | Unset): Request message for BatchUpdateDocument.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        BatchUpdateDocumentResponse
     """


    return (await asyncio_detailed(
        document_id=document_id,
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
