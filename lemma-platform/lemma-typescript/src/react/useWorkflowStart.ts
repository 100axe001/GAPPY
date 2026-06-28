import { useCallback, useEffect, useMemo, useState } from "react";
import type { LemmaClient } from "../client.js";
import { normalizeRunStatus } from "../run-utils.js";
import type {
  FlowRun,
  FormNodeResponse,
  Workflow,
  WorkflowStartType,
  WorkflowRunInputs,
  WorkflowRunSummary,
} from "../types.js";
import { normalizeError, resolvePodClient } from "./utils.js";
import {
  useFlowSession,
  type UseFlowSessionResult,
} from "./useFlowSession.js";

export interface UseWorkflowStartOptions {
  client: LemmaClient;
  podId?: string;
  workflowName: string;
  runId?: string | null;
  enabled?: boolean;
  autoLoad?: boolean;
  autoPoll?: boolean;
  pollIntervalMs?: number;
  onRun?: (run: FlowRun) => void;
  onError?: (error: unknown) => void;
}

export interface UseWorkflowStartResult
  extends Omit<UseFlowSessionResult, "start" | "listHistory"> {
  workflow: Workflow | null;
  startType: WorkflowStartType | "MANUAL";
  inputSchema: Record<string, unknown> | null;
  inputUiSchema: Record<string, unknown> | null;
  isLoadingWorkflow: boolean;
  isStarting: boolean;
  error: Error | null;
  refreshWorkflow: () => Promise<Workflow | null>;
  listHistory: (options?: { limit?: number; pageToken?: string }) => Promise<WorkflowRunSummary[]>;
  start: (inputs?: WorkflowRunInputs, options?: { forceResume?: boolean }) => Promise<FlowRun>;
}

function findFirstFormNode(workflow: Workflow | null): FormNodeResponse | null {
  if (!workflow?.nodes?.length) return null;

  for (const node of workflow.nodes) {
    if (!node || typeof node !== "object") continue;
    if (!("config" in node) || typeof node.config !== "object" || !node.config) continue;
    if ("input_schema" in node.config) {
      return node as FormNodeResponse;
    }
  }

  return null;
}

function isWaitingOnForm(run: FlowRun | null | undefined): boolean {
  if (!run) return false;
  const normalizedStatus = normalizeRunStatus(run.status);
  return normalizedStatus === "WAITING" && run.active_wait?.wait_type === "HUMAN";
}

export function useWorkflowStart({
  client,
  podId,
  workflowName,
  runId = null,
  enabled = true,
  autoLoad = true,
  autoPoll = true,
  pollIntervalMs = 2000,
  onRun,
  onError,
}: UseWorkflowStartOptions): UseWorkflowStartResult {
  const [workflow, setWorkflow] = useState<Workflow | null>(null);
  const [workflowError, setWorkflowError] = useState<Error | null>(null);
  const [isLoadingWorkflow, setIsLoadingWorkflow] = useState(false);
  const [isStarting, setIsStarting] = useState(false);
  const hasWorkflowName = workflowName.trim().length > 0;
  const isEnabled = enabled && hasWorkflowName;

  const session = useFlowSession({
    client,
    podId,
    flowName: workflowName,
    runId,
    autoPoll,
    pollIntervalMs,
    onRun,
    onError,
  });

  const refreshWorkflow = useCallback(async (): Promise<Workflow | null> => {
    if (!isEnabled) {
      setWorkflow(null);
      setWorkflowError(null);
      setIsLoadingWorkflow(false);
      return null;
    }

    setIsLoadingWorkflow(true);
    setWorkflowError(null);

    try {
      const scopedClient = resolvePodClient(client, podId);
      const nextWorkflow = await scopedClient.workflows.get(workflowName);
      setWorkflow(nextWorkflow);
      return nextWorkflow;
    } catch (refreshError) {
      const normalized = normalizeError(refreshError, "Failed to fetch workflow definition.");
      setWorkflowError(normalized);
      return null;
    } finally {
      setIsLoadingWorkflow(false);
    }
  }, [client, isEnabled, podId, workflowName]);

  useEffect(() => {
    if (!isEnabled) {
      setWorkflow(null);
      setWorkflowError(null);
      setIsLoadingWorkflow(false);
      return;
    }

    if (!autoLoad) return;
    void refreshWorkflow();
  }, [autoLoad, isEnabled, refreshWorkflow]);

  const listHistory = useCallback((options: { limit?: number; pageToken?: string } = {}) => {
    return session.listHistory({
      flowName: workflowName,
      limit: options.limit,
      pageToken: options.pageToken,
    });
  }, [session, workflowName]);

  const start = useCallback(async (
    inputs: WorkflowRunInputs = {},
    options: { forceResume?: boolean } = {},
  ): Promise<FlowRun> => {
    if (!hasWorkflowName) {
      const missingWorkflowError = new Error("workflowName is required.");
      setWorkflowError(missingWorkflowError);
      throw missingWorkflowError;
    }

    setIsStarting(true);
    setWorkflowError(null);

    try {
      // Runs take no start inputs; session.start submits `inputs` to the
      // entry form when the created run waits on one.
      const created = await session.start({
        flowName: workflowName,
        inputs,
      });

      if (
        options.forceResume === true
        && created.id
        && isWaitingOnForm(created)
      ) {
        return session.resume({ runId: created.id, inputs });
      }

      return created;
    } catch (startError) {
      const normalized = normalizeError(startError, "Failed to start workflow.");
      setWorkflowError(normalized);
      throw normalized;
    } finally {
      setIsStarting(false);
    }
  }, [hasWorkflowName, refreshWorkflow, session, workflow, workflowName]);

  return useMemo(() => {
    const formNode = findFirstFormNode(workflow);
    const startType = workflow?.start?.type ?? "MANUAL";
    const error = workflowError ?? session.error;

    return {
      ...session,
      workflow,
      startType,
      inputSchema: formNode?.config.input_schema ?? null,
      inputUiSchema: formNode?.config.ui_schema ?? null,
      isLoadingWorkflow,
      isStarting,
      error,
      refreshWorkflow,
      listHistory,
      start,
    };
  }, [isStarting, isLoadingWorkflow, listHistory, refreshWorkflow, session, start, workflow, workflowError]);
}
