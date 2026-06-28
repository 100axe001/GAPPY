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
    id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/issuetype/{id}".format(id=quote(str(id), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | IssueTypeDetails | None:
    if response.status_code == 200:
        response_200 = IssueTypeDetails.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | IssueTypeDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any | IssueTypeDetails]:
    """ Get issue type

     Returns an issue type.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Browse projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) in a project the issue type is associated
    with or *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | IssueTypeDetails]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    id: str,
    *,
    client: AuthenticatedClient,

) -> Any | IssueTypeDetails | None:
    """ Get issue type

     Returns an issue type.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Browse projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) in a project the issue type is associated
    with or *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | IssueTypeDetails
     """


    return sync_detailed(
        id=id,
client=client,

    ).parsed

async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any | IssueTypeDetails]:
    """ Get issue type

     Returns an issue type.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Browse projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) in a project the issue type is associated
    with or *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | IssueTypeDetails]
     """


    kwargs = _get_kwargs(
        id=id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,

) -> Any | IssueTypeDetails | None:
    """ Get issue type

     Returns an issue type.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Browse projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) in a project the issue type is associated
    with or *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | IssueTypeDetails
     """


    return (await asyncio_detailed(
        id=id,
client=client,

    )).parsed
