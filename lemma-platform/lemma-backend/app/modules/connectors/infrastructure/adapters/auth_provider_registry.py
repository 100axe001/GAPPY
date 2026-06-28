from app.modules.connectors.domain.ports import (
    AuthProviderPort,
    AuthProviderRegistryPort,
)


class AuthProviderRegistry(AuthProviderRegistryPort):
    def __init__(self, providers: dict[str, AuthProviderPort]):
        self._providers = providers

    def get(self, provider_name: str) -> AuthProviderPort | None:
        return self._providers.get(provider_name)
