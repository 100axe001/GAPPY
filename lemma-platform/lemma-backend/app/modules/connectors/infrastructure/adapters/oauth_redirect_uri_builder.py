from app.core.config import settings
from app.modules.connectors.domain.ports import OAuthRedirectUriBuilderPort


class OAuthRedirectUriBuilder(OAuthRedirectUriBuilderPort):
    def build(self) -> str:
        base_url = settings.api_url.rstrip("/")
        return f"{base_url}/connectors/connect-requests/oauth/callback"
