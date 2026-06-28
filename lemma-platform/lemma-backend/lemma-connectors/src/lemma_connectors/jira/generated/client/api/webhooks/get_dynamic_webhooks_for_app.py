from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_collection import ErrorCollection
from ...models.page_bean_webhook import PageBeanWebhook
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    start_at: int | Unset = 0,
    max_results: int | Unset = 100,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["startAt"] = start_at

    params["maxResults"] = max_results


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/webhook",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorCollection | PageBeanWebhook | None:
    if response.status_code == 200:
        response_200 = PageBeanWebhook.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorCollection | PageBeanWebhook]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 100,

) -> Response[ErrorCollection | PageBeanWebhook]:
    """ Get dynamic webhooks for app

     Returns a [paginated](#pagination) list of the webhooks registered by the calling app.

    **[Permissions](#permissions) required:** Only
    [Connect](https://developer.atlassian.com/cloud/jira/platform/#connect-apps) and [OAuth
    2.0](https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps) apps can use this
    operation.

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorCollection | PageBeanWebhook]
     """


    kwargs = _get_kwargs(
        start_at=start_at,
max_results=max_results,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 100,

) -> ErrorCollection | PageBeanWebhook | None:
    """ Get dynamic webhooks for app

     Returns a [paginated](#pagination) list of the webhooks registered by the calling app.

    **[Permissions](#permissions) required:** Only
    [Connect](https://developer.atlassian.com/cloud/jira/platform/#connect-apps) and [OAuth
    2.0](https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps) apps can use this
    operation.

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorCollection | PageBeanWebhook
     """


    return sync_detailed(
        client=client,
start_at=start_at,
max_results=max_results,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 100,

) -> Response[ErrorCollection | PageBeanWebhook]:
    """ Get dynamic webhooks for app

     Returns a [paginated](#pagination) list of the webhooks registered by the calling app.

    **[Permissions](#permissions) required:** Only
    [Connect](https://developer.atlassian.com/cloud/jira/platform/#connect-apps) and [OAuth
    2.0](https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps) apps can use this
    operation.

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorCollection | PageBeanWebhook]
     """


    kwargs = _get_kwargs(
        start_at=start_at,
max_results=max_results,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 100,

) -> ErrorCollection | PageBeanWebhook | None:
    """ Get dynamic webhooks for app

     Returns a [paginated](#pagination) list of the webhooks registered by the calling app.

    **[Permissions](#permissions) required:** Only
    [Connect](https://developer.atlassian.com/cloud/jira/platform/#connect-apps) and [OAuth
    2.0](https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps) apps can use this
    operation.

    Args:
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 100.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorCollection | PageBeanWebhook
     """


    return (await asyncio_detailed(
        client=client,
start_at=start_at,
max_results=max_results,

    )).parsed
