from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.apps_permissions_info_apps_permissions_info_schema_info_app_home import AppsPermissionsInfoAppsPermissionsInfoSchemaInfoAppHome
  from ..models.apps_permissions_info_apps_permissions_info_schema_info_channel import AppsPermissionsInfoAppsPermissionsInfoSchemaInfoChannel
  from ..models.apps_permissions_info_apps_permissions_info_schema_info_group import AppsPermissionsInfoAppsPermissionsInfoSchemaInfoGroup
  from ..models.apps_permissions_info_apps_permissions_info_schema_info_im import AppsPermissionsInfoAppsPermissionsInfoSchemaInfoIm
  from ..models.apps_permissions_info_apps_permissions_info_schema_info_mpim import AppsPermissionsInfoAppsPermissionsInfoSchemaInfoMpim
  from ..models.apps_permissions_info_apps_permissions_info_schema_info_team import AppsPermissionsInfoAppsPermissionsInfoSchemaInfoTeam





T = TypeVar("T", bound="AppsPermissionsInfoAppsPermissionsInfoSchemaInfo")



@_attrs_define
class AppsPermissionsInfoAppsPermissionsInfoSchemaInfo:
    """ 
        Attributes:
            app_home (AppsPermissionsInfoAppsPermissionsInfoSchemaInfoAppHome):
            channel (AppsPermissionsInfoAppsPermissionsInfoSchemaInfoChannel):
            group (AppsPermissionsInfoAppsPermissionsInfoSchemaInfoGroup):
            im (AppsPermissionsInfoAppsPermissionsInfoSchemaInfoIm):
            mpim (AppsPermissionsInfoAppsPermissionsInfoSchemaInfoMpim):
            team (AppsPermissionsInfoAppsPermissionsInfoSchemaInfoTeam):
     """

    app_home: AppsPermissionsInfoAppsPermissionsInfoSchemaInfoAppHome
    channel: AppsPermissionsInfoAppsPermissionsInfoSchemaInfoChannel
    group: AppsPermissionsInfoAppsPermissionsInfoSchemaInfoGroup
    im: AppsPermissionsInfoAppsPermissionsInfoSchemaInfoIm
    mpim: AppsPermissionsInfoAppsPermissionsInfoSchemaInfoMpim
    team: AppsPermissionsInfoAppsPermissionsInfoSchemaInfoTeam
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.apps_permissions_info_apps_permissions_info_schema_info_app_home import AppsPermissionsInfoAppsPermissionsInfoSchemaInfoAppHome
        from ..models.apps_permissions_info_apps_permissions_info_schema_info_channel import AppsPermissionsInfoAppsPermissionsInfoSchemaInfoChannel
        from ..models.apps_permissions_info_apps_permissions_info_schema_info_group import AppsPermissionsInfoAppsPermissionsInfoSchemaInfoGroup
        from ..models.apps_permissions_info_apps_permissions_info_schema_info_im import AppsPermissionsInfoAppsPermissionsInfoSchemaInfoIm
        from ..models.apps_permissions_info_apps_permissions_info_schema_info_mpim import AppsPermissionsInfoAppsPermissionsInfoSchemaInfoMpim
        from ..models.apps_permissions_info_apps_permissions_info_schema_info_team import AppsPermissionsInfoAppsPermissionsInfoSchemaInfoTeam
        app_home = self.app_home.to_dict()

        channel = self.channel.to_dict()

        group = self.group.to_dict()

        im = self.im.to_dict()

        mpim = self.mpim.to_dict()

        team = self.team.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "app_home": app_home,
            "channel": channel,
            "group": group,
            "im": im,
            "mpim": mpim,
            "team": team,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.apps_permissions_info_apps_permissions_info_schema_info_app_home import AppsPermissionsInfoAppsPermissionsInfoSchemaInfoAppHome
        from ..models.apps_permissions_info_apps_permissions_info_schema_info_channel import AppsPermissionsInfoAppsPermissionsInfoSchemaInfoChannel
        from ..models.apps_permissions_info_apps_permissions_info_schema_info_group import AppsPermissionsInfoAppsPermissionsInfoSchemaInfoGroup
        from ..models.apps_permissions_info_apps_permissions_info_schema_info_im import AppsPermissionsInfoAppsPermissionsInfoSchemaInfoIm
        from ..models.apps_permissions_info_apps_permissions_info_schema_info_mpim import AppsPermissionsInfoAppsPermissionsInfoSchemaInfoMpim
        from ..models.apps_permissions_info_apps_permissions_info_schema_info_team import AppsPermissionsInfoAppsPermissionsInfoSchemaInfoTeam
        d = dict(src_dict)
        app_home = AppsPermissionsInfoAppsPermissionsInfoSchemaInfoAppHome.from_dict(d.pop("app_home"))




        channel = AppsPermissionsInfoAppsPermissionsInfoSchemaInfoChannel.from_dict(d.pop("channel"))




        group = AppsPermissionsInfoAppsPermissionsInfoSchemaInfoGroup.from_dict(d.pop("group"))




        im = AppsPermissionsInfoAppsPermissionsInfoSchemaInfoIm.from_dict(d.pop("im"))




        mpim = AppsPermissionsInfoAppsPermissionsInfoSchemaInfoMpim.from_dict(d.pop("mpim"))




        team = AppsPermissionsInfoAppsPermissionsInfoSchemaInfoTeam.from_dict(d.pop("team"))




        apps_permissions_info_apps_permissions_info_schema_info = cls(
            app_home=app_home,
            channel=channel,
            group=group,
            im=im,
            mpim=mpim,
            team=team,
        )


        apps_permissions_info_apps_permissions_info_schema_info.additional_properties = d
        return apps_permissions_info_apps_permissions_info_schema_info

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
