"""Agent surface domain/application errors."""

from app.core.domain.errors import DomainError


class AgentSurfaceError(DomainError):
    def __init__(
        self,
        message: str,
        code: str = "AGENT_SURFACE_ERROR",
        status_code: int = 400,
    ):
        super().__init__(message=message, code=code, status_code=status_code)


class AgentSurfaceValidationError(AgentSurfaceError):
    def __init__(self, message: str):
        super().__init__(
            message=message,
            code="AGENT_SURFACE_VALIDATION_ERROR",
            status_code=400,
        )


class AgentSurfaceNotFoundError(AgentSurfaceError):
    def __init__(self, surface_id: str):
        super().__init__(
            message=f"Agent surface '{surface_id}' not found",
            code="AGENT_SURFACE_NOT_FOUND",
            status_code=404,
        )


class AgentSurfacePlatformError(AgentSurfaceError):
    def __init__(self, platform: str, message: str):
        super().__init__(
            message=f"Surface platform '{platform}' error: {message}",
            code="AGENT_SURFACE_PLATFORM_ERROR",
            status_code=400,
        )


class AgentSurfaceRoutingError(AgentSurfaceError):
    def __init__(self, message: str):
        super().__init__(
            message=message,
            code="AGENT_SURFACE_ROUTING_ERROR",
            status_code=400,
        )


class AgentSurfaceCredentialError(AgentSurfaceError):
    def __init__(self, platform: str, message: str):
        super().__init__(
            message=f"Surface credentials for '{platform}' error: {message}",
            code="AGENT_SURFACE_CREDENTIAL_ERROR",
            status_code=400,
        )
