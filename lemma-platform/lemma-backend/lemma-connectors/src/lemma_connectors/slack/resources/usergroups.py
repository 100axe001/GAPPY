from __future__ import annotations

from lemma_connectors.slack.generated.tool_types import UsergroupsCreateToolInput, UsergroupsCreateToolOutput, UsergroupsDisableToolInput, UsergroupsDisableToolOutput, UsergroupsEnableToolInput, UsergroupsEnableToolOutput, UsergroupsListToolInput, UsergroupsListToolOutput, UsergroupsUpdateToolInput, UsergroupsUpdateToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class UsergroupsCreateInput(UsergroupsCreateToolInput):
    """Operation input for `usergroups_create`."""
    pass

class UsergroupsCreateOutput(UsergroupsCreateToolOutput):
    """Operation output for `usergroups_create`."""
    pass

class UsergroupsDisableInput(UsergroupsDisableToolInput):
    """Operation input for `usergroups_disable`."""
    pass

class UsergroupsDisableOutput(UsergroupsDisableToolOutput):
    """Operation output for `usergroups_disable`."""
    pass

class UsergroupsEnableInput(UsergroupsEnableToolInput):
    """Operation input for `usergroups_enable`."""
    pass

class UsergroupsEnableOutput(UsergroupsEnableToolOutput):
    """Operation output for `usergroups_enable`."""
    pass

class UsergroupsListInput(UsergroupsListToolInput):
    """Operation input for `usergroups_list`."""
    pass

class UsergroupsListOutput(UsergroupsListToolOutput):
    """Operation output for `usergroups_list`."""
    pass

class UsergroupsUpdateInput(UsergroupsUpdateToolInput):
    """Operation input for `usergroups_update`."""
    pass

class UsergroupsUpdateOutput(UsergroupsUpdateToolOutput):
    """Operation output for `usergroups_update`."""
    pass

class SlackUsergroupsResource(BaseResourceClient):
    """Operations for the `usergroups` resource."""

    @operation(
        name='usergroups_create',
        title='UsergroupsCreate',
        input_model=UsergroupsCreateInput,
        output_model=UsergroupsCreateOutput,
        tools_used=('usergroups_create',),
        tags=tuple(['usergroups']),
    )
    async def create(self, data: UsergroupsCreateInput) -> UsergroupsCreateOutput:
        """Create a User Group.

Important inputs: token, body"""
        tool = self._client.get_tool('usergroups_create')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsergroupsCreateOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='usergroups_disable',
        title='UsergroupsDisable',
        input_model=UsergroupsDisableInput,
        output_model=UsergroupsDisableOutput,
        tools_used=('usergroups_disable',),
        tags=tuple(['usergroups']),
    )
    async def disable(self, data: UsergroupsDisableInput) -> UsergroupsDisableOutput:
        """Disable an existing User Group.

Important inputs: token, body"""
        tool = self._client.get_tool('usergroups_disable')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsergroupsDisableOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='usergroups_enable',
        title='UsergroupsEnable',
        input_model=UsergroupsEnableInput,
        output_model=UsergroupsEnableOutput,
        tools_used=('usergroups_enable',),
        tags=tuple(['usergroups']),
    )
    async def enable(self, data: UsergroupsEnableInput) -> UsergroupsEnableOutput:
        """Enable a User Group.

Important inputs: token, body"""
        tool = self._client.get_tool('usergroups_enable')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsergroupsEnableOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='usergroups_list',
        title='UsergroupsList',
        input_model=UsergroupsListInput,
        output_model=UsergroupsListOutput,
        tools_used=('usergroups_list',),
        tags=tuple(['usergroups']),
    )
    async def list(self, data: UsergroupsListInput) -> UsergroupsListOutput:
        """List all User Groups for a team.

Important inputs: include_users, token, include_count, include_disabled"""
        tool = self._client.get_tool('usergroups_list')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsergroupsListOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='usergroups_update',
        title='UsergroupsUpdate',
        input_model=UsergroupsUpdateInput,
        output_model=UsergroupsUpdateOutput,
        tools_used=('usergroups_update',),
        tags=tuple(['usergroups']),
    )
    async def update(self, data: UsergroupsUpdateInput) -> UsergroupsUpdateOutput:
        """Update an existing User Group.

Important inputs: token, body"""
        tool = self._client.get_tool('usergroups_update')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UsergroupsUpdateOutput.model_validate(coerce_tool_result(result))
