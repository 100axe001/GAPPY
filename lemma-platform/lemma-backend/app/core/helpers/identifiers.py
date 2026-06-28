import re

_NON_DIGITS = re.compile(r"\D")


def normalize_mobile_digits(value: str | None) -> str | None:
    """Reduce a phone number to its digits, matching the DB uniqueness index.

    Mirrors ``regexp_replace(mobile_number, '\\D', '', 'g')`` used by
    ``ux_users_mobile_number_digits``. Returns ``None`` when there are no digits.
    """
    if not value:
        return None
    digits = _NON_DIGITS.sub("", value)
    return digits or None


def normalize_telegram(value: str | None) -> str | None:
    """Lower-case a telegram username, matching ``ux_users_telegram_username_lower``."""
    if value is None:
        return None
    normalized = value.strip().lower()
    return normalized or None
