"""Pod module unit test fixtures (mocked ports)."""

from unittest.mock import AsyncMock

import pytest

from app.modules.pod.services.pod_member_service import PodMemberService
from app.modules.pod.services.pod_service import PodService

pytestmark = pytest.mark.unit


@pytest.fixture
def pod_repository_mock() -> AsyncMock:
    return AsyncMock()


@pytest.fixture
def pod_member_repository_mock() -> AsyncMock:
    return AsyncMock()


@pytest.fixture
def organization_repository_mock() -> AsyncMock:
    return AsyncMock()


@pytest.fixture
def authorization_service_mock() -> AsyncMock:
    return AsyncMock()


@pytest.fixture
def pod_service(
    pod_repository_mock: AsyncMock,
    pod_member_repository_mock: AsyncMock,
    organization_repository_mock: AsyncMock,
    authorization_service_mock: AsyncMock,
) -> PodService:
    return PodService(
        pod_repository=pod_repository_mock,
        pod_member_repository=pod_member_repository_mock,
        organization_repository=organization_repository_mock,
        authorization_service=authorization_service_mock,
    )


@pytest.fixture
def pod_member_service(
    pod_member_repository_mock: AsyncMock,
    pod_repository_mock: AsyncMock,
    organization_repository_mock: AsyncMock,
) -> PodMemberService:
    return PodMemberService(
        pod_member_repository=pod_member_repository_mock,
        pod_repository=pod_repository_mock,
        organization_repository=organization_repository_mock,
    )
