from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.create_paragraph_bullets_request_bullet_preset import CreateParagraphBulletsRequestBulletPreset
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.range_ import Range





T = TypeVar("T", bound="CreateParagraphBulletsRequest")



@_attrs_define
class CreateParagraphBulletsRequest:
    """ Creates bullets for all of the paragraphs that overlap with the given range. The nesting level of each paragraph
    will be determined by counting leading tabs in front of each paragraph. To avoid excess space between the bullet and
    the corresponding paragraph, these leading tabs are removed by this request. This may change the indices of parts of
    the text. If the paragraph immediately before paragraphs being updated is in a list with a matching preset, the
    paragraphs being updated are added to that preceding list.

        Attributes:
            bullet_preset (CreateParagraphBulletsRequestBulletPreset | Unset): The kinds of bullet glyphs to be used.
            range_ (Range | Unset): Specifies a contiguous range of text.
     """

    bullet_preset: CreateParagraphBulletsRequestBulletPreset | Unset = UNSET
    range_: Range | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.range_ import Range
        bullet_preset: str | Unset = UNSET
        if not isinstance(self.bullet_preset, Unset):
            bullet_preset = self.bullet_preset.value


        range_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.range_, Unset):
            range_ = self.range_.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if bullet_preset is not UNSET:
            field_dict["bulletPreset"] = bullet_preset
        if range_ is not UNSET:
            field_dict["range"] = range_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.range_ import Range
        d = dict(src_dict)
        _bullet_preset = d.pop("bulletPreset", UNSET)
        bullet_preset: CreateParagraphBulletsRequestBulletPreset | Unset
        if isinstance(_bullet_preset,  Unset):
            bullet_preset = UNSET
        else:
            bullet_preset = CreateParagraphBulletsRequestBulletPreset(_bullet_preset)




        _range_ = d.pop("range", UNSET)
        range_: Range | Unset
        if isinstance(_range_,  Unset):
            range_ = UNSET
        else:
            range_ = Range.from_dict(_range_)




        create_paragraph_bullets_request = cls(
            bullet_preset=bullet_preset,
            range_=range_,
        )


        create_paragraph_bullets_request.additional_properties = d
        return create_paragraph_bullets_request

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
