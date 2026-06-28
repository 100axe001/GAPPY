from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import PurePosixPath
from typing import Any

from app.core.domain.errors import DomainError
from app.core.log.log import get_logger
from app.modules.agent.tools.context import BaseAgentContext
from app.modules.agent.tools.file_access import (
    read_pod_file_bytes,
    read_workspace_file_bytes,
)
from app.modules.agent.tools.tool_errors import approval_error_result
from app.modules.agent.tools.workspace_cli.models import (
    ApplyPatchRequest,
    ExecCommandRequest,
    ExecCommandResult,
    ExecutePythonRequest,
    ListProcessesRequest,
    ListProcessesResult,
    ProcessInfo,
    TerminateProcessRequest,
    UpdatePlanRequest,
    UpdatePlanResult,
    ViewImageRequest,
    ViewImageResponse,
    WriteStdinRequest,
)
from app.modules.agent.tools.workspace_cli.helper import trim_python_result
from app.modules.agent.tools.workspace_entities import PythonExecutionResult
from app.modules.workspace.services.workspace_tool_runtime import (
    get_workspace_tool_runtime,
)
from app.core.file_editor.file_editor import apply_edits
from pydantic_ai import ToolReturn, BinaryContent
import mimetypes

logger = get_logger(__name__)
_DEFAULT_EXEC_YIELD_TIME_MS = 30000
_DEFAULT_EXEC_TIMEOUT_S = 60
# Conservative per-image ceiling: Anthropic caps an image source at ~5 MB, and
# other providers are similar. Over this, ask the agent to downscale first rather
# than letting the provider reject the request mid-run.
MAX_VIEW_IMAGE_BYTES = 5 * 1024 * 1024


@dataclass(frozen=True)
class WorkspaceRuntimeContext:
    default_shell_session_id: str
    default_python_session_id: str
    initial_cwd: str
    scope_key: str


def workspace_runtime_context(ctx: BaseAgentContext) -> WorkspaceRuntimeContext:
    conversation_key = ctx.conversation_id.hex
    return WorkspaceRuntimeContext(
        default_shell_session_id=f"shell-{conversation_key}",
        default_python_session_id=f"python-{conversation_key}",
        initial_cwd=ctx.get_workspace_cwd(),
        scope_key=ctx.get_workspace_scope_key(),
    )


def _workspace_tool_failure(
    exc: Exception,
    *,
    operation: str,
    completed: bool = False,
    process_id: str | None = None,
) -> ExecCommandResult:
    logger.warning("Workspace CLI %s failed: %s", operation, exc, exc_info=True)
    return ExecCommandResult(
        success=False,
        stdout="",
        stderr="",
        exit_code=None,
        completed=completed,
        process_id=process_id,
        error=(
            f"Workspace {operation} failed before the tool could complete: "
            f"{type(exc).__name__}: {exc}. "
            "Treat this as a recoverable tool failure and retry if the operation "
            "is still needed."
        ),
    )


def _python_workspace_tool_failure(exc: Exception, *, operation: str) -> PythonExecutionResult:
    logger.warning("Workspace CLI %s failed: %s", operation, exc, exc_info=True)
    return PythonExecutionResult(
        success=False,
        stdout="",
        stderr="",
        result=None,
        error_in_exec={
            "ename": "WorkspaceToolError",
            "evalue": (
                f"Workspace {operation} failed before Python execution completed: "
                f"{type(exc).__name__}: {exc}. "
                "Treat this as a recoverable tool failure and retry if the operation "
                "is still needed."
            ),
            "traceback": [],
        },
    )


async def _get_workspace_session(
    ctx: BaseAgentContext,
    *,
    session_id: str | None,
    close_on_exit: bool,
):
    runtime_context = workspace_runtime_context(ctx)
    runtime = get_workspace_tool_runtime()
    return await runtime.get_session(
        user_id=ctx.user_id,
        pod_id=ctx.pod_id,
        organization_id=ctx.organization_id,
        workload_type=ctx.workload_type,
        workload_id=ctx.workload_id,
        workload_name=ctx.agent_name,
        scope_key=runtime_context.scope_key,
        session_id=session_id,
        initial_cwd=runtime_context.initial_cwd,
        close_on_exit=close_on_exit,
    )


async def exec_command_internal(
    ctx: BaseAgentContext,
    request: ExecCommandRequest,
) -> ExecCommandResult:
    try:
        runtime = get_workspace_tool_runtime()
        runtime_context = workspace_runtime_context(ctx)

        workspace_session = await _get_workspace_session(
            ctx,
            session_id=runtime_context.default_shell_session_id,
            close_on_exit=False,
        )
        async with workspace_session:
            if request.tty:
                effective_yield_time_ms = request.yield_time_ms
                effective_timeout = _DEFAULT_EXEC_TIMEOUT_S
            elif request.timeout_seconds is not None:
                # Explicit blocking: no yield window, wait until done
                effective_yield_time_ms = None
                effective_timeout = request.timeout_seconds
            else:
                effective_yield_time_ms = (
                    request.yield_time_ms
                    if request.yield_time_ms is not None
                    else _DEFAULT_EXEC_YIELD_TIME_MS
                )
                effective_timeout = _DEFAULT_EXEC_TIMEOUT_S
            result = await workspace_session.exec_command(
                cmd=request.cmd,
                max_output_tokens=request.max_output_tokens,
                tty=request.tty,
                workdir=request.workdir,
                yield_time_ms=effective_yield_time_ms,
                timeout=effective_timeout,
            )
            completed = bool(result.get("completed", True))
            process_id = result.get("process_id")
            if process_id and workspace_session.session_id and not completed:
                await runtime.bind_process_to_session(
                    process_id=process_id,
                    session_id=workspace_session.session_id,
                )
        return ExecCommandResult(
            success=bool(result.get("success")),
            stdout=result.get("stdout"),
            stderr=result.get("stderr"),
            exit_code=result.get("exit_code"),
            completed=completed,
            process_id=process_id if not completed else None,
            error=result.get("error"),
        )
    except Exception as exc:
        return _workspace_tool_failure(
            exc,
            operation="exec_command",
        )


async def write_stdin_internal(
    ctx: BaseAgentContext,
    request: WriteStdinRequest,
) -> ExecCommandResult:
    try:
        runtime = get_workspace_tool_runtime()
        runtime_context = workspace_runtime_context(ctx)
        resolved_session_id = (
            await runtime.resolve_session_for_process(request.process_id)
            or runtime_context.default_shell_session_id
        )
        workspace_session = await _get_workspace_session(
            ctx,
            session_id=resolved_session_id,
            close_on_exit=False,
        )
        async with workspace_session:
            result = await workspace_session.write_stdin(
                process_id=request.process_id,
                chars=request.chars,
                max_output_tokens=request.max_output_tokens,
                yield_time_ms=request.yield_time_ms,
            )
        completed = bool(result.get("completed", True))
        if completed:
            await runtime.clear_process_binding(request.process_id)
        elif result.get("process_id") and workspace_session.session_id:
            await runtime.bind_process_to_session(
                process_id=str(result["process_id"]),
                session_id=workspace_session.session_id,
            )
        return ExecCommandResult(
            success=bool(result.get("success")),
            stdout=result.get("stdout"),
            stderr=result.get("stderr"),
            exit_code=result.get("exit_code"),
            completed=completed,
            process_id=result.get("process_id"),
            error=result.get("error"),
        )
    except Exception as exc:
        return _workspace_tool_failure(
            exc,
            operation="write_stdin",
            process_id=request.process_id,
        )


async def terminate_process_internal(
    ctx: BaseAgentContext,
    request: TerminateProcessRequest,
) -> ExecCommandResult:
    try:
        runtime = get_workspace_tool_runtime()
        runtime_context = workspace_runtime_context(ctx)
        resolved_session_id = (
            await runtime.resolve_session_for_process(request.process_id)
            or runtime_context.default_shell_session_id
        )
        workspace_session = await _get_workspace_session(
            ctx,
            session_id=resolved_session_id,
            close_on_exit=False,
        )
        async with workspace_session:
            result = await workspace_session.terminate_process(request.process_id)
        await runtime.clear_process_binding(request.process_id)
        return ExecCommandResult(
            success=bool(result.get("success")),
            stdout=result.get("stdout"),
            stderr=result.get("stderr"),
            exit_code=result.get("exit_code"),
            completed=bool(result.get("completed", True)),
            process_id=result.get("process_id"),
            error=result.get("error"),
        )
    except Exception as exc:
        return _workspace_tool_failure(
            exc,
            operation="terminate_process",
            process_id=request.process_id,
        )


async def list_processes_internal(
    ctx: BaseAgentContext,
    request: ListProcessesRequest,
) -> ListProcessesResult:
    del request
    try:
        runtime = get_workspace_tool_runtime()
        runtime_context = workspace_runtime_context(ctx)
        workspace_session = await _get_workspace_session(
            ctx,
            session_id=runtime_context.default_shell_session_id,
            close_on_exit=False,
        )
        async with workspace_session:
            processes = await workspace_session.list_processes()
        for process in processes:
            if not process.get("completed") and workspace_session.session_id:
                await runtime.bind_process_to_session(
                    process_id=str(process["process_id"]),
                    session_id=workspace_session.session_id,
                )
        return ListProcessesResult(
            success=True,
            processes=[ProcessInfo.model_validate(process) for process in processes],
        )
    except Exception as exc:
        logger.warning("Workspace CLI list_processes failed: %s", exc, exc_info=True)
        return ListProcessesResult(
            success=False,
            processes=[],
            error=(
                f"Workspace list_processes failed before the tool could complete: "
                f"{type(exc).__name__}: {exc}. Treat this as a recoverable tool "
                "failure and retry if the operation is still needed."
            ),
        )


async def execute_python_internal(ctx: BaseAgentContext, request: ExecutePythonRequest):
    try:
        workspace_session = await _get_workspace_session(
            ctx,
            session_id=workspace_runtime_context(ctx).default_python_session_id,
            close_on_exit=False,
        )
        async with workspace_session:
            result = await workspace_session.execute_code(
                request.code, request.timeout_seconds
            )
        return trim_python_result(result)
    except Exception as exc:
        return _python_workspace_tool_failure(exc, operation="execute_python")


async def update_plan_internal(
    ctx: BaseAgentContext,
    request: UpdatePlanRequest,
) -> UpdatePlanResult:
    timestamp = datetime.now(timezone.utc).isoformat()
    lines = ["# Task Plan", "", f"- Updated: `{timestamp}`", ""]
    if request.comment:
        lines.extend(["## Explanation", request.comment.strip(), ""])
    lines.append("## Steps")
    lines.append("")
    for item in request.plan:
        marker = "x" if item.status == "completed" else " "
        lines.append(f"- [{marker}] `{item.status}` {item.step}")
    content = "\n".join(lines) + "\n"
    await ctx.file_manager.write_file("plan.md", content)
    return UpdatePlanResult(success=True, file_path="plan.md", content=content)


def _validate_patch_path(path: str) -> str:
    cleaned = path.strip()
    if not cleaned:
        raise ValueError("Patch path cannot be empty")
    if cleaned.startswith("/"):
        raise ValueError(f"Absolute paths are not allowed in patch: {cleaned}")
    pure = PurePosixPath(cleaned)
    if ".." in pure.parts:
        raise ValueError(f"Parent path traversal is not allowed in patch: {cleaned}")
    return cleaned


def _parse_apply_patch_blocks(
    patch_text: str,
) -> list[tuple[str, str, str, str | None]]:
    lines = patch_text.splitlines()
    if not lines or lines[0].strip() != "*** Begin Patch":
        raise ValueError("Patch must start with '*** Begin Patch'")
    if lines[-1].strip() != "*** End Patch":
        raise ValueError("Patch must end with '*** End Patch'")

    blocks: list[list[str]] = []
    current: list[str] = []
    for line in lines[1:-1]:
        if (
            line.startswith("*** Add File: ")
            or line.startswith("*** Update File: ")
            or line.startswith("*** Delete File: ")
        ):
            if current:
                blocks.append(current)
            current = [line]
        else:
            current.append(line)
    if current:
        blocks.append(current)

    parsed: list[tuple[str, str, str, str | None]] = []
    for block in blocks:
        header = block[0]
        if header.startswith("*** Add File: "):
            path = _validate_patch_path(header[len("*** Add File: ") :])
            content_lines = [ln[1:] for ln in block[1:] if ln.startswith("+")]
            parsed.append(
                (
                    "add",
                    path,
                    "\n".join(content_lines) + ("\n" if content_lines else ""),
                    None,
                )
            )
            continue
        if header.startswith("*** Delete File: "):
            path = _validate_patch_path(header[len("*** Delete File: ") :])
            parsed.append(("delete", path, "", None))
            continue
        if header.startswith("*** Update File: "):
            path = _validate_patch_path(header[len("*** Update File: ") :])
            move_to: str | None = None
            body_lines = block[1:]
            if body_lines and body_lines[0].startswith("*** Move to: "):
                move_to = _validate_patch_path(body_lines[0][len("*** Move to: ") :])
                body_lines = body_lines[1:]
            parsed.append(("update", path, "\n".join(body_lines), move_to))
            continue
        raise ValueError(f"Unsupported block header: {header}")
    return parsed


def _split_hunks(update_content: str) -> list[list[str]]:
    hunks: list[list[str]] = []
    current: list[str] = []
    for line in update_content.splitlines():
        if line.startswith("@@"):
            if current:
                hunks.append(current)
            current = []
            continue
        if line.startswith("***"):
            continue
        if line[:1] in {" ", "-", "+"}:
            current.append(line)
    if current:
        hunks.append(current)
    return hunks


async def apply_patch_internal(
    ctx: BaseAgentContext, request: ApplyPatchRequest
) -> ExecCommandResult:
    try:
        blocks = _parse_apply_patch_blocks(request.patch)
        for kind, file_path, payload, move_to in blocks:
            if kind == "add":
                await ctx.file_manager.write_file(file_path, payload)
                continue

            if kind == "delete":
                await ctx.file_manager.delete_file(file_path)
                continue

            existing = await ctx.file_manager.read_file(file_path)
            if isinstance(existing, bytes):
                return ExecCommandResult(
                    success=False, error=f"Cannot patch binary file: {file_path}"
                )

            updated = existing
            for hunk in _split_hunks(payload):
                search = "".join(
                    f"{line[1:]}\n" for line in hunk if line[0] in {" ", "-"}
                )
                replace = "".join(
                    f"{line[1:]}\n" for line in hunk if line[0] in {" ", "+"}
                )
                edit = f"<<<<<<< SEARCH\n{search}=======\n{replace}>>>>>>> REPLACE\n"
                updated = apply_edits(updated, edit)

            target_path = move_to or file_path
            await ctx.file_manager.write_file(target_path, updated)
            if move_to and move_to != file_path:
                await ctx.file_manager.delete_file(file_path)

        return ExecCommandResult(success=True, message="Patch applied successfully")
    except Exception as exc:
        return ExecCommandResult(success=False, error=str(exc))


async def view_image_internal(
    ctx: BaseAgentContext,
    request: ViewImageRequest,
):
    # Require exactly one store path, returning a structured error (never raising)
    # so a wrong call surfaces success=False to the model instead of aborting the
    # run or burning the retry budget. Pick the store the agent explicitly
    # addressed — no path-shape inference.
    pod_path = (request.pod_file_path or "").strip()
    workspace_path = (request.workspace_file_path or "").strip()
    if bool(pod_path) == bool(workspace_path):
        return ViewImageResponse(
            success=False,
            error=(
                "Provide exactly one of `pod_file_path` (datastore) or "
                "`workspace_file_path` (sandbox)."
            ),
        )
    if pod_path:
        file_path = pod_path
        source = "datastore"
    else:
        file_path = workspace_path
        source = "workspace"

    try:
        if source == "datastore":
            content, detected_mime = await read_pod_file_bytes(ctx, file_path)
        else:
            content, detected_mime = await read_workspace_file_bytes(ctx, file_path)
    except DomainError as exc:
        # Datastore reads are grant-checked; surface a missing grant as
        # needs_approval so the agent can request access, like the pod tools.
        return approval_error_result(
            exc, tool_name="view_image", args=request.model_dump()
        )
    except Exception as exc:
        return ExecCommandResult(success=False, error=str(exc))

    media_type = detected_mime or mimetypes.guess_type(file_path)[0]
    if not media_type or not media_type.startswith("image/"):
        if media_type == "application/pdf" or file_path.lower().endswith(".pdf"):
            hint = (
                "This is a PDF, not an image. Use `pod_view_document_pages` to see "
                "pages (layout, tables, figures), or `pod_read_file` with "
                "format='markdown' to read the text."
            )
        else:
            hint = (
                f"This file is not an image (detected type: {media_type or 'unknown'}). "
                "`view_image` only handles image files. For documents, use "
                "`pod_read_file`; for PDFs, `pod_view_document_pages`."
            )
        return ViewImageResponse(
            success=False,
            error=hint,
            file_path=file_path,
            media_type=media_type,
            source=source,
        )

    if len(content) > MAX_VIEW_IMAGE_BYTES:
        return ViewImageResponse(
            success=False,
            error=(
                f"Image is {len(content) // 1024} KB, over the "
                f"{MAX_VIEW_IMAGE_BYTES // (1024 * 1024)} MB limit. Downscale or "
                "compress it first (e.g. with `execute_python` in the workspace) "
                "before viewing."
            ),
            file_path=file_path,
            media_type=media_type,
            source=source,
            size_bytes=len(content),
        )

    return ToolReturn(
        return_value=ViewImageResponse(
            success=True,
            message=f"Successfully read image {file_path}",
            file_path=file_path,
            media_type=media_type,
            source=source,
            size_bytes=len(content),
        ),
        content=[
            BinaryContent(data=content, media_type=media_type),
        ],
    )


async def exec_command(
    ctx: BaseAgentContext,
    request: ExecCommandRequest,
) -> ExecCommandResult:
    """
    Run a shell command in the private conversation workspace.

    Use this for repo inspection, builds, tests, file edits, and Lemma CLI operations.
    The workspace injects Lemma environment variables for the current user/pod, so
    `lemma ...` CLI commands may be used for pod operations.
    Do not use raw localhost probes to diagnose host Lemma API/Auth availability:
    `localhost` is the workspace container, not the host backend.
    The workspace is a sandbox: files created here are not directly visible to the
    user. Upload final deliverables to pod files under `/me/...` with `lemma files
    upload` before presenting or referencing them as user-accessible files.

    Modes:
    - Default (`tty=false`, no `timeout_seconds`): waits up to 30 s for the command to
      complete. Commands finishing within 30 s return `completed: true` with full output.
      Commands still running after 30 s return `completed: false` + `process_id` — use
      `write_stdin` to poll or `terminate_process` to stop.
    - Blocking (`timeout_seconds=N`): waits up to N seconds (max 300). Use this for
      commands known to take longer than 30 s (e.g. large data fetches, slow builds).
      Always returns `completed: true` or kills the process on timeout.
    - Interactive (`tty=true`): starts a real TTY terminal process and returns
      `process_id` immediately for follow-up with `write_stdin`.

    Lemma connector operations tip: pass the payload with `--data`; the default
    output is compact and complete (long bodies fold — add `--full` to expand).
    Use `--output json` only to pipe/save, e.g.:
      `lemma connectors operations execute <auth-config> GMAIL_FETCH_EMAILS --data '{}'`

    Interactive workflow (for long-running servers like `npm run dev`):
    1) Start: `{"cmd":"npm run dev","tty":true,"yield_time_ms":3000}`
    2) Poll:  `{"process_id":"...","chars":"","yield_time_ms":1000}`
    3) Input: `{"process_id":"...","chars":"q\\n"}`
    4) Stop:  `terminate_process` with the same `process_id`

    Use `list_processes` before starting another long-running server or when you
    need to find a process started earlier.

    Editing files via CLI example:
    - Overwrite file:
      `{"cmd":"cat > src/config.json <<'EOF'\\n{\\\"mode\\\":\\\"dev\\\"}\\nEOF"}`
    - Append line:
      `{"cmd":"echo 'export DEBUG=1' >> .env.local"}`
    """
    return await exec_command_internal(ctx, request)


async def write_stdin(
    ctx: BaseAgentContext,
    request: WriteStdinRequest,
) -> ExecCommandResult:
    """
    Send input to an existing interactive terminal session and read incremental output.

    Use only with a `process_id` returned by `exec_command` for an unfinished command.
    Typical uses:
    - Poll logs without typing anything: `chars=""`
    - Respond to prompts / hotkeys: `chars="y\\n"` or `chars="q\\n"`
    - Run another command in the same shell: `chars="npm test\\n"`
    """
    return await write_stdin_internal(ctx, request)


async def terminate_process(
    ctx: BaseAgentContext,
    request: TerminateProcessRequest,
) -> ExecCommandResult:
    """
    Stop a running workspace process by `process_id`.

    Use this for long-running servers, REPLs, watchers, or commands that were
    started accidentally and need to be cleaned up before continuing.
    """
    return await terminate_process_internal(ctx, request)


async def list_processes(
    ctx: BaseAgentContext,
    request: ListProcessesRequest,
) -> ListProcessesResult:
    """
    List tracked shell processes in the current conversation workspace.

    Use this to inspect dev servers, REPLs, or other long-running commands before
    polling them with `write_stdin`, stopping them with `terminate_process`, or
    starting another server.
    """
    return await list_processes_internal(ctx, request)


async def execute_python(
    ctx: BaseAgentContext,
    request: ExecutePythonRequest,
) -> Any:
    """
    Execute Python code in the shared conversation-scoped IPython kernel.

    Use this for structured data analysis, transformations, parsing, and calculations
    that are awkward in pure shell commands. Put the entire code snippet in
    `request.code`. The kernel state persists across calls in the same conversation session.
    Variables, imports, and in-memory objects from earlier executions remain available
    for later executions, so use it for stepwise analysis when helpful.
    Include a short `request.comment` to show the user-facing intent.

    The kernel runs in your conversation working directory, so write to relative
    paths (e.g. `plt.savefig('chart.png')`, `open('data/out.csv', 'w')`) to keep
    files there — avoid `/tmp`. Common data packages (numpy, pandas, matplotlib,
    pillow, openpyxl) are pre-installed; for anything else, install it first with
    `exec_command` (`pip install <package>` — plain pip, not uv), then import it
    here.
    """
    return await execute_python_internal(ctx, request)


async def update_plan(
    ctx: BaseAgentContext,
    request: UpdatePlanRequest,
) -> UpdatePlanResult:
    """
    Write or replace `plan.md` for the current private conversation workspace.

    Use this when the agent should expose a clear execution plan to the user.
    Provide ordered steps in `request.plan` and optionally summarize the reason
    for the latest change in `request.comment`.
    """
    return await update_plan_internal(ctx, request)


async def apply_patch(
    ctx: BaseAgentContext,
    request: ApplyPatchRequest,
) -> ExecCommandResult:
    """
    Apply a Codex-style patch block to private workspace files.

    Input contract:
    - Tool arguments must be a JSON object matching `ApplyPatchRequest`.
    - Put the full patch text in `request.patch`.
    - Do not send raw patch text as top-level args.

    Minimal request object:
    `{"patch":"*** Begin Patch\\n*** Update File: path/to/file.py\\n@@\\n-old\\n+new\\n*** End Patch"}`

    Patch format:
    - Must start with `*** Begin Patch`
    - Must end with `*** End Patch`
    - Include one or more file operation blocks

    Supported file operation blocks:
    - `*** Add File: <path>`
    - `*** Update File: <path>`
    - `*** Delete File: <path>`
    - optional after update header: `*** Move to: <new-path>`

    Path constraints:
    - Paths must be relative to workspace
    - Absolute paths are rejected
    - Parent traversal (`..`) is rejected

    Update hunk rules:
    - Use `@@` to start a hunk
    - In hunk lines, use:
      - ` ` (space) for context
      - `-` for removed lines
      - `+` for added lines

    Example:
    `{"patch":"*** Begin Patch\\n*** Add File: notes/todo.txt\\n+first\\n*** Update File: src/main.py\\n@@\\n-print('old')\\n+print('new')\\n*** End Patch"}`

    Use this when precise multi-file edits are needed and shell text manipulation
    would be brittle.
    """
    return await apply_patch_internal(ctx, request)


async def view_image(
    ctx: BaseAgentContext,
    request: ViewImageRequest,
) -> Any:
    """
    Load an image file and return it as binary content so you can see it.

    Use this for screenshots, photos, generated images, charts, or any other
    image the agent should inspect. Reads from EITHER store — set exactly one of:
    - `workspace_file_path`: an image in the conversation workspace sandbox, e.g.
      `images/output.png` (relative) or `/workspace/...` — for artifacts you just
      produced.
    - `pod_file_path`: an image in the pod datastore, e.g. `/me/photo.jpg` — for
      user-uploaded or ingested images. Find paths with `pod_list_files` or
      `pod_search_files`.

    Only image files are supported. For a PDF, use `pod_view_document_pages` to
    see pages or `pod_read_file` (format='markdown') to read text. Very large
    images are rejected — downscale them first.
    """
    return await view_image_internal(ctx, request)
