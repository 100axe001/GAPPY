from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import CreatePermissionSchemeToolInput, CreatePermissionSchemeToolOutput, DeletePermissionSchemeToolInput, DeletePermissionSchemeToolOutput, GetPermissionSchemeToolInput, GetPermissionSchemeToolOutput, UpdatePermissionSchemeToolInput, UpdatePermissionSchemeToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class CreatePermissionSchemeInput(CreatePermissionSchemeToolInput):
    """Operation input for `create_permission_scheme`."""
    pass

class CreatePermissionSchemeOutput(CreatePermissionSchemeToolOutput):
    """Operation output for `create_permission_scheme`."""
    pass

class DeletePermissionSchemeInput(DeletePermissionSchemeToolInput):
    """Operation input for `delete_permission_scheme`."""
    pass

class DeletePermissionSchemeOutput(DeletePermissionSchemeToolOutput):
    """Operation output for `delete_permission_scheme`."""
    pass

class GetPermissionSchemeInput(GetPermissionSchemeToolInput):
    """Operation input for `get_permission_scheme`."""
    pass

class GetPermissionSchemeOutput(GetPermissionSchemeToolOutput):
    """Operation output for `get_permission_scheme`."""
    pass

class UpdatePermissionSchemeInput(UpdatePermissionSchemeToolInput):
    """Operation input for `update_permission_scheme`."""
    pass

class UpdatePermissionSchemeOutput(UpdatePermissionSchemeToolOutput):
    """Operation output for `update_permission_scheme`."""
    pass

class JiraPermissionSchemeResource(BaseResourceClient):
    """Operations for the `permission_scheme` resource."""

    @operation(
        name='create_permission_scheme',
        title='CreatePermissionScheme',
        input_model=CreatePermissionSchemeInput,
        output_model=CreatePermissionSchemeOutput,
        tools_used=('create_permission_scheme',),
        tags=tuple(['Permission schemes']),
    )
    async def create(self, data: CreatePermissionSchemeInput) -> CreatePermissionSchemeOutput:
        """Creates a new permission scheme. You can create a permission scheme with or without defining a set of permission grants. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: expand, body"""
        tool = self._client.get_tool('create_permission_scheme')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return CreatePermissionSchemeOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='delete_permission_scheme',
        title='DeletePermissionScheme',
        input_model=DeletePermissionSchemeInput,
        output_model=DeletePermissionSchemeOutput,
        tools_used=('delete_permission_scheme',),
        tags=tuple(['Permission schemes']),
    )
    async def delete(self, data: DeletePermissionSchemeInput) -> DeletePermissionSchemeOutput:
        """Deletes a permission scheme. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: scheme_id"""
        tool = self._client.get_tool('delete_permission_scheme')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DeletePermissionSchemeOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='get_permission_scheme',
        title='GetPermissionScheme',
        input_model=GetPermissionSchemeInput,
        output_model=GetPermissionSchemeOutput,
        tools_used=('get_permission_scheme',),
        tags=tuple(['Permission schemes']),
    )
    async def get(self, data: GetPermissionSchemeInput) -> GetPermissionSchemeOutput:
        """Returns a permission scheme. **[Permissions](#permissions) required:** Permission to access Jira.

Important inputs: scheme_id, expand"""
        tool = self._client.get_tool('get_permission_scheme')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetPermissionSchemeOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='update_permission_scheme',
        title='UpdatePermissionScheme',
        input_model=UpdatePermissionSchemeInput,
        output_model=UpdatePermissionSchemeOutput,
        tools_used=('update_permission_scheme',),
        tags=tuple(['Permission schemes']),
    )
    async def update(self, data: UpdatePermissionSchemeInput) -> UpdatePermissionSchemeOutput:
        """Updates a permission scheme. Below are some important things to note when using this resource: * If a permissions list is present in the request, then it is set in the permission scheme, overwriting *all existing* grants. * If you want to update only the name and description, then do not send a permissions list in the request. * Sending an empty list will remove all permission grants from the permission scheme. If you want to add or delete a permission grant instead of updating the whole list, see [Create permission grant](#api-rest-api-3-permissionscheme-schemeId-permission-post) or [Delete permission scheme entity](#api-rest-api-3-permissionscheme-schemeId-permission-permissionId-delete). See [About permission schemes and grants](../api-group-permission-schemes/#about-permission-schemes-and-grants) for more details. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: scheme_id, expand, body"""
        tool = self._client.get_tool('update_permission_scheme')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UpdatePermissionSchemeOutput.model_validate(coerce_tool_result(result))
