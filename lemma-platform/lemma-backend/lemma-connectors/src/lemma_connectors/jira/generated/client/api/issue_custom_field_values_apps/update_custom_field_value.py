from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.custom_field_value_update_details import CustomFieldValueUpdateDetails
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    field_id_or_key: str,
    *,
    body: CustomFieldValueUpdateDetails,
    generate_changelog: bool | Unset = True,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["generateChangelog"] = generate_changelog


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/rest/api/3/app/field/{field_id_or_key}/value".format(field_id_or_key=quote(str(field_id_or_key), safe=""),),
        "params": params,
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

    if response.status_code == 403:
        return None

    if response.status_code == 404:
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
    field_id_or_key: str,
    *,
    client: AuthenticatedClient,
    body: CustomFieldValueUpdateDetails,
    generate_changelog: bool | Unset = True,

) -> Response[Any]:
    """ Update custom field value

     Updates the value of a custom field on one or more issues. Custom fields can only be updated by the
    Forge app that created them.

    **[Permissions](#permissions) required:** Only the app that created the custom field can update its
    values with this operation.

    Args:
        field_id_or_key (str):
        generate_changelog (bool | Unset):  Default: True.
        body (CustomFieldValueUpdateDetails): Details of updates for a custom field.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        field_id_or_key=field_id_or_key,
body=body,
generate_changelog=generate_changelog,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    field_id_or_key: str,
    *,
    client: AuthenticatedClient,
    body: CustomFieldValueUpdateDetails,
    generate_changelog: bool | Unset = True,

) -> Response[Any]:
    """ Update custom field value

     Updates the value of a custom field on one or more issues. Custom fields can only be updated by the
    Forge app that created them.

    **[Permissions](#permissions) required:** Only the app that created the custom field can update its
    values with this operation.

    Args:
        field_id_or_key (str):
        generate_changelog (bool | Unset):  Default: True.
        body (CustomFieldValueUpdateDetails): Details of updates for a custom field.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        field_id_or_key=field_id_or_key,
body=body,
generate_changelog=generate_changelog,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

