from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.find_users_and_groups_avatar_size import FindUsersAndGroupsAvatarSize
from ...models.found_users_and_groups import FoundUsersAndGroups
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    query: str,
    max_results: int | Unset = 50,
    show_avatar: bool | Unset = False,
    field_id: str | Unset = UNSET,
    project_id: list[str] | Unset = UNSET,
    issue_type_id: list[str] | Unset = UNSET,
    avatar_size: FindUsersAndGroupsAvatarSize | Unset = FindUsersAndGroupsAvatarSize.XSMALL,
    case_insensitive: bool | Unset = False,
    exclude_connect_addons: bool | Unset = False,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["query"] = query

    params["maxResults"] = max_results

    params["showAvatar"] = show_avatar

    params["fieldId"] = field_id

    json_project_id: list[str] | Unset = UNSET
    if not isinstance(project_id, Unset):
        json_project_id = project_id


    params["projectId"] = json_project_id

    json_issue_type_id: list[str] | Unset = UNSET
    if not isinstance(issue_type_id, Unset):
        json_issue_type_id = issue_type_id


    params["issueTypeId"] = json_issue_type_id

    json_avatar_size: str | Unset = UNSET
    if not isinstance(avatar_size, Unset):
        json_avatar_size = avatar_size.value

    params["avatarSize"] = json_avatar_size

    params["caseInsensitive"] = case_insensitive

    params["excludeConnectAddons"] = exclude_connect_addons


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/groupuserpicker",
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | FoundUsersAndGroups | None:
    if response.status_code == 200:
        response_200 = FoundUsersAndGroups.from_dict(response.json())



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

    if response.status_code == 429:
        response_429 = cast(Any, None)
        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | FoundUsersAndGroups]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    query: str,
    max_results: int | Unset = 50,
    show_avatar: bool | Unset = False,
    field_id: str | Unset = UNSET,
    project_id: list[str] | Unset = UNSET,
    issue_type_id: list[str] | Unset = UNSET,
    avatar_size: FindUsersAndGroupsAvatarSize | Unset = FindUsersAndGroupsAvatarSize.XSMALL,
    case_insensitive: bool | Unset = False,
    exclude_connect_addons: bool | Unset = False,

) -> Response[Any | FoundUsersAndGroups]:
    """ Find users and groups

     Returns a list of users and groups matching a string. The string is used:

     *  for users, to find a case-insensitive match with display name and e-mail address. Note that if a
    user has hidden their email address in their user profile, partial matches of the email address will
    not find the user. An exact match is required.
     *  for groups, to find a case-sensitive match with group name.

    For example, if the string *tin* is used, records with the display name *Tina*, email address
    *sarah@tinplatetraining.com*, and the group *accounting* would be returned.

    Optionally, the search can be refined to:

     *  the projects and issue types associated with a custom field, such as a user picker. The search
    can then be further refined to return only users and groups that have permission to view specific:

         *  projects.
         *  issue types.

        If multiple projects or issue types are specified, they must be a subset of those enabled for
    the custom field or no results are returned. For example, if a field is enabled for projects A, B,
    and C then the search could be limited to projects B and C. However, if the search is limited to
    projects B and D, nothing is returned.
     *  not return Connect app users and groups.
     *  return groups that have a case-insensitive match with the query.

    The primary use case for this resource is to populate a picker field suggestion list with users or
    groups. To this end, the returned object includes an `html` field for each list. This field
    highlights the matched query term in the item name with the HTML strong tag. Also, each list is
    wrapped in a response object that contains a header for use in a picker, specifically *Showing X of
    Y matching groups*.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Browse users and groups* [global
    permission](https://confluence.atlassian.com/x/yodKLg).

    Args:
        query (str):
        max_results (int | Unset):  Default: 50.
        show_avatar (bool | Unset):  Default: False.
        field_id (str | Unset):
        project_id (list[str] | Unset):
        issue_type_id (list[str] | Unset):
        avatar_size (FindUsersAndGroupsAvatarSize | Unset):  Default:
            FindUsersAndGroupsAvatarSize.XSMALL.
        case_insensitive (bool | Unset):  Default: False.
        exclude_connect_addons (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FoundUsersAndGroups]
     """


    kwargs = _get_kwargs(
        query=query,
max_results=max_results,
show_avatar=show_avatar,
field_id=field_id,
project_id=project_id,
issue_type_id=issue_type_id,
avatar_size=avatar_size,
case_insensitive=case_insensitive,
exclude_connect_addons=exclude_connect_addons,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    query: str,
    max_results: int | Unset = 50,
    show_avatar: bool | Unset = False,
    field_id: str | Unset = UNSET,
    project_id: list[str] | Unset = UNSET,
    issue_type_id: list[str] | Unset = UNSET,
    avatar_size: FindUsersAndGroupsAvatarSize | Unset = FindUsersAndGroupsAvatarSize.XSMALL,
    case_insensitive: bool | Unset = False,
    exclude_connect_addons: bool | Unset = False,

) -> Any | FoundUsersAndGroups | None:
    """ Find users and groups

     Returns a list of users and groups matching a string. The string is used:

     *  for users, to find a case-insensitive match with display name and e-mail address. Note that if a
    user has hidden their email address in their user profile, partial matches of the email address will
    not find the user. An exact match is required.
     *  for groups, to find a case-sensitive match with group name.

    For example, if the string *tin* is used, records with the display name *Tina*, email address
    *sarah@tinplatetraining.com*, and the group *accounting* would be returned.

    Optionally, the search can be refined to:

     *  the projects and issue types associated with a custom field, such as a user picker. The search
    can then be further refined to return only users and groups that have permission to view specific:

         *  projects.
         *  issue types.

        If multiple projects or issue types are specified, they must be a subset of those enabled for
    the custom field or no results are returned. For example, if a field is enabled for projects A, B,
    and C then the search could be limited to projects B and C. However, if the search is limited to
    projects B and D, nothing is returned.
     *  not return Connect app users and groups.
     *  return groups that have a case-insensitive match with the query.

    The primary use case for this resource is to populate a picker field suggestion list with users or
    groups. To this end, the returned object includes an `html` field for each list. This field
    highlights the matched query term in the item name with the HTML strong tag. Also, each list is
    wrapped in a response object that contains a header for use in a picker, specifically *Showing X of
    Y matching groups*.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Browse users and groups* [global
    permission](https://confluence.atlassian.com/x/yodKLg).

    Args:
        query (str):
        max_results (int | Unset):  Default: 50.
        show_avatar (bool | Unset):  Default: False.
        field_id (str | Unset):
        project_id (list[str] | Unset):
        issue_type_id (list[str] | Unset):
        avatar_size (FindUsersAndGroupsAvatarSize | Unset):  Default:
            FindUsersAndGroupsAvatarSize.XSMALL.
        case_insensitive (bool | Unset):  Default: False.
        exclude_connect_addons (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FoundUsersAndGroups
     """


    return sync_detailed(
        client=client,
query=query,
max_results=max_results,
show_avatar=show_avatar,
field_id=field_id,
project_id=project_id,
issue_type_id=issue_type_id,
avatar_size=avatar_size,
case_insensitive=case_insensitive,
exclude_connect_addons=exclude_connect_addons,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    query: str,
    max_results: int | Unset = 50,
    show_avatar: bool | Unset = False,
    field_id: str | Unset = UNSET,
    project_id: list[str] | Unset = UNSET,
    issue_type_id: list[str] | Unset = UNSET,
    avatar_size: FindUsersAndGroupsAvatarSize | Unset = FindUsersAndGroupsAvatarSize.XSMALL,
    case_insensitive: bool | Unset = False,
    exclude_connect_addons: bool | Unset = False,

) -> Response[Any | FoundUsersAndGroups]:
    """ Find users and groups

     Returns a list of users and groups matching a string. The string is used:

     *  for users, to find a case-insensitive match with display name and e-mail address. Note that if a
    user has hidden their email address in their user profile, partial matches of the email address will
    not find the user. An exact match is required.
     *  for groups, to find a case-sensitive match with group name.

    For example, if the string *tin* is used, records with the display name *Tina*, email address
    *sarah@tinplatetraining.com*, and the group *accounting* would be returned.

    Optionally, the search can be refined to:

     *  the projects and issue types associated with a custom field, such as a user picker. The search
    can then be further refined to return only users and groups that have permission to view specific:

         *  projects.
         *  issue types.

        If multiple projects or issue types are specified, they must be a subset of those enabled for
    the custom field or no results are returned. For example, if a field is enabled for projects A, B,
    and C then the search could be limited to projects B and C. However, if the search is limited to
    projects B and D, nothing is returned.
     *  not return Connect app users and groups.
     *  return groups that have a case-insensitive match with the query.

    The primary use case for this resource is to populate a picker field suggestion list with users or
    groups. To this end, the returned object includes an `html` field for each list. This field
    highlights the matched query term in the item name with the HTML strong tag. Also, each list is
    wrapped in a response object that contains a header for use in a picker, specifically *Showing X of
    Y matching groups*.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Browse users and groups* [global
    permission](https://confluence.atlassian.com/x/yodKLg).

    Args:
        query (str):
        max_results (int | Unset):  Default: 50.
        show_avatar (bool | Unset):  Default: False.
        field_id (str | Unset):
        project_id (list[str] | Unset):
        issue_type_id (list[str] | Unset):
        avatar_size (FindUsersAndGroupsAvatarSize | Unset):  Default:
            FindUsersAndGroupsAvatarSize.XSMALL.
        case_insensitive (bool | Unset):  Default: False.
        exclude_connect_addons (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | FoundUsersAndGroups]
     """


    kwargs = _get_kwargs(
        query=query,
max_results=max_results,
show_avatar=show_avatar,
field_id=field_id,
project_id=project_id,
issue_type_id=issue_type_id,
avatar_size=avatar_size,
case_insensitive=case_insensitive,
exclude_connect_addons=exclude_connect_addons,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    query: str,
    max_results: int | Unset = 50,
    show_avatar: bool | Unset = False,
    field_id: str | Unset = UNSET,
    project_id: list[str] | Unset = UNSET,
    issue_type_id: list[str] | Unset = UNSET,
    avatar_size: FindUsersAndGroupsAvatarSize | Unset = FindUsersAndGroupsAvatarSize.XSMALL,
    case_insensitive: bool | Unset = False,
    exclude_connect_addons: bool | Unset = False,

) -> Any | FoundUsersAndGroups | None:
    """ Find users and groups

     Returns a list of users and groups matching a string. The string is used:

     *  for users, to find a case-insensitive match with display name and e-mail address. Note that if a
    user has hidden their email address in their user profile, partial matches of the email address will
    not find the user. An exact match is required.
     *  for groups, to find a case-sensitive match with group name.

    For example, if the string *tin* is used, records with the display name *Tina*, email address
    *sarah@tinplatetraining.com*, and the group *accounting* would be returned.

    Optionally, the search can be refined to:

     *  the projects and issue types associated with a custom field, such as a user picker. The search
    can then be further refined to return only users and groups that have permission to view specific:

         *  projects.
         *  issue types.

        If multiple projects or issue types are specified, they must be a subset of those enabled for
    the custom field or no results are returned. For example, if a field is enabled for projects A, B,
    and C then the search could be limited to projects B and C. However, if the search is limited to
    projects B and D, nothing is returned.
     *  not return Connect app users and groups.
     *  return groups that have a case-insensitive match with the query.

    The primary use case for this resource is to populate a picker field suggestion list with users or
    groups. To this end, the returned object includes an `html` field for each list. This field
    highlights the matched query term in the item name with the HTML strong tag. Also, each list is
    wrapped in a response object that contains a header for use in a picker, specifically *Showing X of
    Y matching groups*.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Browse users and groups* [global
    permission](https://confluence.atlassian.com/x/yodKLg).

    Args:
        query (str):
        max_results (int | Unset):  Default: 50.
        show_avatar (bool | Unset):  Default: False.
        field_id (str | Unset):
        project_id (list[str] | Unset):
        issue_type_id (list[str] | Unset):
        avatar_size (FindUsersAndGroupsAvatarSize | Unset):  Default:
            FindUsersAndGroupsAvatarSize.XSMALL.
        case_insensitive (bool | Unset):  Default: False.
        exclude_connect_addons (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | FoundUsersAndGroups
     """


    return (await asyncio_detailed(
        client=client,
query=query,
max_results=max_results,
show_avatar=show_avatar,
field_id=field_id,
project_id=project_id,
issue_type_id=issue_type_id,
avatar_size=avatar_size,
case_insensitive=case_insensitive,
exclude_connect_addons=exclude_connect_addons,

    )).parsed
