from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="WeightedFontFamily")



@_attrs_define
class WeightedFontFamily:
    """ Represents a font family and weight of text.

        Attributes:
            font_family (str | Unset): The font family of the text. The font family can be any font from the Font menu in
                Docs or from [Google Fonts] (https://fonts.google.com/). If the font name is unrecognized, the text is rendered
                in `Arial`.
            weight (int | Unset): The weight of the font. This field can have any value that's a multiple of `100` between
                `100` and `900`, inclusive. This range corresponds to the numerical values described in the CSS 2.1
                Specification, [section 15.6](https://www.w3.org/TR/CSS21/fonts.html#font-boldness), with non-numerical values
                disallowed. The default value is `400` ("normal"). The font weight makes up just one component of the rendered
                font weight. A combination of the `weight` and the text style's resolved `bold` value determine the rendered
                weight, after accounting for inheritance: * If the text is bold and the weight is less than `400`, the rendered
                weight is 400. * If the text is bold and the weight is greater than or equal to `400` but is less than `700`,
                the rendered weight is `700`. * If the weight is greater than or equal to `700`, the rendered weight is equal to
                the weight. * If the text is not bold, the rendered weight is equal to the weight.
     """

    font_family: str | Unset = UNSET
    weight: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        font_family = self.font_family

        weight = self.weight


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if font_family is not UNSET:
            field_dict["fontFamily"] = font_family
        if weight is not UNSET:
            field_dict["weight"] = weight

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        font_family = d.pop("fontFamily", UNSET)

        weight = d.pop("weight", UNSET)

        weighted_font_family = cls(
            font_family=font_family,
            weight=weight,
        )


        weighted_font_family.additional_properties = d
        return weighted_font_family

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
