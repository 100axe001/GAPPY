from __future__ import annotations

from lemma_connectors.jira.generated.tool_types import GetColumnsToolInput, GetColumnsToolOutput, SetColumnsToolInput, SetColumnsToolOutput
from lemma_connectors.core.resource import BaseResourceClient, coerce_tool_result, operation

class GetColumnsInput(GetColumnsToolInput):
    """Operation input for `get_columns`."""
    pass

class GetColumnsOutput(GetColumnsToolOutput):
    """Operation output for `get_columns`."""
    pass

class SetColumnsInput(SetColumnsToolInput):
    """Operation input for `set_columns`."""
    pass

class SetColumnsOutput(SetColumnsToolOutput):
    """Operation output for `set_columns`."""
    pass

class JiraColumnsResource(BaseResourceClient):
    """Operations for the `columns` resource."""

    @operation(
        name='get_columns',
        title='GetColumns',
        input_model=GetColumnsInput,
        output_model=GetColumnsOutput,
        tools_used=('get_columns',),
        tags=tuple(['Filters']),
    )
    async def get(self, data: GetColumnsInput) -> GetColumnsOutput:
        """Returns the columns configured for a filter. The column configuration is used when the filter's results are viewed in *List View* with the *Columns* set to *Filter*. This operation can be accessed anonymously. **[Permissions](#permissions) required:** None, however, column details are only returned for: * filters owned by the user. * filters shared with a group that the user is a member of. * filters shared with a private project that the user has *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for. * filters shared with a public project. * filters shared with the public.

Important inputs: id"""
        tool = self._client.get_tool('get_columns')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return GetColumnsOutput.model_validate(coerce_tool_result(result))

    @operation(
        name='set_columns',
        title='SetColumns',
        input_model=SetColumnsInput,
        output_model=SetColumnsOutput,
        tools_used=('set_columns',),
        tags=tuple(['Filters']),
    )
    async def set(self, data: SetColumnsInput) -> SetColumnsOutput:
        """Sets the columns for a filter. Only navigable fields can be set as columns. Use [Get fields](#api-rest-api-3-field-get) to get the list fields in Jira. A navigable field has `navigable` set to `true`. The parameters for this resource are expressed as HTML form data. For example, in curl: `curl -X PUT -d columns=summary -d columns=description https://your-domain.atlassian.net/rest/api/3/filter/10000/columns` **[Permissions](#permissions) required:** Permission to access Jira, however, columns are only set for: * filters owned by the user. * filters shared with a group that the user is a member of. * filters shared with a private project that the user has *Browse projects* [project permission](https://confluence.atlassian.com/x/yodKLg) for. * filters shared with a public project. * filters shared with the public.

Important inputs: id, body"""
        tool = self._client.get_tool('set_columns')
        result = await tool.execute(data.model_dump(exclude_none=True, exclude_unset=True, by_alias=False))
        return SetColumnsOutput.model_validate(coerce_tool_result(result))
