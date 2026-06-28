from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import CreateProjectAvatarToolInput, CreateProjectAvatarToolOutput, DeleteProjectAvatarToolInput, DeleteProjectAvatarToolOutput, UpdateProjectAvatarToolInput, UpdateProjectAvatarToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class CreateProjectAvatarInput(CreateProjectAvatarToolInput):
    """Operation input for `create_project_avatar`."""
    pass

class CreateProjectAvatarOutput(CreateProjectAvatarToolOutput):
    """Operation output for `create_project_avatar`."""
    pass

class DeleteProjectAvatarInput(DeleteProjectAvatarToolInput):
    """Operation input for `delete_project_avatar`."""
    pass

class DeleteProjectAvatarOutput(DeleteProjectAvatarToolOutput):
    """Operation output for `delete_project_avatar`."""
    pass

class UpdateProjectAvatarInput(UpdateProjectAvatarToolInput):
    """Operation input for `update_project_avatar`."""
    pass

class UpdateProjectAvatarOutput(UpdateProjectAvatarToolOutput):
    """Operation output for `update_project_avatar`."""
    pass

class JiraProjectAvatarResource(BaseResourceClient):
    """Operations for the `project_avatar` resource."""

    @operation(
        name='create_project_avatar',
        title='CreateProjectAvatar',
        input_model=CreateProjectAvatarInput,
        output_model=CreateProjectAvatarOutput,
        tools_used=('create_project_avatar',),
        tags=tuple(['Project avatars']),
    )
    async def create(self, data: CreateProjectAvatarInput) -> CreateProjectAvatarOutput:
        """Loads an avatar for a project. Specify the avatar's local file location in the body of the request. Also, include the following headers: * `X-Atlassian-Token: no-check` To prevent XSRF protection blocking the request, for more information see [Special Headers](#special-request-headers). * `Content-Type: image/image type` Valid image types are JPEG, GIF, or PNG. For example: `curl --request POST ` `--user email@example.com:<api_token> ` `--header 'X-Atlassian-Token: no-check' ` `--header 'Content-Type: image/< image_type>' ` `--data-binary "<@/path/to/file/with/your/avatar>" ` `--url 'https://your-domain.atlassian.net/rest/api/3/project/{projectIdOrKey}/avatar2'` The avatar is cropped to a square. If no crop parameters are specified, the square originates at the top left of the image. The length of the square's sides is set to the smaller of the height or width of the image. The cropped image is then used to create avatars of 16x16, 24x24, 32x32, and 48x48 in size. After creating the avatar use [Set project avatar](#api-rest-api-3-project-projectIdOrKey-avatar-put) to set it as the project's displayed avatar. **[Permissions](#permissions) required:** *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg).

Important inputs: project_id_or_key, x, y, size, body"""
        tool = self._client.get_tool('create_project_avatar')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return CreateProjectAvatarOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='delete_project_avatar',
        title='DeleteProjectAvatar',
        input_model=DeleteProjectAvatarInput,
        output_model=DeleteProjectAvatarOutput,
        tools_used=('delete_project_avatar',),
        tags=tuple(['Project avatars']),
    )
    async def delete(self, data: DeleteProjectAvatarInput) -> DeleteProjectAvatarOutput:
        """Deletes a custom avatar from a project. Note that system avatars cannot be deleted. **[Permissions](#permissions) required:** *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg).

Important inputs: project_id_or_key, id"""
        tool = self._client.get_tool('delete_project_avatar')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return DeleteProjectAvatarOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='update_project_avatar',
        title='UpdateProjectAvatar',
        input_model=UpdateProjectAvatarInput,
        output_model=UpdateProjectAvatarOutput,
        tools_used=('update_project_avatar',),
        tags=tuple(['Project avatars']),
    )
    async def update(self, data: UpdateProjectAvatarInput) -> UpdateProjectAvatarOutput:
        """Sets the avatar displayed for a project. Use [Load project avatar](#api-rest-api-3-project-projectIdOrKey-avatar2-post) to store avatars against the project, before using this operation to set the displayed avatar. **[Permissions](#permissions) required:** *Administer projects* [project permission](https://confluence.atlassian.com/x/yodKLg).

Important inputs: project_id_or_key, body"""
        tool = self._client.get_tool('update_project_avatar')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return UpdateProjectAvatarOutput.model_validate(coerce_tool_result(result))
