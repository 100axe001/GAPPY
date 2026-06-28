from app.modules.workspace.services.workspace_sandbox_service import (
    WorkspaceSandboxService,
)
from uuid import UUID
import asyncio
from app.modules.identity.infrastructure.supertokens_auth.helpers import (
    initialize_supertokens,
)


async def main():
    pod_id = UUID("019c650f-8cf5-74f1-90ca-10b3e1a2c534")
    session_id = str(pod_id)
    user_id = UUID("23d89da5-a204-44bc-94d6-dee41eb576a8")
    workspace_service = WorkspaceSandboxService()
    session = await workspace_service.get_session(
        user_id=user_id, pod_id=pod_id, session_id=session_id, close_on_exit=False
    )
    async with session:
        code = """from lemma_sdk import get_info_client, get_execution_client

app_name = "gmail"  # must be a pod-installed app alias from accessible apps
execution_client = await get_execution_client(app_name)
result =await execution_client.list_messages({})
print(result)
        """
        result = await session.execute_code(code=code)
        print(result)


if __name__ == "__main__":
    initialize_supertokens()
    asyncio.run(main())
