import { useEffect, useRef, useState } from "react";
import type { LemmaClient } from "../client.js";
import type { ChangeStreamStatus, DatastoreChangeFrame } from "../datastore-changes.js";
import { resolvePodClient } from "./utils.js";

export interface UseWatchChangesOptions {
  client: LemmaClient;
  podId?: string;
  /** Restrict to one table; omit to watch every readable table in the pod. */
  table?: string;
  /** Invoked for every record change frame (insert / update / delete). */
  onChange: (frame: DatastoreChangeFrame) => void;
  /** Connection lifecycle notifications. */
  onStatus?: (status: ChangeStreamStatus) => void;
  /** Terminal errors (e.g. auth failed, max retries reached). */
  onError?: (error: Error) => void;
  /** Stop watching when `false` (default `true`). */
  enabled?: boolean;
  /** Rely on a same-site session cookie instead of a token in the URL. */
  useCookie?: boolean;
  /** Cap reconnect attempts; unlimited by default. */
  maxRetries?: number;
}

export interface UseWatchChangesResult {
  /** Current connection status of the change stream. */
  status: ChangeStreamStatus;
}

/**
 * Subscribe to the pod's live datastore change stream for the lifetime of a component.
 *
 * This is the thin, correct lifecycle wrapper around `client.datastore.watchChanges`:
 * it opens **one** WebSocket and tears it down on unmount. Callbacks are held in refs,
 * so passing a fresh inline `onChange` on every render does **not** resubscribe — the
 * stream stays open and keeps its resume cursor. (That resubscribe-every-render bug is
 * the usual reason a hand-rolled `useEffect` flickers or drops events.)
 *
 * Do not poll for fresh data — subscribe with this (or `useLiveRecords`) instead.
 *
 * ```tsx
 * useWatchChanges({ client, table: "tickets", onChange: (f) => mergeIntoState(f) });
 * ```
 */
export function useWatchChanges({
  client,
  podId,
  table,
  onChange,
  onStatus,
  onError,
  enabled = true,
  useCookie,
  maxRetries,
}: UseWatchChangesOptions): UseWatchChangesResult {
  const [status, setStatus] = useState<ChangeStreamStatus>("closed");

  // Latest callbacks in refs: a new callback identity must not tear down the socket.
  const onChangeRef = useRef(onChange);
  const onStatusRef = useRef(onStatus);
  const onErrorRef = useRef(onError);
  onChangeRef.current = onChange;
  onStatusRef.current = onStatus;
  onErrorRef.current = onError;

  useEffect(() => {
    if (!enabled) {
      setStatus("closed");
      return;
    }

    const scoped = resolvePodClient(client, podId);
    const handle = scoped.datastore.watchChanges({
      table,
      useCookie,
      maxRetries,
      onChange: (frame) => onChangeRef.current(frame),
      onStatus: (next) => {
        setStatus(next);
        onStatusRef.current?.(next);
      },
      onError: (error) => onErrorRef.current?.(error),
    });

    return () => handle.close();
    // Resubscribe only when the connection identity changes — never on a new callback.
  }, [client, podId, table, enabled, useCookie, maxRetries]);

  return { status };
}
