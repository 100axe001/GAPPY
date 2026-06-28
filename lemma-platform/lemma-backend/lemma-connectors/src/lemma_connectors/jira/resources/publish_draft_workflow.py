from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import PublishDraftWorkflowSchemeToolInput, PublishDraftWorkflowSchemeToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class PublishDraftWorkflowSchemeInput(PublishDraftWorkflowSchemeToolInput):
    """Operation input for `publish_draft_workflow_scheme`."""
    pass

class PublishDraftWorkflowSchemeOutput(PublishDraftWorkflowSchemeToolOutput):
    """Operation output for `publish_draft_workflow_scheme`."""
    pass

class JiraPublishDraftWorkflowResource(BaseResourceClient):
    """Operations for the `publish_draft_workflow` resource."""

    @operation(
        name='publish_draft_workflow_scheme',
        title='PublishDraftWorkflowScheme',
        input_model=PublishDraftWorkflowSchemeInput,
        output_model=PublishDraftWorkflowSchemeOutput,
        tools_used=('publish_draft_workflow_scheme',),
        tags=tuple(['Workflow scheme drafts']),
    )
    async def scheme(self, data: PublishDraftWorkflowSchemeInput) -> PublishDraftWorkflowSchemeOutput:
        """Publishes a draft workflow scheme. Where the draft workflow includes new workflow statuses for an issue type, mappings are provided to update issues with the original workflow status to the new workflow status. This operation is [asynchronous](#async). Follow the `location` link in the response to determine the status of the task and use [Get task](#api-rest-api-3-task-taskId-get) to obtain updates. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: id, validate_only, body"""
        tool = self._client.get_tool('publish_draft_workflow_scheme')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return PublishDraftWorkflowSchemeOutput.model_validate(coerce_tool_result(result))
