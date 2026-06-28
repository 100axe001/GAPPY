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
    *,
    body: IssueLinkType,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/rest/api/3/issueLinkType",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | IssueLinkType | None:
    if response.status_code == 201:
        response_201 = IssueLinkType.from_dict(response.json())



        return response_201

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
    *,
    client: AuthenticatedClient,
    body: IssueLinkType,

) -> Response[Any | IssueLinkType]:
    """ Create issue link type

     Creates an issue link type. Use this operation to create descriptions of the reasons why issues are
    linked. The issue link type consists of a name and descriptions for a link's inward and outward
    relationships.

    To use this operation, the site must have [issue linking](https://confluence.atlassian.com/x/yoXKM)
    enabled.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
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
        body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: IssueLinkType,

) -> Any | IssueLinkType | None:
    """ Create issue link type

     Creates an issue link type. Use this operation to create descriptions of the reasons why issues are
    linked. The issue link type consists of a name and descriptions for a link's inward and outward
    relationships.

    To use this operation, the site must have [issue linking](https://confluence.atlassian.com/x/yoXKM)
    enabled.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
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
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: IssueLinkType,

) -> Response[Any | IssueLinkType]:
    """ Create issue link type

     Creates an issue link type. Use this operation to create descriptions of the reasons why issues are
    linked. The issue link type consists of a name and descriptions for a link's inward and outward
    relationships.

    To use this operation, the site must have [issue linking](https://confluence.atlassian.com/x/yoXKM)
    enabled.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
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
        body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: IssueLinkType,

) -> Any | IssueLinkType | None:
    """ Create issue link type

     Creates an issue link type. Use this operation to create descriptions of the reasons why issues are
    linked. The issue link type consists of a name and descriptions for a link's inward and outward
    relationships.

    To use this operation, the site must have [issue linking](https://confluence.atlassian.com/x/yoXKM)
    enabled.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
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
        client=client,
body=body,

    )).parsed
