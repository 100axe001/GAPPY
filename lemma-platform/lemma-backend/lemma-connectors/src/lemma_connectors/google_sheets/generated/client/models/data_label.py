from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.data_label_placement import DataLabelPlacement
from ..models.data_label_type import DataLabelType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.chart_data import ChartData
  from ..models.text_format import TextFormat





T = TypeVar("T", bound="DataLabel")



@_attrs_define
class DataLabel:
    """ Settings for one set of data labels. Data labels are annotations that appear next to a set of data, such as the
    points on a line chart, and provide additional information about what the data represents, such as a text
    representation of the value behind that point on the graph.

        Attributes:
            custom_label_data (ChartData | Unset): The data included in a domain or series.
            placement (DataLabelPlacement | Unset): The placement of the data label relative to the labeled data.
            text_format (TextFormat | Unset): The format of a run of text in a cell. Absent values indicate that the field
                isn't specified.
            type_ (DataLabelType | Unset): The type of the data label.
     """

    custom_label_data: ChartData | Unset = UNSET
    placement: DataLabelPlacement | Unset = UNSET
    text_format: TextFormat | Unset = UNSET
    type_: DataLabelType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.chart_data import ChartData
        from ..models.text_format import TextFormat
        custom_label_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.custom_label_data, Unset):
            custom_label_data = self.custom_label_data.to_dict()

        placement: str | Unset = UNSET
        if not isinstance(self.placement, Unset):
            placement = self.placement.value


        text_format: dict[str, Any] | Unset = UNSET
        if not isinstance(self.text_format, Unset):
            text_format = self.text_format.to_dict()

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if custom_label_data is not UNSET:
            field_dict["customLabelData"] = custom_label_data
        if placement is not UNSET:
            field_dict["placement"] = placement
        if text_format is not UNSET:
            field_dict["textFormat"] = text_format
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chart_data import ChartData
        from ..models.text_format import TextFormat
        d = dict(src_dict)
        _custom_label_data = d.pop("customLabelData", UNSET)
        custom_label_data: ChartData | Unset
        if isinstance(_custom_label_data,  Unset):
            custom_label_data = UNSET
        else:
            custom_label_data = ChartData.from_dict(_custom_label_data)




        _placement = d.pop("placement", UNSET)
        placement: DataLabelPlacement | Unset
        if isinstance(_placement,  Unset):
            placement = UNSET
        else:
            placement = DataLabelPlacement(_placement)




        _text_format = d.pop("textFormat", UNSET)
        text_format: TextFormat | Unset
        if isinstance(_text_format,  Unset):
            text_format = UNSET
        else:
            text_format = TextFormat.from_dict(_text_format)




        _type_ = d.pop("type", UNSET)
        type_: DataLabelType | Unset
        if isinstance(_type_,  Unset):
            type_ = UNSET
        else:
            type_ = DataLabelType(_type_)




        data_label = cls(
            custom_label_data=custom_label_data,
            placement=placement,
            text_format=text_format,
            type_=type_,
        )


        data_label.additional_properties = d
        return data_label

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
