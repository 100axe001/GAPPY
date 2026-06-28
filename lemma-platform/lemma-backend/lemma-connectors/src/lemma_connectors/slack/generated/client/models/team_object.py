from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.team_object_plan import TeamObjectPlan
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.external_org_migrations import ExternalOrgMigrations
  from ..models.objs_icon import ObjsIcon
  from ..models.objs_primary_owner import ObjsPrimaryOwner
  from ..models.team_object_sso_provider import TeamObjectSsoProvider





T = TypeVar("T", bound="TeamObject")



@_attrs_define
class TeamObject:
    """ 
        Attributes:
            domain (str):
            email_domain (str):
            icon (ObjsIcon):
            id (str):
            name (str):
            archived (bool | Unset):
            avatar_base_url (str | Unset):
            created (int | Unset):
            date_create (int | Unset):
            deleted (bool | Unset):
            description (None | str | Unset):
            discoverable (Any | Unset):
            enterprise_id (str | Unset):
            enterprise_name (str | Unset):
            external_org_migrations (ExternalOrgMigrations | Unset):
            has_compliance_export (bool | Unset):
            is_assigned (bool | Unset):
            is_enterprise (int | Unset):
            is_over_storage_limit (bool | Unset):
            limit_ts (int | Unset):
            locale (str | Unset):
            messages_count (int | Unset):
            msg_edit_window_mins (int | Unset):
            over_integrations_limit (bool | Unset):
            over_storage_limit (bool | Unset):
            pay_prod_cur (str | Unset):
            plan (TeamObjectPlan | Unset):
            primary_owner (ObjsPrimaryOwner | Unset):
            sso_provider (TeamObjectSsoProvider | Unset):
     """

    domain: str
    email_domain: str
    icon: ObjsIcon
    id: str
    name: str
    archived: bool | Unset = UNSET
    avatar_base_url: str | Unset = UNSET
    created: int | Unset = UNSET
    date_create: int | Unset = UNSET
    deleted: bool | Unset = UNSET
    description: None | str | Unset = UNSET
    discoverable: Any | Unset = UNSET
    enterprise_id: str | Unset = UNSET
    enterprise_name: str | Unset = UNSET
    external_org_migrations: ExternalOrgMigrations | Unset = UNSET
    has_compliance_export: bool | Unset = UNSET
    is_assigned: bool | Unset = UNSET
    is_enterprise: int | Unset = UNSET
    is_over_storage_limit: bool | Unset = UNSET
    limit_ts: int | Unset = UNSET
    locale: str | Unset = UNSET
    messages_count: int | Unset = UNSET
    msg_edit_window_mins: int | Unset = UNSET
    over_integrations_limit: bool | Unset = UNSET
    over_storage_limit: bool | Unset = UNSET
    pay_prod_cur: str | Unset = UNSET
    plan: TeamObjectPlan | Unset = UNSET
    primary_owner: ObjsPrimaryOwner | Unset = UNSET
    sso_provider: TeamObjectSsoProvider | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.external_org_migrations import ExternalOrgMigrations
        from ..models.objs_icon import ObjsIcon
        from ..models.objs_primary_owner import ObjsPrimaryOwner
        from ..models.team_object_sso_provider import TeamObjectSsoProvider
        domain = self.domain

        email_domain = self.email_domain

        icon = self.icon.to_dict()

        id = self.id

        name = self.name

        archived = self.archived

        avatar_base_url = self.avatar_base_url

        created = self.created

        date_create = self.date_create

        deleted = self.deleted

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        discoverable = self.discoverable

        enterprise_id = self.enterprise_id

        enterprise_name = self.enterprise_name

        external_org_migrations: dict[str, Any] | Unset = UNSET
        if not isinstance(self.external_org_migrations, Unset):
            external_org_migrations = self.external_org_migrations.to_dict()

        has_compliance_export = self.has_compliance_export

        is_assigned = self.is_assigned

        is_enterprise = self.is_enterprise

        is_over_storage_limit = self.is_over_storage_limit

        limit_ts = self.limit_ts

        locale = self.locale

        messages_count = self.messages_count

        msg_edit_window_mins = self.msg_edit_window_mins

        over_integrations_limit = self.over_integrations_limit

        over_storage_limit = self.over_storage_limit

        pay_prod_cur = self.pay_prod_cur

        plan: str | Unset = UNSET
        if not isinstance(self.plan, Unset):
            plan = self.plan.value


        primary_owner: dict[str, Any] | Unset = UNSET
        if not isinstance(self.primary_owner, Unset):
            primary_owner = self.primary_owner.to_dict()

        sso_provider: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sso_provider, Unset):
            sso_provider = self.sso_provider.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "domain": domain,
            "email_domain": email_domain,
            "icon": icon,
            "id": id,
            "name": name,
        })
        if archived is not UNSET:
            field_dict["archived"] = archived
        if avatar_base_url is not UNSET:
            field_dict["avatar_base_url"] = avatar_base_url
        if created is not UNSET:
            field_dict["created"] = created
        if date_create is not UNSET:
            field_dict["date_create"] = date_create
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if description is not UNSET:
            field_dict["description"] = description
        if discoverable is not UNSET:
            field_dict["discoverable"] = discoverable
        if enterprise_id is not UNSET:
            field_dict["enterprise_id"] = enterprise_id
        if enterprise_name is not UNSET:
            field_dict["enterprise_name"] = enterprise_name
        if external_org_migrations is not UNSET:
            field_dict["external_org_migrations"] = external_org_migrations
        if has_compliance_export is not UNSET:
            field_dict["has_compliance_export"] = has_compliance_export
        if is_assigned is not UNSET:
            field_dict["is_assigned"] = is_assigned
        if is_enterprise is not UNSET:
            field_dict["is_enterprise"] = is_enterprise
        if is_over_storage_limit is not UNSET:
            field_dict["is_over_storage_limit"] = is_over_storage_limit
        if limit_ts is not UNSET:
            field_dict["limit_ts"] = limit_ts
        if locale is not UNSET:
            field_dict["locale"] = locale
        if messages_count is not UNSET:
            field_dict["messages_count"] = messages_count
        if msg_edit_window_mins is not UNSET:
            field_dict["msg_edit_window_mins"] = msg_edit_window_mins
        if over_integrations_limit is not UNSET:
            field_dict["over_integrations_limit"] = over_integrations_limit
        if over_storage_limit is not UNSET:
            field_dict["over_storage_limit"] = over_storage_limit
        if pay_prod_cur is not UNSET:
            field_dict["pay_prod_cur"] = pay_prod_cur
        if plan is not UNSET:
            field_dict["plan"] = plan
        if primary_owner is not UNSET:
            field_dict["primary_owner"] = primary_owner
        if sso_provider is not UNSET:
            field_dict["sso_provider"] = sso_provider

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.external_org_migrations import ExternalOrgMigrations
        from ..models.objs_icon import ObjsIcon
        from ..models.objs_primary_owner import ObjsPrimaryOwner
        from ..models.team_object_sso_provider import TeamObjectSsoProvider
        d = dict(src_dict)
        domain = d.pop("domain")

        email_domain = d.pop("email_domain")

        icon = ObjsIcon.from_dict(d.pop("icon"))




        id = d.pop("id")

        name = d.pop("name")

        archived = d.pop("archived", UNSET)

        avatar_base_url = d.pop("avatar_base_url", UNSET)

        created = d.pop("created", UNSET)

        date_create = d.pop("date_create", UNSET)

        deleted = d.pop("deleted", UNSET)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        discoverable = d.pop("discoverable", UNSET)

        enterprise_id = d.pop("enterprise_id", UNSET)

        enterprise_name = d.pop("enterprise_name", UNSET)

        _external_org_migrations = d.pop("external_org_migrations", UNSET)
        external_org_migrations: ExternalOrgMigrations | Unset
        if isinstance(_external_org_migrations,  Unset):
            external_org_migrations = UNSET
        else:
            external_org_migrations = ExternalOrgMigrations.from_dict(_external_org_migrations)




        has_compliance_export = d.pop("has_compliance_export", UNSET)

        is_assigned = d.pop("is_assigned", UNSET)

        is_enterprise = d.pop("is_enterprise", UNSET)

        is_over_storage_limit = d.pop("is_over_storage_limit", UNSET)

        limit_ts = d.pop("limit_ts", UNSET)

        locale = d.pop("locale", UNSET)

        messages_count = d.pop("messages_count", UNSET)

        msg_edit_window_mins = d.pop("msg_edit_window_mins", UNSET)

        over_integrations_limit = d.pop("over_integrations_limit", UNSET)

        over_storage_limit = d.pop("over_storage_limit", UNSET)

        pay_prod_cur = d.pop("pay_prod_cur", UNSET)

        _plan = d.pop("plan", UNSET)
        plan: TeamObjectPlan | Unset
        if isinstance(_plan,  Unset):
            plan = UNSET
        else:
            plan = TeamObjectPlan(_plan)




        _primary_owner = d.pop("primary_owner", UNSET)
        primary_owner: ObjsPrimaryOwner | Unset
        if isinstance(_primary_owner,  Unset):
            primary_owner = UNSET
        else:
            primary_owner = ObjsPrimaryOwner.from_dict(_primary_owner)




        _sso_provider = d.pop("sso_provider", UNSET)
        sso_provider: TeamObjectSsoProvider | Unset
        if isinstance(_sso_provider,  Unset):
            sso_provider = UNSET
        else:
            sso_provider = TeamObjectSsoProvider.from_dict(_sso_provider)




        team_object = cls(
            domain=domain,
            email_domain=email_domain,
            icon=icon,
            id=id,
            name=name,
            archived=archived,
            avatar_base_url=avatar_base_url,
            created=created,
            date_create=date_create,
            deleted=deleted,
            description=description,
            discoverable=discoverable,
            enterprise_id=enterprise_id,
            enterprise_name=enterprise_name,
            external_org_migrations=external_org_migrations,
            has_compliance_export=has_compliance_export,
            is_assigned=is_assigned,
            is_enterprise=is_enterprise,
            is_over_storage_limit=is_over_storage_limit,
            limit_ts=limit_ts,
            locale=locale,
            messages_count=messages_count,
            msg_edit_window_mins=msg_edit_window_mins,
            over_integrations_limit=over_integrations_limit,
            over_storage_limit=over_storage_limit,
            pay_prod_cur=pay_prod_cur,
            plan=plan,
            primary_owner=primary_owner,
            sso_provider=sso_provider,
        )

        return team_object

