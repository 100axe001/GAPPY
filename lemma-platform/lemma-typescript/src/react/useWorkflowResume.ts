import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import type { LemmaClient } from "../client.js";
import type { FlowRun, WorkflowRunInputs } from "../types.js";
import { normalizeError, resolvePodId } from "./utils.js";

export interface UseWorkflowResumeOptions {
  client: LemmaClient;
  podId?: string;
  runId?: string | null;
  onRun?: (run: FlowRun) => void;
  onError?: (error: unknown) => void;
}

export interface UseWorkflowResumeResult {
  run: FlowRun | null;
  isResuming: boolean;
  error: Error | null;
  resume: (
    inputs?: WorkflowRunInputs,
    options?: { runId?: string | null; nodeId?: string },
  ) => Promise<FlowRun>;
}

function resolveRunId(base?: string | null, override?: string | null): string {
  const resolved = override ?? base;
  if (!resolved) {
    throw new Error("runId is required.");
  }
  return resolved;
}

export function useWorkflowResume({
  client,
  podId,
  runId,
  onRun,
  onError,
}: UseWorkflowResumeOptions): UseWorkflowResumeResult {
  const [run, setRun] = useState<FlowRun | null>(null);
  const [isResuming, setIsResuming] = useState(false);
  const [error, setError] = useState<Error | null>(null);

  const onRunRef = useRef(onRun);
  const onErrorRef = useRef(onError);

  useEffect(() => { onRunRef.current = onRun; }, [onRun]);
  useEffect(() => { onErrorRef.current = onError; }, [onError]);

  const resume = useCallback(async (
    inputs: WorkflowRunInputs = {},
    options: { runId?: string | null; nodeId?: string } = {},
  ): Promise<FlowRun> => {
    setIsResuming(true);
    setError(null);

    try {
      const resolvedPodId = resolvePodId(client, podId);
      const resolvedRunId = resolveRunId(runId, options.runId);
      let nodeId = options.nodeId;
      if (!nodeId) {
        const current = await client.workflows.runs.get(resolvedRunId, resolvedPodId);
        const wait = current.active_wait;
        if (!wait || wait.wait_type !== "HUMAN") {
          throw new Error("Run is not waiting on a form; pass nodeId explicitly.");
        }
        nodeId = wait.node_id;
      }
      const nextRun = await client.workflows.runs.submitForm(
        resolvedRunId,
        { node_id: nodeId, inputs },
        resolvedPodId,
      );
      setRun(nextRun);
      onRunRef.current?.(nextRun);
      return nextRun;
    } catch (resumeError) {
      const normalized = normalizeError(resumeError, "Failed to resume workflow run.");
      setError(normalized);
      onErrorRef.current?.(resumeError);
      throw normalized;
    } finally {
      setIsResuming(false);
    }
  }, [client, podId, runId]);

  return useMemo(() => ({
    run,
    isResuming,
    error,
    resume,
  }), [error, isResuming, resume, run]);
}
