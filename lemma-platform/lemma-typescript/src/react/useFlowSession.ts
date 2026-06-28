import { useEffect, useRef, useSyncExternalStore } from "react";
import type { LemmaClient } from "../client.js";
import type { FlowRun, WorkflowRunInputs, WorkflowRunSummary } from "../types.js";
import {
  WorkflowController,
  type WorkflowControllerOptions,
} from "../core/workflow/index.js";

// The run state machine now lives in the framework-agnostic `WorkflowController`
// (src/core/workflow). This hook is a thin React adapter over it via
// `useSyncExternalStore` — same public API, behavior unchanged.
export interface UseFlowSessionOptions {
  client: LemmaClient;
  podId?: string;
  flowName?: string;
  runId?: string | null;
  autoPoll?: boolean;
  pollIntervalMs?: number;
  onRun?: (run: FlowRun) => void;
  onError?: (error: unknown) => void;
}

export interface UseFlowSessionResult {
  runId: string | null;
  run: FlowRun | null;
  status?: string;
  isPolling: boolean;
  error: Error | null;
  setRunId: (runId: string | null) => void;
  start: (options?: {
    flowName?: string;
    /** Submitted to the entry form when the created run waits on one. */
    inputs?: WorkflowRunInputs;
    connect?: boolean;
  }) => Promise<FlowRun>;
  /** Submit the form the run is waiting on (run.active_wait). */
  resume: (options: {
    runId?: string | null;
    nodeId?: string;
    inputs?: WorkflowRunInputs;
    connect?: boolean;
  }) => Promise<FlowRun>;
  refresh: (runId?: string | null) => Promise<FlowRun | null>;
  listHistory: (options?: {
    flowName?: string;
    limit?: number;
    pageToken?: string;
  }) => Promise<WorkflowRunSummary[]>;
  cancel: (runId?: string | null) => Promise<void>;
}

function toControllerOptions(options: UseFlowSessionOptions): WorkflowControllerOptions {
  return {
    client: options.client,
    scope: { podId: options.podId ?? null, flowName: options.flowName ?? null },
    autoPoll: options.autoPoll ?? true,
    pollIntervalMs: options.pollIntervalMs ?? 2000,
    initialRunId: options.runId ?? null,
    onRun: options.onRun,
    onError: options.onError,
  };
}

export function useFlowSession(options: UseFlowSessionOptions): UseFlowSessionResult {
  const { runId: initialRunId = null } = options;

  const controllerRef = useRef<WorkflowController | null>(null);
  if (controllerRef.current === null) {
    controllerRef.current = new WorkflowController(toControllerOptions(options));
  }
  const controller = controllerRef.current;

  // Keep the controller's live options (client/scope/poll/callbacks) current.
  useEffect(() => {
    controller.setOptions(toControllerOptions(options));
  });

  const state = useSyncExternalStore(
    controller.subscribe,
    controller.getState,
    controller.getState,
  );

  // Attach to the controlled runId (also kicks off refresh + polling).
  useEffect(() => {
    if (initialRunId) {
      controller.setRunId(initialRunId);
    }
  }, [controller, initialRunId]);

  // Stop polling and drop listeners on unmount.
  useEffect(() => () => controller.destroy(), [controller]);

  return {
    runId: state.runId,
    run: state.run,
    status: state.status,
    isPolling: state.isPolling,
    error: state.error,
    setRunId: controller.setRunId,
    start: controller.start,
    resume: controller.resume,
    refresh: controller.refresh,
    listHistory: controller.listHistory,
    cancel: controller.cancel,
  };
}
