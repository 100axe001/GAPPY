from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import CreateGroupToolInput, CreateGroupToolOutput, GetGroupToolInput, GetGroupToolOutput, RemoveGroupToolInput, RemoveGroupToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class CreateGroupInput(CreateGroupToolInput):
    """Operation input for `create_group`."""
    pass

class CreateGroupOutput(CreateGroupToolOutput):
    """Operation output for `create_group`."""
    pass

class GetGroupInput(GetGroupToolInput):
    """Operation input for `get_group`."""
    pass

class GetGroupOutput(GetGroupToolOutput):
    """Operation output for `get_group`."""
    pass

class RemoveGroupInput(RemoveGroupToolInput):
    """Operation input for `remove_group`."""
    pass

class RemoveGroupOutput(RemoveGroupToolOutput):
    """Operation output for `remove_group`."""
    pass

class JiraGroupResource(BaseResourceClient):
    """Operations for the `group` resource."""

    @operation(
        name='create_group',
        title='CreateGroup',
        input_model=CreateGroupInput,
        output_model=CreateGroupOutput,
        tools_used=('create_group',),
        tags=tuple(['Groups']),
    )
    async def create(self, data: CreateGroupInput) -> CreateGroupOutput:
        """Creates a group. **[Permissions](#permissions) required:** Site administration (that is, member of the *site-admin* [group](https://confluence.atlassian.com/x/24xjL)).

Important inputs: body"""
        tool = self._client.get_tool('create_group')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return CreateGroupOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='get_group',
        title='GetGroup',
        input_model=GetGroupInput,
        output_model=GetGroupOutput,
        tools_used=('get_group',),
        tags=tuple(['Groups']),
    )
    async def get(self, data: GetGroupInput) -> GetGroupOutput:
        """This operation is deprecated, use [`group/member`](#api-rest-api-3-group-member-get). Returns all users in a group. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: groupname, group_id, expand"""
        tool = self._client.get_tool('get_group')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetGroupOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='remove_group',
        title='RemoveGroup',
        input_model=RemoveGroupInput,
        output_model=RemoveGroupOutput,
        tools_used=('remove_group',),
        tags=tuple(['Groups']),
    )
    async def remove(self, data: RemoveGroupInput) -> RemoveGroupOutput:
        """Deletes a group. **[Permissions](#permissions) required:** Site administration (that is, member of the *site-admin* strategic [group](https://confluence.atlassian.com/x/24xjL)).

Important inputs: groupname, group_id, swap_group, swap_group_id"""
        tool = self._client.get_tool('remove_group')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return RemoveGroupOutput.model_validate(coerce_tool_result(result))
