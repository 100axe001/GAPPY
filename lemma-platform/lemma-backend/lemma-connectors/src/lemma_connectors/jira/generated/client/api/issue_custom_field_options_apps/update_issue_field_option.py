from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.issue_field_option import IssueFieldOption
from typing import cast



def _get_kwargs(
    field_key: str,
    option_id: int,
    *,
    body: IssueFieldOption,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/rest/api/3/field/{field_key}/option/{option_id}".format(field_key=quote(str(field_key), safe=""),option_id=quote(str(option_id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | IssueFieldOption | None:
    if response.status_code == 200:
        response_200 = IssueFieldOption.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | IssueFieldOption]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    field_key: str,
    option_id: int,
    *,
    client: AuthenticatedClient,
    body: IssueFieldOption,

) -> Response[Any | IssueFieldOption]:
    """ Update issue field option

     Updates or creates an option for a select list issue field. This operation requires that the option
    ID is provided when creating an option, therefore, the option ID needs to be specified as a path and
    body parameter. The option ID provided in the path and body must be identical.

    Note that this operation **only works for issue field select list options added by Connect apps**,
    it cannot be used with issue field select list options created in Jira or using operations from the
    [Issue custom field options](#api-group-Issue-custom-field-options) resource.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg). Jira permissions are not required for the
    app providing the field.

    Args:
        field_key (str):
        option_id (int):
        body (IssueFieldOption): Details of the options for a select list issue field.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | IssueFieldOption]
     """


    kwargs = _get_kwargs(
        field_key=field_key,
option_id=option_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    field_key: str,
    option_id: int,
    *,
    client: AuthenticatedClient,
    body: IssueFieldOption,

) -> Any | IssueFieldOption | None:
    """ Update issue field option

     Updates or creates an option for a select list issue field. This operation requires that the option
    ID is provided when creating an option, therefore, the option ID needs to be specified as a path and
    body parameter. The option ID provided in the path and body must be identical.

    Note that this operation **only works for issue field select list options added by Connect apps**,
    it cannot be used with issue field select list options created in Jira or using operations from the
    [Issue custom field options](#api-group-Issue-custom-field-options) resource.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg). Jira permissions are not required for the
    app providing the field.

    Args:
        field_key (str):
        option_id (int):
        body (IssueFieldOption): Details of the options for a select list issue field.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | IssueFieldOption
     """


    return sync_detailed(
        field_key=field_key,
option_id=option_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    field_key: str,
    option_id: int,
    *,
    client: AuthenticatedClient,
    body: IssueFieldOption,

) -> Response[Any | IssueFieldOption]:
    """ Update issue field option

     Updates or creates an option for a select list issue field. This operation requires that the option
    ID is provided when creating an option, therefore, the option ID needs to be specified as a path and
    body parameter. The option ID provided in the path and body must be identical.

    Note that this operation **only works for issue field select list options added by Connect apps**,
    it cannot be used with issue field select list options created in Jira or using operations from the
    [Issue custom field options](#api-group-Issue-custom-field-options) resource.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg). Jira permissions are not required for the
    app providing the field.

    Args:
        field_key (str):
        option_id (int):
        body (IssueFieldOption): Details of the options for a select list issue field.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | IssueFieldOption]
     """


    kwargs = _get_kwargs(
        field_key=field_key,
option_id=option_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    field_key: str,
    option_id: int,
    *,
    client: AuthenticatedClient,
    body: IssueFieldOption,

) -> Any | IssueFieldOption | None:
    """ Update issue field option

     Updates or creates an option for a select list issue field. This operation requires that the option
    ID is provided when creating an option, therefore, the option ID needs to be specified as a path and
    body parameter. The option ID provided in the path and body must be identical.

    Note that this operation **only works for issue field select list options added by Connect apps**,
    it cannot be used with issue field select list options created in Jira or using operations from the
    [Issue custom field options](#api-group-Issue-custom-field-options) resource.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg). Jira permissions are not required for the
    app providing the field.

    Args:
        field_key (str):
        option_id (int):
        body (IssueFieldOption): Details of the options for a select list issue field.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | IssueFieldOption
     """


    return (await asyncio_detailed(
        field_key=field_key,
option_id=option_id,
client=client,
body=body,

    )).parsed
