from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.create_project_details import CreateProjectDetails
from ...models.project_identifiers import ProjectIdentifiers
from typing import cast



def _get_kwargs(
    *,
    body: CreateProjectDetails,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/rest/api/3/project",
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ProjectIdentifiers | None:
    if response.status_code == 201:
        response_201 = ProjectIdentifiers.from_dict(response.json())



        return response_201

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ProjectIdentifiers]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateProjectDetails,

) -> Response[Any | ProjectIdentifiers]:
    """ Create project

     Creates a project based on a project type template, as shown in the following table:

    | Project Type Key | Project Template Key |
    |--|--|
    | `business` | `com.atlassian.jira-core-project-templates:jira-core-simplified-content-management`,
    `com.atlassian.jira-core-project-templates:jira-core-simplified-document-approval`,
    `com.atlassian.jira-core-project-templates:jira-core-simplified-lead-tracking`, `com.atlassian.jira-
    core-project-templates:jira-core-simplified-process-control`, `com.atlassian.jira-core-project-
    templates:jira-core-simplified-procurement`, `com.atlassian.jira-core-project-templates:jira-core-
    simplified-project-management`, `com.atlassian.jira-core-project-templates:jira-core-simplified-
    recruitment`, `com.atlassian.jira-core-project-templates:jira-core-simplified-task-tracking` |
    | `service_desk` | `com.atlassian.servicedesk:simplified-it-service-management`,
    `com.atlassian.servicedesk:simplified-general-service-desk-it`,
    `com.atlassian.servicedesk:simplified-general-service-desk-business`,
    `com.atlassian.servicedesk:simplified-internal-service-desk`, `com.atlassian.servicedesk:simplified-
    external-service-desk`, `com.atlassian.servicedesk:simplified-hr-service-desk`,
    `com.atlassian.servicedesk:simplified-facilities-service-desk`,
    `com.atlassian.servicedesk:simplified-legal-service-desk`, `com.atlassian.servicedesk:simplified-
    analytics-service-desk`, `com.atlassian.servicedesk:simplified-marketing-service-desk`,
    `com.atlassian.servicedesk:simplified-finance-service-desk` |
    | `software` | `com.pyxis.greenhopper.jira:gh-simplified-agility-kanban`,
    `com.pyxis.greenhopper.jira:gh-simplified-agility-scrum`, `com.pyxis.greenhopper.jira:gh-simplified-
    basic`, `com.pyxis.greenhopper.jira:gh-simplified-kanban-classic`, `com.pyxis.greenhopper.jira:gh-
    simplified-scrum-classic` |
    The project types are available according to the installed Jira features as follows:

     *  Jira Core, the default, enables `business` projects.
     *  Jira Service Management enables `service_desk` projects.
     *  Jira Software enables `software` projects.

    To determine which features are installed, go to **Jira settings** > **Apps** > **Manage apps** and
    review the System Apps list. To add Jira Software or Jira Service Management into a JIRA instance,
    use **Jira settings** > **Apps** > **Finding new apps**. For more information, see [ Managing add-
    ons](https://confluence.atlassian.com/x/S31NLg).

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        body (CreateProjectDetails): Details about the project.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProjectIdentifiers]
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
    body: CreateProjectDetails,

) -> Any | ProjectIdentifiers | None:
    """ Create project

     Creates a project based on a project type template, as shown in the following table:

    | Project Type Key | Project Template Key |
    |--|--|
    | `business` | `com.atlassian.jira-core-project-templates:jira-core-simplified-content-management`,
    `com.atlassian.jira-core-project-templates:jira-core-simplified-document-approval`,
    `com.atlassian.jira-core-project-templates:jira-core-simplified-lead-tracking`, `com.atlassian.jira-
    core-project-templates:jira-core-simplified-process-control`, `com.atlassian.jira-core-project-
    templates:jira-core-simplified-procurement`, `com.atlassian.jira-core-project-templates:jira-core-
    simplified-project-management`, `com.atlassian.jira-core-project-templates:jira-core-simplified-
    recruitment`, `com.atlassian.jira-core-project-templates:jira-core-simplified-task-tracking` |
    | `service_desk` | `com.atlassian.servicedesk:simplified-it-service-management`,
    `com.atlassian.servicedesk:simplified-general-service-desk-it`,
    `com.atlassian.servicedesk:simplified-general-service-desk-business`,
    `com.atlassian.servicedesk:simplified-internal-service-desk`, `com.atlassian.servicedesk:simplified-
    external-service-desk`, `com.atlassian.servicedesk:simplified-hr-service-desk`,
    `com.atlassian.servicedesk:simplified-facilities-service-desk`,
    `com.atlassian.servicedesk:simplified-legal-service-desk`, `com.atlassian.servicedesk:simplified-
    analytics-service-desk`, `com.atlassian.servicedesk:simplified-marketing-service-desk`,
    `com.atlassian.servicedesk:simplified-finance-service-desk` |
    | `software` | `com.pyxis.greenhopper.jira:gh-simplified-agility-kanban`,
    `com.pyxis.greenhopper.jira:gh-simplified-agility-scrum`, `com.pyxis.greenhopper.jira:gh-simplified-
    basic`, `com.pyxis.greenhopper.jira:gh-simplified-kanban-classic`, `com.pyxis.greenhopper.jira:gh-
    simplified-scrum-classic` |
    The project types are available according to the installed Jira features as follows:

     *  Jira Core, the default, enables `business` projects.
     *  Jira Service Management enables `service_desk` projects.
     *  Jira Software enables `software` projects.

    To determine which features are installed, go to **Jira settings** > **Apps** > **Manage apps** and
    review the System Apps list. To add Jira Software or Jira Service Management into a JIRA instance,
    use **Jira settings** > **Apps** > **Finding new apps**. For more information, see [ Managing add-
    ons](https://confluence.atlassian.com/x/S31NLg).

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        body (CreateProjectDetails): Details about the project.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProjectIdentifiers
     """


    return sync_detailed(
        client=client,
body=body,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: CreateProjectDetails,

) -> Response[Any | ProjectIdentifiers]:
    """ Create project

     Creates a project based on a project type template, as shown in the following table:

    | Project Type Key | Project Template Key |
    |--|--|
    | `business` | `com.atlassian.jira-core-project-templates:jira-core-simplified-content-management`,
    `com.atlassian.jira-core-project-templates:jira-core-simplified-document-approval`,
    `com.atlassian.jira-core-project-templates:jira-core-simplified-lead-tracking`, `com.atlassian.jira-
    core-project-templates:jira-core-simplified-process-control`, `com.atlassian.jira-core-project-
    templates:jira-core-simplified-procurement`, `com.atlassian.jira-core-project-templates:jira-core-
    simplified-project-management`, `com.atlassian.jira-core-project-templates:jira-core-simplified-
    recruitment`, `com.atlassian.jira-core-project-templates:jira-core-simplified-task-tracking` |
    | `service_desk` | `com.atlassian.servicedesk:simplified-it-service-management`,
    `com.atlassian.servicedesk:simplified-general-service-desk-it`,
    `com.atlassian.servicedesk:simplified-general-service-desk-business`,
    `com.atlassian.servicedesk:simplified-internal-service-desk`, `com.atlassian.servicedesk:simplified-
    external-service-desk`, `com.atlassian.servicedesk:simplified-hr-service-desk`,
    `com.atlassian.servicedesk:simplified-facilities-service-desk`,
    `com.atlassian.servicedesk:simplified-legal-service-desk`, `com.atlassian.servicedesk:simplified-
    analytics-service-desk`, `com.atlassian.servicedesk:simplified-marketing-service-desk`,
    `com.atlassian.servicedesk:simplified-finance-service-desk` |
    | `software` | `com.pyxis.greenhopper.jira:gh-simplified-agility-kanban`,
    `com.pyxis.greenhopper.jira:gh-simplified-agility-scrum`, `com.pyxis.greenhopper.jira:gh-simplified-
    basic`, `com.pyxis.greenhopper.jira:gh-simplified-kanban-classic`, `com.pyxis.greenhopper.jira:gh-
    simplified-scrum-classic` |
    The project types are available according to the installed Jira features as follows:

     *  Jira Core, the default, enables `business` projects.
     *  Jira Service Management enables `service_desk` projects.
     *  Jira Software enables `software` projects.

    To determine which features are installed, go to **Jira settings** > **Apps** > **Manage apps** and
    review the System Apps list. To add Jira Software or Jira Service Management into a JIRA instance,
    use **Jira settings** > **Apps** > **Finding new apps**. For more information, see [ Managing add-
    ons](https://confluence.atlassian.com/x/S31NLg).

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        body (CreateProjectDetails): Details about the project.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ProjectIdentifiers]
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
    body: CreateProjectDetails,

) -> Any | ProjectIdentifiers | None:
    """ Create project

     Creates a project based on a project type template, as shown in the following table:

    | Project Type Key | Project Template Key |
    |--|--|
    | `business` | `com.atlassian.jira-core-project-templates:jira-core-simplified-content-management`,
    `com.atlassian.jira-core-project-templates:jira-core-simplified-document-approval`,
    `com.atlassian.jira-core-project-templates:jira-core-simplified-lead-tracking`, `com.atlassian.jira-
    core-project-templates:jira-core-simplified-process-control`, `com.atlassian.jira-core-project-
    templates:jira-core-simplified-procurement`, `com.atlassian.jira-core-project-templates:jira-core-
    simplified-project-management`, `com.atlassian.jira-core-project-templates:jira-core-simplified-
    recruitment`, `com.atlassian.jira-core-project-templates:jira-core-simplified-task-tracking` |
    | `service_desk` | `com.atlassian.servicedesk:simplified-it-service-management`,
    `com.atlassian.servicedesk:simplified-general-service-desk-it`,
    `com.atlassian.servicedesk:simplified-general-service-desk-business`,
    `com.atlassian.servicedesk:simplified-internal-service-desk`, `com.atlassian.servicedesk:simplified-
    external-service-desk`, `com.atlassian.servicedesk:simplified-hr-service-desk`,
    `com.atlassian.servicedesk:simplified-facilities-service-desk`,
    `com.atlassian.servicedesk:simplified-legal-service-desk`, `com.atlassian.servicedesk:simplified-
    analytics-service-desk`, `com.atlassian.servicedesk:simplified-marketing-service-desk`,
    `com.atlassian.servicedesk:simplified-finance-service-desk` |
    | `software` | `com.pyxis.greenhopper.jira:gh-simplified-agility-kanban`,
    `com.pyxis.greenhopper.jira:gh-simplified-agility-scrum`, `com.pyxis.greenhopper.jira:gh-simplified-
    basic`, `com.pyxis.greenhopper.jira:gh-simplified-kanban-classic`, `com.pyxis.greenhopper.jira:gh-
    simplified-scrum-classic` |
    The project types are available according to the installed Jira features as follows:

     *  Jira Core, the default, enables `business` projects.
     *  Jira Service Management enables `service_desk` projects.
     *  Jira Software enables `software` projects.

    To determine which features are installed, go to **Jira settings** > **Apps** > **Manage apps** and
    review the System Apps list. To add Jira Software or Jira Service Management into a JIRA instance,
    use **Jira settings** > **Apps** > **Finding new apps**. For more information, see [ Managing add-
    ons](https://confluence.atlassian.com/x/S31NLg).

    **[Permissions](#permissions) required:** *Administer Jira* [global
    permission](https://confluence.atlassian.com/x/x4dKLg).

    Args:
        body (CreateProjectDetails): Details about the project.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ProjectIdentifiers
     """


    return (await asyncio_detailed(
        client=client,
body=body,

    )).parsed
