from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.entity_property import EntityProperty
from typing import cast



def _get_kwargs(
    dashboard_id: str,
    item_id: str,
    property_key: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/dashboard/{dashboard_id}/items/{item_id}/properties/{property_key}".format(dashboard_id=quote(str(dashboard_id), safe=""),item_id=quote(str(item_id), safe=""),property_key=quote(str(property_key), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | EntityProperty | None:
    if response.status_code == 200:
        response_200 = EntityProperty.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | EntityProperty]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dashboard_id: str,
    item_id: str,
    property_key: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any | EntityProperty]:
    """ Get dashboard item property

     Returns the key and value of a dashboard item property.

    A dashboard item enables an app to add user-specific information to a user dashboard. Dashboard
    items are exposed to users as gadgets that users can add to their dashboards. For more information
    on how users do this, see [Adding and customizing
    gadgets](https://confluence.atlassian.com/x/7AeiLQ).

    When an app creates a dashboard item it registers a callback to receive the dashboard item ID. The
    callback fires whenever the item is rendered or, where the item is configurable, the user edits the
    item. The app then uses this resource to store the item's content or configuration details. For more
    information on working with dashboard items, see [ Building a dashboard item for a JIRA Connect add-
    on](https://developer.atlassian.com/server/jira/platform/guide-building-a-dashboard-item-for-a-jira-
    connect-add-on-33746254/) and the [Dashboard
    Item](https://developer.atlassian.com/cloud/jira/platform/modules/dashboard-item/) documentation.

    There is no resource to set or get dashboard items.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** The user must be the owner of the dashboard or have the
    dashboard shared with them. Note, users with the *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg) are considered owners of the System
    dashboard. The System dashboard is considered to be shared with all other users, and is accessible
    to anonymous users when Jira’s anonymous access is permitted.

    Args:
        dashboard_id (str):
        item_id (str):
        property_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EntityProperty]
     """


    kwargs = _get_kwargs(
        dashboard_id=dashboard_id,
item_id=item_id,
property_key=property_key,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    dashboard_id: str,
    item_id: str,
    property_key: str,
    *,
    client: AuthenticatedClient,

) -> Any | EntityProperty | None:
    """ Get dashboard item property

     Returns the key and value of a dashboard item property.

    A dashboard item enables an app to add user-specific information to a user dashboard. Dashboard
    items are exposed to users as gadgets that users can add to their dashboards. For more information
    on how users do this, see [Adding and customizing
    gadgets](https://confluence.atlassian.com/x/7AeiLQ).

    When an app creates a dashboard item it registers a callback to receive the dashboard item ID. The
    callback fires whenever the item is rendered or, where the item is configurable, the user edits the
    item. The app then uses this resource to store the item's content or configuration details. For more
    information on working with dashboard items, see [ Building a dashboard item for a JIRA Connect add-
    on](https://developer.atlassian.com/server/jira/platform/guide-building-a-dashboard-item-for-a-jira-
    connect-add-on-33746254/) and the [Dashboard
    Item](https://developer.atlassian.com/cloud/jira/platform/modules/dashboard-item/) documentation.

    There is no resource to set or get dashboard items.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** The user must be the owner of the dashboard or have the
    dashboard shared with them. Note, users with the *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg) are considered owners of the System
    dashboard. The System dashboard is considered to be shared with all other users, and is accessible
    to anonymous users when Jira’s anonymous access is permitted.

    Args:
        dashboard_id (str):
        item_id (str):
        property_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EntityProperty
     """


    return sync_detailed(
        dashboard_id=dashboard_id,
item_id=item_id,
property_key=property_key,
client=client,

    ).parsed

async def asyncio_detailed(
    dashboard_id: str,
    item_id: str,
    property_key: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any | EntityProperty]:
    """ Get dashboard item property

     Returns the key and value of a dashboard item property.

    A dashboard item enables an app to add user-specific information to a user dashboard. Dashboard
    items are exposed to users as gadgets that users can add to their dashboards. For more information
    on how users do this, see [Adding and customizing
    gadgets](https://confluence.atlassian.com/x/7AeiLQ).

    When an app creates a dashboard item it registers a callback to receive the dashboard item ID. The
    callback fires whenever the item is rendered or, where the item is configurable, the user edits the
    item. The app then uses this resource to store the item's content or configuration details. For more
    information on working with dashboard items, see [ Building a dashboard item for a JIRA Connect add-
    on](https://developer.atlassian.com/server/jira/platform/guide-building-a-dashboard-item-for-a-jira-
    connect-add-on-33746254/) and the [Dashboard
    Item](https://developer.atlassian.com/cloud/jira/platform/modules/dashboard-item/) documentation.

    There is no resource to set or get dashboard items.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** The user must be the owner of the dashboard or have the
    dashboard shared with them. Note, users with the *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg) are considered owners of the System
    dashboard. The System dashboard is considered to be shared with all other users, and is accessible
    to anonymous users when Jira’s anonymous access is permitted.

    Args:
        dashboard_id (str):
        item_id (str):
        property_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EntityProperty]
     """


    kwargs = _get_kwargs(
        dashboard_id=dashboard_id,
item_id=item_id,
property_key=property_key,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    dashboard_id: str,
    item_id: str,
    property_key: str,
    *,
    client: AuthenticatedClient,

) -> Any | EntityProperty | None:
    """ Get dashboard item property

     Returns the key and value of a dashboard item property.

    A dashboard item enables an app to add user-specific information to a user dashboard. Dashboard
    items are exposed to users as gadgets that users can add to their dashboards. For more information
    on how users do this, see [Adding and customizing
    gadgets](https://confluence.atlassian.com/x/7AeiLQ).

    When an app creates a dashboard item it registers a callback to receive the dashboard item ID. The
    callback fires whenever the item is rendered or, where the item is configurable, the user edits the
    item. The app then uses this resource to store the item's content or configuration details. For more
    information on working with dashboard items, see [ Building a dashboard item for a JIRA Connect add-
    on](https://developer.atlassian.com/server/jira/platform/guide-building-a-dashboard-item-for-a-jira-
    connect-add-on-33746254/) and the [Dashboard
    Item](https://developer.atlassian.com/cloud/jira/platform/modules/dashboard-item/) documentation.

    There is no resource to set or get dashboard items.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** The user must be the owner of the dashboard or have the
    dashboard shared with them. Note, users with the *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg) are considered owners of the System
    dashboard. The System dashboard is considered to be shared with all other users, and is accessible
    to anonymous users when Jira’s anonymous access is permitted.

    Args:
        dashboard_id (str):
        item_id (str):
        property_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EntityProperty
     """


    return (await asyncio_detailed(
        dashboard_id=dashboard_id,
item_id=item_id,
property_key=property_key,
client=client,

    )).parsed
