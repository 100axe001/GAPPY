'use client';

import Link from 'next/link';
import { X } from 'lucide-react';

import { ConceptIllustration, hasConceptIllustration } from '@/components/education/concept-illustration';
import { ProductIcon } from '@/components/pod/product-icon';
import { Button } from '@/components/ui/button';
import { getConcept, type ConceptId } from '@/lib/education/concepts';
import { useEducationEnabled } from '@/lib/education/use-education-audience';
import { useSectionPrimer } from '@/lib/education/use-education-state';
import { cn } from '@/lib/utils';

interface SectionPrimerCta {
    label: string;
    href?: string;
    onClick?: () => void;
}

interface SectionPrimerProps {
    concept: ConceptId;
    cta?: SectionPrimerCta;
    className?: string;
}

export function SectionPrimer({ concept, cta, className }: SectionPrimerProps) {
    const entry = getConcept(concept);
    const enabled = useEducationEnabled();
    const { visible, dismiss } = useSectionPrimer(`primer:${concept}`);

    if (!enabled || !visible) return null;

    return (
        <section
            aria-label={`About ${entry.term.toLowerCase()}s`}
            className={cn('surface-panel relative px-5 py-4', className)}
        >
            <button
                type="button"
                aria-label="Dismiss"
                onClick={dismiss}
                className="absolute right-3 top-3 inline-flex h-7 w-7 items-center justify-center rounded-md text-[var(--text-tertiary)] transition-gentle hover:bg-[var(--surface-2)] hover:text-[var(--text-primary)] focus-ring"
            >
                <X className="h-4 w-4" aria-hidden="true" />
            </button>
            <div className="flex items-start gap-3 pr-8">
                <div className="mt-0.5 shrink-0">
                    <ProductIcon tone={entry.tone} size="md" />
                </div>
                <div className="min-w-0 flex-1">
                    <h3 className="text-sm font-semibold text-[var(--text-primary)]">
                        {entry.term}s, in short
                    </h3>
                    {entry.explainer.map((paragraph) => (
                        <p key={paragraph} className="mt-2 max-w-2xl text-sm leading-6 text-[var(--text-secondary)]">
                            {paragraph}
                        </p>
                    ))}
                    <p className="mt-3 max-w-2xl border-l-2 border-[var(--delight)] pl-3 text-sm leading-6 text-[var(--text-secondary)]">
                        <span className="font-medium text-[var(--text-primary)]">For example: </span>
                        {entry.example}
                    </p>
                    <div className="mt-3 flex flex-wrap items-center gap-2">
                        {cta ? (
                            cta.href ? (
                                <Button asChild size="xs" variant="accent">
                                    <Link href={cta.href}>{cta.label}</Link>
                                </Button>
                            ) : (
                                <Button size="xs" variant="accent" onClick={cta.onClick}>
                                    {cta.label}
                                </Button>
                            )
                        ) : null}
                        <Button
                            size="xs"
                            variant="link"
                            onClick={dismiss}
                            className="px-0 text-[var(--text-tertiary)] hover:text-[var(--text-primary)] hover:no-underline"
                        >
                            Got it
                        </Button>
                        <Button
                            asChild
                            size="xs"
                            variant="link"
                            className="px-0 text-[var(--text-tertiary)] hover:text-[var(--text-primary)]"
                        >
                            <Link href={`/docs/${entry.guideSlug}`} target="_blank" rel="noopener noreferrer">
                                Learn more
                            </Link>
                        </Button>
                    </div>
                </div>
                {hasConceptIllustration(concept) ? (
                    <div className="hidden w-60 shrink-0 self-center lg:block xl:w-72">
                        <ConceptIllustration concept={concept} />
                    </div>
                ) : null}
            </div>
        </section>
    );
}
