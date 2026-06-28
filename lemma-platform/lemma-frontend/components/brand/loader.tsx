"use client";

import React from "react";
import { LemmaMark } from "@/components/brand/logo";
import { cn } from "@/lib/utils";

type LoaderSize = "xs" | "sm" | "md" | "lg";

/**
 * StepLoader — Loader A: "Proof Steps"
 * Five vertical bars that rise sequentially, each one a step in a proof.
 * Use for: in-page loading states, list skeletons, section transitions.
 */
export function StepLoader({
    size = "md",
    className,
}: {
    size?: LoaderSize;
    className?: string;
}) {
    return (
        <span
            className={cn("lemma-step-loader", `lemma-step-loader-${size}`, className)}
            aria-label="Loading…"
            role="status"
        >
            {[0, 1, 2, 3, 4].map((i) => (
                <span
                    key={i}
                    className="lemma-step-bar"
                />
            ))}
        </span>
    );
}

export function InlineLoader({
    size = "sm",
    label = "Working",
    className,
}: {
    size?: LoaderSize;
    label?: string;
    className?: string;
}) {
    return (
        <span className={cn("inline-flex items-center gap-2 text-[var(--text-secondary)]", className)}>
            <StepLoader size={size} />
            <span>{label}</span>
        </span>
    );
}

export function LoadingState({
    title = "Loading",
    description,
    variant = "panel",
    shape = "lines",
    className,
}: {
    title?: string;
    description?: string;
    variant?: "inline" | "panel" | "page";
    shape?: "none" | "lines" | "cards" | "table";
    className?: string;
}) {
    const isPage = variant === "page";
    const isInline = variant === "inline";

    return (
        <div
            className={cn(
                "lemma-loading-state",
                isPage
                    ? "flex min-h-screen flex-col items-center justify-center gap-6"
                    : isInline
                        ? "inline-flex items-center gap-2"
                        : "surface-panel flex min-h-[12rem] flex-col items-center justify-center gap-5 px-6 py-10 text-center",
                className
            )}
            role="status"
            aria-live="polite"
        >
            <StepLoader size={isPage ? "md" : isInline ? "xs" : "sm"} />
            <div className={cn("min-w-0", isInline ? "text-left" : "text-center")}>
                <p className={cn("font-medium text-[var(--text-primary)]", isInline ? "text-sm" : "text-base")}>
                    {title}
                </p>
                {description ? (
                    <p className={cn("mt-1 text-[var(--text-tertiary)]", isInline ? "text-xs" : "text-sm")}>
                        {description}
                    </p>
                ) : null}
            </div>
            {!isInline && shape !== "none" ? <LoadingSkeleton shape={shape} /> : null}
        </div>
    );
}

export function LoadingSkeleton({
    shape = "lines",
    className,
}: {
    shape?: "lines" | "cards" | "table";
    className?: string;
}) {
    if (shape === "cards") {
        return (
            <div className={cn("grid w-full max-w-2xl gap-3 sm:grid-cols-3", className)} aria-hidden="true">
                {[0, 1, 2].map((item) => (
                    <div key={item} className="lemma-skeleton h-24 rounded-lg" />
                ))}
            </div>
        );
    }

    if (shape === "table") {
        return (
            <div className={cn("w-full max-w-2xl space-y-2", className)} aria-hidden="true">
                <div className="lemma-skeleton h-8 rounded-md" />
                {[0, 1, 2, 3].map((item) => (
                    <div key={item} className="lemma-skeleton h-10 rounded-md" />
                ))}
            </div>
        );
    }

    return (
        <div className={cn("w-full max-w-sm space-y-2", className)} aria-hidden="true">
            <div className="lemma-skeleton h-3 w-4/5 rounded-full" />
            <div className="lemma-skeleton h-3 w-full rounded-full" />
            <div className="lemma-skeleton h-3 w-3/5 rounded-full" />
        </div>
    );
}

/**
 * WordmarkLoader — Loader D: "Wordmark Build"
 * The letters of "lemma" arrive one by one, left to right.
 * Use for: full-page loading splash, route transitions.
 */
export function WordmarkLoader({
    size = "md",
    className,
}: {
    size?: "sm" | "md" | "lg";
    className?: string;
}) {
    const letters = ["l", "e", "m", "m", "a"];

    return (
        <span
            className={cn("lemma-wordmark-loader", `lemma-wordmark-loader-${size}`, className)}
            aria-label="lemma — loading…"
            role="status"
        >
            {letters.map((letter, i) => (
                <span
                    key={i}
                    className="lemma-wordmark-letter"
                >
                    {letter}
                </span>
            ))}
        </span>
    );
}

/**
 * PageLoader — full-page centered loading splash.
 * Used for route-level Suspense boundaries.
 */
export function PageLoader() {
    return (
        <div
            className="lemma-page-loader flex min-h-screen items-center justify-center bg-transparent"
            role="status"
            aria-label="Loading Lemma"
            aria-live="polite"
        >
            <div className="lemma-page-loader-mark-shell">
                <LemmaMark size="lg" className="lemma-page-loader-mark" />
            </div>
        </div>
    );
}
