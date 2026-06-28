from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.stars_add_data_body import StarsAddDataBody
from ...models.stars_add_json_body import StarsAddJsonBody
from ...models.stars_add_stars_add_error_schema import StarsAddStarsAddErrorSchema
from ...models.stars_add_stars_add_schema import StarsAddStarsAddSchema
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body:    StarsAddDataBody  |     StarsAddJsonBody  | Unset = UNSET,
    token: str,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["token"] = token



    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/stars.add",
    }

    if isinstance(body, StarsAddDataBody):
        if not isinstance(body, Unset):
            _kwargs["data"] = body.to_dict()

        headers["Content-Type"] = "application/x-www-form-urlencoded"
    if isinstance(body, StarsAddJsonBody):
        
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()


        headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> StarsAddStarsAddErrorSchema | StarsAddStarsAddSchema:
    if response.status_code == 200:
        response_200 = StarsAddStarsAddSchema.from_dict(response.json())



        return response_200

    response_default = StarsAddStarsAddErrorSchema.from_dict(response.json())



    return response_default



def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[StarsAddStarsAddErrorSchema | StarsAddStarsAddSchema]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body:    StarsAddDataBody  |     StarsAddJsonBody  | Unset = UNSET,
    token: str,

) -> Response[StarsAddStarsAddErrorSchema | StarsAddStarsAddSchema]:
    """  Adds a star to an item.

    Args:
        token (str):
        body (StarsAddDataBody | Unset):
        body (StarsAddJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StarsAddStarsAddErrorSchema | StarsAddStarsAddSchema]
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
    body:    StarsAddDataBody  |     StarsAddJsonBody  | Unset = UNSET,
    token: str,

) -> StarsAddStarsAddErrorSchema | StarsAddStarsAddSchema | None:
    """  Adds a star to an item.

    Args:
        token (str):
        body (StarsAddDataBody | Unset):
        body (StarsAddJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StarsAddStarsAddErrorSchema | StarsAddStarsAddSchema
     """


    return sync_detailed(
        client=client,
body=body,
token=token,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body:    StarsAddDataBody  |     StarsAddJsonBody  | Unset = UNSET,
    token: str,

) -> Response[StarsAddStarsAddErrorSchema | StarsAddStarsAddSchema]:
    """  Adds a star to an item.

    Args:
        token (str):
        body (StarsAddDataBody | Unset):
        body (StarsAddJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[StarsAddStarsAddErrorSchema | StarsAddStarsAddSchema]
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
    body:    StarsAddDataBody  |     StarsAddJsonBody  | Unset = UNSET,
    token: str,

) -> StarsAddStarsAddErrorSchema | StarsAddStarsAddSchema | None:
    """  Adds a star to an item.

    Args:
        token (str):
        body (StarsAddDataBody | Unset):
        body (StarsAddJsonBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        StarsAddStarsAddErrorSchema | StarsAddStarsAddSchema
     """


    return (await asyncio_detailed(
        client=client,
body=body,
token=token,

    )).parsed
