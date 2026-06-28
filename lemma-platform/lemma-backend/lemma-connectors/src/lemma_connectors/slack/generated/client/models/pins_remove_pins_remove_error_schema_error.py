from enum import Enum

class PinsRemovePinsRemoveErrorSchemaError(str, Enum):
    ACCOUNT_INACTIVE = "account_inactive"
    BAD_TIMESTAMP = "bad_timestamp"
    FILE_COMMENT_NOT_FOUND = "file_comment_not_found"
    FILE_NOT_FOUND = "file_not_found"
    INVALID_ARG_NAME = "invalid_arg_name"
    INVALID_ARRAY_ARG = "invalid_array_arg"
    INVALID_AUTH = "invalid_auth"
    INVALID_CHARSET = "invalid_charset"
    INVALID_FORM_DATA = "invalid_form_data"
    INVALID_JSON = "invalid_json"
    INVALID_POST_TYP = "invalid_post_typ"
    JSON_NOT_OBJECT = "json_not_object"
    MESSAGE_NOT_FOUND = "message_not_found"
    MISSING_POST_TYP = "missing_post_typ"
    NOT_AUTHED = "not_authed"
    NOT_PINNED = "not_pinned"
    NO_ITEM_SPECIFIED = "no_item_specified"
    NO_PERMISSION = "no_permission"
    PERMISSION_DENIED = "permission_denied"
    REQUEST_TIMEOU = "request_timeou"
    TEAM_ADDED_TO_ORG = "team_added_to_org"
    UPGRADE_REQUIRED = "upgrade_required"

    def __str__(self) -> str:
        return str(self.value)
