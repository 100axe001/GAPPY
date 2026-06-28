import re


class NameValidator:
    """Validator for names."""

    @staticmethod
    def validate(name: str, entity_name: str = "Entity") -> None:
        """
        Validate name.

        Rules:
        - Must properly start with alphanumeric
        - Can contain hyphens, underscores
        - Min 1, Max 255
        """
        if not name or len(name) < 1:
            raise ValueError(f"{entity_name} name cannot be empty")

        if len(name) > 255:
            raise ValueError(f"{entity_name} name must be less than 255 characters")

        # Basic regex
        if not re.match(r"^[a-zA-Z0-9_\- ]+$", name):
            raise ValueError(f"{entity_name} name contains invalid characters")
