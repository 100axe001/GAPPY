from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_collection import ErrorCollection
from ...models.failed_webhooks import FailedWebhooks
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    max_results: int | Unset = UNSET,
    after: int | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["maxResults"] = max_results

    params["after"] = after


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/webhook/failed",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ErrorCollection | FailedWebhooks | None:
    if response.status_code == 200:
        response_200 = FailedWebhooks.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ErrorCollection | FailedWebhooks]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    max_results: int | Unset = UNSET,
    after: int | Unset = UNSET,

) -> Response[ErrorCollection | FailedWebhooks]:
    """ Get failed webhooks

     Returns webhooks that have recently failed to be delivered to the requesting app after the maximum
    number of retries.

    After 72 hours the failure may no longer be returned by this operation.

    The oldest failure is returned first.

    This method uses a cursor-based pagination. To request the next page use the failure time of the
    last webhook on the list as the `failedAfter` value or use the URL provided in `next`.

    **[Permissions](#permissions) required:** Only [Connect
    apps](https://developer.atlassian.com/cloud/jira/platform/index/#connect-apps) can use this
    operation.

    Args:
        max_results (int | Unset):
        after (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorCollection | FailedWebhooks]
     """


    kwargs = _get_kwargs(
        max_results=max_results,
after=after,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    max_results: int | Unset = UNSET,
    after: int | Unset = UNSET,

) -> ErrorCollection | FailedWebhooks | None:
    """ Get failed webhooks

     Returns webhooks that have recently failed to be delivered to the requesting app after the maximum
    number of retries.

    After 72 hours the failure may no longer be returned by this operation.

    The oldest failure is returned first.

    This method uses a cursor-based pagination. To request the next page use the failure time of the
    last webhook on the list as the `failedAfter` value or use the URL provided in `next`.

    **[Permissions](#permissions) required:** Only [Connect
    apps](https://developer.atlassian.com/cloud/jira/platform/index/#connect-apps) can use this
    operation.

    Args:
        max_results (int | Unset):
        after (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorCollection | FailedWebhooks
     """


    return sync_detailed(
        client=client,
max_results=max_results,
after=after,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    max_results: int | Unset = UNSET,
    after: int | Unset = UNSET,

) -> Response[ErrorCollection | FailedWebhooks]:
    """ Get failed webhooks

     Returns webhooks that have recently failed to be delivered to the requesting app after the maximum
    number of retries.

    After 72 hours the failure may no longer be returned by this operation.

    The oldest failure is returned first.

    This method uses a cursor-based pagination. To request the next page use the failure time of the
    last webhook on the list as the `failedAfter` value or use the URL provided in `next`.

    **[Permissions](#permissions) required:** Only [Connect
    apps](https://developer.atlassian.com/cloud/jira/platform/index/#connect-apps) can use this
    operation.

    Args:
        max_results (int | Unset):
        after (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorCollection | FailedWebhooks]
     """


    kwargs = _get_kwargs(
        max_results=max_results,
after=after,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    max_results: int | Unset = UNSET,
    after: int | Unset = UNSET,

) -> ErrorCollection | FailedWebhooks | None:
    """ Get failed webhooks

     Returns webhooks that have recently failed to be delivered to the requesting app after the maximum
    number of retries.

    After 72 hours the failure may no longer be returned by this operation.

    The oldest failure is returned first.

    This method uses a cursor-based pagination. To request the next page use the failure time of the
    last webhook on the list as the `failedAfter` value or use the URL provided in `next`.

    **[Permissions](#permissions) required:** Only [Connect
    apps](https://developer.atlassian.com/cloud/jira/platform/index/#connect-apps) can use this
    operation.

    Args:
        max_results (int | Unset):
        after (int | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorCollection | FailedWebhooks
     """


    return (await asyncio_detailed(
        client=client,
max_results=max_results,
after=after,

    )).parsed
