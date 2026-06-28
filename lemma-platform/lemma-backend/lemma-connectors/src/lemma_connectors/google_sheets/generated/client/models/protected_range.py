from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.editors import Editors
  from ..models.grid_range import GridRange





T = TypeVar("T", bound="ProtectedRange")



@_attrs_define
class ProtectedRange:
    """ A protected range.

        Attributes:
            description (str | Unset): The description of this protected range.
            editors (Editors | Unset): The editors of a protected range.
            named_range_id (str | Unset): The named range this protected range is backed by, if any. When writing, only one
                of range or named_range_id may be set.
            protected_range_id (int | Unset): The ID of the protected range. This field is read-only.
            range_ (GridRange | Unset): A range on a sheet. All indexes are zero-based. Indexes are half open, i.e. the
                start index is inclusive and the end index is exclusive -- [start_index, end_index). Missing indexes indicate
                the range is unbounded on that side. For example, if `"Sheet1"` is sheet ID 123456, then: `Sheet1!A1:A1 ==
                sheet_id: 123456, start_row_index: 0, end_row_index: 1, start_column_index: 0, end_column_index: 1`
                `Sheet1!A3:B4 == sheet_id: 123456, start_row_index: 2, end_row_index: 4, start_column_index: 0,
                end_column_index: 2` `Sheet1!A:B == sheet_id: 123456, start_column_index: 0, end_column_index: 2` `Sheet1!A5:B
                == sheet_id: 123456, start_row_index: 4, start_column_index: 0, end_column_index: 2` `Sheet1 == sheet_id:
                123456` The start index must always be less than or equal to the end index. If the start index equals the end
                index, then the range is empty. Empty ranges are typically not meaningful and are usually rendered in the UI as
                `#REF!`.
            requesting_user_can_edit (bool | Unset): True if the user who requested this protected range can edit the
                protected area. This field is read-only.
            unprotected_ranges (list[GridRange] | Unset): The list of unprotected ranges within a protected sheet.
                Unprotected ranges are only supported on protected sheets.
            warning_only (bool | Unset): True if this protected range will show a warning when editing. Warning-based
                protection means that every user can edit data in the protected range, except editing will prompt a warning
                asking the user to confirm the edit. When writing: if this field is true, then editors is ignored. Additionally,
                if this field is changed from true to false and the `editors` field is not set (nor included in the field mask),
                then the editors will be set to all the editors in the document.
     """

    description: str | Unset = UNSET
    editors: Editors | Unset = UNSET
    named_range_id: str | Unset = UNSET
    protected_range_id: int | Unset = UNSET
    range_: GridRange | Unset = UNSET
    requesting_user_can_edit: bool | Unset = UNSET
    unprotected_ranges: list[GridRange] | Unset = UNSET
    warning_only: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.editors import Editors
        from ..models.grid_range import GridRange
        description = self.description

        editors: dict[str, Any] | Unset = UNSET
        if not isinstance(self.editors, Unset):
            editors = self.editors.to_dict()

        named_range_id = self.named_range_id

        protected_range_id = self.protected_range_id

        range_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.range_, Unset):
            range_ = self.range_.to_dict()

        requesting_user_can_edit = self.requesting_user_can_edit

        unprotected_ranges: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.unprotected_ranges, Unset):
            unprotected_ranges = []
            for unprotected_ranges_item_data in self.unprotected_ranges:
                unprotected_ranges_item = unprotected_ranges_item_data.to_dict()
                unprotected_ranges.append(unprotected_ranges_item)



        warning_only = self.warning_only


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
        if editors is not UNSET:
            field_dict["editors"] = editors
        if named_range_id is not UNSET:
            field_dict["namedRangeId"] = named_range_id
        if protected_range_id is not UNSET:
            field_dict["protectedRangeId"] = protected_range_id
        if range_ is not UNSET:
            field_dict["range"] = range_
        if requesting_user_can_edit is not UNSET:
            field_dict["requestingUserCanEdit"] = requesting_user_can_edit
        if unprotected_ranges is not UNSET:
            field_dict["unprotectedRanges"] = unprotected_ranges
        if warning_only is not UNSET:
            field_dict["warningOnly"] = warning_only

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.editors import Editors
        from ..models.grid_range import GridRange
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        _editors = d.pop("editors", UNSET)
        editors: Editors | Unset
        if isinstance(_editors,  Unset):
            editors = UNSET
        else:
            editors = Editors.from_dict(_editors)




        named_range_id = d.pop("namedRangeId", UNSET)

        protected_range_id = d.pop("protectedRangeId", UNSET)

        _range_ = d.pop("range", UNSET)
        range_: GridRange | Unset
        if isinstance(_range_,  Unset):
            range_ = UNSET
        else:
            range_ = GridRange.from_dict(_range_)




        requesting_user_can_edit = d.pop("requestingUserCanEdit", UNSET)

        _unprotected_ranges = d.pop("unprotectedRanges", UNSET)
        unprotected_ranges: list[GridRange] | Unset = UNSET
        if _unprotected_ranges is not UNSET:
            unprotected_ranges = []
            for unprotected_ranges_item_data in _unprotected_ranges:
                unprotected_ranges_item = GridRange.from_dict(unprotected_ranges_item_data)



                unprotected_ranges.append(unprotected_ranges_item)


        warning_only = d.pop("warningOnly", UNSET)

        protected_range = cls(
            description=description,
            editors=editors,
            named_range_id=named_range_id,
            protected_range_id=protected_range_id,
            range_=range_,
            requesting_user_can_edit=requesting_user_can_edit,
            unprotected_ranges=unprotected_ranges,
            warning_only=warning_only,
        )


        protected_range.additional_properties = d
        return protected_range

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
