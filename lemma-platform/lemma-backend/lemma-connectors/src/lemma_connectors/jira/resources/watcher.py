from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import AddWatcherToolInput, AddWatcherToolOutput, RemoveWatcherToolInput, RemoveWatcherToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class AddWatcherInput(AddWatcherToolInput):
    """Operation input for `add_watcher`."""
    pass

class AddWatcherOutput(AddWatcherToolOutput):
    """Operation output for `add_watcher`."""
    pass

class RemoveWatcherInput(RemoveWatcherToolInput):
    """Operation input for `remove_watcher`."""
    pass

class RemoveWatcherOutput(RemoveWatcherToolOutput):
    """Operation output for `remove_watcher`."""
    pass

class JiraWatcherResource(BaseResourceClient):
    """Operations for the `watcher` resource."""

    @operation(
        name='add_watcher',
        title='AddWatcher',
        input_model=AddWatcherInput,
        output_model=AddWatcherOutput,
        tools_used=('add_watcher',),
        tags=tuple(['Issue watchers']),
    )
    async def add(self, data: AddWatcherInput) -> AddWatcherOutput:
        """Adds a user as a watcher of an issue by passing the account ID of the user. For example, `"5b10ac8d82e05b22cc7d4ef5"`. If no user is specified the calling user is added. This operation requires the **Allow users to watch issues** option to be *ON*. This option is set in General configuration for Jira. See [Configuring Jira application options](https://confluence.atlassian.com/x/uYXKM) for details. **[Permissions](#permissions) required:** * *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in. * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue. * To add users other than themselves to the watchlist, *Manage watcher list* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.

Important inputs: issue_id_or_key, body"""
        tool = self._client.get_tool('add_watcher')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return AddWatcherOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='remove_watcher',
        title='RemoveWatcher',
        input_model=RemoveWatcherInput,
        output_model=RemoveWatcherOutput,
        tools_used=('remove_watcher',),
        tags=tuple(['Issue watchers']),
    )
    async def remove(self, data: RemoveWatcherInput) -> RemoveWatcherOutput:
        """Deletes a user as a watcher of an issue. This operation requires the **Allow users to watch issues** option to be *ON*. This option is set in General configuration for Jira. See [Configuring Jira application options](https://confluence.atlassian.com/x/uYXKM) for details. **[Permissions](#permissions) required:** * *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in. * If [issue-level security](https://confluence.atlassian.com/x/J4lKLg) is configured, issue-level security permission to view the issue. * To remove users other than themselves from the watchlist, *Manage watcher list* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that the issue is in.

Important inputs: issue_id_or_key, username, account_id"""
        tool = self._client.get_tool('remove_watcher')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return RemoveWatcherOutput.model_validate(coerce_tool_result(result))
