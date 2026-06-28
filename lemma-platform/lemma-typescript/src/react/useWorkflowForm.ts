import { useCallback, useMemo, useState } from "react";
import {
  buildWorkflowFormSubmit,
  getRunInputFields,
} from "../core/workflow/index.js";
import type { SchemaFormField } from "../schema-form.js";
import type { FlowRun } from "../types.js";

// Headless form binding for a workflow run parked on a HUMAN wait. Derives the
// fields from the wait's input_schema, holds the values, and produces the submit
// payload — the app renders the inputs and wires submit to its own
// `useWorkflowRun().resume`. Workflow ships helpers, never a baked-in UI.
export interface UseWorkflowFormOptions {
  run: FlowRun | null | undefined;
  initialValues?: Record<string, unknown>;
  /** Wired to the run's resume; receives the node id and collected inputs. */
  onSubmit?: (payload: { nodeId: string; inputs: Record<string, unknown> }) => void | Promise<void>;
}

export interface UseWorkflowFormResult {
  fields: SchemaFormField[];
  values: Record<string, unknown>;
  setValue: (name: string, value: unknown) => void;
  setValues: (values: Record<string, unknown>) => void;
  reset: () => void;
  isWaitingForInput: boolean;
  nodeId: string | null;
  canSubmit: boolean;
  isSubmitting: boolean;
  error: Error | null;
  submit: () => Promise<void>;
}

export function useWorkflowForm(options: UseWorkflowFormOptions): UseWorkflowFormResult {
  const { run, initialValues, onSubmit } = options;

  const fields = useMemo(() => getRunInputFields(run), [run]);
  const submitTarget = useMemo(() => buildWorkflowFormSubmit(run), [run]);
  const isWaitingForInput = submitTarget !== null;
  const nodeId = submitTarget?.nodeId ?? null;

  const [values, setValuesState] = useState<Record<string, unknown>>(initialValues ?? {});
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState<Error | null>(null);

  const setValue = useCallback((name: string, value: unknown) => {
    setValuesState((previous) => ({ ...previous, [name]: value }));
  }, []);

  const setValues = useCallback((next: Record<string, unknown>) => {
    setValuesState(next);
  }, []);

  const reset = useCallback(() => {
    setValuesState(initialValues ?? {});
    setError(null);
  }, [initialValues]);

  const submit = useCallback(async () => {
    const payload = buildWorkflowFormSubmit(run, values);
    if (!payload) return;
    setIsSubmitting(true);
    setError(null);
    try {
      await onSubmit?.(payload);
    } catch (submitError) {
      const normalized = submitError instanceof Error ? submitError : new Error(String(submitError));
      setError(normalized);
      throw normalized;
    } finally {
      setIsSubmitting(false);
    }
  }, [onSubmit, run, values]);

  return {
    fields,
    values,
    setValue,
    setValues,
    reset,
    isWaitingForInput,
    nodeId,
    canSubmit: isWaitingForInput && !isSubmitting,
    isSubmitting,
    error,
    submit,
  };
}
