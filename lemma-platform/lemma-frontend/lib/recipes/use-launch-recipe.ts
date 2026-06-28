'use client';

import { useCallback } from 'react';
import { useRouter } from 'next/navigation';

import { buildRecipeConversationHref, type Recipe } from './recipes';

// One gesture for "add this recipe to the pod": open a full conversation primed
// to build it. Prompt recipes seed an intent; repo recipes seed the kit install.
// Either way the user lands in the full conversation view, not a background chat.
export function useLaunchRecipe(podId: string, opts?: { podName?: string | null }) {
    const router = useRouter();
    const podName = opts?.podName ?? null;

    const launchRecipe = useCallback(
        (recipe: Recipe) => {
            router.push(buildRecipeConversationHref(podId, recipe, { podName }));
        },
        [podId, podName, router],
    );

    return { launchRecipe };
}
