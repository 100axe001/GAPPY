"use client";

// Shared control that renders a single JSON-Schema field. Used by both the
// standalone forms/view page and the inline conversation form panel so the two
// surfaces stay visually and behaviourally identical.

import { useState } from "react";
import { Checkbox } from "@/components/ui/checkbox";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Textarea } from "@/components/ui/textarea";
import { asString, fieldType, humanizeLabel } from "@/lib/assistant/form-schema";

const OTHER_OPTION = "__lemma_other__";

export function FieldControl({
    name,
    field,
    value,
    error,
    autoFocus,
    onChange,
}: {
    name: string;
    field: Record<string, unknown>;
    value: unknown;
    error?: string;
    autoFocus?: boolean;
    onChange: (value: unknown) => void;
}) {
    const type = fieldType(field);
    const title = humanizeLabel(asString(field.title), name);
    const description = asString(field.description);
    const enumValues = Array.isArray(field.enum)
        ? field.enum.filter((entry) => typeof entry === "string" || typeof entry === "number").map((entry) => String(entry))
        : [];

    // Multiple-choice fields also allow a free-typed answer via an "Other" option.
    // "Other" is active when the user picked it, or when the current value isn't a
    // listed option (e.g. an answer restored from a previous step).
    const currentString = value === null || typeof value === "undefined" ? "" : String(value);
    const [otherPicked, setOtherPicked] = useState(false);
    const isOther = otherPicked || (currentString.length > 0 && !enumValues.includes(currentString));

    return (
        <div className="grid gap-2">
            <Label className="text-sm font-normal text-[var(--text-primary)]" htmlFor={`form-field-${name}`}>
                {title}
            </Label>
            {description ? <p className="text-xs leading-relaxed text-[var(--text-secondary)]">{description}</p> : null}
            {enumValues.length > 0 ? (
                <div className="grid gap-2">
                    <select
                        id={`form-field-${name}`}
                        autoFocus={autoFocus}
                        value={isOther ? OTHER_OPTION : currentString}
                        onChange={(event) => {
                            if (event.target.value === OTHER_OPTION) {
                                setOtherPicked(true);
                                onChange("");
                            } else {
                                setOtherPicked(false);
                                onChange(event.target.value);
                            }
                        }}
                        className="h-10 rounded-md border border-[var(--border-subtle)] bg-[var(--bg-canvas)] px-3 text-sm text-[var(--text-primary)]"
                    >
                        <option value="">Select</option>
                        {enumValues.map((option) => (
                            <option key={option} value={option}>
                                {option}
                            </option>
                        ))}
                        <option value={OTHER_OPTION}>Other (type your own)</option>
                    </select>
                    {isOther ? (
                        <Input
                            autoFocus
                            type="text"
                            placeholder="Type your answer"
                            value={currentString}
                            onChange={(event) => onChange(event.target.value)}
                        />
                    ) : null}
                </div>
            ) : type === "boolean" ? (
                <label className="flex items-center gap-2 text-sm text-[var(--text-primary)]">
                    <Checkbox checked={Boolean(value)} onCheckedChange={(checked) => onChange(checked === true)} />
                    Yes
                </label>
            ) : type === "array" || type === "object" ? (
                <Textarea
                    id={`form-field-${name}`}
                    autoFocus={autoFocus}
                    value={typeof value === "string" ? value : JSON.stringify(value ?? (type === "array" ? [] : {}), null, 2)}
                    onChange={(event) => onChange(event.target.value)}
                    className="min-h-28 resize-y"
                />
            ) : (
                <Input
                    id={`form-field-${name}`}
                    autoFocus={autoFocus}
                    type={type === "number" || type === "integer" ? "number" : "text"}
                    value={String(value ?? "")}
                    onChange={(event) => onChange(event.target.value)}
                />
            )}
            {error ? <div className="text-xs font-medium text-[var(--state-error)]">{error}</div> : null}
        </div>
    );
}
