import { useCallback, useEffect, useMemo, useState } from "react";
import type { JsonSchemaLike, SchemaFormField } from "../schema-form.js";
import {
  buildSchemaFormFields,
  buildSchemaFormPayload,
  buildSchemaFormValues,
} from "../schema-form.js";
import { normalizeError, stringifyComparable } from "./utils.js";

export interface UseSchemaFormOptions {
  schema?: JsonSchemaLike | null;
  uiSchema?: Record<string, unknown> | null;
  initialValues?: Record<string, unknown>;
  enabled?: boolean;
  onSubmit?: (data: Record<string, unknown>) => Promise<unknown> | unknown;
  onError?: (error: unknown) => void;
}

export interface UseSchemaFormResult {
  fields: SchemaFormField[];
  values: Record<string, unknown>;
  baselineValues: Record<string, unknown>;
  fieldErrors: Record<string, string>;
  isSubmitting: boolean;
  isDirty: boolean;
  error: Error | null;
  setValue: (fieldName: string, value: unknown) => void;
  setValues: (values: Record<string, unknown>) => void;
  reset: (nextValues?: Record<string, unknown>) => void;
  validate: () => boolean;
  submit: () => Promise<Record<string, unknown> | null>;
}



const EMPTY_VALUES: Record<string, unknown> = {};

export function useSchemaForm({
  schema = null,
  uiSchema = null,
  initialValues = EMPTY_VALUES,
  enabled = true,
  onSubmit,
  onError,
}: UseSchemaFormOptions): UseSchemaFormResult {
  const [values, setValuesState] = useState<Record<string, unknown>>({});
  const [baselineValues, setBaselineValues] = useState<Record<string, unknown>>({});
  const [fieldErrors, setFieldErrors] = useState<Record<string, string>>({});
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState<Error | null>(null);

  const schemaKey = stringifyComparable(schema);
  const uiSchemaKey = stringifyComparable(uiSchema);
  const initialValuesKey = stringifyComparable(initialValues);
  const stableSchema = useMemo(() => schema, [schemaKey]);
  const stableUiSchema = useMemo(() => uiSchema, [uiSchemaKey]);
  const stableInitialValues = useMemo(() => initialValues, [initialValuesKey]);

  const fields = useMemo(
    () => buildSchemaFormFields(stableSchema ?? undefined, stableUiSchema ?? undefined),
    [stableSchema, stableUiSchema],
  );

  useEffect(() => {
    if (!enabled) {
      setValuesState({});
      setBaselineValues({});
      setFieldErrors({});
      setError(null);
      setIsSubmitting(false);
      return;
    }

    const nextValues = buildSchemaFormValues(stableSchema ?? undefined, stableInitialValues, stableUiSchema ?? undefined);
    setValuesState(nextValues);
    setBaselineValues(nextValues);
    setFieldErrors({});
  }, [enabled, stableInitialValues, stableSchema, stableUiSchema]);

  const setValue = useCallback((fieldName: string, value: unknown) => {
    setValuesState((current) => ({
      ...current,
      [fieldName]: value,
    }));
    setFieldErrors((current) => {
      if (!(fieldName in current)) return current;
      const next = { ...current };
      delete next[fieldName];
      return next;
    });
  }, []);

  const setValues = useCallback((nextValues: Record<string, unknown>) => {
    setValuesState((current) => ({
      ...current,
      ...nextValues,
    }));
  }, []);

  const reset = useCallback((nextValues?: Record<string, unknown>) => {
    const resolved = buildSchemaFormValues(
      stableSchema ?? undefined,
      nextValues ?? stableInitialValues,
      stableUiSchema ?? undefined,
    );
    setValuesState(resolved);
    setBaselineValues(resolved);
    setFieldErrors({});
    setError(null);
  }, [stableInitialValues, stableSchema, stableUiSchema]);

  const validate = useCallback((): boolean => {
    const result = buildSchemaFormPayload(stableSchema ?? undefined, values, stableUiSchema ?? undefined);
    setFieldErrors(result.errors);
    return result.isValid;
  }, [stableSchema, stableUiSchema, values]);

  const submit = useCallback(async (): Promise<Record<string, unknown> | null> => {
    const result = buildSchemaFormPayload(stableSchema ?? undefined, values, stableUiSchema ?? undefined);
    setFieldErrors(result.errors);

    if (!result.isValid) {
      return null;
    }

    if (!onSubmit) {
      return result.data;
    }

    setIsSubmitting(true);
    setError(null);

    try {
      await onSubmit(result.data);
      setBaselineValues(values);
      return result.data;
    } catch (submitError) {
      const normalized = normalizeError(submitError, "Failed to submit schema form.");
      setError(normalized);
      onError?.(submitError);
      return null;
    } finally {
      setIsSubmitting(false);
    }
  }, [onError, onSubmit, stableSchema, stableUiSchema, values]);

  const isDirty = useMemo(
    () => stringifyComparable(values) !== stringifyComparable(baselineValues),
    [baselineValues, values],
  );

  return useMemo(() => ({
    fields,
    values,
    baselineValues,
    fieldErrors,
    isSubmitting,
    isDirty,
    error,
    setValue,
    setValues,
    reset,
    validate,
    submit,
  }), [baselineValues, error, fieldErrors, fields, isDirty, isSubmitting, reset, setValue, setValues, submit, validate, values]);
}
