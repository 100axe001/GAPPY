from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import AppendMappingsForIssueTypeScreenSchemeToolInput, AppendMappingsForIssueTypeScreenSchemeToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class AppendMappingsForIssueTypeScreenSchemeInput(AppendMappingsForIssueTypeScreenSchemeToolInput):
    """Operation input for `append_mappings_for_issue_type_screen_scheme`."""
    pass

class AppendMappingsForIssueTypeScreenSchemeOutput(AppendMappingsForIssueTypeScreenSchemeToolOutput):
    """Operation output for `append_mappings_for_issue_type_screen_scheme`."""
    pass

class JiraMappingsForIssueTypeScreenSchemeResource(BaseResourceClient):
    """Operations for the `mappings_for_issue_type_screen_scheme` resource."""

    @operation(
        name='append_mappings_for_issue_type_screen_scheme',
        title='AppendMappingsForIssueTypeScreenScheme',
        input_model=AppendMappingsForIssueTypeScreenSchemeInput,
        output_model=AppendMappingsForIssueTypeScreenSchemeOutput,
        tools_used=('append_mappings_for_issue_type_screen_scheme',),
        tags=tuple(['Issue type screen schemes']),
    )
    async def append(self, data: AppendMappingsForIssueTypeScreenSchemeInput) -> AppendMappingsForIssueTypeScreenSchemeOutput:
        """Appends issue type to screen scheme mappings to an issue type screen scheme. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: issue_type_screen_scheme_id, body"""
        tool = self._client.get_tool('append_mappings_for_issue_type_screen_scheme')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return AppendMappingsForIssueTypeScreenSchemeOutput.model_validate(coerce_tool_result(result))
