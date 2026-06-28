from enum import Enum


class PodRole(str, Enum):
    """Explicit pod role names used across authorization and pod APIs."""

    ADMIN = "POD_ADMIN"
    EDITOR = "POD_EDITOR"
    USER = "POD_USER"
    VIEWER = "POD_VIEWER"
