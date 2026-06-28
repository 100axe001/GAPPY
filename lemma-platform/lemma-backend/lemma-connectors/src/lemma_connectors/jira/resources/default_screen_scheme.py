from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import UpdateDefaultScreenSchemeToolInput, UpdateDefaultScreenSchemeToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class UpdateDefaultScreenSchemeInput(UpdateDefaultScreenSchemeToolInput):
    """Operation input for `update_default_screen_scheme`."""
    pass

class UpdateDefaultScreenSchemeOutput(UpdateDefaultScreenSchemeToolOutput):
    """Operation output for `update_default_screen_scheme`."""
    pass

class JiraDefaultScreenSchemeResource(BaseResourceClient):
    """Operations for the `default_screen_scheme` resource."""

    @operation(
        name='update_default_screen_scheme',
        title='UpdateDefaultScreenScheme',
        input_model=UpdateDefaultScreenSchemeInput,
        output_model=UpdateDefaultScreenSchemeOutput,
        tools_used=('update_default_screen_scheme',),
        tags=tuple(['Issue type screen schemes']),
    )
    async def update(self, data: UpdateDefaultScreenSchemeInput) -> UpdateDefaultScreenSchemeOutput:
        """Updates the default screen scheme of an issue type screen scheme. The default screen scheme is used for all unmapped issue types. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: issue_type_screen_scheme_id, body"""
        tool = self._client.get_tool('update_default_screen_scheme')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UpdateDefaultScreenSchemeOutput.model_validate(coerce_tool_result(result))
