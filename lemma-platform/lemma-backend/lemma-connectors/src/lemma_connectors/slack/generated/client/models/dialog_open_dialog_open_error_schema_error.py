from enum import Enum

class DialogOpenDialogOpenErrorSchemaError(str, Enum):
    ACCOUNT_INACTIVE = "account_inactive"
    APP_MISSING_ACTION_URL = "app_missing_action_url"
    CANNOT_CREATE_DIALOG = "cannot_create_dialog"
    FAILED_SENDING_DIALOG = "failed_sending_dialog"
    FATAL_ERROR = "fatal_error"
    INVALID_ARG_NAME = "invalid_arg_name"
    INVALID_ARRAY_ARG = "invalid_array_arg"
    INVALID_AUTH = "invalid_auth"
    INVALID_CHARSET = "invalid_charset"
    INVALID_FORM_DATA = "invalid_form_data"
    INVALID_JSON = "invalid_json"
    INVALID_POST_TYPE = "invalid_post_type"
    INVALID_TRIGGER = "invalid_trigger"
    JSON_NOT_OBJECT = "json_not_object"
    MISSING_DIALOG = "missing_dialog"
    MISSING_POST_TYPE = "missing_post_type"
    MISSING_TRIGGER = "missing_trigger"
    NOT_AUTHED = "not_authed"
    NO_PERMISSION = "no_permission"
    ORG_LOGIN_REQUIRED = "org_login_required"
    REQUEST_TIMEOUT = "request_timeout"
    TEAM_ADDED_TO_ORG = "team_added_to_org"
    TOKEN_REVOKED = "token_revoked"
    TRIGGER_EXCHANGED = "trigger_exchanged"
    TRIGGER_EXPIRED = "trigger_expired"
    UPGRADE_REQUIRED = "upgrade_required"
    VALIDATION_ERRORS = "validation_errors"

    def __str__(self) -> str:
        return str(self.value)
