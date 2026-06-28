from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.visibility_type import VisibilityType
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="Visibility")



@_attrs_define
class Visibility:
    """ The group or role to which this item is visible.

        Attributes:
            identifier (None | str | Unset): The ID of the group or the name of the role that visibility of this item is
                restricted to.
            type_ (VisibilityType | Unset): Whether visibility of this item is restricted to a group or role.
            value (str | Unset): The name of the group or role that visibility of this item is restricted to. Please note
                that the name of a group is mutable, to reliably identify a group use `identifier`.
     """

    identifier: None | str | Unset = UNSET
    type_: VisibilityType | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        identifier: None | str | Unset
        if isinstance(self.identifier, Unset):
            identifier = UNSET
        else:
            identifier = self.identifier

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value


        value = self.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if type_ is not UNSET:
            field_dict["type"] = type_
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_identifier(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        identifier = _parse_identifier(d.pop("identifier", UNSET))


        _type_ = d.pop("type", UNSET)
        type_: VisibilityType | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = VisibilityType(_type_)




        value = d.pop("value", UNSET)

        visibility = cls(
            identifier=identifier,
            type_=type_,
            value=value,
        )


        visibility.additional_properties = d
        return visibility

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
