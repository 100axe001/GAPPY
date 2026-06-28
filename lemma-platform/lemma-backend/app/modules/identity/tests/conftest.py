"""
Identity module shared test fixtures.
Used by both unit and e2e tests within the identity module.
"""

import pytest
from app.core.infrastructure.db.uow import SqlAlchemyUnitOfWork
from app.modules.identity.services.user_service import UserService
from app.modules.identity.services.organization_service import OrganizationService
from app.modules.identity.infrastructure.user_repositories import (
    UserRepository,
)
from app.modules.identity.infrastructure.organization_repositories import (
    OrganizationRepository,
)


@pytest.fixture
def uow(db_session):
    """Unit of Work with test database session."""
    return SqlAlchemyUnitOfWork(session=db_session)


@pytest.fixture
def user_service(uow):
    """User service instance for testing."""
    return UserService(
        user_repository=UserRepository(uow),
        organization_repository=OrganizationRepository(uow),
    )


@pytest.fixture
def organization_service(uow):
    """Organization service instance for testing."""
    return OrganizationService(
        organization_repository=OrganizationRepository(uow),
        user_repository=UserRepository(uow),
        invitation_accept_base_url="http://localhost:3000",
    )
