from enum import Enum

class ConversationsRenameConversationsRenameErrorSchemaError(str, Enum):
    ACCOUNT_INACTIVE = "account_inactive"
    CHANNEL_NOT_FOUND = "channel_not_found"
    INVALID_ARG_NAME = "invalid_arg_name"
    INVALID_ARRAY_ARG = "invalid_array_arg"
    INVALID_AUTH = "invalid_auth"
    INVALID_CHARSET = "invalid_charset"
    INVALID_FORM_DATA = "invalid_form_data"
    INVALID_JSON = "invalid_json"
    INVALID_NAME = "invalid_name"
    INVALID_NAME_MAXLENGTH = "invalid_name_maxlength"
    INVALID_NAME_PUNCTUATION = "invalid_name_punctuation"
    INVALID_NAME_REQUIRED = "invalid_name_required"
    INVALID_NAME_SPECIALS = "invalid_name_specials"
    INVALID_POST_TYPE = "invalid_post_type"
    JSON_NOT_OBJECT = "json_not_object"
    METHOD_NOT_SUPPORTED_FOR_CHANNEL_TYPE = "method_not_supported_for_channel_type"
    MISSING_POST_TYPE = "missing_post_type"
    MISSING_SCOPE = "missing_scope"
    NAME_TAKEN = "name_taken"
    NOT_AUTHED = "not_authed"
    NOT_AUTHORIZED = "not_authorized"
    NOT_IN_CHANNEL = "not_in_channel"
    REQUEST_TIMEOUT = "request_timeout"
    UPGRADE_REQUIRED = "upgrade_required"
    USER_IS_RESTRICTED = "user_is_restricted"

    def __str__(self) -> str:
        return str(self.value)
