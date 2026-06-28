from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.paste_data_request_type import PasteDataRequestType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.grid_coordinate import GridCoordinate





T = TypeVar("T", bound="PasteDataRequest")



@_attrs_define
class PasteDataRequest:
    """ Inserts data into the spreadsheet starting at the specified coordinate.

        Attributes:
            coordinate (GridCoordinate | Unset): A coordinate in a sheet. All indexes are zero-based.
            data (str | Unset): The data to insert.
            delimiter (str | Unset): The delimiter in the data.
            html (bool | Unset): True if the data is HTML.
            type_ (PasteDataRequestType | Unset): How the data should be pasted.
     """

    coordinate: GridCoordinate | Unset = UNSET
    data: str | Unset = UNSET
    delimiter: str | Unset = UNSET
    html: bool | Unset = UNSET
    type_: PasteDataRequestType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.grid_coordinate import GridCoordinate
        coordinate: dict[str, Any] | Unset = UNSET
        if not isinstance(self.coordinate, Unset):
            coordinate = self.coordinate.to_dict()

        data = self.data

        delimiter = self.delimiter

        html = self.html

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if coordinate is not UNSET:
            field_dict["coordinate"] = coordinate
        if data is not UNSET:
            field_dict["data"] = data
        if delimiter is not UNSET:
            field_dict["delimiter"] = delimiter
        if html is not UNSET:
            field_dict["html"] = html
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.grid_coordinate import GridCoordinate
        d = dict(src_dict)
        _coordinate = d.pop("coordinate", UNSET)
        coordinate: GridCoordinate | Unset
        if isinstance(_coordinate,  Unset):
            coordinate = UNSET
        else:
            coordinate = GridCoordinate.from_dict(_coordinate)




        data = d.pop("data", UNSET)

        delimiter = d.pop("delimiter", UNSET)

        html = d.pop("html", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: PasteDataRequestType | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = PasteDataRequestType(_type_)




        paste_data_request = cls(
            coordinate=coordinate,
            data=data,
            delimiter=delimiter,
            html=html,
            type_=type_,
        )


        paste_data_request.additional_properties = d
        return paste_data_request

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
