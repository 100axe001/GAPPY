from enum import Enum

class ConversationsLeaveConversationsLeaveErrorSchemaError(str, Enum):
    ACCOUNT_INACTIVE = "account_inactive"
    CANT_LEAVE_GENERAL = "cant_leave_general"
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
    LAST_MEMBER = "last_member"
    METHOD_NOT_SUPPORTED_FOR_CHANNEL_TYPE = "method_not_supported_for_channel_type"
    MISSING_CHARSET = "missing_charset"
    MISSING_POST_TYPE = "missing_post_type"
    MISSING_SCOPE = "missing_scope"
    NOT_AUTHED = "not_authed"
    REQUEST_TIMEOUT = "request_timeout"
    SUPERFLUOUS_CHARSET = "superfluous_charset"
    TEAM_ADDED_TO_ORG = "team_added_to_org"
    UPGRADE_REQUIRED = "upgrade_required"
    USER_IS_BOT = "user_is_bot"
    USER_IS_RESTRICTED = "user_is_restricted"
    USER_IS_ULTRA_RESTRICTED = "user_is_ultra_restricted"

    def __str__(self) -> str:
        return str(self.value)
