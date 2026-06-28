from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetVotesToolInput, GetVotesToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetVotesInput(GetVotesToolInput):
    """Operation input for `get_votes`."""
    pass

class GetVotesOutput(GetVotesToolOutput):
    """Operation output for `get_votes`."""
    pass

class JiraVotesResource(BaseResourceClient):
    """Operations for the `votes` resource."""

    @operation(
        name='get_votes',
        title='GetVotes',
        input_model=GetVotesInput,
        output_model=GetVotesOutput,
        tools_used=('get_votes',),
        tags=tuple(['Issue votes']),
    )
    async def get(self, data: GetVotesInput) -> GetVotesOutput:
        """Returns details about the votes on an issue. This operation requires the **Allow users to vote on issues** option to be *ON*. This option is set in General configuration for Jira. See [Configuring Jira application options](https://confluence.atlassian.com/x/uYXKM) for details. This operation can be accessed anonymously. **[Permissions](#permissions) required:** * *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is ini * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue. Note that users with the necessary permissions for this operation but without the *View voters and watchers* project permissions are not returned details in the `voters` field.

Important inputs: issue_id_or_key"""
        tool = self._client.get_tool('get_votes')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetVotesOutput.model_validate(coerce_tool_result(result))
