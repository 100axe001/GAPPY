from enum import Enum

class ChatDeleteScheduledMessageChatDeleteScheduledMessageErrorSchemaError(str, Enum):
    ACCOUNT_INACTIVE = "account_inactive"
    BAD_TOKEN = "bad_token"
    CHANNEL_NOT_FOUND = "channel_not_found"
    EKM_ACCESS_DENIED = "ekm_access_denied"
    FATAL_ERROR = "fatal_error"
    INVALID_ARGUMENTS = "invalid_arguments"
    INVALID_ARG_NAME = "invalid_arg_name"
    INVALID_AUTH = "invalid_auth"
    INVALID_CHARSET = "invalid_charset"
    INVALID_FORM_DATA = "invalid_form_data"
    INVALID_JSON = "invalid_json"
    INVALID_POST_TYPE = "invalid_post_type"
    INVALID_SCHEDULED_MESSAGE_ID = "invalid_scheduled_message_id"
    JSON_NOT_OBJECT = "json_not_object"
    MISSING_POST_TYPE = "missing_post_type"
    MISSING_SCOPE = "missing_scope"
    NOT_AUTHED = "not_authed"
    NO_PERMISSION = "no_permission"
    ORG_LOGIN_REQUIRED = "org_login_required"
    REQUEST_TIMEOUT = "request_timeout"
    TEAM_ADDED_TO_ORG = "team_added_to_org"
    TOKEN_REVOKED = "token_revoked"
    UPGRADE_REQUIRED = "upgrade_required"

    def __str__(self) -> str:
        return str(self.value)
