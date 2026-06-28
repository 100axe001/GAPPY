from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.bullet import Bullet
  from ..models.paragraph_element import ParagraphElement
  from ..models.paragraph_style import ParagraphStyle
  from ..models.paragraph_suggested_bullet_changes import ParagraphSuggestedBulletChanges
  from ..models.paragraph_suggested_paragraph_style_changes import ParagraphSuggestedParagraphStyleChanges
  from ..models.paragraph_suggested_positioned_object_ids import ParagraphSuggestedPositionedObjectIds





T = TypeVar("T", bound="Paragraph")



@_attrs_define
class Paragraph:
    """ A StructuralElement representing a paragraph. A paragraph is a range of content that's terminated with a newline
    character.

        Attributes:
            bullet (Bullet | Unset): Describes the bullet of a paragraph.
            elements (list[ParagraphElement] | Unset): The content of the paragraph, broken down into its component parts.
            paragraph_style (ParagraphStyle | Unset): Styles that apply to a whole paragraph. Inherited paragraph styles are
                represented as unset fields in this message. A paragraph style's parent depends on where the paragraph style is
                defined: * The ParagraphStyle on a Paragraph inherits from the paragraph's corresponding named style type. * The
                ParagraphStyle on a named style inherits from the normal text named style. * The ParagraphStyle of the normal
                text named style inherits from the default paragraph style in the Docs editor. * The ParagraphStyle on a
                Paragraph element that's contained in a table may inherit its paragraph style from the table style. If the
                paragraph style does not inherit from a parent, unsetting fields will revert the style to a value matching the
                defaults in the Docs editor.
            positioned_object_ids (list[str] | Unset): The IDs of the positioned objects tethered to this paragraph.
            suggested_bullet_changes (ParagraphSuggestedBulletChanges | Unset): The suggested changes to this paragraph's
                bullet.
            suggested_paragraph_style_changes (ParagraphSuggestedParagraphStyleChanges | Unset): The suggested paragraph
                style changes to this paragraph, keyed by suggestion ID.
            suggested_positioned_object_ids (ParagraphSuggestedPositionedObjectIds | Unset): The IDs of the positioned
                objects suggested to be attached to this paragraph, keyed by suggestion ID.
     """

    bullet: Bullet | Unset = UNSET
    elements: list[ParagraphElement] | Unset = UNSET
    paragraph_style: ParagraphStyle | Unset = UNSET
    positioned_object_ids: list[str] | Unset = UNSET
    suggested_bullet_changes: ParagraphSuggestedBulletChanges | Unset = UNSET
    suggested_paragraph_style_changes: ParagraphSuggestedParagraphStyleChanges | Unset = UNSET
    suggested_positioned_object_ids: ParagraphSuggestedPositionedObjectIds | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.bullet import Bullet
        from ..models.paragraph_element import ParagraphElement
        from ..models.paragraph_style import ParagraphStyle
        from ..models.paragraph_suggested_bullet_changes import ParagraphSuggestedBulletChanges
        from ..models.paragraph_suggested_paragraph_style_changes import ParagraphSuggestedParagraphStyleChanges
        from ..models.paragraph_suggested_positioned_object_ids import ParagraphSuggestedPositionedObjectIds
        bullet: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bullet, Unset):
            bullet = self.bullet.to_dict()

        elements: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.elements, Unset):
            elements = []
            for elements_item_data in self.elements:
                elements_item = elements_item_data.to_dict()
                elements.append(elements_item)



        paragraph_style: dict[str, Any] | Unset = UNSET
        if not isinstance(self.paragraph_style, Unset):
            paragraph_style = self.paragraph_style.to_dict()

        positioned_object_ids: list[str] | Unset = UNSET
        if not isinstance(self.positioned_object_ids, Unset):
            positioned_object_ids = self.positioned_object_ids



        suggested_bullet_changes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.suggested_bullet_changes, Unset):
            suggested_bullet_changes = self.suggested_bullet_changes.to_dict()

        suggested_paragraph_style_changes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.suggested_paragraph_style_changes, Unset):
            suggested_paragraph_style_changes = self.suggested_paragraph_style_changes.to_dict()

        suggested_positioned_object_ids: dict[str, Any] | Unset = UNSET
        if not isinstance(self.suggested_positioned_object_ids, Unset):
            suggested_positioned_object_ids = self.suggested_positioned_object_ids.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if bullet is not UNSET:
            field_dict["bullet"] = bullet
        if elements is not UNSET:
            field_dict["elements"] = elements
        if paragraph_style is not UNSET:
            field_dict["paragraphStyle"] = paragraph_style
        if positioned_object_ids is not UNSET:
            field_dict["positionedObjectIds"] = positioned_object_ids
        if suggested_bullet_changes is not UNSET:
            field_dict["suggestedBulletChanges"] = suggested_bullet_changes
        if suggested_paragraph_style_changes is not UNSET:
            field_dict["suggestedParagraphStyleChanges"] = suggested_paragraph_style_changes
        if suggested_positioned_object_ids is not UNSET:
            field_dict["suggestedPositionedObjectIds"] = suggested_positioned_object_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bullet import Bullet
        from ..models.paragraph_element import ParagraphElement
        from ..models.paragraph_style import ParagraphStyle
        from ..models.paragraph_suggested_bullet_changes import ParagraphSuggestedBulletChanges
        from ..models.paragraph_suggested_paragraph_style_changes import ParagraphSuggestedParagraphStyleChanges
        from ..models.paragraph_suggested_positioned_object_ids import ParagraphSuggestedPositionedObjectIds
        d = dict(src_dict)
        _bullet = d.pop("bullet", UNSET)
        bullet: Bullet | Unset
        if isinstance(_bullet,  Unset):
            bullet = UNSET
        else:
            bullet = Bullet.from_dict(_bullet)




        _elements = d.pop("elements", UNSET)
        elements: list[ParagraphElement] | Unset = UNSET
        if _elements is not UNSET:
            elements = []
            for elements_item_data in _elements:
                elements_item = ParagraphElement.from_dict(elements_item_data)



                elements.append(elements_item)


        _paragraph_style = d.pop("paragraphStyle", UNSET)
        paragraph_style: ParagraphStyle | Unset
        if isinstance(_paragraph_style,  Unset):
            paragraph_style = UNSET
        else:
            paragraph_style = ParagraphStyle.from_dict(_paragraph_style)




        positioned_object_ids = cast(list[str], d.pop("positionedObjectIds", UNSET))


        _suggested_bullet_changes = d.pop("suggestedBulletChanges", UNSET)
        suggested_bullet_changes: ParagraphSuggestedBulletChanges | Unset
        if isinstance(_suggested_bullet_changes,  Unset):
            suggested_bullet_changes = UNSET
        else:
            suggested_bullet_changes = ParagraphSuggestedBulletChanges.from_dict(_suggested_bullet_changes)




        _suggested_paragraph_style_changes = d.pop("suggestedParagraphStyleChanges", UNSET)
        suggested_paragraph_style_changes: ParagraphSuggestedParagraphStyleChanges | Unset
        if isinstance(_suggested_paragraph_style_changes,  Unset):
            suggested_paragraph_style_changes = UNSET
        else:
            suggested_paragraph_style_changes = ParagraphSuggestedParagraphStyleChanges.from_dict(_suggested_paragraph_style_changes)




        _suggested_positioned_object_ids = d.pop("suggestedPositionedObjectIds", UNSET)
        suggested_positioned_object_ids: ParagraphSuggestedPositionedObjectIds | Unset
        if isinstance(_suggested_positioned_object_ids,  Unset):
            suggested_positioned_object_ids = UNSET
        else:
            suggested_positioned_object_ids = ParagraphSuggestedPositionedObjectIds.from_dict(_suggested_positioned_object_ids)




        paragraph = cls(
            bullet=bullet,
            elements=elements,
            paragraph_style=paragraph_style,
            positioned_object_ids=positioned_object_ids,
            suggested_bullet_changes=suggested_bullet_changes,
            suggested_paragraph_style_changes=suggested_paragraph_style_changes,
            suggested_positioned_object_ids=suggested_positioned_object_ids,
        )


        paragraph.additional_properties = d
        return paragraph

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
