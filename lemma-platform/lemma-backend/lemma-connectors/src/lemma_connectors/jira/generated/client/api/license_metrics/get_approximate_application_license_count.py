from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.license_metric import LicenseMetric
from typing import cast



def _get_kwargs(
    application_key: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/license/approximateLicenseCount/product/{application_key}".format(application_key=quote(str(application_key), safe=""),),
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | LicenseMetric | None:
    if response.status_code == 200:
        response_200 = LicenseMetric.from_dict(response.json())



        return response_200

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | LicenseMetric]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    application_key: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any | LicenseMetric]:
    r""" Get approximate application license count

     Returns the total approximate user account for a specific `jira licence application key`. Please
    note this information is cached with a 7-day lifecycle and could be stale at the time of call.

    #### Application Key ####

    An application key represents a specific version of Jira. See \{@link ApplicationKey\} for details

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        application_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | LicenseMetric]
     """


    kwargs = _get_kwargs(
        application_key=application_key,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    application_key: str,
    *,
    client: AuthenticatedClient,

) -> Any | LicenseMetric | None:
    r""" Get approximate application license count

     Returns the total approximate user account for a specific `jira licence application key`. Please
    note this information is cached with a 7-day lifecycle and could be stale at the time of call.

    #### Application Key ####

    An application key represents a specific version of Jira. See \{@link ApplicationKey\} for details

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        application_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | LicenseMetric
     """


    return sync_detailed(
        application_key=application_key,
client=client,

    ).parsed

async def asyncio_detailed(
    application_key: str,
    *,
    client: AuthenticatedClient,

) -> Response[Any | LicenseMetric]:
    r""" Get approximate application license count

     Returns the total approximate user account for a specific `jira licence application key`. Please
    note this information is cached with a 7-day lifecycle and could be stale at the time of call.

    #### Application Key ####

    An application key represents a specific version of Jira. See \{@link ApplicationKey\} for details

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        application_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | LicenseMetric]
     """


    kwargs = _get_kwargs(
        application_key=application_key,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    application_key: str,
    *,
    client: AuthenticatedClient,

) -> Any | LicenseMetric | None:
    r""" Get approximate application license count

     Returns the total approximate user account for a specific `jira licence application key`. Please
    note this information is cached with a 7-day lifecycle and could be stale at the time of call.

    #### Application Key ####

    An application key represents a specific version of Jira. See \{@link ApplicationKey\} for details

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        application_key (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | LicenseMetric
     """


    return (await asyncio_detailed(
        application_key=application_key,
client=client,

    )).parsed
