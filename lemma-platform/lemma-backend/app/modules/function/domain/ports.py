"""Function module ports."""

from __future__ import annotations

from typing import Optional, Protocol, Tuple
from uuid import UUID

from app.core.authorization.context import Context
from app.modules.function.domain.entities import FunctionEntity, FunctionRunEntity


class FunctionRepositoryPort(Protocol):
    async def create(self, entity: FunctionEntity) -> FunctionEntity: ...

    async def get(self, id: UUID) -> Optional[FunctionEntity]: ...

    async def get_by_name(
        self, pod_id: UUID, name: str, ctx: Context | None = None
    ) -> Optional[FunctionEntity]: ...

    async def update(self, function: FunctionEntity) -> FunctionEntity: ...

    async def delete(self, id: UUID) -> bool: ...

    async def list_by_pod(
        self, pod_id: UUID, limit: int = 100, cursor: str | None = None
    ) -> Tuple[list[FunctionEntity], str | None]: ...

    async def list_visible_by_pod(
        self,
        pod_id: UUID,
        ctx: Context,
        limit: int = 100,
        cursor: str | None = None,
    ) -> Tuple[list[FunctionEntity], str | None]: ...


class FunctionRunRepositoryPort(Protocol):
    async def create_run(self, entity: FunctionRunEntity) -> FunctionRunEntity: ...

    async def update_run(self, run_id: UUID, **kwargs) -> FunctionRunEntity: ...

    async def get_run(self, run_id: UUID) -> Optional[FunctionRunEntity]: ...

    async def list_runs_by_function(
        self, function_id: UUID, limit: int = 100, cursor: str | None = None
    ) -> Tuple[list[FunctionRunEntity], str | None]: ...


class WorkspaceSessionPort(Protocol):
    async def get_session(
        self,
        user_id: UUID,
        pod_id: UUID,
        session_id: str | None = None,
        initial_cwd: str = "/workspace",
        close_on_exit: bool = True,
        workload_type: str | None = None,
        workload_id: UUID | None = None,
        workload_name: str | None = None,
        scope: list[str] | None = None,
        env_vars: dict[str, str] | None = None,
    ): ...


class FunctionStoragePort(Protocol):
    async def read_file(self, path: str): ...

    async def write_file(self, path: str, content: str): ...


class FunctionStorageFactoryPort(Protocol):
    def __call__(self, function_id: UUID) -> FunctionStoragePort: ...


class AccountResolutionPort(Protocol):
    async def resolve_account(
        self,
        *,
        user_id: UUID,
        connector_id: str,
        auth_actor=None,
        account_id: UUID | None = None,
    ): ...
