from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.paragraph_border_dash_style import ParagraphBorderDashStyle
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.dimension import Dimension
  from ..models.optional_color import OptionalColor





T = TypeVar("T", bound="ParagraphBorder")



@_attrs_define
class ParagraphBorder:
    """ A border around a paragraph.

        Attributes:
            color (OptionalColor | Unset): A color that can either be fully opaque or fully transparent.
            dash_style (ParagraphBorderDashStyle | Unset): The dash style of the border.
            padding (Dimension | Unset): A magnitude in a single direction in the specified units.
            width (Dimension | Unset): A magnitude in a single direction in the specified units.
     """

    color: OptionalColor | Unset = UNSET
    dash_style: ParagraphBorderDashStyle | Unset = UNSET
    padding: Dimension | Unset = UNSET
    width: Dimension | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.dimension import Dimension
        from ..models.optional_color import OptionalColor
        color: dict[str, Any] | Unset = UNSET
        if not isinstance(self.color, Unset):
            color = self.color.to_dict()

        dash_style: str | Unset = UNSET
        if not isinstance(self.dash_style, Unset):
            dash_style = self.dash_style.value


        padding: dict[str, Any] | Unset = UNSET
        if not isinstance(self.padding, Unset):
            padding = self.padding.to_dict()

        width: dict[str, Any] | Unset = UNSET
        if not isinstance(self.width, Unset):
            width = self.width.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if color is not UNSET:
            field_dict["color"] = color
        if dash_style is not UNSET:
            field_dict["dashStyle"] = dash_style
        if padding is not UNSET:
            field_dict["padding"] = padding
        if width is not UNSET:
            field_dict["width"] = width

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dimension import Dimension
        from ..models.optional_color import OptionalColor
        d = dict(src_dict)
        _color = d.pop("color", UNSET)
        color: OptionalColor | Unset
        if isinstance(_color,  Unset):
            color = UNSET
        else:
            color = OptionalColor.from_dict(_color)




        _dash_style = d.pop("dashStyle", UNSET)
        dash_style: ParagraphBorderDashStyle | Unset
        if isinstance(_dash_style,  Unset):
            dash_style = UNSET
        else:
            dash_style = ParagraphBorderDashStyle(_dash_style)




        _padding = d.pop("padding", UNSET)
        padding: Dimension | Unset
        if isinstance(_padding,  Unset):
            padding = UNSET
        else:
            padding = Dimension.from_dict(_padding)




        _width = d.pop("width", UNSET)
        width: Dimension | Unset
        if isinstance(_width,  Unset):
            width = UNSET
        else:
            width = Dimension.from_dict(_width)




        paragraph_border = cls(
            color=color,
            dash_style=dash_style,
            padding=padding,
            width=width,
        )


        paragraph_border.additional_properties = d
        return paragraph_border

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
