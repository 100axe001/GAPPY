from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import CreateUserToolInput, CreateUserToolOutput, GetUserToolInput, GetUserToolOutput, RemoveUserToolInput, RemoveUserToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class CreateUserInput(CreateUserToolInput):
    """Operation input for `create_user`."""
    pass

class CreateUserOutput(CreateUserToolOutput):
    """Operation output for `create_user`."""
    pass

class GetUserInput(GetUserToolInput):
    """Operation input for `get_user`."""
    pass

class GetUserOutput(GetUserToolOutput):
    """Operation output for `get_user`."""
    pass

class RemoveUserInput(RemoveUserToolInput):
    """Operation input for `remove_user`."""
    pass

class RemoveUserOutput(RemoveUserToolOutput):
    """Operation output for `remove_user`."""
    pass

class JiraUserResource(BaseResourceClient):
    """Operations for the `user` resource."""

    @operation(
        name='create_user',
        title='CreateUser',
        input_model=CreateUserInput,
        output_model=CreateUserOutput,
        tools_used=('create_user',),
        tags=tuple(['Users']),
    )
    async def create(self, data: CreateUserInput) -> CreateUserOutput:
        """Creates a user. This resource is retained for legacy compatibility. As soon as a more suitable alternative is available this resource will be deprecated. If the user exists and has access to Jira, the operation returns a 201 status. If the user exists but does not have access to Jira, the operation returns a 400 status. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: body"""
        tool = self._client.get_tool('create_user')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return CreateUserOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='get_user',
        title='GetUser',
        input_model=GetUserInput,
        output_model=GetUserOutput,
        tools_used=('get_user',),
        tags=tuple(['Users']),
    )
    async def get(self, data: GetUserInput) -> GetUserOutput:
        """Returns a user. Privacy controls are applied to the response based on the user's preferences. This could mean, for example, that the user's email address is hidden. See the [Profile visibility overview](https://developer.atlassian.com/cloud/jira/platform/profile-visibility/) for more details. **[Permissions](#permissions) required:** *Browse users and groups* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: account_id, username, expand"""
        tool = self._client.get_tool('get_user')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetUserOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='remove_user',
        title='RemoveUser',
        input_model=RemoveUserInput,
        output_model=RemoveUserOutput,
        tools_used=('remove_user',),
        tags=tuple(['Users']),
    )
    async def remove(self, data: RemoveUserInput) -> RemoveUserOutput:
        """Deletes a user. If the operation completes successfully then the user is removed from Jira's user base. This operation does not delete the user's Atlassian account. **[Permissions](#permissions) required:** Site administration (that is, membership of the *site-admin* [group](https://confluence.atlassian.com/x/24xjL)).

Important inputs: account_id, username"""
        tool = self._client.get_tool('remove_user')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return RemoveUserOutput.model_validate(coerce_tool_result(result))
