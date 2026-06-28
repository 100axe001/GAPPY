'use client';

import { use, useCallback, useEffect, useMemo, useRef, useState } from 'react';
import { useSearchParams } from 'next/navigation';
import { useQuery } from '@tanstack/react-query';
import { CheckCircle2, Loader2 } from 'lucide-react';

import { Button } from '@/components/ui/button';
import { getLemmaClient } from '@/lib/sdk/lemma-client';
import type { Message as RawConversationMessage } from '@/lib/types';
import { useAIAssistant } from '@/components/ai/ai-assistant-context';
import { findDisplayResourceInMessages } from '@/lib/assistant/display-resource';
import { FieldControl } from '@/components/lemma/assistant/form-field-control';
import {
    asRecord,
    asString,
    buildInitialValues,
    coerceFormValues,
    formatSubmittedFormMessage,
    humanizeLabel,
    schemaProperties,
    schemaRequired,
    validate,
    type FormErrors,
    type FormValues,
} from '@/lib/assistant/form-schema';

export default function DisplayResourceFormPage({
    params,
}: {
    params: Promise<{ id: string }>;
}) {
    const { id: podId } = use(params);
    const searchParams = useSearchParams();
    const conversationId = searchParams.get('assistantConversationId') || searchParams.get('conversationId');
    const toolCallId = searchParams.get('toolCallId');
    const assistant = useAIAssistant();
    const initializedAssistantConversationRef = useRef<string | null>(null);
    const [values, setValues] = useState<FormValues>({});
    const [errors, setErrors] = useState<FormErrors>({});
    const [submitted, setSubmitted] = useState(false);
    const [isSubmitting, setIsSubmitting] = useState(false);

    const query = useQuery({
        queryKey: ['display-resource-form', podId, conversationId, toolCallId],
        queryFn: async () => {
            if (!conversationId || !toolCallId) return null;
            const response = await getLemmaClient(podId).conversations.messages.list(conversationId, {
                pod_id: podId,
                limit: 100,
            });
            return findDisplayResourceInMessages((response.items || []) as RawConversationMessage[], toolCallId);
        },
        enabled: !!podId && !!conversationId && !!toolCallId,
        refetchOnWindowFocus: false,
    });

    const request = query.data?.request;
    const schema = useMemo(() => request?.jsonSchema || {}, [request?.jsonSchema]);
    const properties = useMemo(() => schemaProperties(schema), [schema]);
    const required = useMemo(() => new Set(schemaRequired(schema)), [schema]);
    const requestTitle = humanizeLabel(request?.name || asString(schema.title), 'Input Request');
    const description = asString(schema.description);
    const activeConversationId = assistant.activeConversationId;
    const openAssistant = assistant.openAssistant;
    const selectConversation = assistant.selectConversation;

    useEffect(() => {
        if (!conversationId) return;

        if (initializedAssistantConversationRef.current !== conversationId) {
            initializedAssistantConversationRef.current = conversationId;
            openAssistant();
        }

        if (activeConversationId !== conversationId) {
            selectConversation(conversationId);
        }
    }, [activeConversationId, conversationId, openAssistant, selectConversation]);

    useEffect(() => {
        if (!request) return;
        let cancelled = false;
        window.queueMicrotask(() => {
            if (cancelled) return;
            setValues(buildInitialValues(schema));
            setErrors({});
            setSubmitted(false);
        });
        return () => {
            cancelled = true;
        };
    }, [request, schema]);

    const updateValue = useCallback((name: string, value: unknown) => {
        setValues((prev) => ({ ...prev, [name]: value }));
        setErrors((prev) => {
            if (!prev[name]) return prev;
            const next = { ...prev };
            delete next[name];
            return next;
        });
    }, []);

    const handleSubmit = useCallback(async () => {
        if (!request || !conversationId || assistant.activeConversationId !== conversationId) return;
        const nextErrors = validate(values, schema);
        setErrors(nextErrors);
        if (Object.keys(nextErrors).length > 0) return;

        const coercedValues = coerceFormValues(values, schema);

        setIsSubmitting(true);
        try {
            const sendPromise = assistant.sendMessage(formatSubmittedFormMessage({ request, values: coercedValues }));
            setSubmitted(true);
            setIsSubmitting(false);
            await sendPromise;
        } catch {
            setSubmitted(false);
            setIsSubmitting(false);
        }
    }, [assistant, conversationId, request, schema, values]);

    if (!conversationId || !toolCallId) {
        return (
            <main className="flex min-h-full items-center justify-center p-8">
                <div className="surface-panel max-w-xl p-6 text-sm text-[var(--text-secondary)]">
                    Missing form context.
                </div>
            </main>
        );
    }

    if (query.isLoading) {
        return (
            <main className="flex min-h-full items-center justify-center p-8">
                <div className="flex items-center gap-2 text-sm text-[var(--text-secondary)]">
                    <Loader2 className="h-4 w-4 animate-spin" />
                    Loading form
                </div>
            </main>
        );
    }

    if (!request || request.type !== 'FORM' || Object.keys(properties).length === 0) {
        return (
            <main className="flex min-h-full items-center justify-center p-8">
                <div className="surface-panel max-w-xl p-6 text-sm text-[var(--text-secondary)]">
                    Form unavailable.
                </div>
            </main>
        );
    }

    const canSubmit = assistant.activeConversationId === conversationId && !assistant.isActiveConversationRunning && !isSubmitting && !submitted;

    return (
        <main className="presented-resource-surface mx-auto flex w-full max-w-3xl flex-col gap-4 p-5 lg:p-6">
            <div>
                <div className="min-w-0">
                    <div className="text-xs font-normal text-[var(--text-tertiary)]">{requestTitle}</div>
                    {description ? (
                        <p className="mt-1.5 max-w-2xl text-sm leading-relaxed text-[var(--text-secondary)]">{description}</p>
                    ) : (
                        <p className="mt-1.5 max-w-2xl text-sm leading-relaxed text-[var(--text-secondary)]">
                            Fill this in so the agent can continue.
                        </p>
                    )}
                </div>
            </div>

            <section className="surface-panel grid gap-5 p-5 shadow-none">
                {Object.entries(properties).map(([name, rawField]) => (
                    <FieldControl
                        key={name}
                        name={name}
                        field={asRecord(rawField)}
                        value={values[name]}
                        error={errors[name]}
                        onChange={(value) => updateValue(name, value)}
                    />
                ))}
            </section>

            <footer className="flex flex-wrap items-center justify-between gap-3">
                <div className="text-xs text-[var(--text-secondary)]">
                    {required.size} required field{required.size === 1 ? '' : 's'}
                </div>
                <div className="flex items-center gap-3">
                    {submitted ? (
                        <span className="inline-flex items-center gap-1.5 text-sm font-medium text-[var(--state-success)]">
                            <CheckCircle2 className="h-4 w-4" />
                            Submitted
                        </span>
                    ) : null}
                    <Button type="button" onClick={handleSubmit} disabled={!canSubmit}>
                        {submitted
                            ? 'Submitted'
                            : isSubmitting
                                ? 'Submitting...'
                                : assistant.activeConversationId === conversationId ? 'Submit' : 'Opening conversation...'}
                    </Button>
                </div>
            </footer>
        </main>
    );
}
