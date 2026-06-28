from enum import Enum

class ReactionsAddReactionsAddErrorSchemaError(str, Enum):
    ACCOUNT_INACTIVE = "account_inactive"
    ALREADY_REACTED = "already_reacted"
    BAD_TIMESTAMP = "bad_timestamp"
    INVALID_ARG_NAME = "invalid_arg_name"
    INVALID_ARRAY_ARG = "invalid_array_arg"
    INVALID_AUTH = "invalid_auth"
    INVALID_CHARSET = "invalid_charset"
    INVALID_FORM_DATA = "invalid_form_data"
    INVALID_JSON = "invalid_json"
    INVALID_NAME = "invalid_name"
    INVALID_POST_TYPE = "invalid_post_type"
    JSON_NOT_OBJECT = "json_not_object"
    MESSAGE_NOT_FOUND = "message_not_found"
    MISSING_POST_TYPE = "missing_post_type"
    NOT_AUTHED = "not_authed"
    NO_ITEM_SPECIFIED = "no_item_specified"
    NO_PERMISSION = "no_permission"
    REQUEST_TIMEOUT = "request_timeout"
    TEAM_ADDED_TO_ORG = "team_added_to_org"
    TOO_MANY_EMOJI = "too_many_emoji"
    TOO_MANY_REACTIONS = "too_many_reactions"
    UPGRADE_REQUIRED = "upgrade_required"

    def __str__(self) -> str:
        return str(self.value)
