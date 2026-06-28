import json
from collections.abc import Callable

from markupsafe import Markup, escape


def pretty_json(value: object) -> Markup:
    if value in (None, "", [], {}):
        return Markup("<span class='lz-json-empty'>—</span>")

    rendered = json.dumps(value, indent=2, sort_keys=True, default=str, ensure_ascii=False)
    # The wrapper is styled + syntax-highlighted + made collapsible by
    # admin-pro.css / admin-pro.js (loaded globally in the admin chrome).
    return Markup(f"<div class='lz-json' data-json><pre>{escape(rendered)}</pre></div>")


def json_formatter(attribute: str) -> Callable[[object, str], Markup]:
    def _formatter(model: object, _name: str) -> Markup:
        return pretty_json(getattr(model, attribute))

    return _formatter


class AdminModelViewMixin:
    # Full CRUD for editable config/entity views: enables the "Actions"
    # dropdown (bulk delete) + row edit/delete. Audit/identity/run-history
    # views opt out via ReadOnlyAdminModelViewMixin below.
    can_view_details = True
    can_create = True
    can_edit = True
    can_delete = True
    form_include_pk = True


class ReadOnlyAdminModelViewMixin(AdminModelViewMixin):
    can_create = False
    can_edit = False
    can_delete = False
