from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.container_for_registered_webhooks import ContainerForRegisteredWebhooks
from ...models.error_collection import ErrorCollection
from ...models.webhook_registration_details import WebhookRegistrationDetails
from typing import cast



def _get_kwargs(
    *,
    body: WebhookRegistrationDetails,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/rest/api/3/webhook",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ContainerForRegisteredWebhooks | ErrorCollection | None:
    if response.status_code == 200:
        response_200 = ContainerForRegisteredWebhooks.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ErrorCollection.from_dict(response.json())



        return response_400

    if response.status_code == 403:
        response_403 = ErrorCollection.from_dict(response.json())



        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ContainerForRegisteredWebhooks | ErrorCollection]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: WebhookRegistrationDetails,

) -> Response[ContainerForRegisteredWebhooks | ErrorCollection]:
    """ Register dynamic webhooks

     Registers webhooks.

    **NOTE:** for non-public OAuth apps, webhooks are delivered only if there is a match between the app
    owner and the user who registered a dynamic webhook.

    **[Permissions](#permissions) required:** Only
    [Connect](https://developer.atlassian.com/cloud/jira/platform/#connect-apps) and [OAuth
    2.0](https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps) apps can use this
    operation.

    Args:
        body (WebhookRegistrationDetails): Details of webhooks to register.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContainerForRegisteredWebhooks | ErrorCollection]
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
    client: AuthenticatedClient,
    body: WebhookRegistrationDetails,

) -> ContainerForRegisteredWebhooks | ErrorCollection | None:
    """ Register dynamic webhooks

     Registers webhooks.

    **NOTE:** for non-public OAuth apps, webhooks are delivered only if there is a match between the app
    owner and the user who registered a dynamic webhook.

    **[Permissions](#permissions) required:** Only
    [Connect](https://developer.atlassian.com/cloud/jira/platform/#connect-apps) and [OAuth
    2.0](https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps) apps can use this
    operation.

    Args:
        body (WebhookRegistrationDetails): Details of webhooks to register.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContainerForRegisteredWebhooks | ErrorCollection
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: WebhookRegistrationDetails,

) -> Response[ContainerForRegisteredWebhooks | ErrorCollection]:
    """ Register dynamic webhooks

     Registers webhooks.

    **NOTE:** for non-public OAuth apps, webhooks are delivered only if there is a match between the app
    owner and the user who registered a dynamic webhook.

    **[Permissions](#permissions) required:** Only
    [Connect](https://developer.atlassian.com/cloud/jira/platform/#connect-apps) and [OAuth
    2.0](https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps) apps can use this
    operation.

    Args:
        body (WebhookRegistrationDetails): Details of webhooks to register.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ContainerForRegisteredWebhooks | ErrorCollection]
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
    client: AuthenticatedClient,
    body: WebhookRegistrationDetails,

) -> ContainerForRegisteredWebhooks | ErrorCollection | None:
    """ Register dynamic webhooks

     Registers webhooks.

    **NOTE:** for non-public OAuth apps, webhooks are delivered only if there is a match between the app
    owner and the user who registered a dynamic webhook.

    **[Permissions](#permissions) required:** Only
    [Connect](https://developer.atlassian.com/cloud/jira/platform/#connect-apps) and [OAuth
    2.0](https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps) apps can use this
    operation.

    Args:
        body (WebhookRegistrationDetails): Details of webhooks to register.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ContainerForRegisteredWebhooks | ErrorCollection
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
