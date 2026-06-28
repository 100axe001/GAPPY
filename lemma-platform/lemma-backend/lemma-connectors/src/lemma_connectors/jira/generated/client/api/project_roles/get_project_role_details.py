from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.project_role_details import ProjectRoleDetails
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    project_id_or_key: str,
    *,
    current_member: bool | Unset = False,
    exclude_connect_addons: bool | Unset = False,

) -> dict[str, Any]:
    

    

    params: dict[str, Any] = {}

    params["currentMember"] = current_member

    params["excludeConnectAddons"] = exclude_connect_addons


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/rest/api/3/project/{project_id_or_key}/roledetails".format(project_id_or_key=quote(str(project_id_or_key), safe=""),),
        "params": params,
    }


    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | list[ProjectRoleDetails] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = ProjectRoleDetails.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | list[ProjectRoleDetails]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id_or_key: str,
    *,
    client: AuthenticatedClient,
    current_member: bool | Unset = False,
    exclude_connect_addons: bool | Unset = False,

) -> Response[Any | list[ProjectRoleDetails]]:
    """ Get project role details

     Returns all [project roles](https://confluence.atlassian.com/x/3odKLg) and the details for each
    role. Note that the list of project roles is common to all projects.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project.

    Args:
        project_id_or_key (str):
        current_member (bool | Unset):  Default: False.
        exclude_connect_addons (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[ProjectRoleDetails]]
     """


    kwargs = _get_kwargs(
        project_id_or_key=project_id_or_key,
current_member=current_member,
exclude_connect_addons=exclude_connect_addons,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    project_id_or_key: str,
    *,
    client: AuthenticatedClient,
    current_member: bool | Unset = False,
    exclude_connect_addons: bool | Unset = False,

) -> Any | list[ProjectRoleDetails] | None:
    """ Get project role details

     Returns all [project roles](https://confluence.atlassian.com/x/3odKLg) and the details for each
    role. Note that the list of project roles is common to all projects.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project.

    Args:
        project_id_or_key (str):
        current_member (bool | Unset):  Default: False.
        exclude_connect_addons (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[ProjectRoleDetails]
     """


    return sync_detailed(
        project_id_or_key=project_id_or_key,
client=client,
current_member=current_member,
exclude_connect_addons=exclude_connect_addons,

    ).parsed

async def asyncio_detailed(
    project_id_or_key: str,
    *,
    client: AuthenticatedClient,
    current_member: bool | Unset = False,
    exclude_connect_addons: bool | Unset = False,

) -> Response[Any | list[ProjectRoleDetails]]:
    """ Get project role details

     Returns all [project roles](https://confluence.atlassian.com/x/3odKLg) and the details for each
    role. Note that the list of project roles is common to all projects.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project.

    Args:
        project_id_or_key (str):
        current_member (bool | Unset):  Default: False.
        exclude_connect_addons (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | list[ProjectRoleDetails]]
     """


    kwargs = _get_kwargs(
        project_id_or_key=project_id_or_key,
current_member=current_member,
exclude_connect_addons=exclude_connect_addons,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    project_id_or_key: str,
    *,
    client: AuthenticatedClient,
    current_member: bool | Unset = False,
    exclude_connect_addons: bool | Unset = False,

) -> Any | list[ProjectRoleDetails] | None:
    """ Get project role details

     Returns all [project roles](https://confluence.atlassian.com/x/3odKLg) and the details for each
    role. Note that the list of project roles is common to all projects.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer projects* [project
    permission](https://confluence.atlassian.com/x/yodKLg) for the project.

    Args:
        project_id_or_key (str):
        current_member (bool | Unset):  Default: False.
        exclude_connect_addons (bool | Unset):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | list[ProjectRoleDetails]
     """


    return (await asyncio_detailed(
        project_id_or_key=project_id_or_key,
client=client,
current_member=current_member,
exclude_connect_addons=exclude_connect_addons,

    )).parsed
