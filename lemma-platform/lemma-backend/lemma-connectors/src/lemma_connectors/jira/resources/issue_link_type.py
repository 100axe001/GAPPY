from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import CreateIssueLinkTypeToolInput, CreateIssueLinkTypeToolOutput, DeleteIssueLinkTypeToolInput, DeleteIssueLinkTypeToolOutput, GetIssueLinkTypeToolInput, GetIssueLinkTypeToolOutput, UpdateIssueLinkTypeToolInput, UpdateIssueLinkTypeToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class CreateIssueLinkTypeInput(CreateIssueLinkTypeToolInput):
    """Operation input for `create_issue_link_type`."""
    pass

class CreateIssueLinkTypeOutput(CreateIssueLinkTypeToolOutput):
    """Operation output for `create_issue_link_type`."""
    pass

class DeleteIssueLinkTypeInput(DeleteIssueLinkTypeToolInput):
    """Operation input for `delete_issue_link_type`."""
    pass

class DeleteIssueLinkTypeOutput(DeleteIssueLinkTypeToolOutput):
    """Operation output for `delete_issue_link_type`."""
    pass

class GetIssueLinkTypeInput(GetIssueLinkTypeToolInput):
    """Operation input for `get_issue_link_type`."""
    pass

class GetIssueLinkTypeOutput(GetIssueLinkTypeToolOutput):
    """Operation output for `get_issue_link_type`."""
    pass

class UpdateIssueLinkTypeInput(UpdateIssueLinkTypeToolInput):
    """Operation input for `update_issue_link_type`."""
    pass

class UpdateIssueLinkTypeOutput(UpdateIssueLinkTypeToolOutput):
    """Operation output for `update_issue_link_type`."""
    pass

class JiraIssueLinkTypeResource(BaseResourceClient):
    """Operations for the `issue_link_type` resource."""

    @operation(
        name='create_issue_link_type',
        title='CreateIssueLinkType',
        input_model=CreateIssueLinkTypeInput,
        output_model=CreateIssueLinkTypeOutput,
        tools_used=('create_issue_link_type',),
        tags=tuple(['Issue link types']),
    )
    async def create(self, data: CreateIssueLinkTypeInput) -> CreateIssueLinkTypeOutput:
        """Creates an issue link type. Use this operation to create descriptions of the reasons why issues are linked. The issue link type consists of a name and descriptions for a link's inward and outward relationships. To use this operation, the site must have [issue linking](https://confluence.atlassian.com/x/yoXKM) enabled. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: body"""
        tool = self._client.get_tool('create_issue_link_type')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return CreateIssueLinkTypeOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='delete_issue_link_type',
        title='DeleteIssueLinkType',
        input_model=DeleteIssueLinkTypeInput,
        output_model=DeleteIssueLinkTypeOutput,
        tools_used=('delete_issue_link_type',),
        tags=tuple(['Issue link types']),
    )
    async def delete(self, data: DeleteIssueLinkTypeInput) -> DeleteIssueLinkTypeOutput:
        """Deletes an issue link type. To use this operation, the site must have [issue linking](https://confluence.atlassian.com/x/yoXKM) enabled. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: issue_link_type_id"""
        tool = self._client.get_tool('delete_issue_link_type')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DeleteIssueLinkTypeOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='get_issue_link_type',
        title='GetIssueLinkType',
        input_model=GetIssueLinkTypeInput,
        output_model=GetIssueLinkTypeOutput,
        tools_used=('get_issue_link_type',),
        tags=tuple(['Issue link types']),
    )
    async def get(self, data: GetIssueLinkTypeInput) -> GetIssueLinkTypeOutput:
        """Returns an issue link type. To use this operation, the site must have [issue linking](https://confluence.atlassian.com/x/yoXKM) enabled. This operation can be accessed anonymously. **[Permissions](#permissions) required:** *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for a project in the site.

Important inputs: issue_link_type_id"""
        tool = self._client.get_tool('get_issue_link_type')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetIssueLinkTypeOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='update_issue_link_type',
        title='UpdateIssueLinkType',
        input_model=UpdateIssueLinkTypeInput,
        output_model=UpdateIssueLinkTypeOutput,
        tools_used=('update_issue_link_type',),
        tags=tuple(['Issue link types']),
    )
    async def update(self, data: UpdateIssueLinkTypeInput) -> UpdateIssueLinkTypeOutput:
        """Updates an issue link type. To use this operation, the site must have [issue linking](https://confluence.atlassian.com/x/yoXKM) enabled. **[Permissions](#permissions) required:** *Administer Jira* [global permission](https://confluence.atlassian.com/x/x4dKLg).

Important inputs: issue_link_type_id, body"""
        tool = self._client.get_tool('update_issue_link_type')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UpdateIssueLinkTypeOutput.model_validate(coerce_tool_result(result))
