from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.custom_field_context_default_value_update import CustomFieldContextDefaultValueUpdate
from typing import cast



def _get_kwargs(
    field_id: str,
    *,
    body: CustomFieldContextDefaultValueUpdate,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/rest/api/3/field/{field_id}/context/defaultValue".format(field_id=quote(str(field_id), safe=""),),
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
    field_id: str,
    *,
    client: AuthenticatedClient,
    body: CustomFieldContextDefaultValueUpdate,

) -> Response[Any]:
    """ Set custom field contexts default values

     Sets default for contexts of a custom field. Default are defined using these objects:

     *  `CustomFieldContextDefaultValueDate` (type `datepicker`) for date fields.
     *  `CustomFieldContextDefaultValueDateTime` (type `datetimepicker`) for date-time fields.
     *  `CustomFieldContextDefaultValueSingleOption` (type `option.single`) for single choice select
    lists and radio buttons.
     *  `CustomFieldContextDefaultValueMultipleOption` (type `option.multiple`) for multiple choice
    select lists and checkboxes.
     *  `CustomFieldContextDefaultValueCascadingOption` (type `option.cascading`) for cascading select
    lists.
     *  `CustomFieldContextSingleUserPickerDefaults` (type `single.user.select`) for single users.
     *  `CustomFieldContextDefaultValueMultiUserPicker` (type `multi.user.select`) for user lists.
     *  `CustomFieldContextDefaultValueSingleGroupPicker` (type `grouppicker.single`) for single choice
    group pickers.
     *  `CustomFieldContextDefaultValueMultipleGroupPicker` (type `grouppicker.multiple`) for multiple
    choice group pickers.
     *  `CustomFieldContextDefaultValueURL` (type `url`) for URLs.
     *  `CustomFieldContextDefaultValueProject` (type `project`) for project pickers.
     *  `CustomFieldContextDefaultValueFloat` (type `float`) for floats (floating-point numbers).
     *  `CustomFieldContextDefaultValueLabels` (type `labels`) for labels.
     *  `CustomFieldContextDefaultValueTextField` (type `textfield`) for text fields.
     *  `CustomFieldContextDefaultValueTextArea` (type `textarea`) for text area fields.
     *  `CustomFieldContextDefaultValueReadOnly` (type `readonly`) for read only (text) fields.
     *  `CustomFieldContextDefaultValueMultipleVersion` (type `version.multiple`) for single choice
    version pickers.
     *  `CustomFieldContextDefaultValueSingleVersion` (type `version.single`) for multiple choice
    version pickers.

    Forge custom fields [types](https://developer.atlassian.com/platform/forge/manifest-
    reference/modules/jira-custom-field-type/#data-types) are also supported, returning:

     *  `CustomFieldContextDefaultValueForgeStringFieldBean` (type `forge.string`) for Forge string
    fields.
     *  `CustomFieldContextDefaultValueForgeMultiStringFieldBean` (type `forge.string.list`) for Forge
    string collection fields.
     *  `CustomFieldContextDefaultValueForgeObjectFieldBean` (type `forge.object`) for Forge object
    fields.
     *  `CustomFieldContextDefaultValueForgeDateTimeFieldBean` (type `forge.datetime`) for Forge date-
    time fields.
     *  `CustomFieldContextDefaultValueForgeGroupFieldBean` (type `forge.group`) for Forge group fields.
     *  `CustomFieldContextDefaultValueForgeMultiGroupFieldBean` (type `forge.group.list`) for Forge
    group collection fields.
     *  `CustomFieldContextDefaultValueForgeNumberFieldBean` (type `forge.number`) for Forge number
    fields.
     *  `CustomFieldContextDefaultValueForgeUserFieldBean` (type `forge.user`) for Forge user fields.
     *  `CustomFieldContextDefaultValueForgeMultiUserFieldBean` (type `forge.user.list`) for Forge user
    collection fields.

    Only one type of default object can be included in a request. To remove a default for a context, set
    the default parameter to `null`.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        field_id (str):
        body (CustomFieldContextDefaultValueUpdate): Default values to update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        field_id=field_id,
body=body,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    field_id: str,
    *,
    client: AuthenticatedClient,
    body: CustomFieldContextDefaultValueUpdate,

) -> Response[Any]:
    """ Set custom field contexts default values

     Sets default for contexts of a custom field. Default are defined using these objects:

     *  `CustomFieldContextDefaultValueDate` (type `datepicker`) for date fields.
     *  `CustomFieldContextDefaultValueDateTime` (type `datetimepicker`) for date-time fields.
     *  `CustomFieldContextDefaultValueSingleOption` (type `option.single`) for single choice select
    lists and radio buttons.
     *  `CustomFieldContextDefaultValueMultipleOption` (type `option.multiple`) for multiple choice
    select lists and checkboxes.
     *  `CustomFieldContextDefaultValueCascadingOption` (type `option.cascading`) for cascading select
    lists.
     *  `CustomFieldContextSingleUserPickerDefaults` (type `single.user.select`) for single users.
     *  `CustomFieldContextDefaultValueMultiUserPicker` (type `multi.user.select`) for user lists.
     *  `CustomFieldContextDefaultValueSingleGroupPicker` (type `grouppicker.single`) for single choice
    group pickers.
     *  `CustomFieldContextDefaultValueMultipleGroupPicker` (type `grouppicker.multiple`) for multiple
    choice group pickers.
     *  `CustomFieldContextDefaultValueURL` (type `url`) for URLs.
     *  `CustomFieldContextDefaultValueProject` (type `project`) for project pickers.
     *  `CustomFieldContextDefaultValueFloat` (type `float`) for floats (floating-point numbers).
     *  `CustomFieldContextDefaultValueLabels` (type `labels`) for labels.
     *  `CustomFieldContextDefaultValueTextField` (type `textfield`) for text fields.
     *  `CustomFieldContextDefaultValueTextArea` (type `textarea`) for text area fields.
     *  `CustomFieldContextDefaultValueReadOnly` (type `readonly`) for read only (text) fields.
     *  `CustomFieldContextDefaultValueMultipleVersion` (type `version.multiple`) for single choice
    version pickers.
     *  `CustomFieldContextDefaultValueSingleVersion` (type `version.single`) for multiple choice
    version pickers.

    Forge custom fields [types](https://developer.atlassian.com/platform/forge/manifest-
    reference/modules/jira-custom-field-type/#data-types) are also supported, returning:

     *  `CustomFieldContextDefaultValueForgeStringFieldBean` (type `forge.string`) for Forge string
    fields.
     *  `CustomFieldContextDefaultValueForgeMultiStringFieldBean` (type `forge.string.list`) for Forge
    string collection fields.
     *  `CustomFieldContextDefaultValueForgeObjectFieldBean` (type `forge.object`) for Forge object
    fields.
     *  `CustomFieldContextDefaultValueForgeDateTimeFieldBean` (type `forge.datetime`) for Forge date-
    time fields.
     *  `CustomFieldContextDefaultValueForgeGroupFieldBean` (type `forge.group`) for Forge group fields.
     *  `CustomFieldContextDefaultValueForgeMultiGroupFieldBean` (type `forge.group.list`) for Forge
    group collection fields.
     *  `CustomFieldContextDefaultValueForgeNumberFieldBean` (type `forge.number`) for Forge number
    fields.
     *  `CustomFieldContextDefaultValueForgeUserFieldBean` (type `forge.user`) for Forge user fields.
     *  `CustomFieldContextDefaultValueForgeMultiUserFieldBean` (type `forge.user.list`) for Forge user
    collection fields.

    Only one type of default object can be included in a request. To remove a default for a context, set
    the default parameter to `null`.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        field_id (str):
        body (CustomFieldContextDefaultValueUpdate): Default values to update.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        field_id=field_id,
body=body,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

