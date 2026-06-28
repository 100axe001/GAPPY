from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ModifyThreadRequest")



@_attrs_define
class ModifyThreadRequest:
    """ 
        Attributes:
            add_label_ids (list[str] | Unset): A list of IDs of labels to add to this thread. You can add up to 100 labels
                with each update.
            remove_label_ids (list[str] | Unset): A list of IDs of labels to remove from this thread. You can remove up to
                100 labels with each update.
     """

    add_label_ids: list[str] | Unset = UNSET
    remove_label_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        add_label_ids: list[str] | Unset = UNSET
        if not isinstance(self.add_label_ids, Unset):
            add_label_ids = self.add_label_ids



        remove_label_ids: list[str] | Unset = UNSET
        if not isinstance(self.remove_label_ids, Unset):
            remove_label_ids = self.remove_label_ids




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if add_label_ids is not UNSET:
            field_dict["addLabelIds"] = add_label_ids
        if remove_label_ids is not UNSET:
            field_dict["removeLabelIds"] = remove_label_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        add_label_ids = cast(list[str], d.pop("addLabelIds", UNSET))


        remove_label_ids = cast(list[str], d.pop("removeLabelIds", UNSET))


        modify_thread_request = cls(
            add_label_ids=add_label_ids,
            remove_label_ids=remove_label_ids,
        )


        modify_thread_request.additional_properties = d
        return modify_thread_request

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
