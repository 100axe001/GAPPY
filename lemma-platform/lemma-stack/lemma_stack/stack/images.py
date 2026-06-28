"""Image pulls for a release (includes pre-pulling the sandbox runtime image
so the first agent workspace doesn't block on a multi-GB download)."""

from __future__ import annotations

from lemma_stack.output import info
from lemma_stack.release.manifest import ReleaseManifest
from lemma_stack.runtime.base import Runtime


def pull_release(
    runtime: Runtime,
    manifest: ReleaseManifest,
    *,
    kreuzberg: bool,
    skip_existing: bool = True,
) -> None:
    for ref in manifest.all_pull_refs(kreuzberg=kreuzberg):
        if skip_existing and runtime.image_exists(ref):
            info(f"image present: {ref}")
            continue
        info(f"pulling {ref}")
        runtime.pull(ref)
