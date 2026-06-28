from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.analyse_expression_check import AnalyseExpressionCheck
from ...models.error_collection import ErrorCollection
from ...models.jira_expression_for_analysis import JiraExpressionForAnalysis
from ...models.jira_expressions_analysis import JiraExpressionsAnalysis
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    *,
    body: JiraExpressionForAnalysis,
    check: AnalyseExpressionCheck | Unset = AnalyseExpressionCheck.SYNTAX,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    json_check: str | Unset = UNSET
    if not isinstance(check, Unset):
        json_check = check.value

    params["check"] = json_check


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/rest/api/3/expression/analyse",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ErrorCollection | JiraExpressionsAnalysis | None:
    if response.status_code == 200:
        response_200 = JiraExpressionsAnalysis.from_dict(response.json())



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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ErrorCollection | JiraExpressionsAnalysis]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: JiraExpressionForAnalysis,
    check: AnalyseExpressionCheck | Unset = AnalyseExpressionCheck.SYNTAX,

) -> Response[Any | ErrorCollection | JiraExpressionsAnalysis]:
    """ Analyse Jira expression

     Analyses and validates Jira expressions.

    As an experimental feature, this operation can also attempt to type-check the expressions.

    Learn more about Jira expressions in the
    [documentation](https://developer.atlassian.com/cloud/jira/platform/jira-expressions/).

    **[Permissions](#permissions) required**: None.

    Args:
        check (AnalyseExpressionCheck | Unset):  Default: AnalyseExpressionCheck.SYNTAX.
        body (JiraExpressionForAnalysis): Details of Jira expressions for analysis.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorCollection | JiraExpressionsAnalysis]
     """


    kwargs = _get_kwargs(
        body=body,
check=check,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: AuthenticatedClient,
    body: JiraExpressionForAnalysis,
    check: AnalyseExpressionCheck | Unset = AnalyseExpressionCheck.SYNTAX,

) -> Any | ErrorCollection | JiraExpressionsAnalysis | None:
    """ Analyse Jira expression

     Analyses and validates Jira expressions.

    As an experimental feature, this operation can also attempt to type-check the expressions.

    Learn more about Jira expressions in the
    [documentation](https://developer.atlassian.com/cloud/jira/platform/jira-expressions/).

    **[Permissions](#permissions) required**: None.

    Args:
        check (AnalyseExpressionCheck | Unset):  Default: AnalyseExpressionCheck.SYNTAX.
        body (JiraExpressionForAnalysis): Details of Jira expressions for analysis.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorCollection | JiraExpressionsAnalysis
     """


    return sync_detailed(
        client=client,
body=body,
check=check,

    ).parsed

async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: JiraExpressionForAnalysis,
    check: AnalyseExpressionCheck | Unset = AnalyseExpressionCheck.SYNTAX,

) -> Response[Any | ErrorCollection | JiraExpressionsAnalysis]:
    """ Analyse Jira expression

     Analyses and validates Jira expressions.

    As an experimental feature, this operation can also attempt to type-check the expressions.

    Learn more about Jira expressions in the
    [documentation](https://developer.atlassian.com/cloud/jira/platform/jira-expressions/).

    **[Permissions](#permissions) required**: None.

    Args:
        check (AnalyseExpressionCheck | Unset):  Default: AnalyseExpressionCheck.SYNTAX.
        body (JiraExpressionForAnalysis): Details of Jira expressions for analysis.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorCollection | JiraExpressionsAnalysis]
     """


    kwargs = _get_kwargs(
        body=body,
check=check,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: AuthenticatedClient,
    body: JiraExpressionForAnalysis,
    check: AnalyseExpressionCheck | Unset = AnalyseExpressionCheck.SYNTAX,

) -> Any | ErrorCollection | JiraExpressionsAnalysis | None:
    """ Analyse Jira expression

     Analyses and validates Jira expressions.

    As an experimental feature, this operation can also attempt to type-check the expressions.

    Learn more about Jira expressions in the
    [documentation](https://developer.atlassian.com/cloud/jira/platform/jira-expressions/).

    **[Permissions](#permissions) required**: None.

    Args:
        check (AnalyseExpressionCheck | Unset):  Default: AnalyseExpressionCheck.SYNTAX.
        body (JiraExpressionForAnalysis): Details of Jira expressions for analysis.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorCollection | JiraExpressionsAnalysis
     """


    return (await asyncio_detailed(
        client=client,
body=body,
check=check,

    )).parsed
