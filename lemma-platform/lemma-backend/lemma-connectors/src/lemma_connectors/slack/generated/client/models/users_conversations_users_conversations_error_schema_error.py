from enum import Enum

class UsersConversationsUsersConversationsErrorSchemaError(str, Enum):
    ACCOUNT_INACTIVE = "account_inactive"
    FATAL_ERROR = "fatal_error"
    INVALID_ARG_NAME = "invalid_arg_name"
    INVALID_ARRAY_ARG = "invalid_array_arg"
    INVALID_AUTH = "invalid_auth"
    INVALID_CHARSET = "invalid_charset"
    INVALID_CURSOR = "invalid_cursor"
    INVALID_FORM_DATA = "invalid_form_data"
    INVALID_JSON = "invalid_json"
    INVALID_LIMIT = "invalid_limit"
    INVALID_POST_TYPE = "invalid_post_type"
    INVALID_TYPES = "invalid_types"
    JSON_NOT_OBJECT = "json_not_object"
    METHOD_NOT_SUPPORTED_FOR_CHANNEL_TYPE = "method_not_supported_for_channel_type"
    MISSING_POST_TYPE = "missing_post_type"
    MISSING_SCOPE = "missing_scope"
    NOT_AUTHED = "not_authed"
    NO_PERMISSION = "no_permission"
    REQUEST_TIMEOUT = "request_timeout"
    TEAM_ADDED_TO_ORG = "team_added_to_org"
    TOKEN_REVOKED = "token_revoked"
    UPGRADE_REQUIRED = "upgrade_required"

    def __str__(self) -> str:
        return str(self.value)
