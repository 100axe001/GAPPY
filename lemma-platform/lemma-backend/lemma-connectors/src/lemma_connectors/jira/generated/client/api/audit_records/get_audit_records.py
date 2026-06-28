from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.audit_records import AuditRecords
from ...types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime



def _get_kwargs(
    *,
    offset: int | Unset = 0,
    limit: int | Unset = 1000,
    filter_: str | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["offset"] = offset

    params["limit"] = limit

    params["filter"] = filter_

    json_from_: str | Unset = UNSET
    if not isinstance(from_, Unset):
        json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to: str | Unset = UNSET
    if not isinstance(to, Unset):
        json_to = to.isoformat()
    params["to"] = json_to


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/auditing/record",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | AuditRecords | None:
    if response.status_code == 200:
        response_200 = AuditRecords.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | AuditRecords]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    offset: int | Unset = 0,
    limit: int | Unset = 1000,
    filter_: str | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,

) -> Response[Any | AuditRecords]:
    r""" Get audit records

     Returns a list of audit records. The list can be filtered to include items:

     *  where each item in `filter` has at least one match in any of these fields:

         *  `summary`
         *  `category`
         *  `eventSource`
         *  `objectItem.name` If the object is a user, account ID is available to filter.
         *  `objectItem.parentName`
         *  `objectItem.typeName`
         *  `changedValues.changedFrom`
         *  `changedValues.changedTo`
         *  `remoteAddress`

        For example, if `filter` contains *man ed*, an audit record containing `summary\": \"User added
    to group\"` and `\"category\": \"group management\"` is returned.
     *  created on or after a date and time.
     *  created or or before a date and time.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 1000.
        filter_ (str | Unset):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AuditRecords]
     """


    kwargs = _get_kwargs(
        offset=offset,
limit=limit,
filter_=filter_,
from_=from_,
to=to,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    offset: int | Unset = 0,
    limit: int | Unset = 1000,
    filter_: str | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,

) -> Any | AuditRecords | None:
    r""" Get audit records

     Returns a list of audit records. The list can be filtered to include items:

     *  where each item in `filter` has at least one match in any of these fields:

         *  `summary`
         *  `category`
         *  `eventSource`
         *  `objectItem.name` If the object is a user, account ID is available to filter.
         *  `objectItem.parentName`
         *  `objectItem.typeName`
         *  `changedValues.changedFrom`
         *  `changedValues.changedTo`
         *  `remoteAddress`

        For example, if `filter` contains *man ed*, an audit record containing `summary\": \"User added
    to group\"` and `\"category\": \"group management\"` is returned.
     *  created on or after a date and time.
     *  created or or before a date and time.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 1000.
        filter_ (str | Unset):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AuditRecords
     """


    return sync_detailed(
        client=client,
offset=offset,
limit=limit,
filter_=filter_,
from_=from_,
to=to,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    offset: int | Unset = 0,
    limit: int | Unset = 1000,
    filter_: str | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,

) -> Response[Any | AuditRecords]:
    r""" Get audit records

     Returns a list of audit records. The list can be filtered to include items:

     *  where each item in `filter` has at least one match in any of these fields:

         *  `summary`
         *  `category`
         *  `eventSource`
         *  `objectItem.name` If the object is a user, account ID is available to filter.
         *  `objectItem.parentName`
         *  `objectItem.typeName`
         *  `changedValues.changedFrom`
         *  `changedValues.changedTo`
         *  `remoteAddress`

        For example, if `filter` contains *man ed*, an audit record containing `summary\": \"User added
    to group\"` and `\"category\": \"group management\"` is returned.
     *  created on or after a date and time.
     *  created or or before a date and time.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 1000.
        filter_ (str | Unset):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | AuditRecords]
     """


    kwargs = _get_kwargs(
        offset=offset,
limit=limit,
filter_=filter_,
from_=from_,
to=to,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    offset: int | Unset = 0,
    limit: int | Unset = 1000,
    filter_: str | Unset = UNSET,
    from_: datetime.datetime | Unset = UNSET,
    to: datetime.datetime | Unset = UNSET,

) -> Any | AuditRecords | None:
    r""" Get audit records

     Returns a list of audit records. The list can be filtered to include items:

     *  where each item in `filter` has at least one match in any of these fields:

         *  `summary`
         *  `category`
         *  `eventSource`
         *  `objectItem.name` If the object is a user, account ID is available to filter.
         *  `objectItem.parentName`
         *  `objectItem.typeName`
         *  `changedValues.changedFrom`
         *  `changedValues.changedTo`
         *  `remoteAddress`

        For example, if `filter` contains *man ed*, an audit record containing `summary\": \"User added
    to group\"` and `\"category\": \"group management\"` is returned.
     *  created on or after a date and time.
     *  created or or before a date and time.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        offset (int | Unset):  Default: 0.
        limit (int | Unset):  Default: 1000.
        filter_ (str | Unset):
        from_ (datetime.datetime | Unset):
        to (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | AuditRecords
     """


    return (await asyncio_detailed(
        client=client,
offset=offset,
limit=limit,
filter_=filter_,
from_=from_,
to=to,

    )).parsed
