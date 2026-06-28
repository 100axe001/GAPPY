from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.section_style_column_separator_style import SectionStyleColumnSeparatorStyle
from ..models.section_style_content_direction import SectionStyleContentDirection
from ..models.section_style_section_type import SectionStyleSectionType
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.dimension import Dimension
  from ..models.section_column_properties import SectionColumnProperties





T = TypeVar("T", bound="SectionStyle")



@_attrs_define
class SectionStyle:
    """ The styling that applies to a section.

        Attributes:
            column_properties (list[SectionColumnProperties] | Unset): The section's columns properties. If empty, the
                section contains one column with the default properties in the Docs editor. A section can be updated to have no
                more than 3 columns. When updating this property, setting a concrete value is required. Unsetting this property
                will result in a 400 bad request error.
            column_separator_style (SectionStyleColumnSeparatorStyle | Unset): The style of column separators. This style
                can be set even when there's one column in the section. When updating this property, setting a concrete value is
                required. Unsetting this property results in a 400 bad request error.
            content_direction (SectionStyleContentDirection | Unset): The content direction of this section. If unset, the
                value defaults to LEFT_TO_RIGHT. When updating this property, setting a concrete value is required. Unsetting
                this property results in a 400 bad request error.
            default_footer_id (str | Unset): The ID of the default footer. If unset, the value inherits from the previous
                SectionBreak's SectionStyle. If the value is unset in the first SectionBreak, it inherits from DocumentStyle's
                default_footer_id. This property is read-only.
            default_header_id (str | Unset): The ID of the default header. If unset, the value inherits from the previous
                SectionBreak's SectionStyle. If the value is unset in the first SectionBreak, it inherits from DocumentStyle's
                default_header_id. This property is read-only.
            even_page_footer_id (str | Unset): The ID of the footer used only for even pages. If the value of
                DocumentStyle's use_even_page_header_footer is true, this value is used for the footers on even pages in the
                section. If it is false, the footers on even pages use the default_footer_id. If unset, the value inherits from
                the previous SectionBreak's SectionStyle. If the value is unset in the first SectionBreak, it inherits from
                DocumentStyle's even_page_footer_id. This property is read-only.
            even_page_header_id (str | Unset): The ID of the header used only for even pages. If the value of
                DocumentStyle's use_even_page_header_footer is true, this value is used for the headers on even pages in the
                section. If it is false, the headers on even pages use the default_header_id. If unset, the value inherits from
                the previous SectionBreak's SectionStyle. If the value is unset in the first SectionBreak, it inherits from
                DocumentStyle's even_page_header_id. This property is read-only.
            first_page_footer_id (str | Unset): The ID of the footer used only for the first page of the section. If
                use_first_page_header_footer is true, this value is used for the footer on the first page of the section. If
                it's false, the footer on the first page of the section uses the default_footer_id. If unset, the value inherits
                from the previous SectionBreak's SectionStyle. If the value is unset in the first SectionBreak, it inherits from
                DocumentStyle's first_page_footer_id. This property is read-only.
            first_page_header_id (str | Unset): The ID of the header used only for the first page of the section. If
                use_first_page_header_footer is true, this value is used for the header on the first page of the section. If
                it's false, the header on the first page of the section uses the default_header_id. If unset, the value inherits
                from the previous SectionBreak's SectionStyle. If the value is unset in the first SectionBreak, it inherits from
                DocumentStyle's first_page_header_id. This property is read-only.
            margin_bottom (Dimension | Unset): A magnitude in a single direction in the specified units.
            margin_footer (Dimension | Unset): A magnitude in a single direction in the specified units.
            margin_header (Dimension | Unset): A magnitude in a single direction in the specified units.
            margin_left (Dimension | Unset): A magnitude in a single direction in the specified units.
            margin_right (Dimension | Unset): A magnitude in a single direction in the specified units.
            margin_top (Dimension | Unset): A magnitude in a single direction in the specified units.
            page_number_start (int | Unset): The page number from which to start counting the number of pages for this
                section. If unset, page numbering continues from the previous section. If the value is unset in the first
                SectionBreak, refer to DocumentStyle's page_number_start. When updating this property, setting a concrete value
                is required. Unsetting this property results in a 400 bad request error.
            section_type (SectionStyleSectionType | Unset): Output only. The type of section.
            use_first_page_header_footer (bool | Unset): Indicates whether to use the first page header / footer IDs for the
                first page of the section. If unset, it inherits from DocumentStyle's use_first_page_header_footer for the first
                section. If the value is unset for subsequent sectors, it should be interpreted as false. When updating this
                property, setting a concrete value is required. Unsetting this property results in a 400 bad request error.
     """

    column_properties: list[SectionColumnProperties] | Unset = UNSET
    column_separator_style: SectionStyleColumnSeparatorStyle | Unset = UNSET
    content_direction: SectionStyleContentDirection | Unset = UNSET
    default_footer_id: str | Unset = UNSET
    default_header_id: str | Unset = UNSET
    even_page_footer_id: str | Unset = UNSET
    even_page_header_id: str | Unset = UNSET
    first_page_footer_id: str | Unset = UNSET
    first_page_header_id: str | Unset = UNSET
    margin_bottom: Dimension | Unset = UNSET
    margin_footer: Dimension | Unset = UNSET
    margin_header: Dimension | Unset = UNSET
    margin_left: Dimension | Unset = UNSET
    margin_right: Dimension | Unset = UNSET
    margin_top: Dimension | Unset = UNSET
    page_number_start: int | Unset = UNSET
    section_type: SectionStyleSectionType | Unset = UNSET
    use_first_page_header_footer: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.dimension import Dimension
        from ..models.section_column_properties import SectionColumnProperties
        column_properties: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.column_properties, Unset):
            column_properties = []
            for column_properties_item_data in self.column_properties:
                column_properties_item = column_properties_item_data.to_dict()
                column_properties.append(column_properties_item)



        column_separator_style: str | Unset = UNSET
        if not isinstance(self.column_separator_style, Unset):
            column_separator_style = self.column_separator_style.value


        content_direction: str | Unset = UNSET
        if not isinstance(self.content_direction, Unset):
            content_direction = self.content_direction.value


        default_footer_id = self.default_footer_id

        default_header_id = self.default_header_id

        even_page_footer_id = self.even_page_footer_id

        even_page_header_id = self.even_page_header_id

        first_page_footer_id = self.first_page_footer_id

        first_page_header_id = self.first_page_header_id

        margin_bottom: dict[str, Any] | Unset = UNSET
        if not isinstance(self.margin_bottom, Unset):
            margin_bottom = self.margin_bottom.to_dict()

        margin_footer: dict[str, Any] | Unset = UNSET
        if not isinstance(self.margin_footer, Unset):
            margin_footer = self.margin_footer.to_dict()

        margin_header: dict[str, Any] | Unset = UNSET
        if not isinstance(self.margin_header, Unset):
            margin_header = self.margin_header.to_dict()

        margin_left: dict[str, Any] | Unset = UNSET
        if not isinstance(self.margin_left, Unset):
            margin_left = self.margin_left.to_dict()

        margin_right: dict[str, Any] | Unset = UNSET
        if not isinstance(self.margin_right, Unset):
            margin_right = self.margin_right.to_dict()

        margin_top: dict[str, Any] | Unset = UNSET
        if not isinstance(self.margin_top, Unset):
            margin_top = self.margin_top.to_dict()

        page_number_start = self.page_number_start

        section_type: str | Unset = UNSET
        if not isinstance(self.section_type, Unset):
            section_type = self.section_type.value


        use_first_page_header_footer = self.use_first_page_header_footer


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if column_properties is not UNSET:
            field_dict["columnProperties"] = column_properties
        if column_separator_style is not UNSET:
            field_dict["columnSeparatorStyle"] = column_separator_style
        if content_direction is not UNSET:
            field_dict["contentDirection"] = content_direction
        if default_footer_id is not UNSET:
            field_dict["defaultFooterId"] = default_footer_id
        if default_header_id is not UNSET:
            field_dict["defaultHeaderId"] = default_header_id
        if even_page_footer_id is not UNSET:
            field_dict["evenPageFooterId"] = even_page_footer_id
        if even_page_header_id is not UNSET:
            field_dict["evenPageHeaderId"] = even_page_header_id
        if first_page_footer_id is not UNSET:
            field_dict["firstPageFooterId"] = first_page_footer_id
        if first_page_header_id is not UNSET:
            field_dict["firstPageHeaderId"] = first_page_header_id
        if margin_bottom is not UNSET:
            field_dict["marginBottom"] = margin_bottom
        if margin_footer is not UNSET:
            field_dict["marginFooter"] = margin_footer
        if margin_header is not UNSET:
            field_dict["marginHeader"] = margin_header
        if margin_left is not UNSET:
            field_dict["marginLeft"] = margin_left
        if margin_right is not UNSET:
            field_dict["marginRight"] = margin_right
        if margin_top is not UNSET:
            field_dict["marginTop"] = margin_top
        if page_number_start is not UNSET:
            field_dict["pageNumberStart"] = page_number_start
        if section_type is not UNSET:
            field_dict["sectionType"] = section_type
        if use_first_page_header_footer is not UNSET:
            field_dict["useFirstPageHeaderFooter"] = use_first_page_header_footer

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dimension import Dimension
        from ..models.section_column_properties import SectionColumnProperties
        d = dict(src_dict)
        _column_properties = d.pop("columnProperties", UNSET)
        column_properties: list[SectionColumnProperties] | Unset = UNSET
        if _column_properties is not UNSET:
            column_properties = []
            for column_properties_item_data in _column_properties:
                column_properties_item = SectionColumnProperties.from_dict(column_properties_item_data)



                column_properties.append(column_properties_item)


        _column_separator_style = d.pop("columnSeparatorStyle", UNSET)
        column_separator_style: SectionStyleColumnSeparatorStyle | Unset
        if isinstance(_column_separator_style,  Unset):
            column_separator_style = UNSET
        else:
            column_separator_style = SectionStyleColumnSeparatorStyle(_column_separator_style)




        _content_direction = d.pop("contentDirection", UNSET)
        content_direction: SectionStyleContentDirection | Unset
        if isinstance(_content_direction,  Unset):
            content_direction = UNSET
        else:
            content_direction = SectionStyleContentDirection(_content_direction)




        default_footer_id = d.pop("defaultFooterId", UNSET)

        default_header_id = d.pop("defaultHeaderId", UNSET)

        even_page_footer_id = d.pop("evenPageFooterId", UNSET)

        even_page_header_id = d.pop("evenPageHeaderId", UNSET)

        first_page_footer_id = d.pop("firstPageFooterId", UNSET)

        first_page_header_id = d.pop("firstPageHeaderId", UNSET)

        _margin_bottom = d.pop("marginBottom", UNSET)
        margin_bottom: Dimension | Unset
        if isinstance(_margin_bottom,  Unset):
            margin_bottom = UNSET
        else:
            margin_bottom = Dimension.from_dict(_margin_bottom)




        _margin_footer = d.pop("marginFooter", UNSET)
        margin_footer: Dimension | Unset
        if isinstance(_margin_footer,  Unset):
            margin_footer = UNSET
        else:
            margin_footer = Dimension.from_dict(_margin_footer)




        _margin_header = d.pop("marginHeader", UNSET)
        margin_header: Dimension | Unset
        if isinstance(_margin_header,  Unset):
            margin_header = UNSET
        else:
            margin_header = Dimension.from_dict(_margin_header)




        _margin_left = d.pop("marginLeft", UNSET)
        margin_left: Dimension | Unset
        if isinstance(_margin_left,  Unset):
            margin_left = UNSET
        else:
            margin_left = Dimension.from_dict(_margin_left)




        _margin_right = d.pop("marginRight", UNSET)
        margin_right: Dimension | Unset
        if isinstance(_margin_right,  Unset):
            margin_right = UNSET
        else:
            margin_right = Dimension.from_dict(_margin_right)




        _margin_top = d.pop("marginTop", UNSET)
        margin_top: Dimension | Unset
        if isinstance(_margin_top,  Unset):
            margin_top = UNSET
        else:
            margin_top = Dimension.from_dict(_margin_top)




        page_number_start = d.pop("pageNumberStart", UNSET)

        _section_type = d.pop("sectionType", UNSET)
        section_type: SectionStyleSectionType | Unset
        if isinstance(_section_type,  Unset):
            section_type = UNSET
        else:
            section_type = SectionStyleSectionType(_section_type)




        use_first_page_header_footer = d.pop("useFirstPageHeaderFooter", UNSET)

        section_style = cls(
            column_properties=column_properties,
            column_separator_style=column_separator_style,
            content_direction=content_direction,
            default_footer_id=default_footer_id,
            default_header_id=default_header_id,
            even_page_footer_id=even_page_footer_id,
            even_page_header_id=even_page_header_id,
            first_page_footer_id=first_page_footer_id,
            first_page_header_id=first_page_header_id,
            margin_bottom=margin_bottom,
            margin_footer=margin_footer,
            margin_header=margin_header,
            margin_left=margin_left,
            margin_right=margin_right,
            margin_top=margin_top,
            page_number_start=page_number_start,
            section_type=section_type,
            use_first_page_header_footer=use_first_page_header_footer,
        )


        section_style.additional_properties = d
        return section_style

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
