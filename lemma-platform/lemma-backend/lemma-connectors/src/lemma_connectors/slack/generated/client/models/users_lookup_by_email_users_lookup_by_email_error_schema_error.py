from enum import Enum

class UsersLookupByEmailUsersLookupByEmailErrorSchemaError(str, Enum):
    ACCOUNT_INACTIVE = "account_inactive"
    ENTERPRISE_IS_RESTRICTED = "enterprise_is_restricted"
    FATAL_ERROR = "fatal_error"
    INVALID_ARG_NAME = "invalid_arg_name"
    INVALID_ARRAY_ARG = "invalid_array_arg"
    INVALID_AUTH = "invalid_auth"
    INVALID_CHARSET = "invalid_charset"
    INVALID_FORM_DATA = "invalid_form_data"
    INVALID_JSON = "invalid_json"
    INVALID_POST_TYPE = "invalid_post_type"
    JSON_NOT_OBJECT = "json_not_object"
    MISSING_POST_TYPE = "missing_post_type"
    NOT_AUTHED = "not_authed"
    NO_PERMISSION = "no_permission"
    REQUEST_TIMEOUT = "request_timeout"
    TEAM_ADDED_TO_ORG = "team_added_to_org"
    UPGRADE_REQUIRED = "upgrade_required"
    USERS_NOT_FOUND = "users_not_found"

    def __str__(self) -> str:
        return str(self.value)
