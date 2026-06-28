from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.page_bean_custom_field_context_default_value import PageBeanCustomFieldContextDefaultValue
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    field_id: str,
    *,
    context_id: list[int] | Unset = UNSET,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    json_context_id: list[int] | Unset = UNSET
    if not isinstance(context_id, Unset):
        json_context_id = context_id


    params["contextId"] = json_context_id

    params["startAt"] = start_at

    params["maxResults"] = max_results


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/field/{field_id}/context/defaultValue".format(field_id=quote(str(field_id), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | PageBeanCustomFieldContextDefaultValue | None:
    if response.status_code == 200:
        response_200 = PageBeanCustomFieldContextDefaultValue.from_dict(response.json())



        return response_200

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | PageBeanCustomFieldContextDefaultValue]:
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
    context_id: list[int] | Unset = UNSET,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,

) -> Response[Any | PageBeanCustomFieldContextDefaultValue]:
    """ Get custom field contexts default values

     Returns a [paginated](#pagination) list of defaults for a custom field. The results can be filtered
    by `contextId`, otherwise all values are returned. If no defaults are set for a context, nothing is
    returned.
    The returned object depends on type of the custom field:

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

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        field_id (str):
        context_id (list[int] | Unset):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PageBeanCustomFieldContextDefaultValue]
     """


    kwargs = _get_kwargs(
        field_id=field_id,
context_id=context_id,
start_at=start_at,
max_results=max_results,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    field_id: str,
    *,
    client: AuthenticatedClient,
    context_id: list[int] | Unset = UNSET,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,

) -> Any | PageBeanCustomFieldContextDefaultValue | None:
    """ Get custom field contexts default values

     Returns a [paginated](#pagination) list of defaults for a custom field. The results can be filtered
    by `contextId`, otherwise all values are returned. If no defaults are set for a context, nothing is
    returned.
    The returned object depends on type of the custom field:

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

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        field_id (str):
        context_id (list[int] | Unset):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PageBeanCustomFieldContextDefaultValue
     """


    return sync_detailed(
        field_id=field_id,
client=client,
context_id=context_id,
start_at=start_at,
max_results=max_results,

    ).parsed

async def asyncio_detailed(
    field_id: str,
    *,
    client: AuthenticatedClient,
    context_id: list[int] | Unset = UNSET,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,

) -> Response[Any | PageBeanCustomFieldContextDefaultValue]:
    """ Get custom field contexts default values

     Returns a [paginated](#pagination) list of defaults for a custom field. The results can be filtered
    by `contextId`, otherwise all values are returned. If no defaults are set for a context, nothing is
    returned.
    The returned object depends on type of the custom field:

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

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        field_id (str):
        context_id (list[int] | Unset):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | PageBeanCustomFieldContextDefaultValue]
     """


    kwargs = _get_kwargs(
        field_id=field_id,
context_id=context_id,
start_at=start_at,
max_results=max_results,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    field_id: str,
    *,
    client: AuthenticatedClient,
    context_id: list[int] | Unset = UNSET,
    start_at: int | Unset = 0,
    max_results: int | Unset = 50,

) -> Any | PageBeanCustomFieldContextDefaultValue | None:
    """ Get custom field contexts default values

     Returns a [paginated](#pagination) list of defaults for a custom field. The results can be filtered
    by `contextId`, otherwise all values are returned. If no defaults are set for a context, nothing is
    returned.
    The returned object depends on type of the custom field:

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

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        field_id (str):
        context_id (list[int] | Unset):
        start_at (int | Unset):  Default: 0.
        max_results (int | Unset):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | PageBeanCustomFieldContextDefaultValue
     """


    return (await asyncio_detailed(
        field_id=field_id,
client=client,
context_id=context_id,
start_at=start_at,
max_results=max_results,

    )).parsed
