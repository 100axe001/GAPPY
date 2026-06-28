from __future__ import annotations

from lemma_connectors.slack.generated.tool_types import ViewsOpenToolInput, ViewsOpenToolOutput, ViewsPublishToolInput, ViewsPublishToolOutput, ViewsPushToolInput, ViewsPushToolOutput, ViewsUpdateToolInput, ViewsUpdateToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class ViewsOpenInput(ViewsOpenToolInput):
    """Operation input for `views_open`."""
    pass

class ViewsOpenOutput(ViewsOpenToolOutput):
    """Operation output for `views_open`."""
    pass

class ViewsPublishInput(ViewsPublishToolInput):
    """Operation input for `views_publish`."""
    pass

class ViewsPublishOutput(ViewsPublishToolOutput):
    """Operation output for `views_publish`."""
    pass

class ViewsPushInput(ViewsPushToolInput):
    """Operation input for `views_push`."""
    pass

class ViewsPushOutput(ViewsPushToolOutput):
    """Operation output for `views_push`."""
    pass

class ViewsUpdateInput(ViewsUpdateToolInput):
    """Operation input for `views_update`."""
    pass

class ViewsUpdateOutput(ViewsUpdateToolOutput):
    """Operation output for `views_update`."""
    pass

class SlackViewsResource(BaseResourceClient):
    """Operations for the `views` resource."""

    @operation(
        name='views_open',
        title='ViewsOpen',
        input_model=ViewsOpenInput,
        output_model=ViewsOpenOutput,
        tools_used=('views_open',),
        tags=tuple(['views']),
    )
    async def open(self, data: ViewsOpenInput) -> ViewsOpenOutput:
        """Open a view for a user.

Important inputs: token, trigger_id, view"""
        tool = self._client.get_tool('views_open')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return ViewsOpenOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='views_publish',
        title='ViewsPublish',
        input_model=ViewsPublishInput,
        output_model=ViewsPublishOutput,
        tools_used=('views_publish',),
        tags=tuple(['views']),
    )
    async def publish(self, data: ViewsPublishInput) -> ViewsPublishOutput:
        """Publish a static view for a User.

Important inputs: token, user_id, view, hash"""
        tool = self._client.get_tool('views_publish')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return ViewsPublishOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='views_push',
        title='ViewsPush',
        input_model=ViewsPushInput,
        output_model=ViewsPushOutput,
        tools_used=('views_push',),
        tags=tuple(['views']),
    )
    async def push(self, data: ViewsPushInput) -> ViewsPushOutput:
        """Push a view onto the stack of a root view.

Important inputs: token, trigger_id, view"""
        tool = self._client.get_tool('views_push')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return ViewsPushOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='views_update',
        title='ViewsUpdate',
        input_model=ViewsUpdateInput,
        output_model=ViewsUpdateOutput,
        tools_used=('views_update',),
        tags=tuple(['views']),
    )
    async def update(self, data: ViewsUpdateInput) -> ViewsUpdateOutput:
        """Update an existing view.

Important inputs: token, view_id, external_id, view, hash"""
        tool = self._client.get_tool('views_update')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return ViewsUpdateOutput.model_validate(coerce_tool_result(result))
