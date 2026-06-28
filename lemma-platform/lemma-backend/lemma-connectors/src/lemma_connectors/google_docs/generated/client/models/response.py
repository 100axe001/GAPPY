from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.create_footer_response import CreateFooterResponse
  from ..models.create_footnote_response import CreateFootnoteResponse
  from ..models.create_header_response import CreateHeaderResponse
  from ..models.create_named_range_response import CreateNamedRangeResponse
  from ..models.insert_inline_image_response import InsertInlineImageResponse
  from ..models.insert_inline_sheets_chart_response import InsertInlineSheetsChartResponse
  from ..models.replace_all_text_response import ReplaceAllTextResponse





T = TypeVar("T", bound="Response")



@_attrs_define
class Response:
    """ A single response from an update.

        Attributes:
            create_footer (CreateFooterResponse | Unset): The result of creating a footer.
            create_footnote (CreateFootnoteResponse | Unset): The result of creating a footnote.
            create_header (CreateHeaderResponse | Unset): The result of creating a header.
            create_named_range (CreateNamedRangeResponse | Unset): The result of creating a named range.
            insert_inline_image (InsertInlineImageResponse | Unset): The result of inserting an inline image.
            insert_inline_sheets_chart (InsertInlineSheetsChartResponse | Unset): The result of inserting an embedded Google
                Sheets chart.
            replace_all_text (ReplaceAllTextResponse | Unset): The result of replacing text.
     """

    create_footer: CreateFooterResponse | Unset = UNSET
    create_footnote: CreateFootnoteResponse | Unset = UNSET
    create_header: CreateHeaderResponse | Unset = UNSET
    create_named_range: CreateNamedRangeResponse | Unset = UNSET
    insert_inline_image: InsertInlineImageResponse | Unset = UNSET
    insert_inline_sheets_chart: InsertInlineSheetsChartResponse | Unset = UNSET
    replace_all_text: ReplaceAllTextResponse | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.create_footer_response import CreateFooterResponse
        from ..models.create_footnote_response import CreateFootnoteResponse
        from ..models.create_header_response import CreateHeaderResponse
        from ..models.create_named_range_response import CreateNamedRangeResponse
        from ..models.insert_inline_image_response import InsertInlineImageResponse
        from ..models.insert_inline_sheets_chart_response import InsertInlineSheetsChartResponse
        from ..models.replace_all_text_response import ReplaceAllTextResponse
        create_footer: dict[str, Any] | Unset = UNSET
        if not isinstance(self.create_footer, Unset):
            create_footer = self.create_footer.to_dict()

        create_footnote: dict[str, Any] | Unset = UNSET
        if not isinstance(self.create_footnote, Unset):
            create_footnote = self.create_footnote.to_dict()

        create_header: dict[str, Any] | Unset = UNSET
        if not isinstance(self.create_header, Unset):
            create_header = self.create_header.to_dict()

        create_named_range: dict[str, Any] | Unset = UNSET
        if not isinstance(self.create_named_range, Unset):
            create_named_range = self.create_named_range.to_dict()

        insert_inline_image: dict[str, Any] | Unset = UNSET
        if not isinstance(self.insert_inline_image, Unset):
            insert_inline_image = self.insert_inline_image.to_dict()

        insert_inline_sheets_chart: dict[str, Any] | Unset = UNSET
        if not isinstance(self.insert_inline_sheets_chart, Unset):
            insert_inline_sheets_chart = self.insert_inline_sheets_chart.to_dict()

        replace_all_text: dict[str, Any] | Unset = UNSET
        if not isinstance(self.replace_all_text, Unset):
            replace_all_text = self.replace_all_text.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if create_footer is not UNSET:
            field_dict["createFooter"] = create_footer
        if create_footnote is not UNSET:
            field_dict["createFootnote"] = create_footnote
        if create_header is not UNSET:
            field_dict["createHeader"] = create_header
        if create_named_range is not UNSET:
            field_dict["createNamedRange"] = create_named_range
        if insert_inline_image is not UNSET:
            field_dict["insertInlineImage"] = insert_inline_image
        if insert_inline_sheets_chart is not UNSET:
            field_dict["insertInlineSheetsChart"] = insert_inline_sheets_chart
        if replace_all_text is not UNSET:
            field_dict["replaceAllText"] = replace_all_text

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_footer_response import CreateFooterResponse
        from ..models.create_footnote_response import CreateFootnoteResponse
        from ..models.create_header_response import CreateHeaderResponse
        from ..models.create_named_range_response import CreateNamedRangeResponse
        from ..models.insert_inline_image_response import InsertInlineImageResponse
        from ..models.insert_inline_sheets_chart_response import InsertInlineSheetsChartResponse
        from ..models.replace_all_text_response import ReplaceAllTextResponse
        d = dict(src_dict)
        _create_footer = d.pop("createFooter", UNSET)
        create_footer: CreateFooterResponse | Unset
        if isinstance(_create_footer,  Unset):
            create_footer = UNSET
        else:
            create_footer = CreateFooterResponse.from_dict(_create_footer)




        _create_footnote = d.pop("createFootnote", UNSET)
        create_footnote: CreateFootnoteResponse | Unset
        if isinstance(_create_footnote,  Unset):
            create_footnote = UNSET
        else:
            create_footnote = CreateFootnoteResponse.from_dict(_create_footnote)




        _create_header = d.pop("createHeader", UNSET)
        create_header: CreateHeaderResponse | Unset
        if isinstance(_create_header,  Unset):
            create_header = UNSET
        else:
            create_header = CreateHeaderResponse.from_dict(_create_header)




        _create_named_range = d.pop("createNamedRange", UNSET)
        create_named_range: CreateNamedRangeResponse | Unset
        if isinstance(_create_named_range,  Unset):
            create_named_range = UNSET
        else:
            create_named_range = CreateNamedRangeResponse.from_dict(_create_named_range)




        _insert_inline_image = d.pop("insertInlineImage", UNSET)
        insert_inline_image: InsertInlineImageResponse | Unset
        if isinstance(_insert_inline_image,  Unset):
            insert_inline_image = UNSET
        else:
            insert_inline_image = InsertInlineImageResponse.from_dict(_insert_inline_image)




        _insert_inline_sheets_chart = d.pop("insertInlineSheetsChart", UNSET)
        insert_inline_sheets_chart: InsertInlineSheetsChartResponse | Unset
        if isinstance(_insert_inline_sheets_chart,  Unset):
            insert_inline_sheets_chart = UNSET
        else:
            insert_inline_sheets_chart = InsertInlineSheetsChartResponse.from_dict(_insert_inline_sheets_chart)




        _replace_all_text = d.pop("replaceAllText", UNSET)
        replace_all_text: ReplaceAllTextResponse | Unset
        if isinstance(_replace_all_text,  Unset):
            replace_all_text = UNSET
        else:
            replace_all_text = ReplaceAllTextResponse.from_dict(_replace_all_text)




        response = cls(
            create_footer=create_footer,
            create_footnote=create_footnote,
            create_header=create_header,
            create_named_range=create_named_range,
            insert_inline_image=insert_inline_image,
            insert_inline_sheets_chart=insert_inline_sheets_chart,
            replace_all_text=replace_all_text,
        )


        response.additional_properties = d
        return response

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
