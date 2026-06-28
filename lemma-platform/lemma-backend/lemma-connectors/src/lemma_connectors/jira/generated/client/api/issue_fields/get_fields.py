from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.field_details import FieldDetails
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/field",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | list[FieldDetails] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = FieldDetails.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | list[FieldDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[Any | list[FieldDetails]]:
    """ Get fields

     Returns system and custom issue fields according to the following rules:

     *  Fields that cannot be added to the issue navigator are always returned.
     *  Fields that cannot be placed on an issue screen are always returned.
     *  Fields that depend on global Jira settings are only returned if the setting is enabled. That is,
    timetracking fields, subtasks, votes, and watches.
     *  For all other fields, this operation only returns the fields that the user has permission to
    view (that is, the field is used in at least one project that the user has *Browse Projects*
    [project permission](https://confluence.atlassian.com/x/yodKLg) for.)

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[FieldDetails]]
     """


    kwargs = _get_kwargs(
        
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,

) -> Any | list[FieldDetails] | None:
    """ Get fields

     Returns system and custom issue fields according to the following rules:

     *  Fields that cannot be added to the issue navigator are always returned.
     *  Fields that cannot be placed on an issue screen are always returned.
     *  Fields that depend on global Jira settings are only returned if the setting is enabled. That is,
    timetracking fields, subtasks, votes, and watches.
     *  For all other fields, this operation only returns the fields that the user has permission to
    view (that is, the field is used in at least one project that the user has *Browse Projects*
    [project permission](https://confluence.atlassian.com/x/yodKLg) for.)

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[FieldDetails]
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[Any | list[FieldDetails]]:
    """ Get fields

     Returns system and custom issue fields according to the following rules:

     *  Fields that cannot be added to the issue navigator are always returned.
     *  Fields that cannot be placed on an issue screen are always returned.
     *  Fields that depend on global Jira settings are only returned if the setting is enabled. That is,
    timetracking fields, subtasks, votes, and watches.
     *  For all other fields, this operation only returns the fields that the user has permission to
    view (that is, the field is used in at least one project that the user has *Browse Projects*
    [project permission](https://confluence.atlassian.com/x/yodKLg) for.)

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[FieldDetails]]
     """


    kwargs = _get_kwargs(
        
    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,

) -> Any | list[FieldDetails] | None:
    """ Get fields

     Returns system and custom issue fields according to the following rules:

     *  Fields that cannot be added to the issue navigator are always returned.
     *  Fields that cannot be placed on an issue screen are always returned.
     *  Fields that depend on global Jira settings are only returned if the setting is enabled. That is,
    timetracking fields, subtasks, votes, and watches.
     *  For all other fields, this operation only returns the fields that the user has permission to
    view (that is, the field is used in at least one project that the user has *Browse Projects*
    [project permission](https://confluence.atlassian.com/x/yodKLg) for.)

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** None.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[FieldDetails]
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
