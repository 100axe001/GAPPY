from __future__ import annotations

from lemma_connectors.slack.generated.tool_types import AppsUninstallToolInput, AppsUninstallToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class AppsUninstallInput(AppsUninstallToolInput):
    """Operation input for `apps_uninstall`."""
    pass

class AppsUninstallOutput(AppsUninstallToolOutput):
    """Operation output for `apps_uninstall`."""
    pass

class SlackAppsResource(BaseResourceClient):
    """Operations for the `apps` resource."""

    @operation(
        name='apps_uninstall',
        title='AppsUninstall',
        input_model=AppsUninstallInput,
        output_model=AppsUninstallOutput,
        tools_used=('apps_uninstall',),
        tags=tuple(['apps']),
    )
    async def uninstall(self, data: AppsUninstallInput) -> AppsUninstallOutput:
        """Uninstalls your app from a workspace.

Important inputs: token, client_id, client_secret"""
        tool = self._client.get_tool('apps_uninstall')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return AppsUninstallOutput.model_validate(coerce_tool_result(result))
