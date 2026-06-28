"""Authorization service factory.

Re-exports the core factory so existing call sites keep importing
``create_authorization_service`` from here; the SQLAlchemy session access lives
in ``app/core/authorization/factory.py`` (not in the service layer).
"""

from app.core.authorization.factory import create_authorization_data_service
from app.core.authorization.service import AuthorizationDataService
from app.core.infrastructure.db.uow import SqlAlchemyUnitOfWork


def create_authorization_service(uow: SqlAlchemyUnitOfWork) -> AuthorizationDataService:
    return create_authorization_data_service(uow)
