from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.connect_modules import ConnectModules
from ...models.error_message import ErrorMessage
from typing import cast



def _get_kwargs(
    *,
    body: ConnectModules,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/rest/atlassian-connect/1/app/module/dynamic",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ErrorMessage | None:
    if response.status_code == 200:
        response_200 = cast(Any, None)
        return response_200

    if response.status_code == 400:
        response_400 = ErrorMessage.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = ErrorMessage.from_dict(response.json())



        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ErrorMessage]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ConnectModules,

) -> Response[Any | ErrorMessage]:
    """ Register modules

     Registers a list of modules.

    **[Permissions](#permissions) required:** Only Connect apps can make this request.

    Args:
        body (ConnectModules):  Example: {'jiraEntityProperties': [{'entityType': 'issue', 'key':
            'dynamic-attachment-entity-property', 'keyConfigurations': [{'extractions': [{'alias':
            'attachmentExtension', 'objectName': 'extension', 'type': 'text'}], 'propertyKey':
            'attachment'}], 'name': {'value': 'Attachment Index Document'}}], 'jiraIssueFields':
            [{'description': {'value': 'A dynamically added single-select field'}, 'extractions':
            [{'name': 'categoryName', 'path': 'category', 'type': 'text'}], 'key': 'dynamic-select-
            field', 'name': {'value': 'Dynamic single select'}, 'type': 'single_select'}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorMessage]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient | Client,
    body: ConnectModules,

) -> Any | ErrorMessage | None:
    """ Register modules

     Registers a list of modules.

    **[Permissions](#permissions) required:** Only Connect apps can make this request.

    Args:
        body (ConnectModules):  Example: {'jiraEntityProperties': [{'entityType': 'issue', 'key':
            'dynamic-attachment-entity-property', 'keyConfigurations': [{'extractions': [{'alias':
            'attachmentExtension', 'objectName': 'extension', 'type': 'text'}], 'propertyKey':
            'attachment'}], 'name': {'value': 'Attachment Index Document'}}], 'jiraIssueFields':
            [{'description': {'value': 'A dynamically added single-select field'}, 'extractions':
            [{'name': 'categoryName', 'path': 'category', 'type': 'text'}], 'key': 'dynamic-select-
            field', 'name': {'value': 'Dynamic single select'}, 'type': 'single_select'}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorMessage
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: ConnectModules,

) -> Response[Any | ErrorMessage]:
    """ Register modules

     Registers a list of modules.

    **[Permissions](#permissions) required:** Only Connect apps can make this request.

    Args:
        body (ConnectModules):  Example: {'jiraEntityProperties': [{'entityType': 'issue', 'key':
            'dynamic-attachment-entity-property', 'keyConfigurations': [{'extractions': [{'alias':
            'attachmentExtension', 'objectName': 'extension', 'type': 'text'}], 'propertyKey':
            'attachment'}], 'name': {'value': 'Attachment Index Document'}}], 'jiraIssueFields':
            [{'description': {'value': 'A dynamically added single-select field'}, 'extractions':
            [{'name': 'categoryName', 'path': 'category', 'type': 'text'}], 'key': 'dynamic-select-
            field', 'name': {'value': 'Dynamic single select'}, 'type': 'single_select'}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorMessage]
     """


    kwargs = _get_kwargs(
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: ConnectModules,

) -> Any | ErrorMessage | None:
    """ Register modules

     Registers a list of modules.

    **[Permissions](#permissions) required:** Only Connect apps can make this request.

    Args:
        body (ConnectModules):  Example: {'jiraEntityProperties': [{'entityType': 'issue', 'key':
            'dynamic-attachment-entity-property', 'keyConfigurations': [{'extractions': [{'alias':
            'attachmentExtension', 'objectName': 'extension', 'type': 'text'}], 'propertyKey':
            'attachment'}], 'name': {'value': 'Attachment Index Document'}}], 'jiraIssueFields':
            [{'description': {'value': 'A dynamically added single-select field'}, 'extractions':
            [{'name': 'categoryName', 'path': 'category', 'type': 'text'}], 'key': 'dynamic-select-
            field', 'name': {'value': 'Dynamic single select'}, 'type': 'single_select'}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorMessage
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
