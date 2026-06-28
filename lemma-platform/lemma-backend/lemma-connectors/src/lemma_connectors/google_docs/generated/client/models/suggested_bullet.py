from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.bullet import Bullet
  from ..models.bullet_suggestion_state import BulletSuggestionState





T = TypeVar("T", bound="SuggestedBullet")



@_attrs_define
class SuggestedBullet:
    """ A suggested change to a Bullet.

        Attributes:
            bullet (Bullet | Unset): Describes the bullet of a paragraph.
            bullet_suggestion_state (BulletSuggestionState | Unset): A mask that indicates which of the fields on the base
                Bullet have been changed in this suggestion. For any field set to true, there's a new suggested value.
     """

    bullet: Bullet | Unset = UNSET
    bullet_suggestion_state: BulletSuggestionState | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.bullet import Bullet
        from ..models.bullet_suggestion_state import BulletSuggestionState
        bullet: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bullet, Unset):
            bullet = self.bullet.to_dict()

        bullet_suggestion_state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bullet_suggestion_state, Unset):
            bullet_suggestion_state = self.bullet_suggestion_state.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if bullet is not UNSET:
            field_dict["bullet"] = bullet
        if bullet_suggestion_state is not UNSET:
            field_dict["bulletSuggestionState"] = bullet_suggestion_state

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bullet import Bullet
        from ..models.bullet_suggestion_state import BulletSuggestionState
        d = dict(src_dict)
        _bullet = d.pop("bullet", UNSET)
        bullet: Bullet | Unset
        if isinstance(_bullet,  Unset):
            bullet = UNSET
        else:
            bullet = Bullet.from_dict(_bullet)




        _bullet_suggestion_state = d.pop("bulletSuggestionState", UNSET)
        bullet_suggestion_state: BulletSuggestionState | Unset
        if isinstance(_bullet_suggestion_state,  Unset):
            bullet_suggestion_state = UNSET
        else:
            bullet_suggestion_state = BulletSuggestionState.from_dict(_bullet_suggestion_state)




        suggested_bullet = cls(
            bullet=bullet,
            bullet_suggestion_state=bullet_suggestion_state,
        )


        suggested_bullet.additional_properties = d
        return suggested_bullet

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
