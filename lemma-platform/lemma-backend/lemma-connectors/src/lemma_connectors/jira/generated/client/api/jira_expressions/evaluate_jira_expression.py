from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.error_collection import ErrorCollection
from ...models.jira_expression_eval_request_bean import JiraExpressionEvalRequestBean
from ...models.jira_expression_result import JiraExpressionResult
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: JiraExpressionEvalRequestBean,
    expand: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    params["expand"] = expand


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/rest/api/3/expression/eval",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ErrorCollection | JiraExpressionResult | None:
    if response.status_code == 200:
        response_200 = JiraExpressionResult.from_dict(response.json())



        return response_200

    if response.status_code == 400:
        response_400 = ErrorCollection.from_dict(response.json())



        return response_400

    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401

    if response.status_code == 404:
        response_404 = ErrorCollection.from_dict(response.json())



        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ErrorCollection | JiraExpressionResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: JiraExpressionEvalRequestBean,
    expand: str | Unset = UNSET,

) -> Response[Any | ErrorCollection | JiraExpressionResult]:
    """ Evaluate Jira expression

     Evaluates a Jira expression and returns its value.

    This resource can be used to test Jira expressions that you plan to use elsewhere, or to fetch data
    in a flexible way. Consult the [Jira expressions
    documentation](https://developer.atlassian.com/cloud/jira/platform/jira-expressions/) for more
    details.

    #### Context variables ####

    The following context variables are available to Jira expressions evaluated by this resource. Their
    presence depends on various factors; usually you need to manually request them in the context object
    sent in the payload, but some of them are added automatically under certain conditions.

     *  `user` ([User](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-
    reference#user)): The current user. Always available and equal to `null` if the request is
    anonymous.
     *  `app` ([App](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-
    reference#app)): The [Connect
    app](https://developer.atlassian.com/cloud/jira/platform/index/#connect-apps) that made the request.
    Available only for authenticated requests made by Connect Apps (read more here: [Authentication for
    Connect apps](https://developer.atlassian.com/cloud/jira/platform/security-for-connect-apps/)).
     *  `issue` ([Issue](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-
    reference#issue)): The current issue. Available only when the issue is provided in the request
    context object.
     *  `issues` ([List](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-
    reference#list) of [Issues](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-
    type-reference#issue)): A collection of issues matching a JQL query. Available only when JQL is
    provided in the request context object.
     *  `project` ([Project](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-
    reference#project)): The current project. Available only when the project is provided in the request
    context object.
     *  `sprint` ([Sprint](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-
    reference#sprint)): The current sprint. Available only when the sprint is provided in the request
    context object.
     *  `board` ([Board](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-
    reference#board)): The current board. Available only when the board is provided in the request
    context object.
     *  `serviceDesk` ([ServiceDesk](https://developer.atlassian.com/cloud/jira/platform/jira-
    expressions-type-reference#servicedesk)): The current service desk. Available only when the service
    desk is provided in the request context object.
     *  `customerRequest` ([CustomerRequest](https://developer.atlassian.com/cloud/jira/platform/jira-
    expressions-type-reference#customerrequest)): The current customer request. Available only when the
    customer request is provided in the request context object.

    Also, custom context variables can be passed in the request with their types. Those variables can be
    accessed by key in the Jira expression. These variable types are available for use in a custom
    context:

     *  `user`: A [user](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-
    reference#user) specified as an Atlassian account ID.
     *  `issue`: An [issue](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-
    reference#issue) specified by ID or key. All the fields of the issue object are available in the
    Jira expression.
     *  `json`: A JSON object containing custom content.
     *  `list`: A JSON list of `user`, `issue`, or `json` variable types.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required**: None. However, an expression may return different results
    for different users depending on their permissions. For example, different users may see different
    comments on the same issue.
    Permission to access Jira Software is required to access Jira Software context variables (`board`
    and `sprint`) or fields (for example, `issue.sprint`).

    Args:
        expand (str | Unset):
        body (JiraExpressionEvalRequestBean):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorCollection | JiraExpressionResult]
     """


    kwargs = _get_kwargs(
        body=body,
expand=expand,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: JiraExpressionEvalRequestBean,
    expand: str | Unset = UNSET,

) -> Any | ErrorCollection | JiraExpressionResult | None:
    """ Evaluate Jira expression

     Evaluates a Jira expression and returns its value.

    This resource can be used to test Jira expressions that you plan to use elsewhere, or to fetch data
    in a flexible way. Consult the [Jira expressions
    documentation](https://developer.atlassian.com/cloud/jira/platform/jira-expressions/) for more
    details.

    #### Context variables ####

    The following context variables are available to Jira expressions evaluated by this resource. Their
    presence depends on various factors; usually you need to manually request them in the context object
    sent in the payload, but some of them are added automatically under certain conditions.

     *  `user` ([User](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-
    reference#user)): The current user. Always available and equal to `null` if the request is
    anonymous.
     *  `app` ([App](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-
    reference#app)): The [Connect
    app](https://developer.atlassian.com/cloud/jira/platform/index/#connect-apps) that made the request.
    Available only for authenticated requests made by Connect Apps (read more here: [Authentication for
    Connect apps](https://developer.atlassian.com/cloud/jira/platform/security-for-connect-apps/)).
     *  `issue` ([Issue](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-
    reference#issue)): The current issue. Available only when the issue is provided in the request
    context object.
     *  `issues` ([List](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-
    reference#list) of [Issues](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-
    type-reference#issue)): A collection of issues matching a JQL query. Available only when JQL is
    provided in the request context object.
     *  `project` ([Project](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-
    reference#project)): The current project. Available only when the project is provided in the request
    context object.
     *  `sprint` ([Sprint](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-
    reference#sprint)): The current sprint. Available only when the sprint is provided in the request
    context object.
     *  `board` ([Board](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-
    reference#board)): The current board. Available only when the board is provided in the request
    context object.
     *  `serviceDesk` ([ServiceDesk](https://developer.atlassian.com/cloud/jira/platform/jira-
    expressions-type-reference#servicedesk)): The current service desk. Available only when the service
    desk is provided in the request context object.
     *  `customerRequest` ([CustomerRequest](https://developer.atlassian.com/cloud/jira/platform/jira-
    expressions-type-reference#customerrequest)): The current customer request. Available only when the
    customer request is provided in the request context object.

    Also, custom context variables can be passed in the request with their types. Those variables can be
    accessed by key in the Jira expression. These variable types are available for use in a custom
    context:

     *  `user`: A [user](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-
    reference#user) specified as an Atlassian account ID.
     *  `issue`: An [issue](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-
    reference#issue) specified by ID or key. All the fields of the issue object are available in the
    Jira expression.
     *  `json`: A JSON object containing custom content.
     *  `list`: A JSON list of `user`, `issue`, or `json` variable types.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required**: None. However, an expression may return different results
    for different users depending on their permissions. For example, different users may see different
    comments on the same issue.
    Permission to access Jira Software is required to access Jira Software context variables (`board`
    and `sprint`) or fields (for example, `issue.sprint`).

    Args:
        expand (str | Unset):
        body (JiraExpressionEvalRequestBean):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorCollection | JiraExpressionResult
     """


    return sync_detailed(
        client=client,
body=body,
expand=expand,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: JiraExpressionEvalRequestBean,
    expand: str | Unset = UNSET,

) -> Response[Any | ErrorCollection | JiraExpressionResult]:
    """ Evaluate Jira expression

     Evaluates a Jira expression and returns its value.

    This resource can be used to test Jira expressions that you plan to use elsewhere, or to fetch data
    in a flexible way. Consult the [Jira expressions
    documentation](https://developer.atlassian.com/cloud/jira/platform/jira-expressions/) for more
    details.

    #### Context variables ####

    The following context variables are available to Jira expressions evaluated by this resource. Their
    presence depends on various factors; usually you need to manually request them in the context object
    sent in the payload, but some of them are added automatically under certain conditions.

     *  `user` ([User](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-
    reference#user)): The current user. Always available and equal to `null` if the request is
    anonymous.
     *  `app` ([App](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-
    reference#app)): The [Connect
    app](https://developer.atlassian.com/cloud/jira/platform/index/#connect-apps) that made the request.
    Available only for authenticated requests made by Connect Apps (read more here: [Authentication for
    Connect apps](https://developer.atlassian.com/cloud/jira/platform/security-for-connect-apps/)).
     *  `issue` ([Issue](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-
    reference#issue)): The current issue. Available only when the issue is provided in the request
    context object.
     *  `issues` ([List](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-
    reference#list) of [Issues](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-
    type-reference#issue)): A collection of issues matching a JQL query. Available only when JQL is
    provided in the request context object.
     *  `project` ([Project](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-
    reference#project)): The current project. Available only when the project is provided in the request
    context object.
     *  `sprint` ([Sprint](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-
    reference#sprint)): The current sprint. Available only when the sprint is provided in the request
    context object.
     *  `board` ([Board](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-
    reference#board)): The current board. Available only when the board is provided in the request
    context object.
     *  `serviceDesk` ([ServiceDesk](https://developer.atlassian.com/cloud/jira/platform/jira-
    expressions-type-reference#servicedesk)): The current service desk. Available only when the service
    desk is provided in the request context object.
     *  `customerRequest` ([CustomerRequest](https://developer.atlassian.com/cloud/jira/platform/jira-
    expressions-type-reference#customerrequest)): The current customer request. Available only when the
    customer request is provided in the request context object.

    Also, custom context variables can be passed in the request with their types. Those variables can be
    accessed by key in the Jira expression. These variable types are available for use in a custom
    context:

     *  `user`: A [user](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-
    reference#user) specified as an Atlassian account ID.
     *  `issue`: An [issue](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-
    reference#issue) specified by ID or key. All the fields of the issue object are available in the
    Jira expression.
     *  `json`: A JSON object containing custom content.
     *  `list`: A JSON list of `user`, `issue`, or `json` variable types.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required**: None. However, an expression may return different results
    for different users depending on their permissions. For example, different users may see different
    comments on the same issue.
    Permission to access Jira Software is required to access Jira Software context variables (`board`
    and `sprint`) or fields (for example, `issue.sprint`).

    Args:
        expand (str | Unset):
        body (JiraExpressionEvalRequestBean):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorCollection | JiraExpressionResult]
     """


    kwargs = _get_kwargs(
        body=body,
expand=expand,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: JiraExpressionEvalRequestBean,
    expand: str | Unset = UNSET,

) -> Any | ErrorCollection | JiraExpressionResult | None:
    """ Evaluate Jira expression

     Evaluates a Jira expression and returns its value.

    This resource can be used to test Jira expressions that you plan to use elsewhere, or to fetch data
    in a flexible way. Consult the [Jira expressions
    documentation](https://developer.atlassian.com/cloud/jira/platform/jira-expressions/) for more
    details.

    #### Context variables ####

    The following context variables are available to Jira expressions evaluated by this resource. Their
    presence depends on various factors; usually you need to manually request them in the context object
    sent in the payload, but some of them are added automatically under certain conditions.

     *  `user` ([User](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-
    reference#user)): The current user. Always available and equal to `null` if the request is
    anonymous.
     *  `app` ([App](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-
    reference#app)): The [Connect
    app](https://developer.atlassian.com/cloud/jira/platform/index/#connect-apps) that made the request.
    Available only for authenticated requests made by Connect Apps (read more here: [Authentication for
    Connect apps](https://developer.atlassian.com/cloud/jira/platform/security-for-connect-apps/)).
     *  `issue` ([Issue](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-
    reference#issue)): The current issue. Available only when the issue is provided in the request
    context object.
     *  `issues` ([List](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-
    reference#list) of [Issues](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-
    type-reference#issue)): A collection of issues matching a JQL query. Available only when JQL is
    provided in the request context object.
     *  `project` ([Project](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-
    reference#project)): The current project. Available only when the project is provided in the request
    context object.
     *  `sprint` ([Sprint](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-
    reference#sprint)): The current sprint. Available only when the sprint is provided in the request
    context object.
     *  `board` ([Board](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-
    reference#board)): The current board. Available only when the board is provided in the request
    context object.
     *  `serviceDesk` ([ServiceDesk](https://developer.atlassian.com/cloud/jira/platform/jira-
    expressions-type-reference#servicedesk)): The current service desk. Available only when the service
    desk is provided in the request context object.
     *  `customerRequest` ([CustomerRequest](https://developer.atlassian.com/cloud/jira/platform/jira-
    expressions-type-reference#customerrequest)): The current customer request. Available only when the
    customer request is provided in the request context object.

    Also, custom context variables can be passed in the request with their types. Those variables can be
    accessed by key in the Jira expression. These variable types are available for use in a custom
    context:

     *  `user`: A [user](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-
    reference#user) specified as an Atlassian account ID.
     *  `issue`: An [issue](https://developer.atlassian.com/cloud/jira/platform/jira-expressions-type-
    reference#issue) specified by ID or key. All the fields of the issue object are available in the
    Jira expression.
     *  `json`: A JSON object containing custom content.
     *  `list`: A JSON list of `user`, `issue`, or `json` variable types.

    This operation can be accessed anonymously.

    **[Permissions](#permissions) required**: None. However, an expression may return different results
    for different users depending on their permissions. For example, different users may see different
    comments on the same issue.
    Permission to access Jira Software is required to access Jira Software context variables (`board`
    and `sprint`) or fields (for example, `issue.sprint`).

    Args:
        expand (str | Unset):
        body (JiraExpressionEvalRequestBean):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorCollection | JiraExpressionResult
     """


    return (await asyncio_detailed(
        client=client,
body=body,
expand=expand,

    )).parsed
