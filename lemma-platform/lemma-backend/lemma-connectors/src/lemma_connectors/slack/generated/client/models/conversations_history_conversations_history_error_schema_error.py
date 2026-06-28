from enum import Enum

class ConversationsHistoryConversationsHistoryErrorSchemaError(str, Enum):
    ACCOUNT_INACTIVE = "account_inactive"
    CHANNEL_NOT_FOUND = "channel_not_found"
    INVALID_ARG_NAME = "invalid_arg_name"
    INVALID_ARRAY_ARG = "invalid_array_arg"
    INVALID_AUTH = "invalid_auth"
    INVALID_CHARSET = "invalid_charset"
    INVALID_FORM_DATA = "invalid_form_data"
    INVALID_JSON = "invalid_json"
    INVALID_POST_TYPE = "invalid_post_type"
    INVALID_TS_LATEST = "invalid_ts_latest"
    INVALID_TS_OLDEST = "invalid_ts_oldest"
    JSON_NOT_OBJECT = "json_not_object"
    MISSING_POST_TYPE = "missing_post_type"
    MISSING_SCOPE = "missing_scope"
    NOT_AUTHED = "not_authed"
    REQUEST_TIMEOUT = "request_timeout"
    UPGRADE_REQUIRED = "upgrade_required"

    def __str__(self) -> str:
        return str(self.value)
