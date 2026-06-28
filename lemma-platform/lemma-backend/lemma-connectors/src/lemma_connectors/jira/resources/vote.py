from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import AddVoteToolInput, AddVoteToolOutput, RemoveVoteToolInput, RemoveVoteToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class AddVoteInput(AddVoteToolInput):
    """Operation input for `add_vote`."""
    pass

class AddVoteOutput(AddVoteToolOutput):
    """Operation output for `add_vote`."""
    pass

class RemoveVoteInput(RemoveVoteToolInput):
    """Operation input for `remove_vote`."""
    pass

class RemoveVoteOutput(RemoveVoteToolOutput):
    """Operation output for `remove_vote`."""
    pass

class JiraVoteResource(BaseResourceClient):
    """Operations for the `vote` resource."""

    @operation(
        name='add_vote',
        title='AddVote',
        input_model=AddVoteInput,
        output_model=AddVoteOutput,
        tools_used=('add_vote',),
        tags=tuple(['Issue votes']),
    )
    async def add(self, data: AddVoteInput) -> AddVoteOutput:
        """Adds the user's vote to an issue. This is the equivalent of the user clicking *Vote* on an issue in Jira. This operation requires the **Allow users to vote on issues** option to be *ON*. This option is set in General configuration for Jira. See [Configuring Jira application options](https://confluence.atlassian.com/x/uYXKM) for details. **[Permissions](#permissions) required:** * *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in. * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

Important inputs: issue_id_or_key"""
        tool = self._client.get_tool('add_vote')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return AddVoteOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='remove_vote',
        title='RemoveVote',
        input_model=RemoveVoteInput,
        output_model=RemoveVoteOutput,
        tools_used=('remove_vote',),
        tags=tuple(['Issue votes']),
    )
    async def remove(self, data: RemoveVoteInput) -> RemoveVoteOutput:
        """Deletes a user's vote from an issue. This is the equivalent of the user clicking *Unvote* on an issue in Jira. This operation requires the **Allow users to vote on issues** option to be *ON*. This option is set in General configuration for Jira. See [Configuring Jira application options](https://confluence.atlassian.com/x/uYXKM) for details. **[Permissions](#permissions) required:** * *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in. * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

Important inputs: issue_id_or_key"""
        tool = self._client.get_tool('remove_vote')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return RemoveVoteOutput.model_validate(coerce_tool_result(result))
