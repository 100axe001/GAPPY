from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.issue_type_details import IssueTypeDetails
from typing import cast



def _get_kwargs(
    
) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/issuetype",
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | list[IssueTypeDetails] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = IssueTypeDetails.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | list[IssueTypeDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[Any | list[IssueTypeDetails]]:
    """ Get all issue types for user

     Returns all issue types.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** Issue types are only returned as follows:

     *  if the user has the *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg), all issue types are returned.
     *  if the user has the *Browse projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for one or more projects, the issue types
    associated with the projects the user has permission to browse are returned.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[IssueTypeDetails]]
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

) -> Any | list[IssueTypeDetails] | None:
    """ Get all issue types for user

     Returns all issue types.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** Issue types are only returned as follows:

     *  if the user has the *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg), all issue types are returned.
     *  if the user has the *Browse projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for one or more projects, the issue types
    associated with the projects the user has permission to browse are returned.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[IssueTypeDetails]
     """


    return sync_detailed(
        client=client,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,

) -> Response[Any | list[IssueTypeDetails]]:
    """ Get all issue types for user

     Returns all issue types.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** Issue types are only returned as follows:

     *  if the user has the *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg), all issue types are returned.
     *  if the user has the *Browse projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for one or more projects, the issue types
    associated with the projects the user has permission to browse are returned.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[IssueTypeDetails]]
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

) -> Any | list[IssueTypeDetails] | None:
    """ Get all issue types for user

     Returns all issue types.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** Issue types are only returned as follows:

     *  if the user has the *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg), all issue types are returned.
     *  if the user has the *Browse projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for one or more projects, the issue types
    associated with the projects the user has permission to browse are returned.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[IssueTypeDetails]
     """


    return (await asyncio_detailed(
        client=client,

    )).parsed
