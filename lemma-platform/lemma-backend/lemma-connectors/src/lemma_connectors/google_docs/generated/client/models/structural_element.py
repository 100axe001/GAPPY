from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.paragraph import Paragraph
  from ..models.section_break import SectionBreak
  from ..models.table import Table
  from ..models.table_of_contents import TableOfContents





T = TypeVar("T", bound="StructuralElement")



@_attrs_define
class StructuralElement:
    """ A StructuralElement describes content that provides structure to the document.

        Attributes:
            end_index (int | Unset): The zero-based end index of this structural element, exclusive, in UTF-16 code units.
            paragraph (Paragraph | Unset): A StructuralElement representing a paragraph. A paragraph is a range of content
                that's terminated with a newline character.
            section_break (SectionBreak | Unset): A StructuralElement representing a section break. A section is a range of
                content that has the same SectionStyle. A section break represents the start of a new section, and the section
                style applies to the section after the section break. The document body always begins with a section break.
            start_index (int | Unset): The zero-based start index of this structural element, in UTF-16 code units.
            table (Table | Unset): A StructuralElement representing a table.
            table_of_contents (TableOfContents | Unset): A StructuralElement representing a table of contents.
     """

    end_index: int | Unset = UNSET
    paragraph: Paragraph | Unset = UNSET
    section_break: SectionBreak | Unset = UNSET
    start_index: int | Unset = UNSET
    table: Table | Unset = UNSET
    table_of_contents: TableOfContents | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.paragraph import Paragraph
        from ..models.section_break import SectionBreak
        from ..models.table import Table
        from ..models.table_of_contents import TableOfContents
        end_index = self.end_index

        paragraph: dict[str, Any] | Unset = UNSET
        if not isinstance(self.paragraph, Unset):
            paragraph = self.paragraph.to_dict()

        section_break: dict[str, Any] | Unset = UNSET
        if not isinstance(self.section_break, Unset):
            section_break = self.section_break.to_dict()

        start_index = self.start_index

        table: dict[str, Any] | Unset = UNSET
        if not isinstance(self.table, Unset):
            table = self.table.to_dict()

        table_of_contents: dict[str, Any] | Unset = UNSET
        if not isinstance(self.table_of_contents, Unset):
            table_of_contents = self.table_of_contents.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if end_index is not UNSET:
            field_dict["endIndex"] = end_index
        if paragraph is not UNSET:
            field_dict["paragraph"] = paragraph
        if section_break is not UNSET:
            field_dict["sectionBreak"] = section_break
        if start_index is not UNSET:
            field_dict["startIndex"] = start_index
        if table is not UNSET:
            field_dict["table"] = table
        if table_of_contents is not UNSET:
            field_dict["tableOfContents"] = table_of_contents

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.paragraph import Paragraph
        from ..models.section_break import SectionBreak
        from ..models.table import Table
        from ..models.table_of_contents import TableOfContents
        d = dict(src_dict)
        end_index = d.pop("endIndex", UNSET)

        _paragraph = d.pop("paragraph", UNSET)
        paragraph: Paragraph | Unset
        if isinstance(_paragraph,  Unset):
            paragraph = UNSET
        else:
            paragraph = Paragraph.from_dict(_paragraph)




        _section_break = d.pop("sectionBreak", UNSET)
        section_break: SectionBreak | Unset
        if isinstance(_section_break,  Unset):
            section_break = UNSET
        else:
            section_break = SectionBreak.from_dict(_section_break)




        start_index = d.pop("startIndex", UNSET)

        _table = d.pop("table", UNSET)
        table: Table | Unset
        if isinstance(_table,  Unset):
            table = UNSET
        else:
            table = Table.from_dict(_table)




        _table_of_contents = d.pop("tableOfContents", UNSET)
        table_of_contents: TableOfContents | Unset
        if isinstance(_table_of_contents,  Unset):
            table_of_contents = UNSET
        else:
            table_of_contents = TableOfContents.from_dict(_table_of_contents)




        structural_element = cls(
            end_index=end_index,
            paragraph=paragraph,
            section_break=section_break,
            start_index=start_index,
            table=table,
            table_of_contents=table_of_contents,
        )


        structural_element.additional_properties = d
        return structural_element

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
