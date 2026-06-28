from enum import Enum

class UsersProfileSetUsersProfileSetErrorSchemaError(str, Enum):
    ACCOUNT_INACTIVE = "account_inactive"
    CANNOT_UPDATE_ADMIN_USER = "cannot_update_admin_user"
    FATAL_ERROR = "fatal_error"
    INVALID_ARG_NAME = "invalid_arg_name"
    INVALID_ARRAY_ARG = "invalid_array_arg"
    INVALID_AUTH = "invalid_auth"
    INVALID_CHARSET = "invalid_charset"
    INVALID_FORM_DATA = "invalid_form_data"
    INVALID_JSON = "invalid_json"
    INVALID_POST_TYPE = "invalid_post_type"
    INVALID_PROFILE = "invalid_profile"
    JSON_NOT_OBJECT = "json_not_object"
    MISSING_POST_TYPE = "missing_post_type"
    NOT_ADMIN = "not_admin"
    NOT_APP_ADMIN = "not_app_admin"
    NOT_AUTHED = "not_authed"
    NO_PERMISSION = "no_permission"
    ORG_LOGIN_REQUIRED = "org_login_required"
    PROFILE_SET_FAILED = "profile_set_failed"
    REQUEST_TIMEOUT = "request_timeout"
    RESERVED_NAME = "reserved_name"
    TEAM_ADDED_TO_ORG = "team_added_to_org"
    TOKEN_REVOKED = "token_revoked"
    UPGRADE_REQUIRED = "upgrade_required"
    USER_IS_BOT = "user_is_bot"

    def __str__(self) -> str:
        return str(self.value)
