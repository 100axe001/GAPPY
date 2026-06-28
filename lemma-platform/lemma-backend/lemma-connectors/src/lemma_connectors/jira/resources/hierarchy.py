from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetHierarchyToolInput, GetHierarchyToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetHierarchyInput(GetHierarchyToolInput):
    """Operation input for `get_hierarchy`."""
    pass

class GetHierarchyOutput(GetHierarchyToolOutput):
    """Operation output for `get_hierarchy`."""
    pass

class JiraHierarchyResource(BaseResourceClient):
    """Operations for the `hierarchy` resource."""

    @operation(
        name='get_hierarchy',
        title='GetHierarchy',
        input_model=GetHierarchyInput,
        output_model=GetHierarchyOutput,
        tools_used=('get_hierarchy',),
        tags=tuple(['Projects']),
    )
    async def get(self, data: GetHierarchyInput) -> GetHierarchyOutput:
        """Get the issue type hierarchy for a next-gen project. The issue type hierarchy for a project consists of: * *Epic* at level 1 (optional). * One or more issue types at level 0 such as *Story*, *Task*, or *Bug*. Where the issue type *Epic* is defined, these issue types are used to break down the content of an epic. * *Subtask* at level -1 (optional). This issue type enables level 0 issue types to be broken down into components. Issues based on a level -1 issue type must have a parent issue. **[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project.

Important inputs: project_id"""
        tool = self._client.get_tool('get_hierarchy')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetHierarchyOutput.model_validate(coerce_tool_result(result))
