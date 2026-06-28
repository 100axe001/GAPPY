import { useCallback, useEffect, useMemo, useState } from "react";
import type { LemmaClient } from "../client.js";
import type { JsonSchemaLike } from "../schema-form.js";
import type { Agent } from "../types.js";
import { normalizeError, resolvePodClient } from "./utils.js";

export interface UseAgentInputSchemaOptions {
  client: LemmaClient;
  podId?: string;
  agentName: string;
  enabled?: boolean;
  autoLoad?: boolean;
}

export interface UseAgentInputSchemaResult {
  agent: Agent | null;
  inputSchema: JsonSchemaLike | null;
  outputSchema: JsonSchemaLike | null;
  isLoading: boolean;
  error: Error | null;
  refresh: () => Promise<Agent | null>;
}

export function useAgentInputSchema({
  client,
  podId,
  agentName,
  enabled = true,
  autoLoad = true,
}: UseAgentInputSchemaOptions): UseAgentInputSchemaResult {
  const [agent, setAgent] = useState<Agent | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<Error | null>(null);

  const trimmedAgentName = agentName.trim();
  const isEnabled = enabled && trimmedAgentName.length > 0;

  const refresh = useCallback(async (signal?: AbortSignal): Promise<Agent | null> => {
    if (!isEnabled) {
      setAgent(null);
      setError(null);
      setIsLoading(false);
      return null;
    }

    setIsLoading(true);
    setError(null);

    try {
      const scopedClient = resolvePodClient(client, podId);
      const nextAgent = await scopedClient.agents.get(trimmedAgentName);
      if (signal?.aborted) return null;
      setAgent(nextAgent);
      return nextAgent;
    } catch (refreshError) {
      if (signal?.aborted) return null;
      const normalized = normalizeError(refreshError, "Failed to load agent schema.");
      setError(normalized);
      setAgent(null);
      return null;
    } finally {
      if (!signal?.aborted) setIsLoading(false);
    }
  }, [client, isEnabled, podId, trimmedAgentName]);

  useEffect(() => {
    if (!isEnabled) {
      setAgent(null);
      setError(null);
      setIsLoading(false);
      return;
    }

    if (!autoLoad) return;
    const controller = new AbortController();
    let cancelled = false;
    (async () => {
      try {
        await refresh(controller.signal);
      } catch {
        if (!cancelled) {
          setError(normalizeError(new Error("Failed to load agent schema."), "Failed to load agent schema."));
        }
      }
    })();
    return () => {
      cancelled = true;
      controller.abort();
    };
  }, [autoLoad, isEnabled, refresh]);

  return useMemo(() => ({
    agent,
    inputSchema: (agent?.input_schema ?? null) as JsonSchemaLike | null,
    outputSchema: (agent?.output_schema ?? null) as JsonSchemaLike | null,
    isLoading,
    error,
    refresh,
  }), [agent, error, isLoading, refresh]);
}
