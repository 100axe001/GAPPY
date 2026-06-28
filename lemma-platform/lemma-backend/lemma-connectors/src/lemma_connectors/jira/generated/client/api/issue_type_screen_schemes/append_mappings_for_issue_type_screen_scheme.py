from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.issue_type_screen_scheme_mapping_details import IssueTypeScreenSchemeMappingDetails
from typing import cast



def _get_kwargs(
    issue_type_screen_scheme_id: str,
    *,
    body: IssueTypeScreenSchemeMappingDetails,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/rest/api/3/issuetypescreenscheme/{issue_type_screen_scheme_id}/mapping".format(issue_type_screen_scheme_id=quote(str(issue_type_screen_scheme_id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 204:
        return None

    if response.status_code == 400:
        return None

    if response.status_code == 401:
        return None

    if response.status_code == 403:
        return None

    if response.status_code == 404:
        return None

    if response.status_code == 409:
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
    issue_type_screen_scheme_id: str,
    *,
    client: AuthenticatedClient,
    body: IssueTypeScreenSchemeMappingDetails,

) -> Response[Any]:
    """ Append mappings to issue type screen scheme

     Appends issue type to screen scheme mappings to an issue type screen scheme.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        issue_type_screen_scheme_id (str):
        body (IssueTypeScreenSchemeMappingDetails): A list of issue type screen scheme mappings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        issue_type_screen_scheme_id=issue_type_screen_scheme_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    issue_type_screen_scheme_id: str,
    *,
    client: AuthenticatedClient,
    body: IssueTypeScreenSchemeMappingDetails,

) -> Response[Any]:
    """ Append mappings to issue type screen scheme

     Appends issue type to screen scheme mappings to an issue type screen scheme.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        issue_type_screen_scheme_id (str):
        body (IssueTypeScreenSchemeMappingDetails): A list of issue type screen scheme mappings.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        issue_type_screen_scheme_id=issue_type_screen_scheme_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

