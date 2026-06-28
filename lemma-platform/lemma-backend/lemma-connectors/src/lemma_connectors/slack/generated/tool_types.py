from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, RootModel

from lemma_connectors.core.results import BinaryContentResult

from lemma_connectors.slack.generated.pydantic_models import ApiTestResponse, AppsEventAuthorizationsListResponse, AppsPermissionsInfoResponse, AppsPermissionsRequestResponse, AppsPermissionsResourcesListResponse, AppsPermissionsScopesListResponse, AppsPermissionsUsersListResponse, AppsPermissionsUsersRequestResponse, AppsUninstallResponse, AuthRevokeResponse, AuthTestResponse, BotsInfoResponse, CallsAddRequest, CallsAddResponse, CallsEndRequest, CallsEndResponse, CallsInfoResponse, CallsParticipantsAddRequest, CallsParticipantsAddResponse, CallsParticipantsRemoveRequest, CallsParticipantsRemoveResponse, CallsUpdateRequest, CallsUpdateResponse, ChatDeleteRequest, ChatDeleteResponse, ChatDeleteScheduledMessageRequest, ChatDeleteScheduledMessageResponse, ChatGetPermalinkResponse, ChatMeMessageRequest, ChatMeMessageResponse, ChatPostEphemeralRequest, ChatPostEphemeralResponse, ChatPostMessageRequest, ChatPostMessageResponse, ChatScheduleMessageRequest, ChatScheduleMessageResponse, ChatScheduledMessagesListResponse, ChatUnfurlRequest, ChatUnfurlResponse, ChatUpdateRequest, ChatUpdateResponse, ConversationsArchiveRequest, ConversationsArchiveResponse, ConversationsCloseRequest, ConversationsCloseResponse, ConversationsCreateRequest, ConversationsCreateResponse, ConversationsHistoryResponse, ConversationsInfoResponse, ConversationsInviteRequest, ConversationsInviteResponse, ConversationsJoinRequest, ConversationsJoinResponse, ConversationsKickRequest, ConversationsKickResponse, ConversationsLeaveRequest, ConversationsLeaveResponse, ConversationsListResponse, ConversationsMarkRequest, ConversationsMarkResponse, ConversationsMembersResponse, ConversationsOpenRequest, ConversationsOpenResponse, ConversationsRenameRequest, ConversationsRenameResponse, ConversationsRepliesResponse, ConversationsSetPurposeRequest, ConversationsSetPurposeResponse, ConversationsSetTopicRequest, ConversationsSetTopicResponse, ConversationsUnarchiveRequest, ConversationsUnarchiveResponse, DialogOpenResponse, DndEndDndResponse, DndEndSnoozeResponse, DndInfoResponse, DndSetSnoozeRequest, DndSetSnoozeResponse, DndTeamInfoResponse, EmojiListResponse, FilesCommentsDeleteRequest, FilesCommentsDeleteResponse, FilesDeleteRequest, FilesDeleteResponse, FilesInfoResponse, FilesListResponse, FilesRemoteAddRequest, FilesRemoteAddResponse, FilesRemoteInfoResponse, FilesRemoteListResponse, FilesRemoteRemoveRequest, FilesRemoteRemoveResponse, FilesRemoteShareResponse, FilesRemoteUpdateRequest, FilesRemoteUpdateResponse, FilesUploadRequest, FilesUploadResponse, MigrationExchangeResponse, OauthAccessResponse, OauthTokenResponse, OauthV2AccessResponse, PinsAddRequest, PinsAddResponse, PinsListResponse, PinsRemoveRequest, PinsRemoveResponse, ReactionsAddRequest, ReactionsAddResponse, ReactionsGetResponse, ReactionsListResponse, ReactionsRemoveRequest, ReactionsRemoveResponse, RemindersAddRequest, RemindersAddResponse, RemindersCompleteRequest, RemindersCompleteResponse, RemindersDeleteRequest, RemindersDeleteResponse, RemindersInfoResponse, RemindersListResponse, RtmConnectResponse, SearchMessagesResponse, StarsAddRequest, StarsAddResponse, StarsListResponse, StarsRemoveRequest, StarsRemoveResponse, TeamAccessLogsResponse, TeamBillableInfoResponse, TeamInfoResponse, TeamIntegrationLogsResponse, TeamProfileGetResponse, UsergroupsCreateRequest, UsergroupsCreateResponse, UsergroupsDisableRequest, UsergroupsDisableResponse, UsergroupsEnableRequest, UsergroupsEnableResponse, UsergroupsListResponse, UsergroupsUpdateRequest, UsergroupsUpdateResponse, UsergroupsUsersListResponse, UsergroupsUsersUpdateRequest, UsergroupsUsersUpdateResponse, UsersConversationsResponse, UsersDeletePhotoRequest, UsersDeletePhotoResponse, UsersGetPresenceResponse, UsersIdentityResponse, UsersInfoResponse, UsersListResponse, UsersLookupByEmailResponse, UsersProfileGetResponse, UsersProfileSetRequest, UsersProfileSetResponse, UsersSetActiveResponse, UsersSetPhotoRequest, UsersSetPhotoResponse, UsersSetPresenceRequest, UsersSetPresenceResponse, ViewsOpenResponse, ViewsPublishResponse, ViewsPushResponse, ViewsUpdateResponse, WorkflowsStepCompletedResponse, WorkflowsStepFailedResponse, WorkflowsUpdateStepResponse

class ApiTestToolInput(BaseModel):
    """Input for tool `api_test`."""
    error: str | None = Field(default=None, description='Error response to return')
    foo: str | None = Field(default=None, description='example property to return')
    model_config = ConfigDict(extra='forbid')

class ApiTestToolOutput(ApiTestResponse):
    """Output for tool `api_test`."""
    pass

class AppsEventAuthorizationsListToolInput(BaseModel):
    """Input for tool `apps_event_authorizations_list`."""
    token: str = Field(..., description='Authentication token. Requires scope: `authorizations:read`')
    event_context: str = Field(...)
    cursor: str | None = None
    limit: int | None = None
    model_config = ConfigDict(extra='forbid')

class AppsEventAuthorizationsListToolOutput(AppsEventAuthorizationsListResponse):
    """Output for tool `apps_event_authorizations_list`."""
    pass

class AppsPermissionsInfoToolInput(BaseModel):
    """Input for tool `apps_permissions_info`."""
    token: str | None = Field(default=None, description='Authentication token. Requires scope: `none`')
    model_config = ConfigDict(extra='forbid')

class AppsPermissionsInfoToolOutput(AppsPermissionsInfoResponse):
    """Output for tool `apps_permissions_info`."""
    pass

class AppsPermissionsRequestToolInput(BaseModel):
    """Input for tool `apps_permissions_request`."""
    token: str = Field(..., description='Authentication token. Requires scope: `none`')
    scopes: str = Field(..., description='A comma separated list of scopes to request for')
    trigger_id: str = Field(..., description='Token used to trigger the permissions API')
    model_config = ConfigDict(extra='forbid')

class AppsPermissionsRequestToolOutput(AppsPermissionsRequestResponse):
    """Output for tool `apps_permissions_request`."""
    pass

class AppsPermissionsResourcesListToolInput(BaseModel):
    """Input for tool `apps_permissions_resources_list`."""
    token: str = Field(..., description='Authentication token. Requires scope: `none`')
    cursor: str | None = Field(default=None, description='Paginate through collections of data by setting the `cursor` parameter to a `next_cursor` attribute returned by a previous request\'s `response_metadata`. Default value fetches the first "page" of the collection. See [pagination](/docs/pagination) for more detail.')
    limit: int | None = Field(default=None, description='The maximum number of items to return.')
    model_config = ConfigDict(extra='forbid')

class AppsPermissionsResourcesListToolOutput(AppsPermissionsResourcesListResponse):
    """Output for tool `apps_permissions_resources_list`."""
    pass

class AppsPermissionsScopesListToolInput(BaseModel):
    """Input for tool `apps_permissions_scopes_list`."""
    token: str = Field(..., description='Authentication token. Requires scope: `none`')
    model_config = ConfigDict(extra='forbid')

class AppsPermissionsScopesListToolOutput(AppsPermissionsScopesListResponse):
    """Output for tool `apps_permissions_scopes_list`."""
    pass

class AppsPermissionsUsersListToolInput(BaseModel):
    """Input for tool `apps_permissions_users_list`."""
    token: str = Field(..., description='Authentication token. Requires scope: `none`')
    cursor: str | None = Field(default=None, description='Paginate through collections of data by setting the `cursor` parameter to a `next_cursor` attribute returned by a previous request\'s `response_metadata`. Default value fetches the first "page" of the collection. See [pagination](/docs/pagination) for more detail.')
    limit: int | None = Field(default=None, description='The maximum number of items to return.')
    model_config = ConfigDict(extra='forbid')

class AppsPermissionsUsersListToolOutput(AppsPermissionsUsersListResponse):
    """Output for tool `apps_permissions_users_list`."""
    pass

class AppsPermissionsUsersRequestToolInput(BaseModel):
    """Input for tool `apps_permissions_users_request`."""
    token: str = Field(..., description='Authentication token. Requires scope: `none`')
    scopes: str = Field(..., description='A comma separated list of user scopes to request for')
    trigger_id: str = Field(..., description='Token used to trigger the request')
    user: str = Field(..., description='The user this scope is being requested for')
    model_config = ConfigDict(extra='forbid')

class AppsPermissionsUsersRequestToolOutput(AppsPermissionsUsersRequestResponse):
    """Output for tool `apps_permissions_users_request`."""
    pass

class AppsUninstallToolInput(BaseModel):
    """Input for tool `apps_uninstall`."""
    token: str | None = Field(default=None, description='Authentication token. Requires scope: `none`')
    client_id: str | None = Field(default=None, description='Issued when you created your application.')
    client_secret: str | None = Field(default=None, description='Issued when you created your application.')
    model_config = ConfigDict(extra='forbid')

class AppsUninstallToolOutput(AppsUninstallResponse):
    """Output for tool `apps_uninstall`."""
    pass

class AuthRevokeToolInput(BaseModel):
    """Input for tool `auth_revoke`."""
    token: str = Field(..., description='Authentication token. Requires scope: `none`')
    test: bool | None = Field(default=None, description='Setting this parameter to `1` triggers a _testing mode_ where the specified token will not actually be revoked.')
    model_config = ConfigDict(extra='forbid')

class AuthRevokeToolOutput(AuthRevokeResponse):
    """Output for tool `auth_revoke`."""
    pass

class AuthTestToolInput(BaseModel):
    """Input for tool `auth_test`."""
    token: str = Field(..., description='Authentication token. Requires scope: `none`')
    model_config = ConfigDict(extra='forbid')

class AuthTestToolOutput(AuthTestResponse):
    """Output for tool `auth_test`."""
    pass

class BotsInfoToolInput(BaseModel):
    """Input for tool `bots_info`."""
    token: str = Field(..., description='Authentication token. Requires scope: `users:read`')
    bot: str | None = Field(default=None, description='Bot user to get info on')
    model_config = ConfigDict(extra='forbid')

class BotsInfoToolOutput(BotsInfoResponse):
    """Output for tool `bots_info`."""
    pass

class CallsAddToolInput(BaseModel):
    """Input for tool `calls_add`."""
    token: str = Field(..., description='Authentication token. Requires scope: `calls:write`')
    body: CallsAddRequest = Field(..., description='Request body for `calls_add`.')
    model_config = ConfigDict(extra='forbid')

class CallsAddToolOutput(CallsAddResponse):
    """Output for tool `calls_add`."""
    pass

class CallsEndToolInput(BaseModel):
    """Input for tool `calls_end`."""
    token: str = Field(..., description='Authentication token. Requires scope: `calls:write`')
    body: CallsEndRequest = Field(..., description='Request body for `calls_end`.')
    model_config = ConfigDict(extra='forbid')

class CallsEndToolOutput(CallsEndResponse):
    """Output for tool `calls_end`."""
    pass

class CallsInfoToolInput(BaseModel):
    """Input for tool `calls_info`."""
    token: str = Field(..., description='Authentication token. Requires scope: `calls:read`')
    id: str = Field(..., description='`id` of the Call returned by the [`calls.add`](/methods/calls.add) method.')
    model_config = ConfigDict(extra='forbid')

class CallsInfoToolOutput(CallsInfoResponse):
    """Output for tool `calls_info`."""
    pass

class CallsParticipantsAddToolInput(BaseModel):
    """Input for tool `calls_participants_add`."""
    token: str = Field(..., description='Authentication token. Requires scope: `calls:write`')
    body: CallsParticipantsAddRequest = Field(..., description='Request body for `calls_participants_add`.')
    model_config = ConfigDict(extra='forbid')

class CallsParticipantsAddToolOutput(CallsParticipantsAddResponse):
    """Output for tool `calls_participants_add`."""
    pass

class CallsParticipantsRemoveToolInput(BaseModel):
    """Input for tool `calls_participants_remove`."""
    token: str = Field(..., description='Authentication token. Requires scope: `calls:write`')
    body: CallsParticipantsRemoveRequest = Field(..., description='Request body for `calls_participants_remove`.')
    model_config = ConfigDict(extra='forbid')

class CallsParticipantsRemoveToolOutput(CallsParticipantsRemoveResponse):
    """Output for tool `calls_participants_remove`."""
    pass

class CallsUpdateToolInput(BaseModel):
    """Input for tool `calls_update`."""
    token: str = Field(..., description='Authentication token. Requires scope: `calls:write`')
    body: CallsUpdateRequest = Field(..., description='Request body for `calls_update`.')
    model_config = ConfigDict(extra='forbid')

class CallsUpdateToolOutput(CallsUpdateResponse):
    """Output for tool `calls_update`."""
    pass

class ChatDeleteToolInput(BaseModel):
    """Input for tool `chat_delete`."""
    token: str | None = Field(default=None, description='Authentication token. Requires scope: `chat:write`')
    body: ChatDeleteRequest | None = Field(default=None, description='Request body for `chat_delete`.')
    model_config = ConfigDict(extra='forbid')

class ChatDeleteToolOutput(ChatDeleteResponse):
    """Output for tool `chat_delete`."""
    pass

class ChatDeleteScheduledMessageToolInput(BaseModel):
    """Input for tool `chat_delete_scheduled_message`."""
    token: str = Field(..., description='Authentication token. Requires scope: `chat:write`')
    body: ChatDeleteScheduledMessageRequest | None = Field(default=None, description='Request body for `chat_delete_scheduled_message`.')
    model_config = ConfigDict(extra='forbid')

class ChatDeleteScheduledMessageToolOutput(ChatDeleteScheduledMessageResponse):
    """Output for tool `chat_delete_scheduled_message`."""
    pass

class ChatGetPermalinkToolInput(BaseModel):
    """Input for tool `chat_get_permalink`."""
    token: str = Field(..., description='Authentication token. Requires scope: `none`')
    channel: str = Field(..., description='The ID of the conversation or channel containing the message')
    message_ts: str = Field(..., description="A message's `ts` value, uniquely identifying it within a channel")
    model_config = ConfigDict(extra='forbid')

class ChatGetPermalinkToolOutput(ChatGetPermalinkResponse):
    """Output for tool `chat_get_permalink`."""
    pass

class ChatMeMessageToolInput(BaseModel):
    """Input for tool `chat_me_message`."""
    token: str | None = Field(default=None, description='Authentication token. Requires scope: `chat:write`')
    body: ChatMeMessageRequest | None = Field(default=None, description='Request body for `chat_me_message`.')
    model_config = ConfigDict(extra='forbid')

class ChatMeMessageToolOutput(ChatMeMessageResponse):
    """Output for tool `chat_me_message`."""
    pass

class ChatPostEphemeralToolInput(BaseModel):
    """Input for tool `chat_post_ephemeral`."""
    token: str = Field(..., description='Authentication token. Requires scope: `chat:write`')
    body: ChatPostEphemeralRequest | None = Field(default=None, description='Request body for `chat_post_ephemeral`.')
    model_config = ConfigDict(extra='forbid')

class ChatPostEphemeralToolOutput(ChatPostEphemeralResponse):
    """Output for tool `chat_post_ephemeral`."""
    pass

class ChatPostMessageToolInput(BaseModel):
    """Input for tool `chat_post_message`."""
    token: str = Field(..., description='Authentication token. Requires scope: `chat:write`')
    body: ChatPostMessageRequest | None = Field(default=None, description='Request body for `chat_post_message`.')
    model_config = ConfigDict(extra='forbid')

class ChatPostMessageToolOutput(ChatPostMessageResponse):
    """Output for tool `chat_post_message`."""
    pass

class ChatScheduleMessageToolInput(BaseModel):
    """Input for tool `chat_schedule_message`."""
    token: str | None = Field(default=None, description='Authentication token. Requires scope: `chat:write`')
    body: ChatScheduleMessageRequest | None = Field(default=None, description='Request body for `chat_schedule_message`.')
    model_config = ConfigDict(extra='forbid')

class ChatScheduleMessageToolOutput(ChatScheduleMessageResponse):
    """Output for tool `chat_schedule_message`."""
    pass

class ChatScheduledMessagesListToolInput(BaseModel):
    """Input for tool `chat_scheduled_messages_list`."""
    token: str | None = Field(default=None, description='Authentication token. Requires scope: `none`')
    channel: str | None = Field(default=None, description='The channel of the scheduled messages')
    latest: float | None = Field(default=None, description='A UNIX timestamp of the latest value in the time range')
    oldest: float | None = Field(default=None, description='A UNIX timestamp of the oldest value in the time range')
    limit: int | None = Field(default=None, description='Maximum number of original entries to return.')
    cursor: str | None = Field(default=None, description='For pagination purposes, this is the `cursor` value returned from a previous call to `chat.scheduledmessages.list` indicating where you want to start this call from.')
    model_config = ConfigDict(extra='forbid')

class ChatScheduledMessagesListToolOutput(ChatScheduledMessagesListResponse):
    """Output for tool `chat_scheduled_messages_list`."""
    pass

class ChatUnfurlToolInput(BaseModel):
    """Input for tool `chat_unfurl`."""
    token: str = Field(..., description='Authentication token. Requires scope: `links:write`')
    body: ChatUnfurlRequest = Field(..., description='Request body for `chat_unfurl`.')
    model_config = ConfigDict(extra='forbid')

class ChatUnfurlToolOutput(ChatUnfurlResponse):
    """Output for tool `chat_unfurl`."""
    pass

class ChatUpdateToolInput(BaseModel):
    """Input for tool `chat_update`."""
    token: str = Field(..., description='Authentication token. Requires scope: `chat:write`')
    body: ChatUpdateRequest | None = Field(default=None, description='Request body for `chat_update`.')
    model_config = ConfigDict(extra='forbid')

class ChatUpdateToolOutput(ChatUpdateResponse):
    """Output for tool `chat_update`."""
    pass

class ConversationsArchiveToolInput(BaseModel):
    """Input for tool `conversations_archive`."""
    token: str | None = Field(default=None, description='Authentication token. Requires scope: `conversations:write`')
    body: ConversationsArchiveRequest | None = Field(default=None, description='Request body for `conversations_archive`.')
    model_config = ConfigDict(extra='forbid')

class ConversationsArchiveToolOutput(ConversationsArchiveResponse):
    """Output for tool `conversations_archive`."""
    pass

class ConversationsCloseToolInput(BaseModel):
    """Input for tool `conversations_close`."""
    token: str | None = Field(default=None, description='Authentication token. Requires scope: `conversations:write`')
    body: ConversationsCloseRequest | None = Field(default=None, description='Request body for `conversations_close`.')
    model_config = ConfigDict(extra='forbid')

class ConversationsCloseToolOutput(ConversationsCloseResponse):
    """Output for tool `conversations_close`."""
    pass

class ConversationsCreateToolInput(BaseModel):
    """Input for tool `conversations_create`."""
    token: str | None = Field(default=None, description='Authentication token. Requires scope: `conversations:write`')
    body: ConversationsCreateRequest | None = Field(default=None, description='Request body for `conversations_create`.')
    model_config = ConfigDict(extra='forbid')

class ConversationsCreateToolOutput(ConversationsCreateResponse):
    """Output for tool `conversations_create`."""
    pass

class ConversationsHistoryToolInput(BaseModel):
    """Input for tool `conversations_history`."""
    token: str | None = Field(default=None, description='Authentication token. Requires scope: `conversations:history`')
    channel: str | None = Field(default=None, description='Conversation ID to fetch history for.')
    latest: float | None = Field(default=None, description='End of time range of messages to include in results.')
    oldest: float | None = Field(default=None, description='Start of time range of messages to include in results.')
    inclusive: bool | None = Field(default=None, description='Include messages with latest or oldest timestamp in results only when either timestamp is specified.')
    limit: int | None = Field(default=None, description="The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the users list hasn't been reached.")
    cursor: str | None = Field(default=None, description='Paginate through collections of data by setting the `cursor` parameter to a `next_cursor` attribute returned by a previous request\'s `response_metadata`. Default value fetches the first "page" of the collection. See [pagination](/docs/pagination) for more detail.')
    model_config = ConfigDict(extra='forbid')

class ConversationsHistoryToolOutput(ConversationsHistoryResponse):
    """Output for tool `conversations_history`."""
    pass

class ConversationsInfoToolInput(BaseModel):
    """Input for tool `conversations_info`."""
    token: str | None = Field(default=None, description='Authentication token. Requires scope: `conversations:read`')
    channel: str | None = Field(default=None, description='Conversation ID to learn more about')
    include_locale: bool | None = Field(default=None, description='Set this to `true` to receive the locale for this conversation. Defaults to `false`')
    include_num_members: bool | None = Field(default=None, description='Set to `true` to include the member count for the specified conversation. Defaults to `false`')
    model_config = ConfigDict(extra='forbid')

class ConversationsInfoToolOutput(ConversationsInfoResponse):
    """Output for tool `conversations_info`."""
    pass

class ConversationsInviteToolInput(BaseModel):
    """Input for tool `conversations_invite`."""
    token: str | None = Field(default=None, description='Authentication token. Requires scope: `conversations:write`')
    body: ConversationsInviteRequest | None = Field(default=None, description='Request body for `conversations_invite`.')
    model_config = ConfigDict(extra='forbid')

class ConversationsInviteToolOutput(ConversationsInviteResponse):
    """Output for tool `conversations_invite`."""
    pass

class ConversationsJoinToolInput(BaseModel):
    """Input for tool `conversations_join`."""
    token: str | None = Field(default=None, description='Authentication token. Requires scope: `channels:write`')
    body: ConversationsJoinRequest | None = Field(default=None, description='Request body for `conversations_join`.')
    model_config = ConfigDict(extra='forbid')

class ConversationsJoinToolOutput(ConversationsJoinResponse):
    """Output for tool `conversations_join`."""
    pass

class ConversationsKickToolInput(BaseModel):
    """Input for tool `conversations_kick`."""
    token: str | None = Field(default=None, description='Authentication token. Requires scope: `conversations:write`')
    body: ConversationsKickRequest | None = Field(default=None, description='Request body for `conversations_kick`.')
    model_config = ConfigDict(extra='forbid')

class ConversationsKickToolOutput(ConversationsKickResponse):
    """Output for tool `conversations_kick`."""
    pass

class ConversationsLeaveToolInput(BaseModel):
    """Input for tool `conversations_leave`."""
    token: str | None = Field(default=None, description='Authentication token. Requires scope: `conversations:write`')
    body: ConversationsLeaveRequest | None = Field(default=None, description='Request body for `conversations_leave`.')
    model_config = ConfigDict(extra='forbid')

class ConversationsLeaveToolOutput(ConversationsLeaveResponse):
    """Output for tool `conversations_leave`."""
    pass

class ConversationsListToolInput(BaseModel):
    """Input for tool `conversations_list`."""
    token: str | None = Field(default=None, description='Authentication token. Requires scope: `conversations:read`')
    exclude_archived: bool | None = Field(default=None, description='Set to `true` to exclude archived channels from the list')
    types: str | None = Field(default=None, description='Mix and match channel types by providing a comma-separated list of any combination of `public_channel`, `private_channel`, `mpim`, `im`')
    limit: int | None = Field(default=None, description="The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the list hasn't been reached. Must be an integer no larger than 1000.")
    cursor: str | None = Field(default=None, description='Paginate through collections of data by setting the `cursor` parameter to a `next_cursor` attribute returned by a previous request\'s `response_metadata`. Default value fetches the first "page" of the collection. See [pagination](/docs/pagination) for more detail.')
    model_config = ConfigDict(extra='forbid')

class ConversationsListToolOutput(ConversationsListResponse):
    """Output for tool `conversations_list`."""
    pass

class ConversationsMarkToolInput(BaseModel):
    """Input for tool `conversations_mark`."""
    token: str | None = Field(default=None, description='Authentication token. Requires scope: `conversations:write`')
    body: ConversationsMarkRequest | None = Field(default=None, description='Request body for `conversations_mark`.')
    model_config = ConfigDict(extra='forbid')

class ConversationsMarkToolOutput(ConversationsMarkResponse):
    """Output for tool `conversations_mark`."""
    pass

class ConversationsMembersToolInput(BaseModel):
    """Input for tool `conversations_members`."""
    token: str | None = Field(default=None, description='Authentication token. Requires scope: `conversations:read`')
    channel: str | None = Field(default=None, description='ID of the conversation to retrieve members for')
    limit: int | None = Field(default=None, description="The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the users list hasn't been reached.")
    cursor: str | None = Field(default=None, description='Paginate through collections of data by setting the `cursor` parameter to a `next_cursor` attribute returned by a previous request\'s `response_metadata`. Default value fetches the first "page" of the collection. See [pagination](/docs/pagination) for more detail.')
    model_config = ConfigDict(extra='forbid')

class ConversationsMembersToolOutput(ConversationsMembersResponse):
    """Output for tool `conversations_members`."""
    pass

class ConversationsOpenToolInput(BaseModel):
    """Input for tool `conversations_open`."""
    token: str | None = Field(default=None, description='Authentication token. Requires scope: `conversations:write`')
    body: ConversationsOpenRequest | None = Field(default=None, description='Request body for `conversations_open`.')
    model_config = ConfigDict(extra='forbid')

class ConversationsOpenToolOutput(ConversationsOpenResponse):
    """Output for tool `conversations_open`."""
    pass

class ConversationsRenameToolInput(BaseModel):
    """Input for tool `conversations_rename`."""
    token: str | None = Field(default=None, description='Authentication token. Requires scope: `conversations:write`')
    body: ConversationsRenameRequest | None = Field(default=None, description='Request body for `conversations_rename`.')
    model_config = ConfigDict(extra='forbid')

class ConversationsRenameToolOutput(ConversationsRenameResponse):
    """Output for tool `conversations_rename`."""
    pass

class ConversationsRepliesToolInput(BaseModel):
    """Input for tool `conversations_replies`."""
    token: str | None = Field(default=None, description='Authentication token. Requires scope: `conversations:history`')
    channel: str | None = Field(default=None, description='Conversation ID to fetch thread from.')
    ts: float | None = Field(default=None, description="Unique identifier of a thread's parent message. `ts` must be the timestamp of an existing message with 0 or more replies. If there are no replies then just the single message referenced by `ts` will return - it is just an ordinary, unthreaded message.")
    latest: float | None = Field(default=None, description='End of time range of messages to include in results.')
    oldest: float | None = Field(default=None, description='Start of time range of messages to include in results.')
    inclusive: bool | None = Field(default=None, description='Include messages with latest or oldest timestamp in results only when either timestamp is specified.')
    limit: int | None = Field(default=None, description="The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the users list hasn't been reached.")
    cursor: str | None = Field(default=None, description='Paginate through collections of data by setting the `cursor` parameter to a `next_cursor` attribute returned by a previous request\'s `response_metadata`. Default value fetches the first "page" of the collection. See [pagination](/docs/pagination) for more detail.')
    model_config = ConfigDict(extra='forbid')

class ConversationsRepliesToolOutput(ConversationsRepliesResponse):
    """Output for tool `conversations_replies`."""
    pass

class ConversationsSetPurposeToolInput(BaseModel):
    """Input for tool `conversations_set_purpose`."""
    token: str | None = Field(default=None, description='Authentication token. Requires scope: `conversations:write`')
    body: ConversationsSetPurposeRequest | None = Field(default=None, description='Request body for `conversations_set_purpose`.')
    model_config = ConfigDict(extra='forbid')

class ConversationsSetPurposeToolOutput(ConversationsSetPurposeResponse):
    """Output for tool `conversations_set_purpose`."""
    pass

class ConversationsSetTopicToolInput(BaseModel):
    """Input for tool `conversations_set_topic`."""
    token: str | None = Field(default=None, description='Authentication token. Requires scope: `conversations:write`')
    body: ConversationsSetTopicRequest | None = Field(default=None, description='Request body for `conversations_set_topic`.')
    model_config = ConfigDict(extra='forbid')

class ConversationsSetTopicToolOutput(ConversationsSetTopicResponse):
    """Output for tool `conversations_set_topic`."""
    pass

class ConversationsUnarchiveToolInput(BaseModel):
    """Input for tool `conversations_unarchive`."""
    token: str | None = Field(default=None, description='Authentication token. Requires scope: `conversations:write`')
    body: ConversationsUnarchiveRequest | None = Field(default=None, description='Request body for `conversations_unarchive`.')
    model_config = ConfigDict(extra='forbid')

class ConversationsUnarchiveToolOutput(ConversationsUnarchiveResponse):
    """Output for tool `conversations_unarchive`."""
    pass

class DialogOpenToolInput(BaseModel):
    """Input for tool `dialog_open`."""
    token: str = Field(..., description='Authentication token. Requires scope: `none`')
    dialog: str = Field(..., description='The dialog definition. This must be a JSON-encoded string.')
    trigger_id: str = Field(..., description='Exchange a trigger to post to the user.')
    model_config = ConfigDict(extra='forbid')

class DialogOpenToolOutput(DialogOpenResponse):
    """Output for tool `dialog_open`."""
    pass

class DndEndDndToolInput(BaseModel):
    """Input for tool `dnd_end_dnd`."""
    token: str = Field(..., description='Authentication token. Requires scope: `dnd:write`')
    model_config = ConfigDict(extra='forbid')

class DndEndDndToolOutput(DndEndDndResponse):
    """Output for tool `dnd_end_dnd`."""
    pass

class DndEndSnoozeToolInput(BaseModel):
    """Input for tool `dnd_end_snooze`."""
    token: str = Field(..., description='Authentication token. Requires scope: `dnd:write`')
    model_config = ConfigDict(extra='forbid')

class DndEndSnoozeToolOutput(DndEndSnoozeResponse):
    """Output for tool `dnd_end_snooze`."""
    pass

class DndInfoToolInput(BaseModel):
    """Input for tool `dnd_info`."""
    token: str | None = Field(default=None, description='Authentication token. Requires scope: `dnd:read`')
    user: str | None = Field(default=None, description='User to fetch status for (defaults to current user)')
    model_config = ConfigDict(extra='forbid')

class DndInfoToolOutput(DndInfoResponse):
    """Output for tool `dnd_info`."""
    pass

class DndSetSnoozeToolInput(BaseModel):
    """Input for tool `dnd_set_snooze`."""
    body: DndSetSnoozeRequest = Field(..., description='Request body for `dnd_set_snooze`.')
    model_config = ConfigDict(extra='forbid')

class DndSetSnoozeToolOutput(DndSetSnoozeResponse):
    """Output for tool `dnd_set_snooze`."""
    pass

class DndTeamInfoToolInput(BaseModel):
    """Input for tool `dnd_team_info`."""
    token: str | None = Field(default=None, description='Authentication token. Requires scope: `dnd:read`')
    users: str | None = Field(default=None, description='Comma-separated list of users to fetch Do Not Disturb status for')
    model_config = ConfigDict(extra='forbid')

class DndTeamInfoToolOutput(DndTeamInfoResponse):
    """Output for tool `dnd_team_info`."""
    pass

class EmojiListToolInput(BaseModel):
    """Input for tool `emoji_list`."""
    token: str = Field(..., description='Authentication token. Requires scope: `emoji:read`')
    model_config = ConfigDict(extra='forbid')

class EmojiListToolOutput(EmojiListResponse):
    """Output for tool `emoji_list`."""
    pass

class FilesCommentsDeleteToolInput(BaseModel):
    """Input for tool `files_comments_delete`."""
    token: str | None = Field(default=None, description='Authentication token. Requires scope: `files:write:user`')
    body: FilesCommentsDeleteRequest | None = Field(default=None, description='Request body for `files_comments_delete`.')
    model_config = ConfigDict(extra='forbid')

class FilesCommentsDeleteToolOutput(FilesCommentsDeleteResponse):
    """Output for tool `files_comments_delete`."""
    pass

class FilesDeleteToolInput(BaseModel):
    """Input for tool `files_delete`."""
    token: str | None = Field(default=None, description='Authentication token. Requires scope: `files:write:user`')
    body: FilesDeleteRequest | None = Field(default=None, description='Request body for `files_delete`.')
    model_config = ConfigDict(extra='forbid')

class FilesDeleteToolOutput(FilesDeleteResponse):
    """Output for tool `files_delete`."""
    pass

class FilesInfoToolInput(BaseModel):
    """Input for tool `files_info`."""
    token: str | None = Field(default=None, description='Authentication token. Requires scope: `files:read`')
    file: str | None = Field(default=None, description='Specify a file by providing its ID.')
    count: str | None = None
    page: str | None = None
    limit: int | None = Field(default=None, description="The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the list hasn't been reached.")
    cursor: str | None = Field(default=None, description='Parameter for pagination. File comments are paginated for a single file. Set `cursor` equal to the `next_cursor` attribute returned by the previous request\'s `response_metadata`. This parameter is optional, but pagination is mandatory: the default value simply fetches the first "page" of the collection of comments. See [pagination](/docs/pagination) for more details.')
    model_config = ConfigDict(extra='forbid')

class FilesInfoToolOutput(FilesInfoResponse):
    """Output for tool `files_info`."""
    pass

class FilesListToolInput(BaseModel):
    """Input for tool `files_list`."""
    token: str | None = Field(default=None, description='Authentication token. Requires scope: `files:read`')
    user: str | None = Field(default=None, description='Filter files created by a single user.')
    channel: str | None = Field(default=None, description='Filter files appearing in a specific channel, indicated by its ID.')
    ts_from: float | None = Field(default=None, description='Filter files created after this timestamp (inclusive).')
    ts_to: float | None = Field(default=None, description='Filter files created before this timestamp (inclusive).')
    types: str | None = Field(default=None, description='Filter files by type ([see below](#file_types)). You can pass multiple values in the types argument, like `types=spaces,snippets`.The default value is `all`, which does not filter the list.')
    count: str | None = None
    page: str | None = None
    show_files_hidden_by_limit: bool | None = Field(default=None, description='Show truncated file info for files hidden due to being too old, and the team who owns the file being over the file limit.')
    model_config = ConfigDict(extra='forbid')

class FilesListToolOutput(FilesListResponse):
    """Output for tool `files_list`."""
    pass

class FilesRemoteAddToolInput(BaseModel):
    """Input for tool `files_remote_add`."""
    body: FilesRemoteAddRequest | None = Field(default=None, description='Request body for `files_remote_add`.')
    model_config = ConfigDict(extra='forbid')

class FilesRemoteAddToolOutput(FilesRemoteAddResponse):
    """Output for tool `files_remote_add`."""
    pass

class FilesRemoteInfoToolInput(BaseModel):
    """Input for tool `files_remote_info`."""
    token: str | None = Field(default=None, description='Authentication token. Requires scope: `remote_files:read`')
    file: str | None = Field(default=None, description='Specify a file by providing its ID.')
    external_id: str | None = Field(default=None, description='Creator defined GUID for the file.')
    model_config = ConfigDict(extra='forbid')

class FilesRemoteInfoToolOutput(FilesRemoteInfoResponse):
    """Output for tool `files_remote_info`."""
    pass

class FilesRemoteListToolInput(BaseModel):
    """Input for tool `files_remote_list`."""
    token: str | None = Field(default=None, description='Authentication token. Requires scope: `remote_files:read`')
    channel: str | None = Field(default=None, description='Filter files appearing in a specific channel, indicated by its ID.')
    ts_from: float | None = Field(default=None, description='Filter files created after this timestamp (inclusive).')
    ts_to: float | None = Field(default=None, description='Filter files created before this timestamp (inclusive).')
    limit: int | None = Field(default=None, description='The maximum number of items to return.')
    cursor: str | None = Field(default=None, description='Paginate through collections of data by setting the `cursor` parameter to a `next_cursor` attribute returned by a previous request\'s `response_metadata`. Default value fetches the first "page" of the collection. See [pagination](/docs/pagination) for more detail.')
    model_config = ConfigDict(extra='forbid')

class FilesRemoteListToolOutput(FilesRemoteListResponse):
    """Output for tool `files_remote_list`."""
    pass

class FilesRemoteRemoveToolInput(BaseModel):
    """Input for tool `files_remote_remove`."""
    body: FilesRemoteRemoveRequest | None = Field(default=None, description='Request body for `files_remote_remove`.')
    model_config = ConfigDict(extra='forbid')

class FilesRemoteRemoveToolOutput(FilesRemoteRemoveResponse):
    """Output for tool `files_remote_remove`."""
    pass

class FilesRemoteShareToolInput(BaseModel):
    """Input for tool `files_remote_share`."""
    token: str | None = Field(default=None, description='Authentication token. Requires scope: `remote_files:share`')
    file: str | None = Field(default=None, description='Specify a file registered with Slack by providing its ID. Either this field or `external_id` or both are required.')
    external_id: str | None = Field(default=None, description='The globally unique identifier (GUID) for the file, as set by the app registering the file with Slack.  Either this field or `file` or both are required.')
    channels: str | None = Field(default=None, description='Comma-separated list of channel IDs where the file will be shared.')
    model_config = ConfigDict(extra='forbid')

class FilesRemoteShareToolOutput(FilesRemoteShareResponse):
    """Output for tool `files_remote_share`."""
    pass

class FilesRemoteUpdateToolInput(BaseModel):
    """Input for tool `files_remote_update`."""
    body: FilesRemoteUpdateRequest | None = Field(default=None, description='Request body for `files_remote_update`.')
    model_config = ConfigDict(extra='forbid')

class FilesRemoteUpdateToolOutput(FilesRemoteUpdateResponse):
    """Output for tool `files_remote_update`."""
    pass

class FilesRevokePublicUrlToolInput(BaseModel):
    """Input for tool `files_revoke_public_url`."""
    token: str | None = Field(default=None, description='Authentication token. Requires scope: `files:write:user`')
    body: dict[str, object] | None = Field(default=None, description='Request body for `files_revoke_public_url`.')
    model_config = ConfigDict(extra='forbid')

class FilesRevokePublicUrlToolOutput(RootModel[dict[str, object]]):
    """Output for tool `files_revoke_public_url`."""
    pass

class FilesSharedPublicUrlToolInput(BaseModel):
    """Input for tool `files_shared_public_url`."""
    token: str | None = Field(default=None, description='Authentication token. Requires scope: `files:write:user`')
    body: dict[str, object] | None = Field(default=None, description='Request body for `files_shared_public_url`.')
    model_config = ConfigDict(extra='forbid')

class FilesSharedPublicUrlToolOutput(RootModel[dict[str, object]]):
    """Output for tool `files_shared_public_url`."""
    pass

class FilesUploadToolInput(BaseModel):
    """Input for tool `files_upload`."""
    body: FilesUploadRequest | None = Field(default=None, description='Request body for `files_upload`.')
    model_config = ConfigDict(extra='forbid')

class FilesUploadToolOutput(FilesUploadResponse):
    """Output for tool `files_upload`."""
    pass

class MigrationExchangeToolInput(BaseModel):
    """Input for tool `migration_exchange`."""
    token: str = Field(..., description='Authentication token. Requires scope: `tokens.basic`')
    users: str = Field(..., description='A comma-separated list of user ids, up to 400 per request')
    team_id: str | None = Field(default=None, description='Specify team_id starts with `T` in case of Org Token')
    to_old: bool | None = Field(default=None, description='Specify `true` to convert `W` global user IDs to workspace-specific `U` IDs. Defaults to `false`.')
    model_config = ConfigDict(extra='forbid')

class MigrationExchangeToolOutput(MigrationExchangeResponse):
    """Output for tool `migration_exchange`."""
    pass

class OauthAccessToolInput(BaseModel):
    """Input for tool `oauth_access`."""
    client_id: str | None = Field(default=None, description='Issued when you created your application.')
    client_secret: str | None = Field(default=None, description='Issued when you created your application.')
    code: str | None = Field(default=None, description='The `code` param returned via the OAuth callback.')
    redirect_uri: str | None = Field(default=None, description='This must match the originally submitted URI (if one was sent).')
    single_channel: bool | None = Field(default=None, description='Request the user to add your app only to a single channel. Only valid with a [legacy workspace app](https://api.slack.com/legacy-workspace-apps).')
    model_config = ConfigDict(extra='forbid')

class OauthAccessToolOutput(OauthAccessResponse):
    """Output for tool `oauth_access`."""
    pass

class OauthTokenToolInput(BaseModel):
    """Input for tool `oauth_token`."""
    client_id: str | None = Field(default=None, description='Issued when you created your application.')
    client_secret: str | None = Field(default=None, description='Issued when you created your application.')
    code: str | None = Field(default=None, description='The `code` param returned via the OAuth callback.')
    redirect_uri: str | None = Field(default=None, description='This must match the originally submitted URI (if one was sent).')
    single_channel: bool | None = Field(default=None, description='Request the user to add your app only to a single channel.')
    model_config = ConfigDict(extra='forbid')

class OauthTokenToolOutput(OauthTokenResponse):
    """Output for tool `oauth_token`."""
    pass

class OauthV2AccessToolInput(BaseModel):
    """Input for tool `oauth_v2_access`."""
    client_id: str | None = Field(default=None, description='Issued when you created your application.')
    client_secret: str | None = Field(default=None, description='Issued when you created your application.')
    code: str = Field(..., description='The `code` param returned via the OAuth callback.')
    redirect_uri: str | None = Field(default=None, description='This must match the originally submitted URI (if one was sent).')
    model_config = ConfigDict(extra='forbid')

class OauthV2AccessToolOutput(OauthV2AccessResponse):
    """Output for tool `oauth_v2_access`."""
    pass

class PinsAddToolInput(BaseModel):
    """Input for tool `pins_add`."""
    token: str = Field(..., description='Authentication token. Requires scope: `pins:write`')
    body: PinsAddRequest = Field(..., description='Request body for `pins_add`.')
    model_config = ConfigDict(extra='forbid')

class PinsAddToolOutput(PinsAddResponse):
    """Output for tool `pins_add`."""
    pass

class PinsListToolInput(BaseModel):
    """Input for tool `pins_list`."""
    token: str = Field(..., description='Authentication token. Requires scope: `pins:read`')
    channel: str = Field(..., description='Channel to get pinned items for.')
    model_config = ConfigDict(extra='forbid')

class PinsListToolOutput(PinsListResponse):
    """Output for tool `pins_list`."""
    pass

class PinsRemoveToolInput(BaseModel):
    """Input for tool `pins_remove`."""
    token: str = Field(..., description='Authentication token. Requires scope: `pins:write`')
    body: PinsRemoveRequest = Field(..., description='Request body for `pins_remove`.')
    model_config = ConfigDict(extra='forbid')

class PinsRemoveToolOutput(PinsRemoveResponse):
    """Output for tool `pins_remove`."""
    pass

class ReactionsAddToolInput(BaseModel):
    """Input for tool `reactions_add`."""
    token: str = Field(..., description='Authentication token. Requires scope: `reactions:write`')
    body: ReactionsAddRequest = Field(..., description='Request body for `reactions_add`.')
    model_config = ConfigDict(extra='forbid')

class ReactionsAddToolOutput(ReactionsAddResponse):
    """Output for tool `reactions_add`."""
    pass

class ReactionsGetToolInput(BaseModel):
    """Input for tool `reactions_get`."""
    token: str = Field(..., description='Authentication token. Requires scope: `reactions:read`')
    channel: str | None = Field(default=None, description='Channel where the message to get reactions for was posted.')
    file: str | None = Field(default=None, description='File to get reactions for.')
    file_comment: str | None = Field(default=None, description='File comment to get reactions for.')
    full: bool | None = Field(default=None, description='If true always return the complete reaction list.')
    timestamp: str | None = Field(default=None, description='Timestamp of the message to get reactions for.')
    model_config = ConfigDict(extra='forbid')

class ReactionsGetToolOutput(ReactionsGetResponse):
    """Output for tool `reactions_get`."""
    pass

class ReactionsListToolInput(BaseModel):
    """Input for tool `reactions_list`."""
    token: str = Field(..., description='Authentication token. Requires scope: `reactions:read`')
    user: str | None = Field(default=None, description='Show reactions made by this user. Defaults to the authed user.')
    full: bool | None = Field(default=None, description='If true always return the complete reaction list.')
    count: int | None = None
    page: int | None = None
    cursor: str | None = Field(default=None, description='Parameter for pagination. Set `cursor` equal to the `next_cursor` attribute returned by the previous request\'s `response_metadata`. This parameter is optional, but pagination is mandatory: the default value simply fetches the first "page" of the collection. See [pagination](/docs/pagination) for more details.')
    limit: int | None = Field(default=None, description="The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the list hasn't been reached.")
    model_config = ConfigDict(extra='forbid')

class ReactionsListToolOutput(ReactionsListResponse):
    """Output for tool `reactions_list`."""
    pass

class ReactionsRemoveToolInput(BaseModel):
    """Input for tool `reactions_remove`."""
    token: str = Field(..., description='Authentication token. Requires scope: `reactions:write`')
    body: ReactionsRemoveRequest = Field(..., description='Request body for `reactions_remove`.')
    model_config = ConfigDict(extra='forbid')

class ReactionsRemoveToolOutput(ReactionsRemoveResponse):
    """Output for tool `reactions_remove`."""
    pass

class RemindersAddToolInput(BaseModel):
    """Input for tool `reminders_add`."""
    token: str = Field(..., description='Authentication token. Requires scope: `reminders:write`')
    body: RemindersAddRequest = Field(..., description='Request body for `reminders_add`.')
    model_config = ConfigDict(extra='forbid')

class RemindersAddToolOutput(RemindersAddResponse):
    """Output for tool `reminders_add`."""
    pass

class RemindersCompleteToolInput(BaseModel):
    """Input for tool `reminders_complete`."""
    token: str | None = Field(default=None, description='Authentication token. Requires scope: `reminders:write`')
    body: RemindersCompleteRequest | None = Field(default=None, description='Request body for `reminders_complete`.')
    model_config = ConfigDict(extra='forbid')

class RemindersCompleteToolOutput(RemindersCompleteResponse):
    """Output for tool `reminders_complete`."""
    pass

class RemindersDeleteToolInput(BaseModel):
    """Input for tool `reminders_delete`."""
    token: str | None = Field(default=None, description='Authentication token. Requires scope: `reminders:write`')
    body: RemindersDeleteRequest | None = Field(default=None, description='Request body for `reminders_delete`.')
    model_config = ConfigDict(extra='forbid')

class RemindersDeleteToolOutput(RemindersDeleteResponse):
    """Output for tool `reminders_delete`."""
    pass

class RemindersInfoToolInput(BaseModel):
    """Input for tool `reminders_info`."""
    token: str | None = Field(default=None, description='Authentication token. Requires scope: `reminders:read`')
    reminder: str | None = Field(default=None, description='The ID of the reminder')
    model_config = ConfigDict(extra='forbid')

class RemindersInfoToolOutput(RemindersInfoResponse):
    """Output for tool `reminders_info`."""
    pass

class RemindersListToolInput(BaseModel):
    """Input for tool `reminders_list`."""
    token: str | None = Field(default=None, description='Authentication token. Requires scope: `reminders:read`')
    model_config = ConfigDict(extra='forbid')

class RemindersListToolOutput(RemindersListResponse):
    """Output for tool `reminders_list`."""
    pass

class RtmConnectToolInput(BaseModel):
    """Input for tool `rtm_connect`."""
    token: str = Field(..., description='Authentication token. Requires scope: `rtm:stream`')
    batch_presence_aware: bool | None = Field(default=None, description='Batch presence deliveries via subscription. Enabling changes the shape of `presence_change` events. See [batch presence](/docs/presence-and-status#batching).')
    presence_sub: bool | None = Field(default=None, description='Only deliver presence events when requested by subscription. See [presence subscriptions](/docs/presence-and-status#subscriptions).')
    model_config = ConfigDict(extra='forbid')

class RtmConnectToolOutput(RtmConnectResponse):
    """Output for tool `rtm_connect`."""
    pass

class SearchMessagesToolInput(BaseModel):
    """Input for tool `search_messages`."""
    token: str = Field(..., description='Authentication token. Requires scope: `search:read`')
    count: int | None = Field(default=None, description='Pass the number of results you want per "page". Maximum of `100`.')
    highlight: bool | None = Field(default=None, description='Pass a value of `true` to enable query highlight markers (see below).')
    page: int | None = None
    query: str = Field(..., description='Search query.')
    sort: str | None = Field(default=None, description='Return matches sorted by either `score` or `timestamp`.')
    sort_dir: str | None = Field(default=None, description='Change sort direction to ascending (`asc`) or descending (`desc`).')
    model_config = ConfigDict(extra='forbid')

class SearchMessagesToolOutput(SearchMessagesResponse):
    """Output for tool `search_messages`."""
    pass

class StarsAddToolInput(BaseModel):
    """Input for tool `stars_add`."""
    token: str = Field(..., description='Authentication token. Requires scope: `stars:write`')
    body: StarsAddRequest | None = Field(default=None, description='Request body for `stars_add`.')
    model_config = ConfigDict(extra='forbid')

class StarsAddToolOutput(StarsAddResponse):
    """Output for tool `stars_add`."""
    pass

class StarsListToolInput(BaseModel):
    """Input for tool `stars_list`."""
    token: str | None = Field(default=None, description='Authentication token. Requires scope: `stars:read`')
    count: str | None = None
    page: str | None = None
    cursor: str | None = Field(default=None, description='Parameter for pagination. Set `cursor` equal to the `next_cursor` attribute returned by the previous request\'s `response_metadata`. This parameter is optional, but pagination is mandatory: the default value simply fetches the first "page" of the collection. See [pagination](/docs/pagination) for more details.')
    limit: int | None = Field(default=None, description="The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the list hasn't been reached.")
    model_config = ConfigDict(extra='forbid')

class StarsListToolOutput(StarsListResponse):
    """Output for tool `stars_list`."""
    pass

class StarsRemoveToolInput(BaseModel):
    """Input for tool `stars_remove`."""
    token: str = Field(..., description='Authentication token. Requires scope: `stars:write`')
    body: StarsRemoveRequest | None = Field(default=None, description='Request body for `stars_remove`.')
    model_config = ConfigDict(extra='forbid')

class StarsRemoveToolOutput(StarsRemoveResponse):
    """Output for tool `stars_remove`."""
    pass

class TeamAccessLogsToolInput(BaseModel):
    """Input for tool `team_access_logs`."""
    token: str = Field(..., description='Authentication token. Requires scope: `admin`')
    before: str | None = Field(default=None, description='End of time range of logs to include in results (inclusive).')
    count: str | None = None
    page: str | None = None
    model_config = ConfigDict(extra='forbid')

class TeamAccessLogsToolOutput(TeamAccessLogsResponse):
    """Output for tool `team_access_logs`."""
    pass

class TeamBillableInfoToolInput(BaseModel):
    """Input for tool `team_billable_info`."""
    token: str = Field(..., description='Authentication token. Requires scope: `admin`')
    user: str | None = Field(default=None, description='A user to retrieve the billable information for. Defaults to all users.')
    model_config = ConfigDict(extra='forbid')

class TeamBillableInfoToolOutput(TeamBillableInfoResponse):
    """Output for tool `team_billable_info`."""
    pass

class TeamInfoToolInput(BaseModel):
    """Input for tool `team_info`."""
    token: str = Field(..., description='Authentication token. Requires scope: `team:read`')
    team: str | None = Field(default=None, description='Team to get info on, if omitted, will return information about the current team. Will only return team that the authenticated token is allowed to see through external shared channels')
    model_config = ConfigDict(extra='forbid')

class TeamInfoToolOutput(TeamInfoResponse):
    """Output for tool `team_info`."""
    pass

class TeamIntegrationLogsToolInput(BaseModel):
    """Input for tool `team_integration_logs`."""
    token: str = Field(..., description='Authentication token. Requires scope: `admin`')
    app_id: str | None = Field(default=None, description='Filter logs to this Slack app. Defaults to all logs.')
    change_type: str | None = Field(default=None, description='Filter logs with this change type. Defaults to all logs.')
    count: str | None = None
    page: str | None = None
    service_id: str | None = Field(default=None, description='Filter logs to this service. Defaults to all logs.')
    user: str | None = Field(default=None, description='Filter logs generated by this user’s actions. Defaults to all logs.')
    model_config = ConfigDict(extra='forbid')

class TeamIntegrationLogsToolOutput(TeamIntegrationLogsResponse):
    """Output for tool `team_integration_logs`."""
    pass

class TeamProfileGetToolInput(BaseModel):
    """Input for tool `team_profile_get`."""
    token: str = Field(..., description='Authentication token. Requires scope: `users.profile:read`')
    visibility: str | None = Field(default=None, description='Filter by visibility.')
    model_config = ConfigDict(extra='forbid')

class TeamProfileGetToolOutput(TeamProfileGetResponse):
    """Output for tool `team_profile_get`."""
    pass

class UsergroupsCreateToolInput(BaseModel):
    """Input for tool `usergroups_create`."""
    token: str = Field(..., description='Authentication token. Requires scope: `usergroups:write`')
    body: UsergroupsCreateRequest | None = Field(default=None, description='Request body for `usergroups_create`.')
    model_config = ConfigDict(extra='forbid')

class UsergroupsCreateToolOutput(UsergroupsCreateResponse):
    """Output for tool `usergroups_create`."""
    pass

class UsergroupsDisableToolInput(BaseModel):
    """Input for tool `usergroups_disable`."""
    token: str = Field(..., description='Authentication token. Requires scope: `usergroups:write`')
    body: UsergroupsDisableRequest | None = Field(default=None, description='Request body for `usergroups_disable`.')
    model_config = ConfigDict(extra='forbid')

class UsergroupsDisableToolOutput(UsergroupsDisableResponse):
    """Output for tool `usergroups_disable`."""
    pass

class UsergroupsEnableToolInput(BaseModel):
    """Input for tool `usergroups_enable`."""
    token: str = Field(..., description='Authentication token. Requires scope: `usergroups:write`')
    body: UsergroupsEnableRequest | None = Field(default=None, description='Request body for `usergroups_enable`.')
    model_config = ConfigDict(extra='forbid')

class UsergroupsEnableToolOutput(UsergroupsEnableResponse):
    """Output for tool `usergroups_enable`."""
    pass

class UsergroupsListToolInput(BaseModel):
    """Input for tool `usergroups_list`."""
    include_users: bool | None = Field(default=None, description='Include the list of users for each User Group.')
    token: str = Field(..., description='Authentication token. Requires scope: `usergroups:read`')
    include_count: bool | None = Field(default=None, description='Include the number of users in each User Group.')
    include_disabled: bool | None = Field(default=None, description='Include disabled User Groups.')
    model_config = ConfigDict(extra='forbid')

class UsergroupsListToolOutput(UsergroupsListResponse):
    """Output for tool `usergroups_list`."""
    pass

class UsergroupsUpdateToolInput(BaseModel):
    """Input for tool `usergroups_update`."""
    token: str = Field(..., description='Authentication token. Requires scope: `usergroups:write`')
    body: UsergroupsUpdateRequest | None = Field(default=None, description='Request body for `usergroups_update`.')
    model_config = ConfigDict(extra='forbid')

class UsergroupsUpdateToolOutput(UsergroupsUpdateResponse):
    """Output for tool `usergroups_update`."""
    pass

class UsergroupsUsersListToolInput(BaseModel):
    """Input for tool `usergroups_users_list`."""
    token: str = Field(..., description='Authentication token. Requires scope: `usergroups:read`')
    include_disabled: bool | None = Field(default=None, description='Allow results that involve disabled User Groups.')
    usergroup: str = Field(..., description='The encoded ID of the User Group to update.')
    model_config = ConfigDict(extra='forbid')

class UsergroupsUsersListToolOutput(UsergroupsUsersListResponse):
    """Output for tool `usergroups_users_list`."""
    pass

class UsergroupsUsersUpdateToolInput(BaseModel):
    """Input for tool `usergroups_users_update`."""
    token: str = Field(..., description='Authentication token. Requires scope: `usergroups:write`')
    body: UsergroupsUsersUpdateRequest | None = Field(default=None, description='Request body for `usergroups_users_update`.')
    model_config = ConfigDict(extra='forbid')

class UsergroupsUsersUpdateToolOutput(UsergroupsUsersUpdateResponse):
    """Output for tool `usergroups_users_update`."""
    pass

class UsersConversationsToolInput(BaseModel):
    """Input for tool `users_conversations`."""
    token: str | None = Field(default=None, description='Authentication token. Requires scope: `conversations:read`')
    user: str | None = Field(default=None, description="Browse conversations by a specific user ID's membership. Non-public channels are restricted to those where the calling user shares membership.")
    types: str | None = Field(default=None, description='Mix and match channel types by providing a comma-separated list of any combination of `public_channel`, `private_channel`, `mpim`, `im`')
    exclude_archived: bool | None = Field(default=None, description='Set to `true` to exclude archived channels from the list')
    limit: int | None = Field(default=None, description="The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the list hasn't been reached. Must be an integer no larger than 1000.")
    cursor: str | None = Field(default=None, description='Paginate through collections of data by setting the `cursor` parameter to a `next_cursor` attribute returned by a previous request\'s `response_metadata`. Default value fetches the first "page" of the collection. See [pagination](/docs/pagination) for more detail.')
    model_config = ConfigDict(extra='forbid')

class UsersConversationsToolOutput(UsersConversationsResponse):
    """Output for tool `users_conversations`."""
    pass

class UsersDeletePhotoToolInput(BaseModel):
    """Input for tool `users_delete_photo`."""
    body: UsersDeletePhotoRequest = Field(..., description='Request body for `users_delete_photo`.')
    model_config = ConfigDict(extra='forbid')

class UsersDeletePhotoToolOutput(UsersDeletePhotoResponse):
    """Output for tool `users_delete_photo`."""
    pass

class UsersGetPresenceToolInput(BaseModel):
    """Input for tool `users_get_presence`."""
    token: str = Field(..., description='Authentication token. Requires scope: `users:read`')
    user: str | None = Field(default=None, description='User to get presence info on. Defaults to the authed user.')
    model_config = ConfigDict(extra='forbid')

class UsersGetPresenceToolOutput(UsersGetPresenceResponse):
    """Output for tool `users_get_presence`."""
    pass

class UsersIdentityToolInput(BaseModel):
    """Input for tool `users_identity`."""
    token: str | None = Field(default=None, description='Authentication token. Requires scope: `identity.basic`')
    model_config = ConfigDict(extra='forbid')

class UsersIdentityToolOutput(UsersIdentityResponse):
    """Output for tool `users_identity`."""
    pass

class UsersInfoToolInput(BaseModel):
    """Input for tool `users_info`."""
    token: str = Field(..., description='Authentication token. Requires scope: `users:read`')
    include_locale: bool | None = Field(default=None, description='Set this to `true` to receive the locale for this user. Defaults to `false`')
    user: str | None = Field(default=None, description='User to get info on')
    model_config = ConfigDict(extra='forbid')

class UsersInfoToolOutput(UsersInfoResponse):
    """Output for tool `users_info`."""
    pass

class UsersListToolInput(BaseModel):
    """Input for tool `users_list`."""
    token: str | None = Field(default=None, description='Authentication token. Requires scope: `users:read`')
    limit: int | None = Field(default=None, description="The maximum number of items to return. Fewer than the requested number of items may be returned, even if the end of the users list hasn't been reached. Providing no `limit` value will result in Slack attempting to deliver you the entire result set. If the collection is too large you may experience `limit_required` or HTTP 500 errors.")
    cursor: str | None = Field(default=None, description='Paginate through collections of data by setting the `cursor` parameter to a `next_cursor` attribute returned by a previous request\'s `response_metadata`. Default value fetches the first "page" of the collection. See [pagination](/docs/pagination) for more detail.')
    include_locale: bool | None = Field(default=None, description='Set this to `true` to receive the locale for users. Defaults to `false`')
    model_config = ConfigDict(extra='forbid')

class UsersListToolOutput(UsersListResponse):
    """Output for tool `users_list`."""
    pass

class UsersLookupByEmailToolInput(BaseModel):
    """Input for tool `users_lookup_by_email`."""
    token: str = Field(..., description='Authentication token. Requires scope: `users:read.email`')
    email: str = Field(..., description='An email address belonging to a user in the workspace')
    model_config = ConfigDict(extra='forbid')

class UsersLookupByEmailToolOutput(UsersLookupByEmailResponse):
    """Output for tool `users_lookup_by_email`."""
    pass

class UsersProfileGetToolInput(BaseModel):
    """Input for tool `users_profile_get`."""
    token: str = Field(..., description='Authentication token. Requires scope: `users.profile:read`')
    include_labels: bool | None = Field(default=None, description='Include labels for each ID in custom profile fields')
    user: str | None = Field(default=None, description='User to retrieve profile info for')
    model_config = ConfigDict(extra='forbid')

class UsersProfileGetToolOutput(UsersProfileGetResponse):
    """Output for tool `users_profile_get`."""
    pass

class UsersProfileSetToolInput(BaseModel):
    """Input for tool `users_profile_set`."""
    token: str = Field(..., description='Authentication token. Requires scope: `users.profile:write`')
    body: UsersProfileSetRequest | None = Field(default=None, description='Request body for `users_profile_set`.')
    model_config = ConfigDict(extra='forbid')

class UsersProfileSetToolOutput(UsersProfileSetResponse):
    """Output for tool `users_profile_set`."""
    pass

class UsersSetActiveToolInput(BaseModel):
    """Input for tool `users_set_active`."""
    token: str = Field(..., description='Authentication token. Requires scope: `users:write`')
    model_config = ConfigDict(extra='forbid')

class UsersSetActiveToolOutput(UsersSetActiveResponse):
    """Output for tool `users_set_active`."""
    pass

class UsersSetPhotoToolInput(BaseModel):
    """Input for tool `users_set_photo`."""
    body: UsersSetPhotoRequest = Field(..., description='Request body for `users_set_photo`.')
    model_config = ConfigDict(extra='forbid')

class UsersSetPhotoToolOutput(UsersSetPhotoResponse):
    """Output for tool `users_set_photo`."""
    pass

class UsersSetPresenceToolInput(BaseModel):
    """Input for tool `users_set_presence`."""
    token: str = Field(..., description='Authentication token. Requires scope: `users:write`')
    body: UsersSetPresenceRequest = Field(..., description='Request body for `users_set_presence`.')
    model_config = ConfigDict(extra='forbid')

class UsersSetPresenceToolOutput(UsersSetPresenceResponse):
    """Output for tool `users_set_presence`."""
    pass

class ViewsOpenToolInput(BaseModel):
    """Input for tool `views_open`."""
    token: str = Field(..., description='Authentication token. Requires scope: `none`')
    trigger_id: str = Field(..., description='Exchange a trigger to post to the user.')
    view: str = Field(..., description='A [view payload](/reference/surfaces/views). This must be a JSON-encoded string.')
    model_config = ConfigDict(extra='forbid')

class ViewsOpenToolOutput(ViewsOpenResponse):
    """Output for tool `views_open`."""
    pass

class ViewsPublishToolInput(BaseModel):
    """Input for tool `views_publish`."""
    token: str = Field(..., description='Authentication token. Requires scope: `none`')
    user_id: str = Field(..., description='`id` of the user you want publish a view to.')
    view: str = Field(..., description='A [view payload](/reference/surfaces/views). This must be a JSON-encoded string.')
    hash: str | None = Field(default=None, description='A string that represents view state to protect against possible race conditions.')
    model_config = ConfigDict(extra='forbid')

class ViewsPublishToolOutput(ViewsPublishResponse):
    """Output for tool `views_publish`."""
    pass

class ViewsPushToolInput(BaseModel):
    """Input for tool `views_push`."""
    token: str = Field(..., description='Authentication token. Requires scope: `none`')
    trigger_id: str = Field(..., description='Exchange a trigger to post to the user.')
    view: str = Field(..., description='A [view payload](/reference/surfaces/views). This must be a JSON-encoded string.')
    model_config = ConfigDict(extra='forbid')

class ViewsPushToolOutput(ViewsPushResponse):
    """Output for tool `views_push`."""
    pass

class ViewsUpdateToolInput(BaseModel):
    """Input for tool `views_update`."""
    token: str = Field(..., description='Authentication token. Requires scope: `none`')
    view_id: str | None = Field(default=None, description='A unique identifier of the view to be updated. Either `view_id` or `external_id` is required.')
    external_id: str | None = Field(default=None, description='A unique identifier of the view set by the developer. Must be unique for all views on a team. Max length of 255 characters. Either `view_id` or `external_id` is required.')
    view: str | None = Field(default=None, description='A [view object](/reference/surfaces/views). This must be a JSON-encoded string.')
    hash: str | None = Field(default=None, description='A string that represents view state to protect against possible race conditions.')
    model_config = ConfigDict(extra='forbid')

class ViewsUpdateToolOutput(ViewsUpdateResponse):
    """Output for tool `views_update`."""
    pass

class WorkflowsStepCompletedToolInput(BaseModel):
    """Input for tool `workflows_step_completed`."""
    token: str = Field(..., description='Authentication token. Requires scope: `workflow.steps:execute`')
    workflow_step_execute_id: str = Field(..., description='Context identifier that maps to the correct workflow step execution.')
    outputs: str | None = Field(default=None, description='Key-value object of outputs from your step. Keys of this object reflect the configured `key` properties of your [`outputs`](/reference/workflows/workflow_step#output) array from your `workflow_step` object.')
    model_config = ConfigDict(extra='forbid')

class WorkflowsStepCompletedToolOutput(WorkflowsStepCompletedResponse):
    """Output for tool `workflows_step_completed`."""
    pass

class WorkflowsStepFailedToolInput(BaseModel):
    """Input for tool `workflows_step_failed`."""
    token: str = Field(..., description='Authentication token. Requires scope: `workflow.steps:execute`')
    workflow_step_execute_id: str = Field(..., description='Context identifier that maps to the correct workflow step execution.')
    error: str = Field(..., description='A JSON-based object with a `message` property that should contain a human readable error message.')
    model_config = ConfigDict(extra='forbid')

class WorkflowsStepFailedToolOutput(WorkflowsStepFailedResponse):
    """Output for tool `workflows_step_failed`."""
    pass

class WorkflowsUpdateStepToolInput(BaseModel):
    """Input for tool `workflows_update_step`."""
    token: str = Field(..., description='Authentication token. Requires scope: `workflow.steps:execute`')
    workflow_step_edit_id: str = Field(..., description='A context identifier provided with `view_submission` payloads used to call back to `workflows.updateStep`.')
    inputs: str | None = Field(default=None, description='A JSON key-value map of inputs required from a user during configuration. This is the data your app expects to receive when the workflow step starts. **Please note**: the embedded variable format is set and replaced by the workflow system. You cannot create custom variables that will be replaced at runtime. [Read more about variables in workflow steps here](/workflows/steps#variables).')
    outputs: str | None = Field(default=None, description='An JSON array of output objects used during step execution. This is the data your app agrees to provide when your workflow step was executed.')
    step_name: str | None = Field(default=None, description='An optional field that can be used to override the step name that is shown in the Workflow Builder.')
    step_image_url: str | None = Field(default=None, description='An optional field that can be used to override app image that is shown in the Workflow Builder.')
    model_config = ConfigDict(extra='forbid')

class WorkflowsUpdateStepToolOutput(WorkflowsUpdateStepResponse):
    """Output for tool `workflows_update_step`."""
    pass

INPUT_MODELS = {
    'api_test': ApiTestToolInput,
    'apps_event_authorizations_list': AppsEventAuthorizationsListToolInput,
    'apps_permissions_info': AppsPermissionsInfoToolInput,
    'apps_permissions_request': AppsPermissionsRequestToolInput,
    'apps_permissions_resources_list': AppsPermissionsResourcesListToolInput,
    'apps_permissions_scopes_list': AppsPermissionsScopesListToolInput,
    'apps_permissions_users_list': AppsPermissionsUsersListToolInput,
    'apps_permissions_users_request': AppsPermissionsUsersRequestToolInput,
    'apps_uninstall': AppsUninstallToolInput,
    'auth_revoke': AuthRevokeToolInput,
    'auth_test': AuthTestToolInput,
    'bots_info': BotsInfoToolInput,
    'calls_add': CallsAddToolInput,
    'calls_end': CallsEndToolInput,
    'calls_info': CallsInfoToolInput,
    'calls_participants_add': CallsParticipantsAddToolInput,
    'calls_participants_remove': CallsParticipantsRemoveToolInput,
    'calls_update': CallsUpdateToolInput,
    'chat_delete': ChatDeleteToolInput,
    'chat_delete_scheduled_message': ChatDeleteScheduledMessageToolInput,
    'chat_get_permalink': ChatGetPermalinkToolInput,
    'chat_me_message': ChatMeMessageToolInput,
    'chat_post_ephemeral': ChatPostEphemeralToolInput,
    'chat_post_message': ChatPostMessageToolInput,
    'chat_schedule_message': ChatScheduleMessageToolInput,
    'chat_scheduled_messages_list': ChatScheduledMessagesListToolInput,
    'chat_unfurl': ChatUnfurlToolInput,
    'chat_update': ChatUpdateToolInput,
    'conversations_archive': ConversationsArchiveToolInput,
    'conversations_close': ConversationsCloseToolInput,
    'conversations_create': ConversationsCreateToolInput,
    'conversations_history': ConversationsHistoryToolInput,
    'conversations_info': ConversationsInfoToolInput,
    'conversations_invite': ConversationsInviteToolInput,
    'conversations_join': ConversationsJoinToolInput,
    'conversations_kick': ConversationsKickToolInput,
    'conversations_leave': ConversationsLeaveToolInput,
    'conversations_list': ConversationsListToolInput,
    'conversations_mark': ConversationsMarkToolInput,
    'conversations_members': ConversationsMembersToolInput,
    'conversations_open': ConversationsOpenToolInput,
    'conversations_rename': ConversationsRenameToolInput,
    'conversations_replies': ConversationsRepliesToolInput,
    'conversations_set_purpose': ConversationsSetPurposeToolInput,
    'conversations_set_topic': ConversationsSetTopicToolInput,
    'conversations_unarchive': ConversationsUnarchiveToolInput,
    'dialog_open': DialogOpenToolInput,
    'dnd_end_dnd': DndEndDndToolInput,
    'dnd_end_snooze': DndEndSnoozeToolInput,
    'dnd_info': DndInfoToolInput,
    'dnd_set_snooze': DndSetSnoozeToolInput,
    'dnd_team_info': DndTeamInfoToolInput,
    'emoji_list': EmojiListToolInput,
    'files_comments_delete': FilesCommentsDeleteToolInput,
    'files_delete': FilesDeleteToolInput,
    'files_info': FilesInfoToolInput,
    'files_list': FilesListToolInput,
    'files_remote_add': FilesRemoteAddToolInput,
    'files_remote_info': FilesRemoteInfoToolInput,
    'files_remote_list': FilesRemoteListToolInput,
    'files_remote_remove': FilesRemoteRemoveToolInput,
    'files_remote_share': FilesRemoteShareToolInput,
    'files_remote_update': FilesRemoteUpdateToolInput,
    'files_revoke_public_url': FilesRevokePublicUrlToolInput,
    'files_shared_public_url': FilesSharedPublicUrlToolInput,
    'files_upload': FilesUploadToolInput,
    'migration_exchange': MigrationExchangeToolInput,
    'oauth_access': OauthAccessToolInput,
    'oauth_token': OauthTokenToolInput,
    'oauth_v2_access': OauthV2AccessToolInput,
    'pins_add': PinsAddToolInput,
    'pins_list': PinsListToolInput,
    'pins_remove': PinsRemoveToolInput,
    'reactions_add': ReactionsAddToolInput,
    'reactions_get': ReactionsGetToolInput,
    'reactions_list': ReactionsListToolInput,
    'reactions_remove': ReactionsRemoveToolInput,
    'reminders_add': RemindersAddToolInput,
    'reminders_complete': RemindersCompleteToolInput,
    'reminders_delete': RemindersDeleteToolInput,
    'reminders_info': RemindersInfoToolInput,
    'reminders_list': RemindersListToolInput,
    'rtm_connect': RtmConnectToolInput,
    'search_messages': SearchMessagesToolInput,
    'stars_add': StarsAddToolInput,
    'stars_list': StarsListToolInput,
    'stars_remove': StarsRemoveToolInput,
    'team_access_logs': TeamAccessLogsToolInput,
    'team_billable_info': TeamBillableInfoToolInput,
    'team_info': TeamInfoToolInput,
    'team_integration_logs': TeamIntegrationLogsToolInput,
    'team_profile_get': TeamProfileGetToolInput,
    'usergroups_create': UsergroupsCreateToolInput,
    'usergroups_disable': UsergroupsDisableToolInput,
    'usergroups_enable': UsergroupsEnableToolInput,
    'usergroups_list': UsergroupsListToolInput,
    'usergroups_update': UsergroupsUpdateToolInput,
    'usergroups_users_list': UsergroupsUsersListToolInput,
    'usergroups_users_update': UsergroupsUsersUpdateToolInput,
    'users_conversations': UsersConversationsToolInput,
    'users_delete_photo': UsersDeletePhotoToolInput,
    'users_get_presence': UsersGetPresenceToolInput,
    'users_identity': UsersIdentityToolInput,
    'users_info': UsersInfoToolInput,
    'users_list': UsersListToolInput,
    'users_lookup_by_email': UsersLookupByEmailToolInput,
    'users_profile_get': UsersProfileGetToolInput,
    'users_profile_set': UsersProfileSetToolInput,
    'users_set_active': UsersSetActiveToolInput,
    'users_set_photo': UsersSetPhotoToolInput,
    'users_set_presence': UsersSetPresenceToolInput,
    'views_open': ViewsOpenToolInput,
    'views_publish': ViewsPublishToolInput,
    'views_push': ViewsPushToolInput,
    'views_update': ViewsUpdateToolInput,
    'workflows_step_completed': WorkflowsStepCompletedToolInput,
    'workflows_step_failed': WorkflowsStepFailedToolInput,
    'workflows_update_step': WorkflowsUpdateStepToolInput,
}

OUTPUT_MODELS = {
    'api_test': ApiTestToolOutput,
    'apps_event_authorizations_list': AppsEventAuthorizationsListToolOutput,
    'apps_permissions_info': AppsPermissionsInfoToolOutput,
    'apps_permissions_request': AppsPermissionsRequestToolOutput,
    'apps_permissions_resources_list': AppsPermissionsResourcesListToolOutput,
    'apps_permissions_scopes_list': AppsPermissionsScopesListToolOutput,
    'apps_permissions_users_list': AppsPermissionsUsersListToolOutput,
    'apps_permissions_users_request': AppsPermissionsUsersRequestToolOutput,
    'apps_uninstall': AppsUninstallToolOutput,
    'auth_revoke': AuthRevokeToolOutput,
    'auth_test': AuthTestToolOutput,
    'bots_info': BotsInfoToolOutput,
    'calls_add': CallsAddToolOutput,
    'calls_end': CallsEndToolOutput,
    'calls_info': CallsInfoToolOutput,
    'calls_participants_add': CallsParticipantsAddToolOutput,
    'calls_participants_remove': CallsParticipantsRemoveToolOutput,
    'calls_update': CallsUpdateToolOutput,
    'chat_delete': ChatDeleteToolOutput,
    'chat_delete_scheduled_message': ChatDeleteScheduledMessageToolOutput,
    'chat_get_permalink': ChatGetPermalinkToolOutput,
    'chat_me_message': ChatMeMessageToolOutput,
    'chat_post_ephemeral': ChatPostEphemeralToolOutput,
    'chat_post_message': ChatPostMessageToolOutput,
    'chat_schedule_message': ChatScheduleMessageToolOutput,
    'chat_scheduled_messages_list': ChatScheduledMessagesListToolOutput,
    'chat_unfurl': ChatUnfurlToolOutput,
    'chat_update': ChatUpdateToolOutput,
    'conversations_archive': ConversationsArchiveToolOutput,
    'conversations_close': ConversationsCloseToolOutput,
    'conversations_create': ConversationsCreateToolOutput,
    'conversations_history': ConversationsHistoryToolOutput,
    'conversations_info': ConversationsInfoToolOutput,
    'conversations_invite': ConversationsInviteToolOutput,
    'conversations_join': ConversationsJoinToolOutput,
    'conversations_kick': ConversationsKickToolOutput,
    'conversations_leave': ConversationsLeaveToolOutput,
    'conversations_list': ConversationsListToolOutput,
    'conversations_mark': ConversationsMarkToolOutput,
    'conversations_members': ConversationsMembersToolOutput,
    'conversations_open': ConversationsOpenToolOutput,
    'conversations_rename': ConversationsRenameToolOutput,
    'conversations_replies': ConversationsRepliesToolOutput,
    'conversations_set_purpose': ConversationsSetPurposeToolOutput,
    'conversations_set_topic': ConversationsSetTopicToolOutput,
    'conversations_unarchive': ConversationsUnarchiveToolOutput,
    'dialog_open': DialogOpenToolOutput,
    'dnd_end_dnd': DndEndDndToolOutput,
    'dnd_end_snooze': DndEndSnoozeToolOutput,
    'dnd_info': DndInfoToolOutput,
    'dnd_set_snooze': DndSetSnoozeToolOutput,
    'dnd_team_info': DndTeamInfoToolOutput,
    'emoji_list': EmojiListToolOutput,
    'files_comments_delete': FilesCommentsDeleteToolOutput,
    'files_delete': FilesDeleteToolOutput,
    'files_info': FilesInfoToolOutput,
    'files_list': FilesListToolOutput,
    'files_remote_add': FilesRemoteAddToolOutput,
    'files_remote_info': FilesRemoteInfoToolOutput,
    'files_remote_list': FilesRemoteListToolOutput,
    'files_remote_remove': FilesRemoteRemoveToolOutput,
    'files_remote_share': FilesRemoteShareToolOutput,
    'files_remote_update': FilesRemoteUpdateToolOutput,
    'files_revoke_public_url': FilesRevokePublicUrlToolOutput,
    'files_shared_public_url': FilesSharedPublicUrlToolOutput,
    'files_upload': FilesUploadToolOutput,
    'migration_exchange': MigrationExchangeToolOutput,
    'oauth_access': OauthAccessToolOutput,
    'oauth_token': OauthTokenToolOutput,
    'oauth_v2_access': OauthV2AccessToolOutput,
    'pins_add': PinsAddToolOutput,
    'pins_list': PinsListToolOutput,
    'pins_remove': PinsRemoveToolOutput,
    'reactions_add': ReactionsAddToolOutput,
    'reactions_get': ReactionsGetToolOutput,
    'reactions_list': ReactionsListToolOutput,
    'reactions_remove': ReactionsRemoveToolOutput,
    'reminders_add': RemindersAddToolOutput,
    'reminders_complete': RemindersCompleteToolOutput,
    'reminders_delete': RemindersDeleteToolOutput,
    'reminders_info': RemindersInfoToolOutput,
    'reminders_list': RemindersListToolOutput,
    'rtm_connect': RtmConnectToolOutput,
    'search_messages': SearchMessagesToolOutput,
    'stars_add': StarsAddToolOutput,
    'stars_list': StarsListToolOutput,
    'stars_remove': StarsRemoveToolOutput,
    'team_access_logs': TeamAccessLogsToolOutput,
    'team_billable_info': TeamBillableInfoToolOutput,
    'team_info': TeamInfoToolOutput,
    'team_integration_logs': TeamIntegrationLogsToolOutput,
    'team_profile_get': TeamProfileGetToolOutput,
    'usergroups_create': UsergroupsCreateToolOutput,
    'usergroups_disable': UsergroupsDisableToolOutput,
    'usergroups_enable': UsergroupsEnableToolOutput,
    'usergroups_list': UsergroupsListToolOutput,
    'usergroups_update': UsergroupsUpdateToolOutput,
    'usergroups_users_list': UsergroupsUsersListToolOutput,
    'usergroups_users_update': UsergroupsUsersUpdateToolOutput,
    'users_conversations': UsersConversationsToolOutput,
    'users_delete_photo': UsersDeletePhotoToolOutput,
    'users_get_presence': UsersGetPresenceToolOutput,
    'users_identity': UsersIdentityToolOutput,
    'users_info': UsersInfoToolOutput,
    'users_list': UsersListToolOutput,
    'users_lookup_by_email': UsersLookupByEmailToolOutput,
    'users_profile_get': UsersProfileGetToolOutput,
    'users_profile_set': UsersProfileSetToolOutput,
    'users_set_active': UsersSetActiveToolOutput,
    'users_set_photo': UsersSetPhotoToolOutput,
    'users_set_presence': UsersSetPresenceToolOutput,
    'views_open': ViewsOpenToolOutput,
    'views_publish': ViewsPublishToolOutput,
    'views_push': ViewsPushToolOutput,
    'views_update': ViewsUpdateToolOutput,
    'workflows_step_completed': WorkflowsStepCompletedToolOutput,
    'workflows_step_failed': WorkflowsStepFailedToolOutput,
    'workflows_update_step': WorkflowsUpdateStepToolOutput,
}
