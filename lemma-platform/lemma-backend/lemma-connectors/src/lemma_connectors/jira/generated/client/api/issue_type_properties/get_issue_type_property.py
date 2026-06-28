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
    issue_type_id: str,
    property_key: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/issuetype/{issue_type_id}/properties/{property_key}".format(issue_type_id=quote(str(issue_type_id), safe=""),property_key=quote(str(property_key), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | EntityProperty | None:
    if response.status_code == 200:
        response_200 = EntityProperty.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

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
    issue_type_id: str,
    property_key: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any | EntityProperty]:
    """ Get issue type property

     Returns the key and value of the [issue type
    property](https://developer.atlassian.com/cloud/jira/platform/storing-data-without-a-database/#a-id-
    jira-entity-properties-a-jira-entity-properties).

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) to get the
    details of any issue type.
     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) to get the
    details of any issue types associated with the projects the user has permission to browse.

    Args:
        issue_type_id (str):
        property_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EntityProperty]
     """


    kwargs = _get_kwargs(
        issue_type_id=issue_type_id,
property_key=property_key,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    issue_type_id: str,
    property_key: str,
    *,
    client: AuthenticatedClient,

) -> Any | EntityProperty | None:
    """ Get issue type property

     Returns the key and value of the [issue type
    property](https://developer.atlassian.com/cloud/jira/platform/storing-data-without-a-database/#a-id-
    jira-entity-properties-a-jira-entity-properties).

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) to get the
    details of any issue type.
     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) to get the
    details of any issue types associated with the projects the user has permission to browse.

    Args:
        issue_type_id (str):
        property_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EntityProperty
     """


    return sync_detailed(
        issue_type_id=issue_type_id,
property_key=property_key,
client=client,

    ).parsed

async def asyncio_detailed(
    issue_type_id: str,
    property_key: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any | EntityProperty]:
    """ Get issue type property

     Returns the key and value of the [issue type
    property](https://developer.atlassian.com/cloud/jira/platform/storing-data-without-a-database/#a-id-
    jira-entity-properties-a-jira-entity-properties).

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) to get the
    details of any issue type.
     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) to get the
    details of any issue types associated with the projects the user has permission to browse.

    Args:
        issue_type_id (str):
        property_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | EntityProperty]
     """


    kwargs = _get_kwargs(
        issue_type_id=issue_type_id,
property_key=property_key,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    issue_type_id: str,
    property_key: str,
    *,
    client: AuthenticatedClient,

) -> Any | EntityProperty | None:
    """ Get issue type property

     Returns the key and value of the [issue type
    property](https://developer.atlassian.com/cloud/jira/platform/storing-data-without-a-database/#a-id-
    jira-entity-properties-a-jira-entity-properties).

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:**

     *  *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) to get the
    details of any issue type.
     *  *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) to get the
    details of any issue types associated with the projects the user has permission to browse.

    Args:
        issue_type_id (str):
        property_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | EntityProperty
     """


    return (await asyncio_detailed(
        issue_type_id=issue_type_id,
property_key=property_key,
client=client,

    )).parsed
