from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="AppsPermissionsScopesListApiPermissionsScopesListSuccessSchemaScopes")



@_attrs_define
class AppsPermissionsScopesListApiPermissionsScopesListSuccessSchemaScopes:
    """ 
        Attributes:
            app_home (list[str] | Unset):
            channel (list[str] | Unset):
            group (list[str] | Unset):
            im (list[str] | Unset):
            mpim (list[str] | Unset):
            team (list[str] | Unset):
            user (list[str] | Unset):
     """

    app_home: list[str] | Unset = UNSET
    channel: list[str] | Unset = UNSET
    group: list[str] | Unset = UNSET
    im: list[str] | Unset = UNSET
    mpim: list[str] | Unset = UNSET
    team: list[str] | Unset = UNSET
    user: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        app_home: list[str] | Unset = UNSET
        if not isinstance(self.app_home, Unset):
            app_home = self.app_home



        channel: list[str] | Unset = UNSET
        if not isinstance(self.channel, Unset):
            channel = self.channel



        group: list[str] | Unset = UNSET
        if not isinstance(self.group, Unset):
            group = self.group



        im: list[str] | Unset = UNSET
        if not isinstance(self.im, Unset):
            im = self.im



        mpim: list[str] | Unset = UNSET
        if not isinstance(self.mpim, Unset):
            mpim = self.mpim



        team: list[str] | Unset = UNSET
        if not isinstance(self.team, Unset):
            team = self.team



        user: list[str] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = self.user




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if app_home is not UNSET:
            field_dict["app_home"] = app_home
        if channel is not UNSET:
            field_dict["channel"] = channel
        if group is not UNSET:
            field_dict["group"] = group
        if im is not UNSET:
            field_dict["im"] = im
        if mpim is not UNSET:
            field_dict["mpim"] = mpim
        if team is not UNSET:
            field_dict["team"] = team
        if user is not UNSET:
            field_dict["user"] = user

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        app_home = cast(list[str], d.pop("app_home", UNSET))


        channel = cast(list[str], d.pop("channel", UNSET))


        group = cast(list[str], d.pop("group", UNSET))


        im = cast(list[str], d.pop("im", UNSET))


        mpim = cast(list[str], d.pop("mpim", UNSET))


        team = cast(list[str], d.pop("team", UNSET))


        user = cast(list[str], d.pop("user", UNSET))


        apps_permissions_scopes_list_api_permissions_scopes_list_success_schema_scopes = cls(
            app_home=app_home,
            channel=channel,
            group=group,
            im=im,
            mpim=mpim,
            team=team,
            user=user,
        )


        apps_permissions_scopes_list_api_permissions_scopes_list_success_schema_scopes.additional_properties = d
        return apps_permissions_scopes_list_api_permissions_scopes_list_success_schema_scopes

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
