from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.issue_link_type import IssueLinkType
from typing import cast



def _get_kwargs(
    issue_link_type_id: str,
    *,
    body: IssueLinkType,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/rest/api/3/issueLinkType/{issue_link_type_id}".format(issue_link_type_id=quote(str(issue_link_type_id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | IssueLinkType | None:
    if response.status_code == 200:
        response_200 = IssueLinkType.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | IssueLinkType]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    issue_link_type_id: str,
    *,
    client: AuthenticatedClient,
    body: IssueLinkType,

) -> Response[Any | IssueLinkType]:
    """ Update issue link type

     Updates an issue link type.

    To use this operation, the site must have [issue linking](https://confluence.atlassian.com/x/yoXKM)
    enabled.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        issue_link_type_id (str):
        body (IssueLinkType): This object is used as follows:

             *  In the [ issueLink](#api-rest-api-3-issueLink-post) resource it defines and reports on
            the type of link between the issues. Find a list of issue link types with [Get issue link
            types](#api-rest-api-3-issueLinkType-get).
             *  In the [ issueLinkType](#api-rest-api-3-issueLinkType-post) resource it defines and
            reports on issue link types.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | IssueLinkType]
     """


    kwargs = _get_kwargs(
        issue_link_type_id=issue_link_type_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    issue_link_type_id: str,
    *,
    client: AuthenticatedClient,
    body: IssueLinkType,

) -> Any | IssueLinkType | None:
    """ Update issue link type

     Updates an issue link type.

    To use this operation, the site must have [issue linking](https://confluence.atlassian.com/x/yoXKM)
    enabled.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        issue_link_type_id (str):
        body (IssueLinkType): This object is used as follows:

             *  In the [ issueLink](#api-rest-api-3-issueLink-post) resource it defines and reports on
            the type of link between the issues. Find a list of issue link types with [Get issue link
            types](#api-rest-api-3-issueLinkType-get).
             *  In the [ issueLinkType](#api-rest-api-3-issueLinkType-post) resource it defines and
            reports on issue link types.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | IssueLinkType
     """


    return sync_detailed(
        issue_link_type_id=issue_link_type_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    issue_link_type_id: str,
    *,
    client: AuthenticatedClient,
    body: IssueLinkType,

) -> Response[Any | IssueLinkType]:
    """ Update issue link type

     Updates an issue link type.

    To use this operation, the site must have [issue linking](https://confluence.atlassian.com/x/yoXKM)
    enabled.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        issue_link_type_id (str):
        body (IssueLinkType): This object is used as follows:

             *  In the [ issueLink](#api-rest-api-3-issueLink-post) resource it defines and reports on
            the type of link between the issues. Find a list of issue link types with [Get issue link
            types](#api-rest-api-3-issueLinkType-get).
             *  In the [ issueLinkType](#api-rest-api-3-issueLinkType-post) resource it defines and
            reports on issue link types.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | IssueLinkType]
     """


    kwargs = _get_kwargs(
        issue_link_type_id=issue_link_type_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    issue_link_type_id: str,
    *,
    client: AuthenticatedClient,
    body: IssueLinkType,

) -> Any | IssueLinkType | None:
    """ Update issue link type

     Updates an issue link type.

    To use this operation, the site must have [issue linking](https://confluence.atlassian.com/x/yoXKM)
    enabled.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        issue_link_type_id (str):
        body (IssueLinkType): This object is used as follows:

             *  In the [ issueLink](#api-rest-api-3-issueLink-post) resource it defines and reports on
            the type of link between the issues. Find a list of issue link types with [Get issue link
            types](#api-rest-api-3-issueLinkType-get).
             *  In the [ issueLinkType](#api-rest-api-3-issueLinkType-post) resource it defines and
            reports on issue link types.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | IssueLinkType
     """


    return (await asyncio_detailed(
        issue_link_type_id=issue_link_type_id,
client=client,
body=body,

    )).parsed
