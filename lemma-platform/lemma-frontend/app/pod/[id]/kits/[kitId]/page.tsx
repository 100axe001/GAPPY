import { redirect } from 'next/navigation';

// Kits are now folded into Recipes. A kit id is a recipe id.
export default async function KitDetailRedirect({ params }: { params: Promise<{ id: string; kitId: string }> }) {
    const { id, kitId } = await params;
    redirect(`/pod/${id}/recipes/${encodeURIComponent(kitId)}`);
}
