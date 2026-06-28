'use client';

import { getLemmaClient } from '@/lib/sdk/lemma-client';
import { clearLastOpenedPodId } from '@/lib/pods/last-opened-pod';

export async function logoutToHome() {
    try {
        // Revoke the SuperTokens session (clears cookies + backend session).
        // There is no upstream/federated SSO logout endpoint to bounce through,
        // so doing the local sign-out and navigating home is the full flow.
        await getLemmaClient().auth.signOut();
    } catch {
        // Best effort: even if the network sign-out fails, fall through and
        // send the user to the landing page rather than stranding them.
    }

    // Drop the "last opened pod" marker so the root route doesn't immediately
    // redirect a just-logged-out user back into their previous pod.
    clearLastOpenedPodId();

    // Full-document navigation (not router.push) so all in-memory auth/query
    // state is discarded and the landing page renders from a clean slate.
    window.location.assign('/');
}
