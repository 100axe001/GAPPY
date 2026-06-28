from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.range_ import Range
  from ..models.text_style import TextStyle





T = TypeVar("T", bound="UpdateTextStyleRequest")



@_attrs_define
class UpdateTextStyleRequest:
    """ Update the styling of text.

        Attributes:
            fields (str | Unset): The fields that should be updated. At least one field must be specified. The root
                `text_style` is implied and should not be specified. A single `"*"` can be used as short-hand for listing every
                field. For example, to update the text style to bold, set `fields` to `"bold"`. To reset a property to its
                default value, include its field name in the field mask but leave the field itself unset.
            range_ (Range | Unset): Specifies a contiguous range of text.
            text_style (TextStyle | Unset): Represents the styling that can be applied to text. Inherited text styles are
                represented as unset fields in this message. A text style's parent depends on where the text style is defined: *
                The TextStyle of text in a Paragraph inherits from the paragraph's corresponding named style type. * The
                TextStyle on a named style inherits from the normal text named style. * The TextStyle of the normal text named
                style inherits from the default text style in the Docs editor. * The TextStyle on a Paragraph element that's
                contained in a table may inherit its text style from the table style. If the text style does not inherit from a
                parent, unsetting fields will revert the style to a value matching the defaults in the Docs editor.
     """

    fields: str | Unset = UNSET
    range_: Range | Unset = UNSET
    text_style: TextStyle | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.range_ import Range
        from ..models.text_style import TextStyle
        fields = self.fields

        range_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.range_, Unset):
            range_ = self.range_.to_dict()

        text_style: dict[str, Any] | Unset = UNSET
        if not isinstance(self.text_style, Unset):
            text_style = self.text_style.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if fields is not UNSET:
            field_dict["fields"] = fields
        if range_ is not UNSET:
            field_dict["range"] = range_
        if text_style is not UNSET:
            field_dict["textStyle"] = text_style

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.range_ import Range
        from ..models.text_style import TextStyle
        d = dict(src_dict)
        fields = d.pop("fields", UNSET)

        _range_ = d.pop("range", UNSET)
        range_: Range | Unset
        if isinstance(_range_,  Unset):
            range_ = UNSET
        else:
            range_ = Range.from_dict(_range_)




        _text_style = d.pop("textStyle", UNSET)
        text_style: TextStyle | Unset
        if isinstance(_text_style,  Unset):
            text_style = UNSET
        else:
            text_style = TextStyle.from_dict(_text_style)




        update_text_style_request = cls(
            fields=fields,
            range_=range_,
            text_style=text_style,
        )


        update_text_style_request.additional_properties = d
        return update_text_style_request

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
