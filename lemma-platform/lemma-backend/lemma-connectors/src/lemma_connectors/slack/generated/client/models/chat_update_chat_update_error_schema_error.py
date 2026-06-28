from enum import Enum

class ChatUpdateChatUpdateErrorSchemaError(str, Enum):
    ACCOUNT_INACTIVE = "account_inactive"
    CANT_UPDATE_MESSAGE = "cant_update_message"
    CHANNEL_NOT_FOUND = "channel_not_found"
    EDIT_WINDOW_CLOSED = "edit_window_closed"
    FATAL_ERROR = "fatal_error"
    INVALID_ARG_NAME = "invalid_arg_name"
    INVALID_ARRAY_ARG = "invalid_array_arg"
    INVALID_AUTH = "invalid_auth"
    INVALID_CHARSET = "invalid_charset"
    INVALID_FORM_DATA = "invalid_form_data"
    INVALID_JSON = "invalid_json"
    INVALID_POST_TYPE = "invalid_post_type"
    IS_INACTIVE = "is_inactive"
    JSON_NOT_OBJECT = "json_not_object"
    MESSAGE_NOT_FOUND = "message_not_found"
    MISSING_POST_TYPE = "missing_post_type"
    MSG_TOO_LONG = "msg_too_long"
    NOT_AUTHED = "not_authed"
    NO_PERMISSION = "no_permission"
    NO_TEXT = "no_text"
    RATE_LIMITED = "rate_limited"
    REQUEST_TIMEOUT = "request_timeout"
    TOKEN_REVOKED = "token_revoked"
    TOO_MANY_ATTACHMENTS = "too_many_attachments"
    UPGRADE_REQUIRED = "upgrade_required"

    def __str__(self) -> str:
        return str(self.value)
