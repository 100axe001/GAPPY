from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.entity_property_details import EntityPropertyDetails
from ...models.migration_resource_update_entity_properties_value_put_entity_type import MigrationResourceUpdateEntityPropertiesValuePutEntityType
from typing import cast
from uuid import UUID



def _get_kwargs(
    entity_type: MigrationResourceUpdateEntityPropertiesValuePutEntityType,
    *,
    body: list[EntityPropertyDetails],
    atlassian_transfer_id: UUID,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["Atlassian-Transfer-Id"] = atlassian_transfer_id



    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/rest/atlassian-connect/1/migration/properties/{entity_type}".format(entity_type=quote(str(entity_type), safe=""),),
    }

    _kwargs["json"] = []
    for body_item_data in body:
        body_item = body_item_data.to_dict()
        _kwargs["json"].append(body_item)




    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 200:
        return None

    if response.status_code == 400:
        return None

    if response.status_code == 403:
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
    entity_type: MigrationResourceUpdateEntityPropertiesValuePutEntityType,
    *,
    client: AuthenticatedClient | Client,
    body: list[EntityPropertyDetails],
    atlassian_transfer_id: UUID,

) -> Response[Any]:
    """ Bulk update entity properties

     Updates the values of multiple entity properties for an object, up to 50 updates per request. This
    operation is for use by Connect apps during app migration.

    Args:
        entity_type (MigrationResourceUpdateEntityPropertiesValuePutEntityType):
        atlassian_transfer_id (UUID):
        body (list[EntityPropertyDetails]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        entity_type=entity_type,
body=body,
atlassian_transfer_id=atlassian_transfer_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    entity_type: MigrationResourceUpdateEntityPropertiesValuePutEntityType,
    *,
    client: AuthenticatedClient | Client,
    body: list[EntityPropertyDetails],
    atlassian_transfer_id: UUID,

) -> Response[Any]:
    """ Bulk update entity properties

     Updates the values of multiple entity properties for an object, up to 50 updates per request. This
    operation is for use by Connect apps during app migration.

    Args:
        entity_type (MigrationResourceUpdateEntityPropertiesValuePutEntityType):
        atlassian_transfer_id (UUID):
        body (list[EntityPropertyDetails]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        entity_type=entity_type,
body=body,
atlassian_transfer_id=atlassian_transfer_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

