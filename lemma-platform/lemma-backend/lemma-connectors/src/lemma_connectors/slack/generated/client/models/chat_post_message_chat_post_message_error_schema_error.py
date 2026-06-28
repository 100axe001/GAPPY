from enum import Enum

class ChatPostMessageChatPostMessageErrorSchemaError(str, Enum):
    ACCOUNT_INACTIVE = "account_inactive"
    CHANNEL_NOT_FOUND = "channel_not_found"
    INVALID_ARG_NAME = "invalid_arg_name"
    INVALID_ARRAY_ARG = "invalid_array_arg"
    INVALID_AUTH = "invalid_auth"
    INVALID_CHARSET = "invalid_charset"
    INVALID_FORM_DATA = "invalid_form_data"
    INVALID_POST_TYPE = "invalid_post_type"
    IS_ARCHIVED = "is_archived"
    MISSING_POST_TYPE = "missing_post_type"
    MSG_TOO_LONG = "msg_too_long"
    NOT_AUTHED = "not_authed"
    NOT_IN_CHANNEL = "not_in_channel"
    NO_TEXT = "no_text"
    RATE_LIMITED = "rate_limited"
    TOO_MANY_ATTACHMENTS = "too_many_attachments"

    def __str__(self) -> str:
        return str(self.value)
