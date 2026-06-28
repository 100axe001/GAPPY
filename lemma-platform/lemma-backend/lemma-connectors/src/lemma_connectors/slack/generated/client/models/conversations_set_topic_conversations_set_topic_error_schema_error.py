from enum import Enum

class ConversationsSetTopicConversationsSetTopicErrorSchemaError(str, Enum):
    ACCOUNT_INACTIVE = "account_inactive"
    CHANNEL_NOT_FOUND = "channel_not_found"
    INVALID_ARG_NAME = "invalid_arg_name"
    INVALID_ARRAY_ARG = "invalid_array_arg"
    INVALID_AUTH = "invalid_auth"
    INVALID_CHARSET = "invalid_charset"
    INVALID_FORM_DATA = "invalid_form_data"
    INVALID_JSON = "invalid_json"
    INVALID_POST_TYPE = "invalid_post_type"
    IS_ARCHIVED = "is_archived"
    JSON_NOT_OBJECT = "json_not_object"
    METHOD_NOT_SUPPORTED_FOR_CHANNEL_TYPE = "method_not_supported_for_channel_type"
    MISSING_POST_TYPE = "missing_post_type"
    MISSING_SCOPE = "missing_scope"
    NOT_AUTHED = "not_authed"
    NOT_IN_CHANNEL = "not_in_channel"
    REQUEST_TIMEOUT = "request_timeout"
    TEAM_ADDED_TO_ORG = "team_added_to_org"
    TOO_LONG = "too_long"
    UPGRADE_REQUIRED = "upgrade_required"
    USER_IS_RESTRICTED = "user_is_restricted"

    def __str__(self) -> str:
        return str(self.value)
