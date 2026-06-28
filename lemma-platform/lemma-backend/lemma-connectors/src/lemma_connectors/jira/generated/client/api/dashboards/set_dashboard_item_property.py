from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors




def _get_kwargs(
    dashboard_id: str,
    item_id: str,
    property_key: str,
    *,
    body: Any,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/rest/api/3/dashboard/{dashboard_id}/items/{item_id}/properties/{property_key}".format(dashboard_id=quote(str(dashboard_id), safe=""),item_id=quote(str(item_id), safe=""),property_key=quote(str(property_key), safe=""),),
    }

    _kwargs["json"] = body


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 200:
        return None

    if response.status_code == 201:
        return None

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
    dashboard_id: str,
    item_id: str,
    property_key: str,
    *,
    client: AuthenticatedClient,
    body: Any,

) -> Response[Any]:
    """ Set dashboard item property

     Sets the value of a dashboard item property. Use this resource in apps to store custom data against
    a dashboard item.

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

    The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON
    blob. The maximum length is 32768 characters.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** The user must be the owner of the dashboard. Note, users
    with the *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) are
    considered owners of the System dashboard.

    Args:
        dashboard_id (str):
        item_id (str):
        property_key (str):
        body (Any):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        dashboard_id=dashboard_id,
item_id=item_id,
property_key=property_key,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    dashboard_id: str,
    item_id: str,
    property_key: str,
    *,
    client: AuthenticatedClient,
    body: Any,

) -> Response[Any]:
    """ Set dashboard item property

     Sets the value of a dashboard item property. Use this resource in apps to store custom data against
    a dashboard item.

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

    The value of the request body must be a [valid](http://tools.ietf.org/html/rfc4627), non-empty JSON
    blob. The maximum length is 32768 characters.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** The user must be the owner of the dashboard. Note, users
    with the *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) are
    considered owners of the System dashboard.

    Args:
        dashboard_id (str):
        item_id (str):
        property_key (str):
        body (Any):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        dashboard_id=dashboard_id,
item_id=item_id,
property_key=property_key,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

