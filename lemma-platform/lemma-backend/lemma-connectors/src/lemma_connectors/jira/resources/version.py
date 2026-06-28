from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import CreateVersionToolInput, CreateVersionToolOutput, DeleteVersionToolInput, DeleteVersionToolOutput, GetVersionToolInput, GetVersionToolOutput, MoveVersionToolInput, MoveVersionToolOutput, UpdateVersionToolInput, UpdateVersionToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class CreateVersionInput(CreateVersionToolInput):
    """Operation input for `create_version`."""
    pass

class CreateVersionOutput(CreateVersionToolOutput):
    """Operation output for `create_version`."""
    pass

class DeleteVersionInput(DeleteVersionToolInput):
    """Operation input for `delete_version`."""
    pass

class DeleteVersionOutput(DeleteVersionToolOutput):
    """Operation output for `delete_version`."""
    pass

class GetVersionInput(GetVersionToolInput):
    """Operation input for `get_version`."""
    pass

class GetVersionOutput(GetVersionToolOutput):
    """Operation output for `get_version`."""
    pass

class MoveVersionInput(MoveVersionToolInput):
    """Operation input for `move_version`."""
    pass

class MoveVersionOutput(MoveVersionToolOutput):
    """Operation output for `move_version`."""
    pass

class UpdateVersionInput(UpdateVersionToolInput):
    """Operation input for `update_version`."""
    pass

class UpdateVersionOutput(UpdateVersionToolOutput):
    """Operation output for `update_version`."""
    pass

class JiraVersionResource(BaseResourceClient):
    """Operations for the `version` resource."""

    @operation(
        name='create_version',
        title='CreateVersion',
        input_model=CreateVersionInput,
        output_model=CreateVersionOutput,
        tools_used=('create_version',),
        tags=tuple(['Project versions']),
    )
    async def create(self, data: CreateVersionInput) -> CreateVersionOutput:
        """Creates a project version. This operation can be accessed anonymously. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project the version is added to.

Important inputs: body"""
        tool = self._client.get_tool('create_version')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return CreateVersionOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='delete_version',
        title='DeleteVersion',
        input_model=DeleteVersionInput,
        output_model=DeleteVersionOutput,
        tools_used=('delete_version',),
        tags=tuple(['Project versions']),
    )
    async def delete(self, data: DeleteVersionInput) -> DeleteVersionOutput:
        """Deletes a project version. Deprecated, use [ Delete and replace version](#api-rest-api-3-version-id-removeAndSwap-post) that supports swapping version values in custom fields, in addition to the swapping for `fixVersion` and `affectedVersion` provided in this resource. Alternative versions can be provided to update issues that use the deleted version in `fixVersion` or `affectedVersion`. If alternatives are not provided, occurrences of `fixVersion` and `affectedVersion` that contain the deleted version are cleared. This operation can be accessed anonymously. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that contains the version.

Important inputs: id, move_fix_issues_to, move_affected_issues_to"""
        tool = self._client.get_tool('delete_version')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DeleteVersionOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='get_version',
        title='GetVersion',
        input_model=GetVersionInput,
        output_model=GetVersionOutput,
        tools_used=('get_version',),
        tags=tuple(['Project versions']),
    )
    async def get(self, data: GetVersionInput) -> GetVersionOutput:
        """Returns a project version. This operation can be accessed anonymously. **[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project containing the version.

Important inputs: id, expand"""
        tool = self._client.get_tool('get_version')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetVersionOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='move_version',
        title='MoveVersion',
        input_model=MoveVersionInput,
        output_model=MoveVersionOutput,
        tools_used=('move_version',),
        tags=tuple(['Project versions']),
    )
    async def move(self, data: MoveVersionInput) -> MoveVersionOutput:
        """Modifies the version's sequence within the project, which affects the display order of the versions in Jira. This operation can be accessed anonymously. **[Permissions](#permissions) required:** *Browse projects* project permission for the project that contains the version.

Important inputs: id, body"""
        tool = self._client.get_tool('move_version')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return MoveVersionOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='update_version',
        title='UpdateVersion',
        input_model=UpdateVersionInput,
        output_model=UpdateVersionOutput,
        tools_used=('update_version',),
        tags=tuple(['Project versions']),
    )
    async def update(self, data: UpdateVersionInput) -> UpdateVersionOutput:
        """Updates a project version. This operation can be accessed anonymously. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg) or *Administer Projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for the project that contains the version.

Important inputs: id, body"""
        tool = self._client.get_tool('update_version')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UpdateVersionOutput.model_validate(coerce_tool_result(result))
