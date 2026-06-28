from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import RemoveMappingsFromIssueTypeScreenSchemeToolInput, RemoveMappingsFromIssueTypeScreenSchemeToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class RemoveMappingsFromIssueTypeScreenSchemeInput(RemoveMappingsFromIssueTypeScreenSchemeToolInput):
    """Operation input for `remove_mappings_from_issue_type_screen_scheme`."""
    pass

class RemoveMappingsFromIssueTypeScreenSchemeOutput(RemoveMappingsFromIssueTypeScreenSchemeToolOutput):
    """Operation output for `remove_mappings_from_issue_type_screen_scheme`."""
    pass

class JiraMappingsFromIssueTypeScreenSchemeResource(BaseResourceClient):
    """Operations for the `mappings_from_issue_type_screen_scheme` resource."""

    @operation(
        name='remove_mappings_from_issue_type_screen_scheme',
        title='RemoveMappingsFromIssueTypeScreenScheme',
        input_model=RemoveMappingsFromIssueTypeScreenSchemeInput,
        output_model=RemoveMappingsFromIssueTypeScreenSchemeOutput,
        tools_used=('remove_mappings_from_issue_type_screen_scheme',),
        tags=tuple(['Issue type screen schemes']),
    )
    async def remove(self, data: RemoveMappingsFromIssueTypeScreenSchemeInput) -> RemoveMappingsFromIssueTypeScreenSchemeOutput:
        """Removes issue type to screen scheme mappings from an issue type screen scheme. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: issue_type_screen_scheme_id, body"""
        tool = self._client.get_tool('remove_mappings_from_issue_type_screen_scheme')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return RemoveMappingsFromIssueTypeScreenSchemeOutput.model_validate(coerce_tool_result(result))
