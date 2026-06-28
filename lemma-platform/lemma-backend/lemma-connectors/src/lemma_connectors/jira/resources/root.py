from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import NotifyToolInput, NotifyToolOutput, RestoreToolInput, RestoreToolOutput, SearchToolInput, SearchToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class NotifyInput(NotifyToolInput):
    """Operation input for `notify`."""
    pass

class NotifyOutput(NotifyToolOutput):
    """Operation output for `notify`."""
    pass

class RestoreInput(RestoreToolInput):
    """Operation input for `restore`."""
    pass

class RestoreOutput(RestoreToolOutput):
    """Operation output for `restore`."""
    pass

class SearchInput(SearchToolInput):
    """Operation input for `search`."""
    pass

class SearchOutput(SearchToolOutput):
    """Operation output for `search`."""
    pass

class JiraRootResource(BaseResourceClient):
    """Operations for the `root` resource."""

    @operation(
        name='notify',
        title='Notify',
        input_model=NotifyInput,
        output_model=NotifyOutput,
        tools_used=('notify',),
        tags=tuple(['Issues']),
    )
    async def notify(self, data: NotifyInput) -> NotifyOutput:
        """Creates an email notification for an issue and adds it to the mail queue. **[Permissions](#permissions) required:** * *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in. * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue.

Important inputs: issue_id_or_key, body"""
        tool = self._client.get_tool('notify')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return NotifyOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='restore',
        title='Restore',
        input_model=RestoreInput,
        output_model=RestoreOutput,
        tools_used=('restore',),
        tags=tuple(['Projects']),
    )
    async def restore(self, data: RestoreInput) -> RestoreOutput:
        """Restores a project that has been archived or placed in the Jira recycle bin. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: project_id_or_key"""
        tool = self._client.get_tool('restore')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return RestoreOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='search',
        title='Search',
        input_model=SearchInput,
        output_model=SearchOutput,
        tools_used=('search',),
        tags=tuple(['Status']),
    )
    async def search(self, data: SearchInput) -> SearchOutput:
        """Returns a [paginated](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/#pagination) list of statuses that match a search on name or project. **[Permissions](#permissions) required:** * *Administer projects* [project permission.](https://confluence.atlassian.com/x/yodKLg) * *Administer Jira* [project permission.](https://confluence.atlassian.com/x/yodKLg).

Important inputs: expand, project_id, start_at, max_results, search_string, status_category"""
        tool = self._client.get_tool('search')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SearchOutput.model_validate(coerce_tool_result(result))
