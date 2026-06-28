import { redirect } from 'next/navigation';

// Kits are now folded into Recipes. Preserve old links.
export default async function KitsRedirect({ params }: { params: Promise<{ id: string }> }) {
    const { id } = await params;
    redirect(`/pod/${id}/recipes`);
}
