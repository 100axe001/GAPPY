from enum import Enum

class ChatPostEphemeralChatPostEphemeralErrorSchemaError(str, Enum):
    ACCOUNT_INACTIVE = "account_inactive"
    CHANNEL_NOT_FOUND = "channel_not_found"
    FATAL_ERROR = "fatal_error"
    INVALID_ARG_NAME = "invalid_arg_name"
    INVALID_ARRAY_ARG = "invalid_array_arg"
    INVALID_AUTH = "invalid_auth"
    INVALID_CHARSET = "invalid_charset"
    INVALID_FORM_DATA = "invalid_form_data"
    INVALID_JSON = "invalid_json"
    INVALID_POST_TYPE = "invalid_post_type"
    IS_ARCHIVED = "is_archived"
    JSON_NOT_OBJECT = "json_not_object"
    MISSING_POST_TYPE = "missing_post_type"
    MSG_TOO_LONG = "msg_too_long"
    NOT_AUTHED = "not_authed"
    NO_PERMISSION = "no_permission"
    NO_TEXT = "no_text"
    ORG_LOGIN_REQUIRED = "org_login_required"
    REQUEST_TIMEOUT = "request_timeout"
    RESTRICTED_ACTION = "restricted_action"
    TEAM_ADDED_TO_ORG = "team_added_to_org"
    TOKEN_REVOKED = "token_revoked"
    TOO_MANY_ATTACHMENTS = "too_many_attachments"
    UPGRADE_REQUIRED = "upgrade_required"
    USER_NOT_IN_CHANNEL = "user_not_in_channel"

    def __str__(self) -> str:
        return str(self.value)
