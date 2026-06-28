from enum import Enum

class ConversationsOpenConversationsOpenErrorSchemaError(str, Enum):
    ACCOUNT_INACTIVE = "account_inactive"
    CHANNEL_NOT_FOUND = "channel_not_found"
    INVALID_ARG_NAME = "invalid_arg_name"
    INVALID_ARRAY_ARG = "invalid_array_arg"
    INVALID_AUTH = "invalid_auth"
    INVALID_CHARSET = "invalid_charset"
    INVALID_FORM_DATA = "invalid_form_data"
    INVALID_JSON = "invalid_json"
    INVALID_POST_TYPE = "invalid_post_type"
    INVALID_USER_COMBINATION = "invalid_user_combination"
    JSON_NOT_OBJECT = "json_not_object"
    METHOD_NOT_SUPPORTED_FOR_CHANNEL_TYPE = "method_not_supported_for_channel_type"
    MISSING_POST_TYPE = "missing_post_type"
    NOT_AUTHED = "not_authed"
    NOT_ENOUGH_USERS = "not_enough_users"
    REQUEST_TIMEOUT = "request_timeout"
    TEAM_ADDED_TO_ORG = "team_added_to_org"
    TOO_MANY_USERS = "too_many_users"
    UPGRADE_REQUIRED = "upgrade_required"
    USERS_LIST_NOT_SUPPLIED = "users_list_not_supplied"
    USER_DISABLED = "user_disabled"
    USER_NOT_FOUND = "user_not_found"
    USER_NOT_VISIBLE = "user_not_visible"

    def __str__(self) -> str:
        return str(self.value)
