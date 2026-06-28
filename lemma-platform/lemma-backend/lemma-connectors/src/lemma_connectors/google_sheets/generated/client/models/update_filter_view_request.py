from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.filter_view import FilterView





T = TypeVar("T", bound="UpdateFilterViewRequest")



@_attrs_define
class UpdateFilterViewRequest:
    """ Updates properties of the filter view.

        Attributes:
            fields (str | Unset): The fields that should be updated. At least one field must be specified. The root `filter`
                is implied and should not be specified. A single `"*"` can be used as short-hand for listing every field.
            filter_ (FilterView | Unset): A filter view.
     """

    fields: str | Unset = UNSET
    filter_: FilterView | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.filter_view import FilterView
        fields = self.fields

        filter_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.filter_, Unset):
            filter_ = self.filter_.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if fields is not UNSET:
            field_dict["fields"] = fields
        if filter_ is not UNSET:
            field_dict["filter"] = filter_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.filter_view import FilterView
        d = dict(src_dict)
        fields = d.pop("fields", UNSET)

        _filter_ = d.pop("filter", UNSET)
        filter_: FilterView | Unset
        if isinstance(_filter_,  Unset):
            filter_ = UNSET
        else:
            filter_ = FilterView.from_dict(_filter_)




        update_filter_view_request = cls(
            fields=fields,
            filter_=filter_,
        )


        update_filter_view_request.additional_properties = d
        return update_filter_view_request

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
