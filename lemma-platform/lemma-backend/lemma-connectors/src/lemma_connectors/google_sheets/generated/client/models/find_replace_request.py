from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.grid_range import GridRange





T = TypeVar("T", bound="FindReplaceRequest")



@_attrs_define
class FindReplaceRequest:
    """ Finds and replaces data in cells over a range, sheet, or all sheets.

        Attributes:
            all_sheets (bool | Unset): True to find/replace over all sheets.
            find (str | Unset): The value to search.
            include_formulas (bool | Unset): True if the search should include cells with formulas. False to skip cells with
                formulas.
            match_case (bool | Unset): True if the search is case sensitive.
            match_entire_cell (bool | Unset): True if the find value should match the entire cell.
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
            replacement (str | Unset): The value to use as the replacement.
            search_by_regex (bool | Unset): True if the find value is a regex. The regular expression and replacement should
                follow Java regex rules at https://docs.oracle.com/javase/8/docs/api/java/util/regex/Pattern.html. The
                replacement string is allowed to refer to capturing groups. For example, if one cell has the contents `"Google
                Sheets"` and another has `"Google Docs"`, then searching for `"o.* (.*)"` with a replacement of `"$1 Rocks"`
                would change the contents of the cells to `"GSheets Rocks"` and `"GDocs Rocks"` respectively.
            sheet_id (int | Unset): The sheet to find/replace over.
     """

    all_sheets: bool | Unset = UNSET
    find: str | Unset = UNSET
    include_formulas: bool | Unset = UNSET
    match_case: bool | Unset = UNSET
    match_entire_cell: bool | Unset = UNSET
    range_: GridRange | Unset = UNSET
    replacement: str | Unset = UNSET
    search_by_regex: bool | Unset = UNSET
    sheet_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.grid_range import GridRange
        all_sheets = self.all_sheets

        find = self.find

        include_formulas = self.include_formulas

        match_case = self.match_case

        match_entire_cell = self.match_entire_cell

        range_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.range_, Unset):
            range_ = self.range_.to_dict()

        replacement = self.replacement

        search_by_regex = self.search_by_regex

        sheet_id = self.sheet_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if all_sheets is not UNSET:
            field_dict["allSheets"] = all_sheets
        if find is not UNSET:
            field_dict["find"] = find
        if include_formulas is not UNSET:
            field_dict["includeFormulas"] = include_formulas
        if match_case is not UNSET:
            field_dict["matchCase"] = match_case
        if match_entire_cell is not UNSET:
            field_dict["matchEntireCell"] = match_entire_cell
        if range_ is not UNSET:
            field_dict["range"] = range_
        if replacement is not UNSET:
            field_dict["replacement"] = replacement
        if search_by_regex is not UNSET:
            field_dict["searchByRegex"] = search_by_regex
        if sheet_id is not UNSET:
            field_dict["sheetId"] = sheet_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.grid_range import GridRange
        d = dict(src_dict)
        all_sheets = d.pop("allSheets", UNSET)

        find = d.pop("find", UNSET)

        include_formulas = d.pop("includeFormulas", UNSET)

        match_case = d.pop("matchCase", UNSET)

        match_entire_cell = d.pop("matchEntireCell", UNSET)

        _range_ = d.pop("range", UNSET)
        range_: GridRange | Unset
        if isinstance(_range_,  Unset):
            range_ = UNSET
        else:
            range_ = GridRange.from_dict(_range_)




        replacement = d.pop("replacement", UNSET)

        search_by_regex = d.pop("searchByRegex", UNSET)

        sheet_id = d.pop("sheetId", UNSET)

        find_replace_request = cls(
            all_sheets=all_sheets,
            find=find,
            include_formulas=include_formulas,
            match_case=match_case,
            match_entire_cell=match_entire_cell,
            range_=range_,
            replacement=replacement,
            search_by_regex=search_by_regex,
            sheet_id=sheet_id,
        )


        find_replace_request.additional_properties = d
        return find_replace_request

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
