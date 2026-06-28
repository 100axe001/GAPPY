from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.stars_remove_data_body import StarsRemoveDataBody
from ...models.stars_remove_json_body import StarsRemoveJsonBody
from ...models.stars_remove_stars_remove_error_schema import StarsRemoveStarsRemoveErrorSchema
from ...models.stars_remove_stars_remove_schema import StarsRemoveStarsRemoveSchema
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body:    StarsRemoveDataBody  |     StarsRemoveJsonBody  | Unset = UNSET,
    token: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["token"] = token



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/stars.remove",
    }

    if isinstance(body, StarsRemoveDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, StarsRemoveJsonBody):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> StarsRemoveStarsRemoveErrorSchema | StarsRemoveStarsRemoveSchema:
    if response.status_code == 200:
        response_200 = StarsRemoveStarsRemoveSchema.from_dict(response.json())



        return response_200

    response_default = StarsRemoveStarsRemoveErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[StarsRemoveStarsRemoveErrorSchema | StarsRemoveStarsRemoveSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body:    StarsRemoveDataBody  |     StarsRemoveJsonBody  | Unset = UNSET,
    token: str,

) -> Response[StarsRemoveStarsRemoveErrorSchema | StarsRemoveStarsRemoveSchema]:
    """  Removes a star from an item.

    Args:
        token (str):
        body (StarsRemoveDataBody | Unset):
        body (StarsRemoveJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StarsRemoveStarsRemoveErrorSchema | StarsRemoveStarsRemoveSchema]
     """


    kwargs = _get_kwargs(
        body=body,
token=token,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body:    StarsRemoveDataBody  |     StarsRemoveJsonBody  | Unset = UNSET,
    token: str,

) -> StarsRemoveStarsRemoveErrorSchema | StarsRemoveStarsRemoveSchema | None:
    """  Removes a star from an item.

    Args:
        token (str):
        body (StarsRemoveDataBody | Unset):
        body (StarsRemoveJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StarsRemoveStarsRemoveErrorSchema | StarsRemoveStarsRemoveSchema
     """


    return sync_detailed(
        client=client,
body=body,
token=token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body:    StarsRemoveDataBody  |     StarsRemoveJsonBody  | Unset = UNSET,
    token: str,

) -> Response[StarsRemoveStarsRemoveErrorSchema | StarsRemoveStarsRemoveSchema]:
    """  Removes a star from an item.

    Args:
        token (str):
        body (StarsRemoveDataBody | Unset):
        body (StarsRemoveJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StarsRemoveStarsRemoveErrorSchema | StarsRemoveStarsRemoveSchema]
     """


    kwargs = _get_kwargs(
        body=body,
token=token,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body:    StarsRemoveDataBody  |     StarsRemoveJsonBody  | Unset = UNSET,
    token: str,

) -> StarsRemoveStarsRemoveErrorSchema | StarsRemoveStarsRemoveSchema | None:
    """  Removes a star from an item.

    Args:
        token (str):
        body (StarsRemoveDataBody | Unset):
        body (StarsRemoveJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StarsRemoveStarsRemoveErrorSchema | StarsRemoveStarsRemoveSchema
     """


    return (await asyncio_detailed(
        client=client,
body=body,
token=token,

    )).parsed
