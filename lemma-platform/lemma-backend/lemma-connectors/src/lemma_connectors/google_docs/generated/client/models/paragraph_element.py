from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.auto_text import AutoText
  from ..models.column_break import ColumnBreak
  from ..models.equation import Equation
  from ..models.footnote_reference import FootnoteReference
  from ..models.horizontal_rule import HorizontalRule
  from ..models.inline_object_element import InlineObjectElement
  from ..models.page_break import PageBreak
  from ..models.person import Person
  from ..models.rich_link import RichLink
  from ..models.text_run import TextRun





T = TypeVar("T", bound="ParagraphElement")



@_attrs_define
class ParagraphElement:
    """ A ParagraphElement describes content within a Paragraph.

        Attributes:
            auto_text (AutoText | Unset): A ParagraphElement representing a spot in the text that's dynamically replaced
                with content that can change over time, like a page number.
            column_break (ColumnBreak | Unset): A ParagraphElement representing a column break. A column break makes the
                subsequent text start at the top of the next column.
            end_index (int | Unset): The zero-base end index of this paragraph element, exclusive, in UTF-16 code units.
            equation (Equation | Unset): A ParagraphElement representing an equation.
            footnote_reference (FootnoteReference | Unset): A ParagraphElement representing a footnote reference. A footnote
                reference is the inline content rendered with a number and is used to identify the footnote.
            horizontal_rule (HorizontalRule | Unset): A ParagraphElement representing a horizontal line.
            inline_object_element (InlineObjectElement | Unset): A ParagraphElement that contains an InlineObject.
            page_break (PageBreak | Unset): A ParagraphElement representing a page break. A page break makes the subsequent
                text start at the top of the next page.
            person (Person | Unset): A person or email address mentioned in a document. These mentions behave as a single,
                immutable element containing the person's name or email address.
            rich_link (RichLink | Unset): A link to a Google resource (such as a file in Drive, a YouTube video, or a
                Calendar event).
            start_index (int | Unset): The zero-based start index of this paragraph element, in UTF-16 code units.
            text_run (TextRun | Unset): A ParagraphElement that represents a run of text that all has the same styling.
     """

    auto_text: AutoText | Unset = UNSET
    column_break: ColumnBreak | Unset = UNSET
    end_index: int | Unset = UNSET
    equation: Equation | Unset = UNSET
    footnote_reference: FootnoteReference | Unset = UNSET
    horizontal_rule: HorizontalRule | Unset = UNSET
    inline_object_element: InlineObjectElement | Unset = UNSET
    page_break: PageBreak | Unset = UNSET
    person: Person | Unset = UNSET
    rich_link: RichLink | Unset = UNSET
    start_index: int | Unset = UNSET
    text_run: TextRun | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.auto_text import AutoText
        from ..models.column_break import ColumnBreak
        from ..models.equation import Equation
        from ..models.footnote_reference import FootnoteReference
        from ..models.horizontal_rule import HorizontalRule
        from ..models.inline_object_element import InlineObjectElement
        from ..models.page_break import PageBreak
        from ..models.person import Person
        from ..models.rich_link import RichLink
        from ..models.text_run import TextRun
        auto_text: dict[str, Any] | Unset = UNSET
        if not isinstance(self.auto_text, Unset):
            auto_text = self.auto_text.to_dict()

        column_break: dict[str, Any] | Unset = UNSET
        if not isinstance(self.column_break, Unset):
            column_break = self.column_break.to_dict()

        end_index = self.end_index

        equation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.equation, Unset):
            equation = self.equation.to_dict()

        footnote_reference: dict[str, Any] | Unset = UNSET
        if not isinstance(self.footnote_reference, Unset):
            footnote_reference = self.footnote_reference.to_dict()

        horizontal_rule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.horizontal_rule, Unset):
            horizontal_rule = self.horizontal_rule.to_dict()

        inline_object_element: dict[str, Any] | Unset = UNSET
        if not isinstance(self.inline_object_element, Unset):
            inline_object_element = self.inline_object_element.to_dict()

        page_break: dict[str, Any] | Unset = UNSET
        if not isinstance(self.page_break, Unset):
            page_break = self.page_break.to_dict()

        person: dict[str, Any] | Unset = UNSET
        if not isinstance(self.person, Unset):
            person = self.person.to_dict()

        rich_link: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rich_link, Unset):
            rich_link = self.rich_link.to_dict()

        start_index = self.start_index

        text_run: dict[str, Any] | Unset = UNSET
        if not isinstance(self.text_run, Unset):
            text_run = self.text_run.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if auto_text is not UNSET:
            field_dict["autoText"] = auto_text
        if column_break is not UNSET:
            field_dict["columnBreak"] = column_break
        if end_index is not UNSET:
            field_dict["endIndex"] = end_index
        if equation is not UNSET:
            field_dict["equation"] = equation
        if footnote_reference is not UNSET:
            field_dict["footnoteReference"] = footnote_reference
        if horizontal_rule is not UNSET:
            field_dict["horizontalRule"] = horizontal_rule
        if inline_object_element is not UNSET:
            field_dict["inlineObjectElement"] = inline_object_element
        if page_break is not UNSET:
            field_dict["pageBreak"] = page_break
        if person is not UNSET:
            field_dict["person"] = person
        if rich_link is not UNSET:
            field_dict["richLink"] = rich_link
        if start_index is not UNSET:
            field_dict["startIndex"] = start_index
        if text_run is not UNSET:
            field_dict["textRun"] = text_run

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.auto_text import AutoText
        from ..models.column_break import ColumnBreak
        from ..models.equation import Equation
        from ..models.footnote_reference import FootnoteReference
        from ..models.horizontal_rule import HorizontalRule
        from ..models.inline_object_element import InlineObjectElement
        from ..models.page_break import PageBreak
        from ..models.person import Person
        from ..models.rich_link import RichLink
        from ..models.text_run import TextRun
        d = dict(src_dict)
        _auto_text = d.pop("autoText", UNSET)
        auto_text: AutoText | Unset
        if isinstance(_auto_text,  Unset):
            auto_text = UNSET
        else:
            auto_text = AutoText.from_dict(_auto_text)




        _column_break = d.pop("columnBreak", UNSET)
        column_break: ColumnBreak | Unset
        if isinstance(_column_break,  Unset):
            column_break = UNSET
        else:
            column_break = ColumnBreak.from_dict(_column_break)




        end_index = d.pop("endIndex", UNSET)

        _equation = d.pop("equation", UNSET)
        equation: Equation | Unset
        if isinstance(_equation,  Unset):
            equation = UNSET
        else:
            equation = Equation.from_dict(_equation)




        _footnote_reference = d.pop("footnoteReference", UNSET)
        footnote_reference: FootnoteReference | Unset
        if isinstance(_footnote_reference,  Unset):
            footnote_reference = UNSET
        else:
            footnote_reference = FootnoteReference.from_dict(_footnote_reference)




        _horizontal_rule = d.pop("horizontalRule", UNSET)
        horizontal_rule: HorizontalRule | Unset
        if isinstance(_horizontal_rule,  Unset):
            horizontal_rule = UNSET
        else:
            horizontal_rule = HorizontalRule.from_dict(_horizontal_rule)




        _inline_object_element = d.pop("inlineObjectElement", UNSET)
        inline_object_element: InlineObjectElement | Unset
        if isinstance(_inline_object_element,  Unset):
            inline_object_element = UNSET
        else:
            inline_object_element = InlineObjectElement.from_dict(_inline_object_element)




        _page_break = d.pop("pageBreak", UNSET)
        page_break: PageBreak | Unset
        if isinstance(_page_break,  Unset):
            page_break = UNSET
        else:
            page_break = PageBreak.from_dict(_page_break)




        _person = d.pop("person", UNSET)
        person: Person | Unset
        if isinstance(_person,  Unset):
            person = UNSET
        else:
            person = Person.from_dict(_person)




        _rich_link = d.pop("richLink", UNSET)
        rich_link: RichLink | Unset
        if isinstance(_rich_link,  Unset):
            rich_link = UNSET
        else:
            rich_link = RichLink.from_dict(_rich_link)




        start_index = d.pop("startIndex", UNSET)

        _text_run = d.pop("textRun", UNSET)
        text_run: TextRun | Unset
        if isinstance(_text_run,  Unset):
            text_run = UNSET
        else:
            text_run = TextRun.from_dict(_text_run)




        paragraph_element = cls(
            auto_text=auto_text,
            column_break=column_break,
            end_index=end_index,
            equation=equation,
            footnote_reference=footnote_reference,
            horizontal_rule=horizontal_rule,
            inline_object_element=inline_object_element,
            page_break=page_break,
            person=person,
            rich_link=rich_link,
            start_index=start_index,
            text_run=text_run,
        )


        paragraph_element.additional_properties = d
        return paragraph_element

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
