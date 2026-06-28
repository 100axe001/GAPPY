from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.project_feature_state import ProjectFeatureState
from typing import cast



def _get_kwargs(
    project_id_or_key: str,
    feature_key: str,
    *,
    body: ProjectFeatureState,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/rest/api/3/project/{project_id_or_key}/features/{feature_key}".format(project_id_or_key=quote(str(project_id_or_key), safe=""),feature_key=quote(str(feature_key), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 400:
        return None

    if response.status_code == 401:
        return None

    if response.status_code == 403:
        return None

    if response.status_code == 404:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id_or_key: str,
    feature_key: str,
    *,
    client: AuthenticatedClient,
    body: ProjectFeatureState,

) -> Response[Any]:
    """ Set project feature state

     Sets the state of a project feature.

    Args:
        project_id_or_key (str):
        feature_key (str):
        body (ProjectFeatureState): Details of the feature state.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        project_id_or_key=project_id_or_key,
feature_key=feature_key,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    project_id_or_key: str,
    feature_key: str,
    *,
    client: AuthenticatedClient,
    body: ProjectFeatureState,

) -> Response[Any]:
    """ Set project feature state

     Sets the state of a project feature.

    Args:
        project_id_or_key (str):
        feature_key (str):
        body (ProjectFeatureState): Details of the feature state.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        project_id_or_key=project_id_or_key,
feature_key=feature_key,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

