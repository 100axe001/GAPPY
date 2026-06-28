"use client";

// A pending FORM display-resource rendered as a progressive panel over the
// composer: one question at a time, with the right control per field type. On the
// final step it submits the collected answers back to the assistant as a message
// (the same payload the standalone forms/view page sends). Optional fields can be
// skipped; required fields gate Next/Submit.

import { useCallback, useMemo, useState } from "react";
import { ArrowLeft, CheckCircle2, X } from "lucide-react";

import { Button } from "@/components/ui/button";
import { FieldControl } from "./form-field-control";
import {
    asRecord,
    asString,
    coerceFormValues,
    formatSubmittedFormMessage,
    humanizeLabel,
    isFieldEmpty,
    schemaProperties,
    schemaRequired,
    buildInitialValues,
    type FormValues,
} from "@/lib/assistant/form-schema";
import type { DisplayResourceRequest } from "@/lib/assistant/display-resource";

export function ConversationFormPanel({
    request,
    disabled,
    onSubmit,
    onDismiss,
}: {
    request: DisplayResourceRequest;
    disabled?: boolean;
    onSubmit: (message: string) => Promise<void>;
    onDismiss: () => void;
}) {
    const schema = useMemo(() => request.jsonSchema || {}, [request.jsonSchema]);
    const entries = useMemo(() => Object.entries(schemaProperties(schema)), [schema]);
    const required = useMemo(() => new Set(schemaRequired(schema)), [schema]);
    const title = humanizeLabel(request.name || asString(schema.title), "Input Request");
    const description = asString(schema.description);

    const [values, setValues] = useState<FormValues>(() => buildInitialValues(schema));
    const [step, setStep] = useState(0);
    const [error, setError] = useState<string | null>(null);
    const [isSubmitting, setIsSubmitting] = useState(false);

    const total = entries.length;
    const safeStep = Math.min(step, Math.max(0, total - 1));
    const [currentName, rawField] = entries[safeStep] || ["", {}];
    const field = asRecord(rawField);
    const isRequired = required.has(currentName);
    const isLast = safeStep >= total - 1;

    const updateValue = useCallback((name: string, value: unknown) => {
        setValues((prev) => ({ ...prev, [name]: value }));
        setError(null);
    }, []);

    const stepIsValid = !isRequired || asRecord(field).type === "boolean" || !isFieldEmpty(values[currentName]);

    const goNext = useCallback(() => {
        if (!stepIsValid) {
            setError("This field is required.");
            return;
        }
        setError(null);
        setStep((prev) => Math.min(prev + 1, total - 1));
    }, [stepIsValid, total]);

    const goBack = useCallback(() => {
        setError(null);
        setStep((prev) => Math.max(prev - 1, 0));
    }, []);

    const handleSubmit = useCallback(async () => {
        if (!stepIsValid) {
            setError("This field is required.");
            return;
        }
        // Validate every required field, not just the last visited one.
        const missing = Array.from(required).find((name) => {
            const def = asRecord(schemaProperties(schema)[name]);
            return def.type !== "boolean" && isFieldEmpty(values[name]);
        });
        if (missing) {
            const missingIndex = entries.findIndex(([name]) => name === missing);
            if (missingIndex >= 0) setStep(missingIndex);
            setError(`${humanizeLabel(asString(asRecord(schemaProperties(schema)[missing]).title), missing)} is required.`);
            return;
        }

        setIsSubmitting(true);
        setError(null);
        try {
            await onSubmit(formatSubmittedFormMessage({ request, values: coerceFormValues(values, schema) }));
        } catch {
            setIsSubmitting(false);
            setError("Could not submit. Please try again.");
        }
    }, [entries, onSubmit, request, required, schema, stepIsValid, values]);

    if (total === 0) return null;

    return (
        <div className="lemma-assistant-user-approval-card flex min-h-[clamp(240px,40vh,440px)] flex-col border border-[color:color-mix(in_srgb,var(--row-border)_86%,transparent)] bg-[color:color-mix(in_srgb,var(--surface-1)_96%,transparent)] p-5 shadow-[var(--shadow-sm)]">
            <div className="flex items-start justify-between gap-3">
                <div className="min-w-0">
                    <div className="text-sm font-medium text-[var(--text-primary)]">{title}</div>
                    <p className="mt-0.5 text-xs leading-relaxed text-[var(--text-secondary)]">
                        {description || "Fill this in so the agent can continue."}
                    </p>
                </div>
                <button
                    type="button"
                    onClick={onDismiss}
                    className="flex size-7 shrink-0 items-center justify-center rounded-md text-[var(--text-tertiary)] transition-colors hover:bg-[var(--surface-2)] hover:text-[var(--text-primary)] focus-ring"
                    aria-label="Dismiss form and type instead"
                    title="Dismiss and type instead"
                >
                    <X className="size-4" />
                </button>
            </div>

            <div className="flex min-h-0 flex-1 flex-col justify-center py-5">
                <FieldControl
                    key={currentName}
                    name={currentName}
                    field={field}
                    value={values[currentName]}
                    autoFocus
                    onChange={(value) => updateValue(currentName, value)}
                />
                {error ? <p className="mt-2 text-xs font-medium text-[var(--state-error)]">{error}</p> : null}
            </div>

            <div className="flex items-center justify-between gap-3">
                <div className="flex items-center gap-2 text-xs text-[var(--text-tertiary)]">
                    <span>{`Question ${safeStep + 1} of ${total}`}</span>
                    {isRequired ? <span className="text-[var(--text-secondary)]">· required</span> : <span>· optional</span>}
                </div>
                <div className="flex items-center gap-2">
                    {safeStep > 0 ? (
                        <Button
                            type="button"
                            variant="ghost"
                            size="sm"
                            onClick={goBack}
                            disabled={isSubmitting}
                            className="h-9 px-3 text-sm"
                        >
                            <ArrowLeft className="size-3.5" />
                            Back
                        </Button>
                    ) : null}
                    {isLast ? (
                        <Button
                            type="button"
                            variant="primary"
                            size="sm"
                            onClick={() => { void handleSubmit(); }}
                            disabled={disabled || isSubmitting}
                            className="h-9 px-4 text-sm"
                        >
                            {isSubmitting ? (
                                "Submitting..."
                            ) : (
                                <>
                                    <CheckCircle2 className="size-3.5" />
                                    Submit
                                </>
                            )}
                        </Button>
                    ) : (
                        <Button
                            type="button"
                            variant="primary"
                            size="sm"
                            onClick={goNext}
                            disabled={isSubmitting}
                            className="h-9 px-4 text-sm"
                        >
                            Next
                        </Button>
                    )}
                </div>
            </div>
        </div>
    );
}
