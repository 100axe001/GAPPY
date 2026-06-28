from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.tab_stop_alignment import TabStopAlignment
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.dimension import Dimension





T = TypeVar("T", bound="TabStop")



@_attrs_define
class TabStop:
    """ A tab stop within a paragraph.

        Attributes:
            alignment (TabStopAlignment | Unset): The alignment of this tab stop. If unset, the value defaults to START.
            offset (Dimension | Unset): A magnitude in a single direction in the specified units.
     """

    alignment: TabStopAlignment | Unset = UNSET
    offset: Dimension | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.dimension import Dimension
        alignment: str | Unset = UNSET
        if not isinstance(self.alignment, Unset):
            alignment = self.alignment.value


        offset: dict[str, Any] | Unset = UNSET
        if not isinstance(self.offset, Unset):
            offset = self.offset.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if alignment is not UNSET:
            field_dict["alignment"] = alignment
        if offset is not UNSET:
            field_dict["offset"] = offset

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dimension import Dimension
        d = dict(src_dict)
        _alignment = d.pop("alignment", UNSET)
        alignment: TabStopAlignment | Unset
        if isinstance(_alignment,  Unset):
            alignment = UNSET
        else:
            alignment = TabStopAlignment(_alignment)




        _offset = d.pop("offset", UNSET)
        offset: Dimension | Unset
        if isinstance(_offset,  Unset):
            offset = UNSET
        else:
            offset = Dimension.from_dict(_offset)




        tab_stop = cls(
            alignment=alignment,
            offset=offset,
        )


        tab_stop.additional_properties = d
        return tab_stop

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
