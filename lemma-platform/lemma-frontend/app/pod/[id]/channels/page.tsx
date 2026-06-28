'use client';

import { use } from 'react';
import { redirect } from 'next/navigation';

export default function PodChannelsPage({
    params,
}: {
    params: Promise<{ id: string }>;
}) {
    const { id: podId } = use(params);
    redirect(`/pod/${podId}/surfaces`);
}
