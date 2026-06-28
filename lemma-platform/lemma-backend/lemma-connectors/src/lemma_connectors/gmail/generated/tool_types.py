from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, RootModel

from lemma_connectors.core.results import BinaryContentResult

from lemma_connectors.gmail.generated.pydantic_models import AutoForwarding, BatchDeleteMessagesRequest, BatchModifyMessagesRequest, CseIdentity, CseKeyPair, Delegate, DisableCseKeyPairRequest, Draft, EnableCseKeyPairRequest, Filter, ForwardingAddress, ImapSettings, Label, LanguageSettings, ListCseIdentitiesResponse, ListCseKeyPairsResponse, ListDelegatesResponse, ListDraftsResponse, ListFiltersResponse, ListForwardingAddressesResponse, ListHistoryResponse, ListLabelsResponse, ListMessagesResponse, ListSendAsResponse, ListSmimeInfoResponse, ListThreadsResponse, Message, MessagePartBody, ModifyMessageRequest, ModifyThreadRequest, ObliterateCseKeyPairRequest, PopSettings, Profile, SendAs, SmimeInfo, Thread, VacationSettings, WatchRequest, WatchResponse

class GmailUsersDraftsCreateToolInput(BaseModel):
    """Input for tool `gmail_users_drafts_create`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description="The user's email address. The special value `me` can be used to indicate the authenticated user.")
    body: Draft | None = Field(default=None, description='Request body for `gmail_users_drafts_create`.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersDraftsCreateToolOutput(Draft):
    """Output for tool `gmail_users_drafts_create`."""
    pass

class GmailUsersDraftsDeleteToolInput(BaseModel):
    """Input for tool `gmail_users_drafts_delete`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description="The user's email address. The special value `me` can be used to indicate the authenticated user.")
    id: str = Field(..., description='The ID of the draft to delete.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersDraftsDeleteToolOutput(RootModel[dict[str, object]]):
    """Output for tool `gmail_users_drafts_delete`."""
    pass

class GmailUsersDraftsGetToolInput(BaseModel):
    """Input for tool `gmail_users_drafts_get`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description="The user's email address. The special value `me` can be used to indicate the authenticated user.")
    id: str = Field(..., description='The ID of the draft to retrieve.')
    format: Literal['minimal', 'full', 'raw', 'metadata'] | None = Field(default=None, description='The format to return the draft in.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersDraftsGetToolOutput(Draft):
    """Output for tool `gmail_users_drafts_get`."""
    pass

class GmailUsersDraftsListToolInput(BaseModel):
    """Input for tool `gmail_users_drafts_list`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description="The user's email address. The special value `me` can be used to indicate the authenticated user.")
    include_spam_trash: bool | None = Field(default=None, description='Include drafts from `SPAM` and `TRASH` in the results.')
    max_results: int | None = Field(default=None, description='Maximum number of drafts to return. This field defaults to 100. The maximum allowed value for this field is 500.')
    page_token: str | None = Field(default=None, description='Page token to retrieve a specific page of results in the list.')
    q: str | None = Field(default=None, description='Only return draft messages matching the specified query. Supports the same query format as the Gmail search box. For example, `"from:someuser@example.com rfc822msgid: is:unread"`.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersDraftsListToolOutput(ListDraftsResponse):
    """Output for tool `gmail_users_drafts_list`."""
    pass

class GmailUsersDraftsSendToolInput(BaseModel):
    """Input for tool `gmail_users_drafts_send`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description="The user's email address. The special value `me` can be used to indicate the authenticated user.")
    body: Draft | None = Field(default=None, description='Request body for `gmail_users_drafts_send`.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersDraftsSendToolOutput(Message):
    """Output for tool `gmail_users_drafts_send`."""
    pass

class GmailUsersDraftsUpdateToolInput(BaseModel):
    """Input for tool `gmail_users_drafts_update`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description="The user's email address. The special value `me` can be used to indicate the authenticated user.")
    id: str = Field(..., description='The ID of the draft to update.')
    body: Draft | None = Field(default=None, description='Request body for `gmail_users_drafts_update`.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersDraftsUpdateToolOutput(Draft):
    """Output for tool `gmail_users_drafts_update`."""
    pass

class GmailUsersGetProfileToolInput(BaseModel):
    """Input for tool `gmail_users_get_profile`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description="The user's email address. The special value `me` can be used to indicate the authenticated user.")
    model_config = ConfigDict(extra='forbid')

class GmailUsersGetProfileToolOutput(Profile):
    """Output for tool `gmail_users_get_profile`."""
    pass

class GmailUsersHistoryListToolInput(BaseModel):
    """Input for tool `gmail_users_history_list`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description="The user's email address. The special value `me` can be used to indicate the authenticated user.")
    history_types: list[Literal['messageAdded', 'messageDeleted', 'labelAdded', 'labelRemoved']] | None = Field(default=None, description='History types to be returned by the function')
    label_id: str | None = Field(default=None, description='Only return messages with a label matching the ID.')
    max_results: int | None = Field(default=None, description='Maximum number of history records to return. This field defaults to 100. The maximum allowed value for this field is 500.')
    page_token: str | None = Field(default=None, description='Page token to retrieve a specific page of results in the list.')
    start_history_id: str | None = Field(default=None, description='Required. Returns history records after the specified `startHistoryId`. The supplied `startHistoryId` should be obtained from the `historyId` of a message, thread, or previous `list` response. History IDs increase chronologically but are not contiguous with random gaps in between valid IDs. Supplying an invalid or out of date `startHistoryId` typically returns an `HTTP 404` error code. A `historyId` is typically valid for at least a week, but in some rare circumstances may be valid for only a few hours. If you receive an `HTTP 404` error response, your application should perform a full sync. If you receive no `nextPageToken` in the response, there are no updates to retrieve and you can store the returned `historyId` for a future request.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersHistoryListToolOutput(ListHistoryResponse):
    """Output for tool `gmail_users_history_list`."""
    pass

class GmailUsersLabelsCreateToolInput(BaseModel):
    """Input for tool `gmail_users_labels_create`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description="The user's email address. The special value `me` can be used to indicate the authenticated user.")
    body: Label | None = Field(default=None, description='Request body for `gmail_users_labels_create`.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersLabelsCreateToolOutput(Label):
    """Output for tool `gmail_users_labels_create`."""
    pass

class GmailUsersLabelsDeleteToolInput(BaseModel):
    """Input for tool `gmail_users_labels_delete`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description="The user's email address. The special value `me` can be used to indicate the authenticated user.")
    id: str = Field(..., description='The ID of the label to delete.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersLabelsDeleteToolOutput(RootModel[dict[str, object]]):
    """Output for tool `gmail_users_labels_delete`."""
    pass

class GmailUsersLabelsGetToolInput(BaseModel):
    """Input for tool `gmail_users_labels_get`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description="The user's email address. The special value `me` can be used to indicate the authenticated user.")
    id: str = Field(..., description='The ID of the label to retrieve.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersLabelsGetToolOutput(Label):
    """Output for tool `gmail_users_labels_get`."""
    pass

class GmailUsersLabelsListToolInput(BaseModel):
    """Input for tool `gmail_users_labels_list`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description="The user's email address. The special value `me` can be used to indicate the authenticated user.")
    model_config = ConfigDict(extra='forbid')

class GmailUsersLabelsListToolOutput(ListLabelsResponse):
    """Output for tool `gmail_users_labels_list`."""
    pass

class GmailUsersLabelsPatchToolInput(BaseModel):
    """Input for tool `gmail_users_labels_patch`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description="The user's email address. The special value `me` can be used to indicate the authenticated user.")
    id: str = Field(..., description='The ID of the label to update.')
    body: Label | None = Field(default=None, description='Request body for `gmail_users_labels_patch`.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersLabelsPatchToolOutput(Label):
    """Output for tool `gmail_users_labels_patch`."""
    pass

class GmailUsersLabelsUpdateToolInput(BaseModel):
    """Input for tool `gmail_users_labels_update`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description="The user's email address. The special value `me` can be used to indicate the authenticated user.")
    id: str = Field(..., description='The ID of the label to update.')
    body: Label | None = Field(default=None, description='Request body for `gmail_users_labels_update`.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersLabelsUpdateToolOutput(Label):
    """Output for tool `gmail_users_labels_update`."""
    pass

class GmailUsersMessagesAttachmentsGetToolInput(BaseModel):
    """Input for tool `gmail_users_messages_attachments_get`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description="The user's email address. The special value `me` can be used to indicate the authenticated user.")
    message_id: str = Field(..., description='The ID of the message containing the attachment.')
    id: str = Field(..., description='The ID of the attachment.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersMessagesAttachmentsGetToolOutput(MessagePartBody):
    """Output for tool `gmail_users_messages_attachments_get`."""
    pass

class GmailUsersMessagesBatchDeleteToolInput(BaseModel):
    """Input for tool `gmail_users_messages_batch_delete`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description="The user's email address. The special value `me` can be used to indicate the authenticated user.")
    body: BatchDeleteMessagesRequest | None = Field(default=None, description='Request body for `gmail_users_messages_batch_delete`.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersMessagesBatchDeleteToolOutput(RootModel[dict[str, object]]):
    """Output for tool `gmail_users_messages_batch_delete`."""
    pass

class GmailUsersMessagesBatchModifyToolInput(BaseModel):
    """Input for tool `gmail_users_messages_batch_modify`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description="The user's email address. The special value `me` can be used to indicate the authenticated user.")
    body: BatchModifyMessagesRequest | None = Field(default=None, description='Request body for `gmail_users_messages_batch_modify`.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersMessagesBatchModifyToolOutput(RootModel[dict[str, object]]):
    """Output for tool `gmail_users_messages_batch_modify`."""
    pass

class GmailUsersMessagesDeleteToolInput(BaseModel):
    """Input for tool `gmail_users_messages_delete`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description="The user's email address. The special value `me` can be used to indicate the authenticated user.")
    id: str = Field(..., description='The ID of the message to delete.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersMessagesDeleteToolOutput(RootModel[dict[str, object]]):
    """Output for tool `gmail_users_messages_delete`."""
    pass

class GmailUsersMessagesGetToolInput(BaseModel):
    """Input for tool `gmail_users_messages_get`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description="The user's email address. The special value `me` can be used to indicate the authenticated user.")
    id: str = Field(..., description='The ID of the message to retrieve. This ID is usually retrieved using `messages.list`. The ID is also contained in the result when a message is inserted (`messages.insert`) or imported (`messages.import`).')
    format: Literal['minimal', 'full', 'raw', 'metadata'] | None = Field(default=None, description='The format to return the message in.')
    metadata_headers: list[str] | None = Field(default=None, description='When given and format is `METADATA`, only include headers specified.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersMessagesGetToolOutput(Message):
    """Output for tool `gmail_users_messages_get`."""
    pass

class GmailUsersMessagesImportToolInput(BaseModel):
    """Input for tool `gmail_users_messages_import`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description="The user's email address. The special value `me` can be used to indicate the authenticated user.")
    deleted: bool | None = Field(default=None, description='Mark the email as permanently deleted (not TRASH) and only visible in Google Vault to a Vault administrator. Only used for Google Workspace accounts.')
    internal_date_source: Literal['receivedTime', 'dateHeader'] | None = Field(default=None, description="Source for Gmail's internal date of the message.")
    never_mark_spam: bool | None = Field(default=None, description='Ignore the Gmail spam classifier decision and never mark this email as SPAM in the mailbox.')
    process_for_calendar: bool | None = Field(default=None, description='Process calendar invites in the email and add any extracted meetings to the Google Calendar for this user.')
    body: Message | None = Field(default=None, description='Request body for `gmail_users_messages_import`.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersMessagesImportToolOutput(Message):
    """Output for tool `gmail_users_messages_import`."""
    pass

class GmailUsersMessagesInsertToolInput(BaseModel):
    """Input for tool `gmail_users_messages_insert`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description="The user's email address. The special value `me` can be used to indicate the authenticated user.")
    deleted: bool | None = Field(default=None, description='Mark the email as permanently deleted (not TRASH) and only visible in Google Vault to a Vault administrator. Only used for Google Workspace accounts.')
    internal_date_source: Literal['receivedTime', 'dateHeader'] | None = Field(default=None, description="Source for Gmail's internal date of the message.")
    body: Message | None = Field(default=None, description='Request body for `gmail_users_messages_insert`.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersMessagesInsertToolOutput(Message):
    """Output for tool `gmail_users_messages_insert`."""
    pass

class GmailUsersMessagesListToolInput(BaseModel):
    """Input for tool `gmail_users_messages_list`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description="The user's email address. The special value `me` can be used to indicate the authenticated user.")
    include_spam_trash: bool | None = Field(default=None, description='Include messages from `SPAM` and `TRASH` in the results.')
    label_ids: list[str] | None = Field(default=None, description="Only return messages with labels that match all of the specified label IDs. Messages in a thread might have labels that other messages in the same thread don't have. To learn more, see [Manage labels on messages and threads](https://developers.google.com/gmail/api/guides/labels#manage_labels_on_messages_threads).")
    max_results: int | None = Field(default=None, description='Maximum number of messages to return. This field defaults to 100. The maximum allowed value for this field is 500.')
    page_token: str | None = Field(default=None, description='Page token to retrieve a specific page of results in the list.')
    q: str | None = Field(default=None, description='Only return messages matching the specified query. Supports the same query format as the Gmail search box. For example, `"from:someuser@example.com rfc822msgid: is:unread"`. Parameter cannot be used when accessing the api using the gmail.metadata scope.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersMessagesListToolOutput(ListMessagesResponse):
    """Output for tool `gmail_users_messages_list`."""
    pass

class GmailUsersMessagesModifyToolInput(BaseModel):
    """Input for tool `gmail_users_messages_modify`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description="The user's email address. The special value `me` can be used to indicate the authenticated user.")
    id: str = Field(..., description='The ID of the message to modify.')
    body: ModifyMessageRequest | None = Field(default=None, description='Request body for `gmail_users_messages_modify`.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersMessagesModifyToolOutput(Message):
    """Output for tool `gmail_users_messages_modify`."""
    pass

class GmailUsersMessagesSendToolInput(BaseModel):
    """Input for tool `gmail_users_messages_send`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description="The user's email address. The special value `me` can be used to indicate the authenticated user.")
    body: Message | None = Field(default=None, description='Request body for `gmail_users_messages_send`.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersMessagesSendToolOutput(Message):
    """Output for tool `gmail_users_messages_send`."""
    pass

class GmailUsersMessagesTrashToolInput(BaseModel):
    """Input for tool `gmail_users_messages_trash`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description="The user's email address. The special value `me` can be used to indicate the authenticated user.")
    id: str = Field(..., description='The ID of the message to Trash.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersMessagesTrashToolOutput(Message):
    """Output for tool `gmail_users_messages_trash`."""
    pass

class GmailUsersMessagesUntrashToolInput(BaseModel):
    """Input for tool `gmail_users_messages_untrash`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description="The user's email address. The special value `me` can be used to indicate the authenticated user.")
    id: str = Field(..., description='The ID of the message to remove from Trash.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersMessagesUntrashToolOutput(Message):
    """Output for tool `gmail_users_messages_untrash`."""
    pass

class GmailUsersSettingsCseIdentitiesCreateToolInput(BaseModel):
    """Input for tool `gmail_users_settings_cse_identities_create`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description="The requester's primary email address. To indicate the authenticated user, you can use the special value `me`.")
    body: CseIdentity | None = Field(default=None, description='Request body for `gmail_users_settings_cse_identities_create`.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersSettingsCseIdentitiesCreateToolOutput(CseIdentity):
    """Output for tool `gmail_users_settings_cse_identities_create`."""
    pass

class GmailUsersSettingsCseIdentitiesDeleteToolInput(BaseModel):
    """Input for tool `gmail_users_settings_cse_identities_delete`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description="The requester's primary email address. To indicate the authenticated user, you can use the special value `me`.")
    cse_email_address: str = Field(..., description="The primary email address associated with the client-side encryption identity configuration that's removed.")
    model_config = ConfigDict(extra='forbid')

class GmailUsersSettingsCseIdentitiesDeleteToolOutput(RootModel[dict[str, object]]):
    """Output for tool `gmail_users_settings_cse_identities_delete`."""
    pass

class GmailUsersSettingsCseIdentitiesGetToolInput(BaseModel):
    """Input for tool `gmail_users_settings_cse_identities_get`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description="The requester's primary email address. To indicate the authenticated user, you can use the special value `me`.")
    cse_email_address: str = Field(..., description="The primary email address associated with the client-side encryption identity configuration that's retrieved.")
    model_config = ConfigDict(extra='forbid')

class GmailUsersSettingsCseIdentitiesGetToolOutput(CseIdentity):
    """Output for tool `gmail_users_settings_cse_identities_get`."""
    pass

class GmailUsersSettingsCseIdentitiesListToolInput(BaseModel):
    """Input for tool `gmail_users_settings_cse_identities_list`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description="The requester's primary email address. To indicate the authenticated user, you can use the special value `me`.")
    page_size: int | None = Field(default=None, description='The number of identities to return. If not provided, the page size will default to 20 entries.')
    page_token: str | None = Field(default=None, description='Pagination token indicating which page of identities to return. If the token is not supplied, then the API will return the first page of results.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersSettingsCseIdentitiesListToolOutput(ListCseIdentitiesResponse):
    """Output for tool `gmail_users_settings_cse_identities_list`."""
    pass

class GmailUsersSettingsCseIdentitiesPatchToolInput(BaseModel):
    """Input for tool `gmail_users_settings_cse_identities_patch`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description="The requester's primary email address. To indicate the authenticated user, you can use the special value `me`.")
    email_address: str = Field(..., description='The email address of the client-side encryption identity to update.')
    body: CseIdentity | None = Field(default=None, description='Request body for `gmail_users_settings_cse_identities_patch`.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersSettingsCseIdentitiesPatchToolOutput(CseIdentity):
    """Output for tool `gmail_users_settings_cse_identities_patch`."""
    pass

class GmailUsersSettingsCseKeypairsCreateToolInput(BaseModel):
    """Input for tool `gmail_users_settings_cse_keypairs_create`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description="The requester's primary email address. To indicate the authenticated user, you can use the special value `me`.")
    body: CseKeyPair | None = Field(default=None, description='Request body for `gmail_users_settings_cse_keypairs_create`.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersSettingsCseKeypairsCreateToolOutput(CseKeyPair):
    """Output for tool `gmail_users_settings_cse_keypairs_create`."""
    pass

class GmailUsersSettingsCseKeypairsDisableToolInput(BaseModel):
    """Input for tool `gmail_users_settings_cse_keypairs_disable`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description="The requester's primary email address. To indicate the authenticated user, you can use the special value `me`.")
    key_pair_id: str = Field(..., description='The identifier of the key pair to turn off.')
    body: DisableCseKeyPairRequest | None = Field(default=None, description='Request body for `gmail_users_settings_cse_keypairs_disable`.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersSettingsCseKeypairsDisableToolOutput(CseKeyPair):
    """Output for tool `gmail_users_settings_cse_keypairs_disable`."""
    pass

class GmailUsersSettingsCseKeypairsEnableToolInput(BaseModel):
    """Input for tool `gmail_users_settings_cse_keypairs_enable`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description="The requester's primary email address. To indicate the authenticated user, you can use the special value `me`.")
    key_pair_id: str = Field(..., description='The identifier of the key pair to turn on.')
    body: EnableCseKeyPairRequest | None = Field(default=None, description='Request body for `gmail_users_settings_cse_keypairs_enable`.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersSettingsCseKeypairsEnableToolOutput(CseKeyPair):
    """Output for tool `gmail_users_settings_cse_keypairs_enable`."""
    pass

class GmailUsersSettingsCseKeypairsGetToolInput(BaseModel):
    """Input for tool `gmail_users_settings_cse_keypairs_get`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description="The requester's primary email address. To indicate the authenticated user, you can use the special value `me`.")
    key_pair_id: str = Field(..., description='The identifier of the key pair to retrieve.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersSettingsCseKeypairsGetToolOutput(CseKeyPair):
    """Output for tool `gmail_users_settings_cse_keypairs_get`."""
    pass

class GmailUsersSettingsCseKeypairsListToolInput(BaseModel):
    """Input for tool `gmail_users_settings_cse_keypairs_list`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description="The requester's primary email address. To indicate the authenticated user, you can use the special value `me`.")
    page_size: int | None = Field(default=None, description='The number of key pairs to return. If not provided, the page size will default to 20 entries.')
    page_token: str | None = Field(default=None, description='Pagination token indicating which page of key pairs to return. If the token is not supplied, then the API will return the first page of results.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersSettingsCseKeypairsListToolOutput(ListCseKeyPairsResponse):
    """Output for tool `gmail_users_settings_cse_keypairs_list`."""
    pass

class GmailUsersSettingsCseKeypairsObliterateToolInput(BaseModel):
    """Input for tool `gmail_users_settings_cse_keypairs_obliterate`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description="The requester's primary email address. To indicate the authenticated user, you can use the special value `me`.")
    key_pair_id: str = Field(..., description='The identifier of the key pair to obliterate.')
    body: ObliterateCseKeyPairRequest | None = Field(default=None, description='Request body for `gmail_users_settings_cse_keypairs_obliterate`.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersSettingsCseKeypairsObliterateToolOutput(RootModel[dict[str, object]]):
    """Output for tool `gmail_users_settings_cse_keypairs_obliterate`."""
    pass

class GmailUsersSettingsDelegatesCreateToolInput(BaseModel):
    """Input for tool `gmail_users_settings_delegates_create`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description='User\'s email address. The special value "me" can be used to indicate the authenticated user.')
    body: Delegate | None = Field(default=None, description='Request body for `gmail_users_settings_delegates_create`.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersSettingsDelegatesCreateToolOutput(Delegate):
    """Output for tool `gmail_users_settings_delegates_create`."""
    pass

class GmailUsersSettingsDelegatesDeleteToolInput(BaseModel):
    """Input for tool `gmail_users_settings_delegates_delete`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description='User\'s email address. The special value "me" can be used to indicate the authenticated user.')
    delegate_email: str = Field(..., description='The email address of the user to be removed as a delegate.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersSettingsDelegatesDeleteToolOutput(RootModel[dict[str, object]]):
    """Output for tool `gmail_users_settings_delegates_delete`."""
    pass

class GmailUsersSettingsDelegatesGetToolInput(BaseModel):
    """Input for tool `gmail_users_settings_delegates_get`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description='User\'s email address. The special value "me" can be used to indicate the authenticated user.')
    delegate_email: str = Field(..., description='The email address of the user whose delegate relationship is to be retrieved.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersSettingsDelegatesGetToolOutput(Delegate):
    """Output for tool `gmail_users_settings_delegates_get`."""
    pass

class GmailUsersSettingsDelegatesListToolInput(BaseModel):
    """Input for tool `gmail_users_settings_delegates_list`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description='User\'s email address. The special value "me" can be used to indicate the authenticated user.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersSettingsDelegatesListToolOutput(ListDelegatesResponse):
    """Output for tool `gmail_users_settings_delegates_list`."""
    pass

class GmailUsersSettingsFiltersCreateToolInput(BaseModel):
    """Input for tool `gmail_users_settings_filters_create`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description='User\'s email address. The special value "me" can be used to indicate the authenticated user.')
    body: Filter | None = Field(default=None, description='Request body for `gmail_users_settings_filters_create`.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersSettingsFiltersCreateToolOutput(Filter):
    """Output for tool `gmail_users_settings_filters_create`."""
    pass

class GmailUsersSettingsFiltersDeleteToolInput(BaseModel):
    """Input for tool `gmail_users_settings_filters_delete`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description='User\'s email address. The special value "me" can be used to indicate the authenticated user.')
    id: str = Field(..., description='The ID of the filter to be deleted.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersSettingsFiltersDeleteToolOutput(RootModel[dict[str, object]]):
    """Output for tool `gmail_users_settings_filters_delete`."""
    pass

class GmailUsersSettingsFiltersGetToolInput(BaseModel):
    """Input for tool `gmail_users_settings_filters_get`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description='User\'s email address. The special value "me" can be used to indicate the authenticated user.')
    id: str = Field(..., description='The ID of the filter to be fetched.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersSettingsFiltersGetToolOutput(Filter):
    """Output for tool `gmail_users_settings_filters_get`."""
    pass

class GmailUsersSettingsFiltersListToolInput(BaseModel):
    """Input for tool `gmail_users_settings_filters_list`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description='User\'s email address. The special value "me" can be used to indicate the authenticated user.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersSettingsFiltersListToolOutput(ListFiltersResponse):
    """Output for tool `gmail_users_settings_filters_list`."""
    pass

class GmailUsersSettingsForwardingAddressesCreateToolInput(BaseModel):
    """Input for tool `gmail_users_settings_forwarding_addresses_create`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description='User\'s email address. The special value "me" can be used to indicate the authenticated user.')
    body: ForwardingAddress | None = Field(default=None, description='Request body for `gmail_users_settings_forwarding_addresses_create`.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersSettingsForwardingAddressesCreateToolOutput(ForwardingAddress):
    """Output for tool `gmail_users_settings_forwarding_addresses_create`."""
    pass

class GmailUsersSettingsForwardingAddressesDeleteToolInput(BaseModel):
    """Input for tool `gmail_users_settings_forwarding_addresses_delete`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description='User\'s email address. The special value "me" can be used to indicate the authenticated user.')
    forwarding_email: str = Field(..., description='The forwarding address to be deleted.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersSettingsForwardingAddressesDeleteToolOutput(RootModel[dict[str, object]]):
    """Output for tool `gmail_users_settings_forwarding_addresses_delete`."""
    pass

class GmailUsersSettingsForwardingAddressesGetToolInput(BaseModel):
    """Input for tool `gmail_users_settings_forwarding_addresses_get`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description='User\'s email address. The special value "me" can be used to indicate the authenticated user.')
    forwarding_email: str = Field(..., description='The forwarding address to be retrieved.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersSettingsForwardingAddressesGetToolOutput(ForwardingAddress):
    """Output for tool `gmail_users_settings_forwarding_addresses_get`."""
    pass

class GmailUsersSettingsForwardingAddressesListToolInput(BaseModel):
    """Input for tool `gmail_users_settings_forwarding_addresses_list`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description='User\'s email address. The special value "me" can be used to indicate the authenticated user.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersSettingsForwardingAddressesListToolOutput(ListForwardingAddressesResponse):
    """Output for tool `gmail_users_settings_forwarding_addresses_list`."""
    pass

class GmailUsersSettingsGetAutoForwardingToolInput(BaseModel):
    """Input for tool `gmail_users_settings_get_auto_forwarding`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description='User\'s email address. The special value "me" can be used to indicate the authenticated user.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersSettingsGetAutoForwardingToolOutput(AutoForwarding):
    """Output for tool `gmail_users_settings_get_auto_forwarding`."""
    pass

class GmailUsersSettingsGetImapToolInput(BaseModel):
    """Input for tool `gmail_users_settings_get_imap`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description='User\'s email address. The special value "me" can be used to indicate the authenticated user.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersSettingsGetImapToolOutput(ImapSettings):
    """Output for tool `gmail_users_settings_get_imap`."""
    pass

class GmailUsersSettingsGetLanguageToolInput(BaseModel):
    """Input for tool `gmail_users_settings_get_language`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description='User\'s email address. The special value "me" can be used to indicate the authenticated user.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersSettingsGetLanguageToolOutput(LanguageSettings):
    """Output for tool `gmail_users_settings_get_language`."""
    pass

class GmailUsersSettingsGetPopToolInput(BaseModel):
    """Input for tool `gmail_users_settings_get_pop`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description='User\'s email address. The special value "me" can be used to indicate the authenticated user.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersSettingsGetPopToolOutput(PopSettings):
    """Output for tool `gmail_users_settings_get_pop`."""
    pass

class GmailUsersSettingsGetVacationToolInput(BaseModel):
    """Input for tool `gmail_users_settings_get_vacation`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description='User\'s email address. The special value "me" can be used to indicate the authenticated user.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersSettingsGetVacationToolOutput(VacationSettings):
    """Output for tool `gmail_users_settings_get_vacation`."""
    pass

class GmailUsersSettingsSendAsCreateToolInput(BaseModel):
    """Input for tool `gmail_users_settings_send_as_create`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description='User\'s email address. The special value "me" can be used to indicate the authenticated user.')
    body: SendAs | None = Field(default=None, description='Request body for `gmail_users_settings_send_as_create`.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersSettingsSendAsCreateToolOutput(SendAs):
    """Output for tool `gmail_users_settings_send_as_create`."""
    pass

class GmailUsersSettingsSendAsDeleteToolInput(BaseModel):
    """Input for tool `gmail_users_settings_send_as_delete`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description='User\'s email address. The special value "me" can be used to indicate the authenticated user.')
    send_as_email: str = Field(..., description='The send-as alias to be deleted.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersSettingsSendAsDeleteToolOutput(RootModel[dict[str, object]]):
    """Output for tool `gmail_users_settings_send_as_delete`."""
    pass

class GmailUsersSettingsSendAsGetToolInput(BaseModel):
    """Input for tool `gmail_users_settings_send_as_get`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description='User\'s email address. The special value "me" can be used to indicate the authenticated user.')
    send_as_email: str = Field(..., description='The send-as alias to be retrieved.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersSettingsSendAsGetToolOutput(SendAs):
    """Output for tool `gmail_users_settings_send_as_get`."""
    pass

class GmailUsersSettingsSendAsListToolInput(BaseModel):
    """Input for tool `gmail_users_settings_send_as_list`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description='User\'s email address. The special value "me" can be used to indicate the authenticated user.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersSettingsSendAsListToolOutput(ListSendAsResponse):
    """Output for tool `gmail_users_settings_send_as_list`."""
    pass

class GmailUsersSettingsSendAsPatchToolInput(BaseModel):
    """Input for tool `gmail_users_settings_send_as_patch`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description='User\'s email address. The special value "me" can be used to indicate the authenticated user.')
    send_as_email: str = Field(..., description='The send-as alias to be updated.')
    body: SendAs | None = Field(default=None, description='Request body for `gmail_users_settings_send_as_patch`.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersSettingsSendAsPatchToolOutput(SendAs):
    """Output for tool `gmail_users_settings_send_as_patch`."""
    pass

class GmailUsersSettingsSendAsSmimeInfoDeleteToolInput(BaseModel):
    """Input for tool `gmail_users_settings_send_as_smime_info_delete`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description="The user's email address. The special value `me` can be used to indicate the authenticated user.")
    send_as_email: str = Field(..., description='The email address that appears in the "From:" header for mail sent using this alias.')
    id: str = Field(..., description='The immutable ID for the SmimeInfo.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersSettingsSendAsSmimeInfoDeleteToolOutput(RootModel[dict[str, object]]):
    """Output for tool `gmail_users_settings_send_as_smime_info_delete`."""
    pass

class GmailUsersSettingsSendAsSmimeInfoGetToolInput(BaseModel):
    """Input for tool `gmail_users_settings_send_as_smime_info_get`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description="The user's email address. The special value `me` can be used to indicate the authenticated user.")
    send_as_email: str = Field(..., description='The email address that appears in the "From:" header for mail sent using this alias.')
    id: str = Field(..., description='The immutable ID for the SmimeInfo.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersSettingsSendAsSmimeInfoGetToolOutput(SmimeInfo):
    """Output for tool `gmail_users_settings_send_as_smime_info_get`."""
    pass

class GmailUsersSettingsSendAsSmimeInfoInsertToolInput(BaseModel):
    """Input for tool `gmail_users_settings_send_as_smime_info_insert`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description="The user's email address. The special value `me` can be used to indicate the authenticated user.")
    send_as_email: str = Field(..., description='The email address that appears in the "From:" header for mail sent using this alias.')
    body: SmimeInfo | None = Field(default=None, description='Request body for `gmail_users_settings_send_as_smime_info_insert`.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersSettingsSendAsSmimeInfoInsertToolOutput(SmimeInfo):
    """Output for tool `gmail_users_settings_send_as_smime_info_insert`."""
    pass

class GmailUsersSettingsSendAsSmimeInfoListToolInput(BaseModel):
    """Input for tool `gmail_users_settings_send_as_smime_info_list`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description="The user's email address. The special value `me` can be used to indicate the authenticated user.")
    send_as_email: str = Field(..., description='The email address that appears in the "From:" header for mail sent using this alias.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersSettingsSendAsSmimeInfoListToolOutput(ListSmimeInfoResponse):
    """Output for tool `gmail_users_settings_send_as_smime_info_list`."""
    pass

class GmailUsersSettingsSendAsSmimeInfoSetDefaultToolInput(BaseModel):
    """Input for tool `gmail_users_settings_send_as_smime_info_set_default`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description="The user's email address. The special value `me` can be used to indicate the authenticated user.")
    send_as_email: str = Field(..., description='The email address that appears in the "From:" header for mail sent using this alias.')
    id: str = Field(..., description='The immutable ID for the SmimeInfo.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersSettingsSendAsSmimeInfoSetDefaultToolOutput(RootModel[dict[str, object]]):
    """Output for tool `gmail_users_settings_send_as_smime_info_set_default`."""
    pass

class GmailUsersSettingsSendAsUpdateToolInput(BaseModel):
    """Input for tool `gmail_users_settings_send_as_update`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description='User\'s email address. The special value "me" can be used to indicate the authenticated user.')
    send_as_email: str = Field(..., description='The send-as alias to be updated.')
    body: SendAs | None = Field(default=None, description='Request body for `gmail_users_settings_send_as_update`.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersSettingsSendAsUpdateToolOutput(SendAs):
    """Output for tool `gmail_users_settings_send_as_update`."""
    pass

class GmailUsersSettingsSendAsVerifyToolInput(BaseModel):
    """Input for tool `gmail_users_settings_send_as_verify`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description='User\'s email address. The special value "me" can be used to indicate the authenticated user.')
    send_as_email: str = Field(..., description='The send-as alias to be verified.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersSettingsSendAsVerifyToolOutput(RootModel[dict[str, object]]):
    """Output for tool `gmail_users_settings_send_as_verify`."""
    pass

class GmailUsersSettingsUpdateAutoForwardingToolInput(BaseModel):
    """Input for tool `gmail_users_settings_update_auto_forwarding`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description='User\'s email address. The special value "me" can be used to indicate the authenticated user.')
    body: AutoForwarding | None = Field(default=None, description='Request body for `gmail_users_settings_update_auto_forwarding`.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersSettingsUpdateAutoForwardingToolOutput(AutoForwarding):
    """Output for tool `gmail_users_settings_update_auto_forwarding`."""
    pass

class GmailUsersSettingsUpdateImapToolInput(BaseModel):
    """Input for tool `gmail_users_settings_update_imap`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description='User\'s email address. The special value "me" can be used to indicate the authenticated user.')
    body: ImapSettings | None = Field(default=None, description='Request body for `gmail_users_settings_update_imap`.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersSettingsUpdateImapToolOutput(ImapSettings):
    """Output for tool `gmail_users_settings_update_imap`."""
    pass

class GmailUsersSettingsUpdateLanguageToolInput(BaseModel):
    """Input for tool `gmail_users_settings_update_language`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description='User\'s email address. The special value "me" can be used to indicate the authenticated user.')
    body: LanguageSettings | None = Field(default=None, description='Request body for `gmail_users_settings_update_language`.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersSettingsUpdateLanguageToolOutput(LanguageSettings):
    """Output for tool `gmail_users_settings_update_language`."""
    pass

class GmailUsersSettingsUpdatePopToolInput(BaseModel):
    """Input for tool `gmail_users_settings_update_pop`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description='User\'s email address. The special value "me" can be used to indicate the authenticated user.')
    body: PopSettings | None = Field(default=None, description='Request body for `gmail_users_settings_update_pop`.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersSettingsUpdatePopToolOutput(PopSettings):
    """Output for tool `gmail_users_settings_update_pop`."""
    pass

class GmailUsersSettingsUpdateVacationToolInput(BaseModel):
    """Input for tool `gmail_users_settings_update_vacation`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description='User\'s email address. The special value "me" can be used to indicate the authenticated user.')
    body: VacationSettings | None = Field(default=None, description='Request body for `gmail_users_settings_update_vacation`.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersSettingsUpdateVacationToolOutput(VacationSettings):
    """Output for tool `gmail_users_settings_update_vacation`."""
    pass

class GmailUsersStopToolInput(BaseModel):
    """Input for tool `gmail_users_stop`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description="The user's email address. The special value `me` can be used to indicate the authenticated user.")
    model_config = ConfigDict(extra='forbid')

class GmailUsersStopToolOutput(RootModel[dict[str, object]]):
    """Output for tool `gmail_users_stop`."""
    pass

class GmailUsersThreadsDeleteToolInput(BaseModel):
    """Input for tool `gmail_users_threads_delete`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description="The user's email address. The special value `me` can be used to indicate the authenticated user.")
    id: str = Field(..., description='ID of the Thread to delete.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersThreadsDeleteToolOutput(RootModel[dict[str, object]]):
    """Output for tool `gmail_users_threads_delete`."""
    pass

class GmailUsersThreadsGetToolInput(BaseModel):
    """Input for tool `gmail_users_threads_get`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description="The user's email address. The special value `me` can be used to indicate the authenticated user.")
    id: str = Field(..., description='The ID of the thread to retrieve.')
    format: Literal['full', 'metadata', 'minimal'] | None = Field(default=None, description='The format to return the messages in.')
    metadata_headers: list[str] | None = Field(default=None, description='When given and format is METADATA, only include headers specified.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersThreadsGetToolOutput(Thread):
    """Output for tool `gmail_users_threads_get`."""
    pass

class GmailUsersThreadsListToolInput(BaseModel):
    """Input for tool `gmail_users_threads_list`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description="The user's email address. The special value `me` can be used to indicate the authenticated user.")
    include_spam_trash: bool | None = Field(default=None, description='Include threads from `SPAM` and `TRASH` in the results.')
    label_ids: list[str] | None = Field(default=None, description='Only return threads with labels that match all of the specified label IDs.')
    max_results: int | None = Field(default=None, description='Maximum number of threads to return. This field defaults to 100. The maximum allowed value for this field is 500.')
    page_token: str | None = Field(default=None, description='Page token to retrieve a specific page of results in the list.')
    q: str | None = Field(default=None, description='Only return threads matching the specified query. Supports the same query format as the Gmail search box. For example, `"from:someuser@example.com rfc822msgid: is:unread"`. Parameter cannot be used when accessing the api using the gmail.metadata scope.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersThreadsListToolOutput(ListThreadsResponse):
    """Output for tool `gmail_users_threads_list`."""
    pass

class GmailUsersThreadsModifyToolInput(BaseModel):
    """Input for tool `gmail_users_threads_modify`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description="The user's email address. The special value `me` can be used to indicate the authenticated user.")
    id: str = Field(..., description='The ID of the thread to modify.')
    body: ModifyThreadRequest | None = Field(default=None, description='Request body for `gmail_users_threads_modify`.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersThreadsModifyToolOutput(Thread):
    """Output for tool `gmail_users_threads_modify`."""
    pass

class GmailUsersThreadsTrashToolInput(BaseModel):
    """Input for tool `gmail_users_threads_trash`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description="The user's email address. The special value `me` can be used to indicate the authenticated user.")
    id: str = Field(..., description='The ID of the thread to Trash.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersThreadsTrashToolOutput(Thread):
    """Output for tool `gmail_users_threads_trash`."""
    pass

class GmailUsersThreadsUntrashToolInput(BaseModel):
    """Input for tool `gmail_users_threads_untrash`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description="The user's email address. The special value `me` can be used to indicate the authenticated user.")
    id: str = Field(..., description='The ID of the thread to remove from Trash.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersThreadsUntrashToolOutput(Thread):
    """Output for tool `gmail_users_threads_untrash`."""
    pass

class GmailUsersWatchToolInput(BaseModel):
    """Input for tool `gmail_users_watch`."""
    fields: str | None = Field(default=None, description='Selector specifying which fields to include in a partial response.')
    user_id: str = Field(..., description="The user's email address. The special value `me` can be used to indicate the authenticated user.")
    body: WatchRequest | None = Field(default=None, description='Request body for `gmail_users_watch`.')
    model_config = ConfigDict(extra='forbid')

class GmailUsersWatchToolOutput(WatchResponse):
    """Output for tool `gmail_users_watch`."""
    pass

INPUT_MODELS = {
    'gmail_users_drafts_create': GmailUsersDraftsCreateToolInput,
    'gmail_users_drafts_delete': GmailUsersDraftsDeleteToolInput,
    'gmail_users_drafts_get': GmailUsersDraftsGetToolInput,
    'gmail_users_drafts_list': GmailUsersDraftsListToolInput,
    'gmail_users_drafts_send': GmailUsersDraftsSendToolInput,
    'gmail_users_drafts_update': GmailUsersDraftsUpdateToolInput,
    'gmail_users_get_profile': GmailUsersGetProfileToolInput,
    'gmail_users_history_list': GmailUsersHistoryListToolInput,
    'gmail_users_labels_create': GmailUsersLabelsCreateToolInput,
    'gmail_users_labels_delete': GmailUsersLabelsDeleteToolInput,
    'gmail_users_labels_get': GmailUsersLabelsGetToolInput,
    'gmail_users_labels_list': GmailUsersLabelsListToolInput,
    'gmail_users_labels_patch': GmailUsersLabelsPatchToolInput,
    'gmail_users_labels_update': GmailUsersLabelsUpdateToolInput,
    'gmail_users_messages_attachments_get': GmailUsersMessagesAttachmentsGetToolInput,
    'gmail_users_messages_batch_delete': GmailUsersMessagesBatchDeleteToolInput,
    'gmail_users_messages_batch_modify': GmailUsersMessagesBatchModifyToolInput,
    'gmail_users_messages_delete': GmailUsersMessagesDeleteToolInput,
    'gmail_users_messages_get': GmailUsersMessagesGetToolInput,
    'gmail_users_messages_import': GmailUsersMessagesImportToolInput,
    'gmail_users_messages_insert': GmailUsersMessagesInsertToolInput,
    'gmail_users_messages_list': GmailUsersMessagesListToolInput,
    'gmail_users_messages_modify': GmailUsersMessagesModifyToolInput,
    'gmail_users_messages_send': GmailUsersMessagesSendToolInput,
    'gmail_users_messages_trash': GmailUsersMessagesTrashToolInput,
    'gmail_users_messages_untrash': GmailUsersMessagesUntrashToolInput,
    'gmail_users_settings_cse_identities_create': GmailUsersSettingsCseIdentitiesCreateToolInput,
    'gmail_users_settings_cse_identities_delete': GmailUsersSettingsCseIdentitiesDeleteToolInput,
    'gmail_users_settings_cse_identities_get': GmailUsersSettingsCseIdentitiesGetToolInput,
    'gmail_users_settings_cse_identities_list': GmailUsersSettingsCseIdentitiesListToolInput,
    'gmail_users_settings_cse_identities_patch': GmailUsersSettingsCseIdentitiesPatchToolInput,
    'gmail_users_settings_cse_keypairs_create': GmailUsersSettingsCseKeypairsCreateToolInput,
    'gmail_users_settings_cse_keypairs_disable': GmailUsersSettingsCseKeypairsDisableToolInput,
    'gmail_users_settings_cse_keypairs_enable': GmailUsersSettingsCseKeypairsEnableToolInput,
    'gmail_users_settings_cse_keypairs_get': GmailUsersSettingsCseKeypairsGetToolInput,
    'gmail_users_settings_cse_keypairs_list': GmailUsersSettingsCseKeypairsListToolInput,
    'gmail_users_settings_cse_keypairs_obliterate': GmailUsersSettingsCseKeypairsObliterateToolInput,
    'gmail_users_settings_delegates_create': GmailUsersSettingsDelegatesCreateToolInput,
    'gmail_users_settings_delegates_delete': GmailUsersSettingsDelegatesDeleteToolInput,
    'gmail_users_settings_delegates_get': GmailUsersSettingsDelegatesGetToolInput,
    'gmail_users_settings_delegates_list': GmailUsersSettingsDelegatesListToolInput,
    'gmail_users_settings_filters_create': GmailUsersSettingsFiltersCreateToolInput,
    'gmail_users_settings_filters_delete': GmailUsersSettingsFiltersDeleteToolInput,
    'gmail_users_settings_filters_get': GmailUsersSettingsFiltersGetToolInput,
    'gmail_users_settings_filters_list': GmailUsersSettingsFiltersListToolInput,
    'gmail_users_settings_forwarding_addresses_create': GmailUsersSettingsForwardingAddressesCreateToolInput,
    'gmail_users_settings_forwarding_addresses_delete': GmailUsersSettingsForwardingAddressesDeleteToolInput,
    'gmail_users_settings_forwarding_addresses_get': GmailUsersSettingsForwardingAddressesGetToolInput,
    'gmail_users_settings_forwarding_addresses_list': GmailUsersSettingsForwardingAddressesListToolInput,
    'gmail_users_settings_get_auto_forwarding': GmailUsersSettingsGetAutoForwardingToolInput,
    'gmail_users_settings_get_imap': GmailUsersSettingsGetImapToolInput,
    'gmail_users_settings_get_language': GmailUsersSettingsGetLanguageToolInput,
    'gmail_users_settings_get_pop': GmailUsersSettingsGetPopToolInput,
    'gmail_users_settings_get_vacation': GmailUsersSettingsGetVacationToolInput,
    'gmail_users_settings_send_as_create': GmailUsersSettingsSendAsCreateToolInput,
    'gmail_users_settings_send_as_delete': GmailUsersSettingsSendAsDeleteToolInput,
    'gmail_users_settings_send_as_get': GmailUsersSettingsSendAsGetToolInput,
    'gmail_users_settings_send_as_list': GmailUsersSettingsSendAsListToolInput,
    'gmail_users_settings_send_as_patch': GmailUsersSettingsSendAsPatchToolInput,
    'gmail_users_settings_send_as_smime_info_delete': GmailUsersSettingsSendAsSmimeInfoDeleteToolInput,
    'gmail_users_settings_send_as_smime_info_get': GmailUsersSettingsSendAsSmimeInfoGetToolInput,
    'gmail_users_settings_send_as_smime_info_insert': GmailUsersSettingsSendAsSmimeInfoInsertToolInput,
    'gmail_users_settings_send_as_smime_info_list': GmailUsersSettingsSendAsSmimeInfoListToolInput,
    'gmail_users_settings_send_as_smime_info_set_default': GmailUsersSettingsSendAsSmimeInfoSetDefaultToolInput,
    'gmail_users_settings_send_as_update': GmailUsersSettingsSendAsUpdateToolInput,
    'gmail_users_settings_send_as_verify': GmailUsersSettingsSendAsVerifyToolInput,
    'gmail_users_settings_update_auto_forwarding': GmailUsersSettingsUpdateAutoForwardingToolInput,
    'gmail_users_settings_update_imap': GmailUsersSettingsUpdateImapToolInput,
    'gmail_users_settings_update_language': GmailUsersSettingsUpdateLanguageToolInput,
    'gmail_users_settings_update_pop': GmailUsersSettingsUpdatePopToolInput,
    'gmail_users_settings_update_vacation': GmailUsersSettingsUpdateVacationToolInput,
    'gmail_users_stop': GmailUsersStopToolInput,
    'gmail_users_threads_delete': GmailUsersThreadsDeleteToolInput,
    'gmail_users_threads_get': GmailUsersThreadsGetToolInput,
    'gmail_users_threads_list': GmailUsersThreadsListToolInput,
    'gmail_users_threads_modify': GmailUsersThreadsModifyToolInput,
    'gmail_users_threads_trash': GmailUsersThreadsTrashToolInput,
    'gmail_users_threads_untrash': GmailUsersThreadsUntrashToolInput,
    'gmail_users_watch': GmailUsersWatchToolInput,
}

OUTPUT_MODELS = {
    'gmail_users_drafts_create': GmailUsersDraftsCreateToolOutput,
    'gmail_users_drafts_delete': GmailUsersDraftsDeleteToolOutput,
    'gmail_users_drafts_get': GmailUsersDraftsGetToolOutput,
    'gmail_users_drafts_list': GmailUsersDraftsListToolOutput,
    'gmail_users_drafts_send': GmailUsersDraftsSendToolOutput,
    'gmail_users_drafts_update': GmailUsersDraftsUpdateToolOutput,
    'gmail_users_get_profile': GmailUsersGetProfileToolOutput,
    'gmail_users_history_list': GmailUsersHistoryListToolOutput,
    'gmail_users_labels_create': GmailUsersLabelsCreateToolOutput,
    'gmail_users_labels_delete': GmailUsersLabelsDeleteToolOutput,
    'gmail_users_labels_get': GmailUsersLabelsGetToolOutput,
    'gmail_users_labels_list': GmailUsersLabelsListToolOutput,
    'gmail_users_labels_patch': GmailUsersLabelsPatchToolOutput,
    'gmail_users_labels_update': GmailUsersLabelsUpdateToolOutput,
    'gmail_users_messages_attachments_get': GmailUsersMessagesAttachmentsGetToolOutput,
    'gmail_users_messages_batch_delete': GmailUsersMessagesBatchDeleteToolOutput,
    'gmail_users_messages_batch_modify': GmailUsersMessagesBatchModifyToolOutput,
    'gmail_users_messages_delete': GmailUsersMessagesDeleteToolOutput,
    'gmail_users_messages_get': GmailUsersMessagesGetToolOutput,
    'gmail_users_messages_import': GmailUsersMessagesImportToolOutput,
    'gmail_users_messages_insert': GmailUsersMessagesInsertToolOutput,
    'gmail_users_messages_list': GmailUsersMessagesListToolOutput,
    'gmail_users_messages_modify': GmailUsersMessagesModifyToolOutput,
    'gmail_users_messages_send': GmailUsersMessagesSendToolOutput,
    'gmail_users_messages_trash': GmailUsersMessagesTrashToolOutput,
    'gmail_users_messages_untrash': GmailUsersMessagesUntrashToolOutput,
    'gmail_users_settings_cse_identities_create': GmailUsersSettingsCseIdentitiesCreateToolOutput,
    'gmail_users_settings_cse_identities_delete': GmailUsersSettingsCseIdentitiesDeleteToolOutput,
    'gmail_users_settings_cse_identities_get': GmailUsersSettingsCseIdentitiesGetToolOutput,
    'gmail_users_settings_cse_identities_list': GmailUsersSettingsCseIdentitiesListToolOutput,
    'gmail_users_settings_cse_identities_patch': GmailUsersSettingsCseIdentitiesPatchToolOutput,
    'gmail_users_settings_cse_keypairs_create': GmailUsersSettingsCseKeypairsCreateToolOutput,
    'gmail_users_settings_cse_keypairs_disable': GmailUsersSettingsCseKeypairsDisableToolOutput,
    'gmail_users_settings_cse_keypairs_enable': GmailUsersSettingsCseKeypairsEnableToolOutput,
    'gmail_users_settings_cse_keypairs_get': GmailUsersSettingsCseKeypairsGetToolOutput,
    'gmail_users_settings_cse_keypairs_list': GmailUsersSettingsCseKeypairsListToolOutput,
    'gmail_users_settings_cse_keypairs_obliterate': GmailUsersSettingsCseKeypairsObliterateToolOutput,
    'gmail_users_settings_delegates_create': GmailUsersSettingsDelegatesCreateToolOutput,
    'gmail_users_settings_delegates_delete': GmailUsersSettingsDelegatesDeleteToolOutput,
    'gmail_users_settings_delegates_get': GmailUsersSettingsDelegatesGetToolOutput,
    'gmail_users_settings_delegates_list': GmailUsersSettingsDelegatesListToolOutput,
    'gmail_users_settings_filters_create': GmailUsersSettingsFiltersCreateToolOutput,
    'gmail_users_settings_filters_delete': GmailUsersSettingsFiltersDeleteToolOutput,
    'gmail_users_settings_filters_get': GmailUsersSettingsFiltersGetToolOutput,
    'gmail_users_settings_filters_list': GmailUsersSettingsFiltersListToolOutput,
    'gmail_users_settings_forwarding_addresses_create': GmailUsersSettingsForwardingAddressesCreateToolOutput,
    'gmail_users_settings_forwarding_addresses_delete': GmailUsersSettingsForwardingAddressesDeleteToolOutput,
    'gmail_users_settings_forwarding_addresses_get': GmailUsersSettingsForwardingAddressesGetToolOutput,
    'gmail_users_settings_forwarding_addresses_list': GmailUsersSettingsForwardingAddressesListToolOutput,
    'gmail_users_settings_get_auto_forwarding': GmailUsersSettingsGetAutoForwardingToolOutput,
    'gmail_users_settings_get_imap': GmailUsersSettingsGetImapToolOutput,
    'gmail_users_settings_get_language': GmailUsersSettingsGetLanguageToolOutput,
    'gmail_users_settings_get_pop': GmailUsersSettingsGetPopToolOutput,
    'gmail_users_settings_get_vacation': GmailUsersSettingsGetVacationToolOutput,
    'gmail_users_settings_send_as_create': GmailUsersSettingsSendAsCreateToolOutput,
    'gmail_users_settings_send_as_delete': GmailUsersSettingsSendAsDeleteToolOutput,
    'gmail_users_settings_send_as_get': GmailUsersSettingsSendAsGetToolOutput,
    'gmail_users_settings_send_as_list': GmailUsersSettingsSendAsListToolOutput,
    'gmail_users_settings_send_as_patch': GmailUsersSettingsSendAsPatchToolOutput,
    'gmail_users_settings_send_as_smime_info_delete': GmailUsersSettingsSendAsSmimeInfoDeleteToolOutput,
    'gmail_users_settings_send_as_smime_info_get': GmailUsersSettingsSendAsSmimeInfoGetToolOutput,
    'gmail_users_settings_send_as_smime_info_insert': GmailUsersSettingsSendAsSmimeInfoInsertToolOutput,
    'gmail_users_settings_send_as_smime_info_list': GmailUsersSettingsSendAsSmimeInfoListToolOutput,
    'gmail_users_settings_send_as_smime_info_set_default': GmailUsersSettingsSendAsSmimeInfoSetDefaultToolOutput,
    'gmail_users_settings_send_as_update': GmailUsersSettingsSendAsUpdateToolOutput,
    'gmail_users_settings_send_as_verify': GmailUsersSettingsSendAsVerifyToolOutput,
    'gmail_users_settings_update_auto_forwarding': GmailUsersSettingsUpdateAutoForwardingToolOutput,
    'gmail_users_settings_update_imap': GmailUsersSettingsUpdateImapToolOutput,
    'gmail_users_settings_update_language': GmailUsersSettingsUpdateLanguageToolOutput,
    'gmail_users_settings_update_pop': GmailUsersSettingsUpdatePopToolOutput,
    'gmail_users_settings_update_vacation': GmailUsersSettingsUpdateVacationToolOutput,
    'gmail_users_stop': GmailUsersStopToolOutput,
    'gmail_users_threads_delete': GmailUsersThreadsDeleteToolOutput,
    'gmail_users_threads_get': GmailUsersThreadsGetToolOutput,
    'gmail_users_threads_list': GmailUsersThreadsListToolOutput,
    'gmail_users_threads_modify': GmailUsersThreadsModifyToolOutput,
    'gmail_users_threads_trash': GmailUsersThreadsTrashToolOutput,
    'gmail_users_threads_untrash': GmailUsersThreadsUntrashToolOutput,
    'gmail_users_watch': GmailUsersWatchToolOutput,
}
