from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.background import Background
  from ..models.dimension import Dimension
  from ..models.size import Size





T = TypeVar("T", bound="DocumentStyle")



@_attrs_define
class DocumentStyle:
    """ The style of the document.

        Attributes:
            background (Background | Unset): Represents the background of a document.
            default_footer_id (str | Unset): The ID of the default footer. If not set, there's no default footer. This
                property is read-only.
            default_header_id (str | Unset): The ID of the default header. If not set, there's no default header. This
                property is read-only.
            even_page_footer_id (str | Unset): The ID of the footer used only for even pages. The value of
                use_even_page_header_footer determines whether to use the default_footer_id or this value for the footer on even
                pages. If not set, there's no even page footer. This property is read-only.
            even_page_header_id (str | Unset): The ID of the header used only for even pages. The value of
                use_even_page_header_footer determines whether to use the default_header_id or this value for the header on even
                pages. If not set, there's no even page header. This property is read-only.
            first_page_footer_id (str | Unset): The ID of the footer used only for the first page. If not set then a unique
                footer for the first page does not exist. The value of use_first_page_header_footer determines whether to use
                the default_footer_id or this value for the footer on the first page. If not set, there's no first page footer.
                This property is read-only.
            first_page_header_id (str | Unset): The ID of the header used only for the first page. If not set then a unique
                header for the first page does not exist. The value of use_first_page_header_footer determines whether to use
                the default_header_id or this value for the header on the first page. If not set, there's no first page header.
                This property is read-only.
            margin_bottom (Dimension | Unset): A magnitude in a single direction in the specified units.
            margin_footer (Dimension | Unset): A magnitude in a single direction in the specified units.
            margin_header (Dimension | Unset): A magnitude in a single direction in the specified units.
            margin_left (Dimension | Unset): A magnitude in a single direction in the specified units.
            margin_right (Dimension | Unset): A magnitude in a single direction in the specified units.
            margin_top (Dimension | Unset): A magnitude in a single direction in the specified units.
            page_number_start (int | Unset): The page number from which to start counting the number of pages.
            page_size (Size | Unset): A width and height.
            use_custom_header_footer_margins (bool | Unset): Indicates whether DocumentStyle margin_header, SectionStyle
                margin_header and DocumentStyle margin_footer, SectionStyle margin_footer are respected. When false, the default
                values in the Docs editor for header and footer margin are used. This property is read-only.
            use_even_page_header_footer (bool | Unset): Indicates whether to use the even page header / footer IDs for the
                even pages.
            use_first_page_header_footer (bool | Unset): Indicates whether to use the first page header / footer IDs for the
                first page.
     """

    background: Background | Unset = UNSET
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
    page_size: Size | Unset = UNSET
    use_custom_header_footer_margins: bool | Unset = UNSET
    use_even_page_header_footer: bool | Unset = UNSET
    use_first_page_header_footer: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.background import Background
        from ..models.dimension import Dimension
        from ..models.size import Size
        background: dict[str, Any] | Unset = UNSET
        if not isinstance(self.background, Unset):
            background = self.background.to_dict()

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

        page_size: dict[str, Any] | Unset = UNSET
        if not isinstance(self.page_size, Unset):
            page_size = self.page_size.to_dict()

        use_custom_header_footer_margins = self.use_custom_header_footer_margins

        use_even_page_header_footer = self.use_even_page_header_footer

        use_first_page_header_footer = self.use_first_page_header_footer


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if background is not UNSET:
            field_dict["background"] = background
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
        if page_size is not UNSET:
            field_dict["pageSize"] = page_size
        if use_custom_header_footer_margins is not UNSET:
            field_dict["useCustomHeaderFooterMargins"] = use_custom_header_footer_margins
        if use_even_page_header_footer is not UNSET:
            field_dict["useEvenPageHeaderFooter"] = use_even_page_header_footer
        if use_first_page_header_footer is not UNSET:
            field_dict["useFirstPageHeaderFooter"] = use_first_page_header_footer

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.background import Background
        from ..models.dimension import Dimension
        from ..models.size import Size
        d = dict(src_dict)
        _background = d.pop("background", UNSET)
        background: Background | Unset
        if isinstance(_background,  Unset):
            background = UNSET
        else:
            background = Background.from_dict(_background)




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

        _page_size = d.pop("pageSize", UNSET)
        page_size: Size | Unset
        if isinstance(_page_size,  Unset):
            page_size = UNSET
        else:
            page_size = Size.from_dict(_page_size)




        use_custom_header_footer_margins = d.pop("useCustomHeaderFooterMargins", UNSET)

        use_even_page_header_footer = d.pop("useEvenPageHeaderFooter", UNSET)

        use_first_page_header_footer = d.pop("useFirstPageHeaderFooter", UNSET)

        document_style = cls(
            background=background,
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
            page_size=page_size,
            use_custom_header_footer_margins=use_custom_header_footer_margins,
            use_even_page_header_footer=use_even_page_header_footer,
            use_first_page_header_footer=use_first_page_header_footer,
        )


        document_style.additional_properties = d
        return document_style

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
