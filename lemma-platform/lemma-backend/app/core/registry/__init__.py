"""Module registry: Django-``INSTALLED_APPS``-style self-registration.

Each backend module exposes a :class:`LemmaModule` (in ``app/modules/<name>/module.py``)
declaring what it contributes to the API process and the worker process. The
entrypoints (``app/app.py``, ``app/events.py``, the worker lifespan) stitch a
*provided* list of modules instead of importing every router/handler by hand.

Because the assembly functions take the module list as a parameter, a separate
deployment (``lemma-cloud``) can compose its own app/worker/scheduler from the
open-source core modules plus extra proprietary ones.
"""

from app.core.registry.contract import LemmaModule

__all__ = ["LemmaModule"]
