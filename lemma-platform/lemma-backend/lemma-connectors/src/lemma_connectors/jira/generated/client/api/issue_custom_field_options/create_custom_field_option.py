from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.bulk_custom_field_option_create_request import BulkCustomFieldOptionCreateRequest
from ...models.custom_field_created_context_options_list import CustomFieldCreatedContextOptionsList
from typing import cast



def _get_kwargs(
    field_id: str,
    context_id: int,
    *,
    body: BulkCustomFieldOptionCreateRequest,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/rest/api/3/field/{field_id}/context/{context_id}/option".format(field_id=quote(str(field_id), safe=""),context_id=quote(str(context_id), safe=""),),
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | CustomFieldCreatedContextOptionsList | None:
    if response.status_code == 200:
        response_200 = CustomFieldCreatedContextOptionsList.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | CustomFieldCreatedContextOptionsList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    field_id: str,
    context_id: int,
    *,
    client: AuthenticatedClient,
    body: BulkCustomFieldOptionCreateRequest,

) -> Response[Any | CustomFieldCreatedContextOptionsList]:
    """ Create custom field options (context)

     Creates options and, where the custom select field is of the type Select List (cascading), cascading
    options for a custom select field. The options are added to a context of the field.

    The maximum number of options that can be created per request is 1000 and each field can have a
    maximum of 10000 options.

    This operation works for custom field options created in Jira or the operations from this resource.
    **To work with issue field select list options created for Connect apps use the [Issue custom field
    options (apps)](#api-group-issue-custom-field-options--apps-) operations.**

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        field_id (str):
        context_id (int):
        body (BulkCustomFieldOptionCreateRequest): Details of the options to create for a custom
            field.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CustomFieldCreatedContextOptionsList]
     """


    kwargs = _get_kwargs(
        field_id=field_id,
context_id=context_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    field_id: str,
    context_id: int,
    *,
    client: AuthenticatedClient,
    body: BulkCustomFieldOptionCreateRequest,

) -> Any | CustomFieldCreatedContextOptionsList | None:
    """ Create custom field options (context)

     Creates options and, where the custom select field is of the type Select List (cascading), cascading
    options for a custom select field. The options are added to a context of the field.

    The maximum number of options that can be created per request is 1000 and each field can have a
    maximum of 10000 options.

    This operation works for custom field options created in Jira or the operations from this resource.
    **To work with issue field select list options created for Connect apps use the [Issue custom field
    options (apps)](#api-group-issue-custom-field-options--apps-) operations.**

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        field_id (str):
        context_id (int):
        body (BulkCustomFieldOptionCreateRequest): Details of the options to create for a custom
            field.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CustomFieldCreatedContextOptionsList
     """


    return sync_detailed(
        field_id=field_id,
context_id=context_id,
client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    field_id: str,
    context_id: int,
    *,
    client: AuthenticatedClient,
    body: BulkCustomFieldOptionCreateRequest,

) -> Response[Any | CustomFieldCreatedContextOptionsList]:
    """ Create custom field options (context)

     Creates options and, where the custom select field is of the type Select List (cascading), cascading
    options for a custom select field. The options are added to a context of the field.

    The maximum number of options that can be created per request is 1000 and each field can have a
    maximum of 10000 options.

    This operation works for custom field options created in Jira or the operations from this resource.
    **To work with issue field select list options created for Connect apps use the [Issue custom field
    options (apps)](#api-group-issue-custom-field-options--apps-) operations.**

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        field_id (str):
        context_id (int):
        body (BulkCustomFieldOptionCreateRequest): Details of the options to create for a custom
            field.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CustomFieldCreatedContextOptionsList]
     """


    kwargs = _get_kwargs(
        field_id=field_id,
context_id=context_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    field_id: str,
    context_id: int,
    *,
    client: AuthenticatedClient,
    body: BulkCustomFieldOptionCreateRequest,

) -> Any | CustomFieldCreatedContextOptionsList | None:
    """ Create custom field options (context)

     Creates options and, where the custom select field is of the type Select List (cascading), cascading
    options for a custom select field. The options are added to a context of the field.

    The maximum number of options that can be created per request is 1000 and each field can have a
    maximum of 10000 options.

    This operation works for custom field options created in Jira or the operations from this resource.
    **To work with issue field select list options created for Connect apps use the [Issue custom field
    options (apps)](#api-group-issue-custom-field-options--apps-) operations.**

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        field_id (str):
        context_id (int):
        body (BulkCustomFieldOptionCreateRequest): Details of the options to create for a custom
            field.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CustomFieldCreatedContextOptionsList
     """


    return (await asyncio_detailed(
        field_id=field_id,
context_id=context_id,
client=client,
body=body,

    )).parsed
