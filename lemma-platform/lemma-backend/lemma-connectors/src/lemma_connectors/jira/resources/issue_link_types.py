from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetIssueLinkTypesToolInput, GetIssueLinkTypesToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetIssueLinkTypesInput(GetIssueLinkTypesToolInput):
    """Operation input for `get_issue_link_types`."""
    pass

class GetIssueLinkTypesOutput(GetIssueLinkTypesToolOutput):
    """Operation output for `get_issue_link_types`."""
    pass

class JiraIssueLinkTypesResource(BaseResourceClient):
    """Operations for the `issue_link_types` resource."""

    @operation(
        name='get_issue_link_types',
        title='GetIssueLinkTypes',
        input_model=GetIssueLinkTypesInput,
        output_model=GetIssueLinkTypesOutput,
        tools_used=('get_issue_link_types',),
        tags=tuple(['Issue link types']),
    )
    async def get(self, data: GetIssueLinkTypesInput) -> GetIssueLinkTypesOutput:
        """Returns a list of all issue link types. To use this operation, the site must have [issue linking](https://confluence.atlassian.com/x/yoXKM) enabled. This operation can be accessed anonymously. **[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for a project in the site.

Important inputs: No explicit inputs."""
        tool = self._client.get_tool('get_issue_link_types')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetIssueLinkTypesOutput.model_validate(coerce_tool_result(result))
