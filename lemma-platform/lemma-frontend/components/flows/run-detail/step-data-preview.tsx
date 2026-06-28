import { cn } from '@/lib/utils';
import { getPreviewFields, truncatePreview } from '@/lib/utils/payload-preview';
import {
    formatStructuredOutput,
    getVisibleStepData,
    hasVisibleData,
    isRecord,
} from '../run-format';

export function StepDataPreview({ label, data, variant = 'boxed' }: { label: string; data: unknown; variant?: 'boxed' | 'flat' }) {
    const payload = getVisibleStepData(data);
    if (!hasVisibleData(payload)) return null;

    const fields = isRecord(payload) ? getPreviewFields(payload).slice(0, 8) : [];
    const isFlat = variant === 'flat';

    return (
        <div className={cn(isFlat ? 'py-1' : 'rounded-lg bg-[var(--surface-2)] px-3 py-3')}>
            <p className="mb-2 type-eyebrow">{label}</p>
            {fields.length > 0 ? (
                <div className={cn('grid gap-2 sm:grid-cols-2', isFlat && 'max-w-3xl gap-x-8 gap-y-4')}>
                    {fields.map((field) => (
                        <div key={field.label} className={cn('min-w-0', !isFlat && 'rounded-md bg-[var(--card-bg)] px-3 py-2')}>
                            <p className="truncate text-xs font-medium text-[var(--text-tertiary)]">{field.label}</p>
                            <p className="mt-0.5 break-words text-sm text-[var(--text-primary)]">{field.value}</p>
                        </div>
                    ))}
                </div>
            ) : (
                <p className="whitespace-pre-wrap break-words text-sm leading-6 text-[var(--text-primary)]">
                    {truncatePreview(formatStructuredOutput(payload), 900)}
                </p>
            )}
        </div>
    );
}
