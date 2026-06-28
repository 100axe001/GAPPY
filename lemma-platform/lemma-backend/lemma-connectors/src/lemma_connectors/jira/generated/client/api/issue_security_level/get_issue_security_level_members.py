from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.page_bean_issue_security_level_member import PageBeanIssueSecurityLevelMember
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    issue_security_scheme_id: int,
    *,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    issue_security_level_id: list[int] | Unset = UNSET,
    expand: str | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["startAt"] = start_at

    params["maxResults"] = max_results

    json_issue_security_level_id: list[int] | Unset = UNSET
    if not isinstance(issue_security_level_id, Unset):
        json_issue_security_level_id = issue_security_level_id


    params["issueSecurityLevelId"] = json_issue_security_level_id

    params["expand"] = expand


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/issuesecurityschemes/{issue_security_scheme_id}/members".format(issue_security_scheme_id=quote(str(issue_security_scheme_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | PageBeanIssueSecurityLevelMember | None:
    if response.status_code == 200:
        response_200 = PageBeanIssueSecurityLevelMember.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | PageBeanIssueSecurityLevelMember]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    issue_security_scheme_id: int,
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    issue_security_level_id: list[int] | Unset = UNSET,
    expand: str | Unset = UNSET,

) -> Response[Any | PageBeanIssueSecurityLevelMember]:
    """ Get issue security level members

     Returns issue security level members.

    Only issue security level members in context of classic projects are returned.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        issue_security_scheme_id (int):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        issue_security_level_id (list[int] | Unset):
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PageBeanIssueSecurityLevelMember]
     """


    kwargs = _get_kwargs(
        issue_security_scheme_id=issue_security_scheme_id,
start_at=start_at,
max_results=max_results,
issue_security_level_id=issue_security_level_id,
expand=expand,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    issue_security_scheme_id: int,
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    issue_security_level_id: list[int] | Unset = UNSET,
    expand: str | Unset = UNSET,

) -> Any | PageBeanIssueSecurityLevelMember | None:
    """ Get issue security level members

     Returns issue security level members.

    Only issue security level members in context of classic projects are returned.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        issue_security_scheme_id (int):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        issue_security_level_id (list[int] | Unset):
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PageBeanIssueSecurityLevelMember
     """


    return sync_detailed(
        issue_security_scheme_id=issue_security_scheme_id,
client=client,
start_at=start_at,
max_results=max_results,
issue_security_level_id=issue_security_level_id,
expand=expand,

    ).parsed

async def asyncio_detailed(
    issue_security_scheme_id: int,
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    issue_security_level_id: list[int] | Unset = UNSET,
    expand: str | Unset = UNSET,

) -> Response[Any | PageBeanIssueSecurityLevelMember]:
    """ Get issue security level members

     Returns issue security level members.

    Only issue security level members in context of classic projects are returned.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        issue_security_scheme_id (int):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        issue_security_level_id (list[int] | Unset):
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PageBeanIssueSecurityLevelMember]
     """


    kwargs = _get_kwargs(
        issue_security_scheme_id=issue_security_scheme_id,
start_at=start_at,
max_results=max_results,
issue_security_level_id=issue_security_level_id,
expand=expand,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    issue_security_scheme_id: int,
    *,
    client: AuthenticatedClient,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,
    issue_security_level_id: list[int] | Unset = UNSET,
    expand: str | Unset = UNSET,

) -> Any | PageBeanIssueSecurityLevelMember | None:
    """ Get issue security level members

     Returns issue security level members.

    Only issue security level members in context of classic projects are returned.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        issue_security_scheme_id (int):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.
        issue_security_level_id (list[int] | Unset):
        expand (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PageBeanIssueSecurityLevelMember
     """


    return (await asyncio_detailed(
        issue_security_scheme_id=issue_security_scheme_id,
client=client,
start_at=start_at,
max_results=max_results,
issue_security_level_id=issue_security_level_id,
expand=expand,

    )).parsed
