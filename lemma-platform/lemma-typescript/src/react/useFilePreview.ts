import { useCallback, useEffect, useMemo, useState } from "react";
import type { LemmaClient } from "../client.js";
import { normalizeError, resolvePodClient } from "./utils.js";

/**
 * - `"rendered"` fetches the document's converted markdown (`document.md`) as
 *   text. The server no longer renders HTML — the caller is responsible for
 *   rendering markdown → HTML (and resolving inline figure refs to the document's
 *   image child files); see the `lemma-document-workspace` registry block for a
 *   reference renderer.
 * - `"artifact"` fetches a single named child artifact (e.g. an extracted figure
 *   or `pages/page_0001.jpg`) as text/bytes.
 */
export type FilePreviewMode = "rendered" | "artifact";

export interface UseFilePreviewOptions {
  client: LemmaClient;
  podId?: string;
  path?: string | null;
  enabled?: boolean;
  autoLoad?: boolean;
  mode?: FilePreviewMode;
  /** Child artifact path (relative to the document), used when `mode="artifact"`. */
  artifact?: string;
}

export interface UseFilePreviewResult {
  /** Converted markdown text (`mode="rendered"`) or the artifact's text. */
  content: string | null;
  blob: Blob | null;
  isLoading: boolean;
  error: Error | null;
  refresh: (overrides?: {
    path?: string | null;
    mode?: FilePreviewMode;
    artifact?: string;
  }) => Promise<string | null>;
}

export function useFilePreview({
  client,
  podId,
  path = null,
  enabled = true,
  autoLoad = true,
  mode = "rendered",
  artifact = "document.md",
}: UseFilePreviewOptions): UseFilePreviewResult {
  const [content, setContent] = useState<string | null>(null);
  const [blob, setBlob] = useState<Blob | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<Error | null>(null);
  const trimmedPath = typeof path === "string" ? path.trim() : "";
  const isEnabled = enabled && trimmedPath.length > 0;

  const refresh = useCallback(async (
    overrides: {
      path?: string | null;
      mode?: FilePreviewMode;
      artifact?: string;
    } = {},
    signal?: AbortSignal,
  ): Promise<string | null> => {
    const nextPath = typeof overrides.path === "string" ? overrides.path.trim() : trimmedPath;
    const nextMode = overrides.mode ?? mode;
    const nextArtifact = overrides.artifact ?? artifact;
    if (!enabled || nextPath.length === 0) {
      setContent(null);
      setBlob(null);
      setError(null);
      setIsLoading(false);
      return null;
    }

    setIsLoading(true);
    setError(null);

    try {
      const scopedClient = resolvePodClient(client, podId);
      if (nextMode === "artifact") {
        const childPath = nextArtifact ? `${nextPath}/${nextArtifact}` : nextPath;
        const nextBlob = await scopedClient.files.children.content(childPath);
        const text = await nextBlob.text();
        if (signal?.aborted) return null;
        setBlob(nextBlob);
        setContent(text);
        return text;
      }

      const renderedBlob = await scopedClient.files.children.markdown(nextPath);
      const text = await renderedBlob.text();
      if (signal?.aborted) return null;
      setBlob(null);
      setContent(text);
      return text;
    } catch (refreshError) {
      if (signal?.aborted) return null;
      setError(normalizeError(refreshError, "Failed to load file preview."));
      setContent(null);
      setBlob(null);
      return null;
    } finally {
      if (!signal?.aborted) setIsLoading(false);
    }
  }, [artifact, client, enabled, mode, podId, trimmedPath]);

  useEffect(() => {
    if (!isEnabled) {
      setContent(null);
      setBlob(null);
      setError(null);
      setIsLoading(false);
      return;
    }

    if (!autoLoad) return;
    const controller = new AbortController();
    void refresh({}, controller.signal);
    return () => controller.abort();
  }, [autoLoad, isEnabled, refresh]);

  return useMemo(() => ({
    content,
    blob,
    isLoading,
    error,
    refresh,
  }), [blob, content, error, isLoading, refresh]);
}
