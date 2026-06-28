from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetAllStatusesToolInput, GetAllStatusesToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetAllStatusesInput(GetAllStatusesToolInput):
    """Operation input for `get_all_statuses`."""
    pass

class GetAllStatusesOutput(GetAllStatusesToolOutput):
    """Operation output for `get_all_statuses`."""
    pass

class JiraAllStatusesResource(BaseResourceClient):
    """Operations for the `all_statuses` resource."""

    @operation(
        name='get_all_statuses',
        title='GetAllStatuses',
        input_model=GetAllStatusesInput,
        output_model=GetAllStatusesOutput,
        tools_used=('get_all_statuses',),
        tags=tuple(['Projects']),
    )
    async def get(self, data: GetAllStatusesInput) -> GetAllStatusesOutput:
        """Returns the valid statuses for a project. The statuses are grouped by issue type, as each project has a set of valid issue types and each issue type has a set of valid statuses. This operation can be accessed anonymously. **[Permissions](#permissions) required:** *Browse Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.

Important inputs: project_id_or_key"""
        tool = self._client.get_tool('get_all_statuses')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetAllStatusesOutput.model_validate(coerce_tool_result(result))
