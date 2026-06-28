from __future__ import annotations


class IntegrationError(Exception):
    pass


class ToolNotFoundError(IntegrationError):
    pass


class OperationNotFoundError(IntegrationError):
    pass


class ToolValidationError(IntegrationError):
    pass


class IntegrationExecutionError(IntegrationError):
    def __init__(self, message: str, *, status_code: int | None = None):
        super().__init__(message)
        self.status_code = status_code
