from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import MergeVersionsToolInput, MergeVersionsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class MergeVersionsInput(MergeVersionsToolInput):
    """Operation input for `merge_versions`."""
    pass

class MergeVersionsOutput(MergeVersionsToolOutput):
    """Operation output for `merge_versions`."""
    pass

class JiraMergeResource(BaseResourceClient):
    """Operations for the `merge` resource."""

    @operation(
        name='merge_versions',
        title='MergeVersions',
        input_model=MergeVersionsInput,
        output_model=MergeVersionsOutput,
        tools_used=('merge_versions',),
        tags=tuple(['Project versions']),
    )
    async def versions(self, data: MergeVersionsInput) -> MergeVersionsOutput:
        """Merges two project versions. The merge is completed by deleting the version specified in `id` and replacing any occurrences of its ID in `fixVersion` with the version ID specified in `moveIssuesTo`. Consider using [ Delete and replace version](#api-rest-api-3-version-id-removeAndSwap-post) instead. This resource supports swapping version values in `fixVersion`, `affectedVersion`, and custom fields. This operation can be accessed anonymously. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that contains the version.

Important inputs: id, move_issues_to"""
        tool = self._client.get_tool('merge_versions')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return MergeVersionsOutput.model_validate(coerce_tool_result(result))
