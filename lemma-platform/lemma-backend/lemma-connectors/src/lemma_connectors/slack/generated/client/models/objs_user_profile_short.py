from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ObjsUserProfileShort")



@_attrs_define
class ObjsUserProfileShort:
    """ 
        Attributes:
            avatar_hash (str):
            display_name (str):
            first_name (None | str):
            image_72 (str):
            is_restricted (bool):
            is_ultra_restricted (bool):
            name (str):
            real_name (str):
            team (str):
            display_name_normalized (str | Unset):
            real_name_normalized (str | Unset):
     """

    avatar_hash: str
    display_name: str
    first_name: None | str
    image_72: str
    is_restricted: bool
    is_ultra_restricted: bool
    name: str
    real_name: str
    team: str
    display_name_normalized: str | Unset = UNSET
    real_name_normalized: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        avatar_hash = self.avatar_hash

        display_name = self.display_name

        first_name: None | str
        first_name = self.first_name

        image_72 = self.image_72

        is_restricted = self.is_restricted

        is_ultra_restricted = self.is_ultra_restricted

        name = self.name

        real_name = self.real_name

        team = self.team

        display_name_normalized = self.display_name_normalized

        real_name_normalized = self.real_name_normalized


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "avatar_hash": avatar_hash,
            "display_name": display_name,
            "first_name": first_name,
            "image_72": image_72,
            "is_restricted": is_restricted,
            "is_ultra_restricted": is_ultra_restricted,
            "name": name,
            "real_name": real_name,
            "team": team,
        })
        if display_name_normalized is not UNSET:
            field_dict["display_name_normalized"] = display_name_normalized
        if real_name_normalized is not UNSET:
            field_dict["real_name_normalized"] = real_name_normalized

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        avatar_hash = d.pop("avatar_hash")

        display_name = d.pop("display_name")

        def _parse_first_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        first_name = _parse_first_name(d.pop("first_name"))


        image_72 = d.pop("image_72")

        is_restricted = d.pop("is_restricted")

        is_ultra_restricted = d.pop("is_ultra_restricted")

        name = d.pop("name")

        real_name = d.pop("real_name")

        team = d.pop("team")

        display_name_normalized = d.pop("display_name_normalized", UNSET)

        real_name_normalized = d.pop("real_name_normalized", UNSET)

        objs_user_profile_short = cls(
            avatar_hash=avatar_hash,
            display_name=display_name,
            first_name=first_name,
            image_72=image_72,
            is_restricted=is_restricted,
            is_ultra_restricted=is_ultra_restricted,
            name=name,
            real_name=real_name,
            team=team,
            display_name_normalized=display_name_normalized,
            real_name_normalized=real_name_normalized,
        )

        return objs_user_profile_short

