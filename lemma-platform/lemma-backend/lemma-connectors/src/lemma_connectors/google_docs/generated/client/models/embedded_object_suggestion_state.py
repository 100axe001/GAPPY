from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.embedded_drawing_properties_suggestion_state import EmbeddedDrawingPropertiesSuggestionState
  from ..models.embedded_object_border_suggestion_state import EmbeddedObjectBorderSuggestionState
  from ..models.image_properties_suggestion_state import ImagePropertiesSuggestionState
  from ..models.linked_content_reference_suggestion_state import LinkedContentReferenceSuggestionState
  from ..models.size_suggestion_state import SizeSuggestionState





T = TypeVar("T", bound="EmbeddedObjectSuggestionState")



@_attrs_define
class EmbeddedObjectSuggestionState:
    """ A mask that indicates which of the fields on the base EmbeddedObject have been changed in this suggestion. For any
    field set to true, there's a new suggested value.

        Attributes:
            description_suggested (bool | Unset): Indicates if there was a suggested change to description.
            embedded_drawing_properties_suggestion_state (EmbeddedDrawingPropertiesSuggestionState | Unset): A mask that
                indicates which of the fields on the base EmbeddedDrawingProperties have been changed in this suggestion. For
                any field set to true, there's a new suggested value.
            embedded_object_border_suggestion_state (EmbeddedObjectBorderSuggestionState | Unset): A mask that indicates
                which of the fields on the base EmbeddedObjectBorder have been changed in this suggestion. For any field set to
                true, there's a new suggested value.
            image_properties_suggestion_state (ImagePropertiesSuggestionState | Unset): A mask that indicates which of the
                fields on the base ImageProperties have been changed in this suggestion. For any field set to true, there's a
                new suggested value.
            linked_content_reference_suggestion_state (LinkedContentReferenceSuggestionState | Unset): A mask that indicates
                which of the fields on the base LinkedContentReference have been changed in this suggestion. For any field set
                to true, there's a new suggested value.
            margin_bottom_suggested (bool | Unset): Indicates if there was a suggested change to margin_bottom.
            margin_left_suggested (bool | Unset): Indicates if there was a suggested change to margin_left.
            margin_right_suggested (bool | Unset): Indicates if there was a suggested change to margin_right.
            margin_top_suggested (bool | Unset): Indicates if there was a suggested change to margin_top.
            size_suggestion_state (SizeSuggestionState | Unset): A mask that indicates which of the fields on the base Size
                have been changed in this suggestion. For any field set to true, the Size has a new suggested value.
            title_suggested (bool | Unset): Indicates if there was a suggested change to title.
     """

    description_suggested: bool | Unset = UNSET
    embedded_drawing_properties_suggestion_state: EmbeddedDrawingPropertiesSuggestionState | Unset = UNSET
    embedded_object_border_suggestion_state: EmbeddedObjectBorderSuggestionState | Unset = UNSET
    image_properties_suggestion_state: ImagePropertiesSuggestionState | Unset = UNSET
    linked_content_reference_suggestion_state: LinkedContentReferenceSuggestionState | Unset = UNSET
    margin_bottom_suggested: bool | Unset = UNSET
    margin_left_suggested: bool | Unset = UNSET
    margin_right_suggested: bool | Unset = UNSET
    margin_top_suggested: bool | Unset = UNSET
    size_suggestion_state: SizeSuggestionState | Unset = UNSET
    title_suggested: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.embedded_drawing_properties_suggestion_state import EmbeddedDrawingPropertiesSuggestionState
        from ..models.embedded_object_border_suggestion_state import EmbeddedObjectBorderSuggestionState
        from ..models.image_properties_suggestion_state import ImagePropertiesSuggestionState
        from ..models.linked_content_reference_suggestion_state import LinkedContentReferenceSuggestionState
        from ..models.size_suggestion_state import SizeSuggestionState
        description_suggested = self.description_suggested

        embedded_drawing_properties_suggestion_state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.embedded_drawing_properties_suggestion_state, Unset):
            embedded_drawing_properties_suggestion_state = self.embedded_drawing_properties_suggestion_state.to_dict()

        embedded_object_border_suggestion_state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.embedded_object_border_suggestion_state, Unset):
            embedded_object_border_suggestion_state = self.embedded_object_border_suggestion_state.to_dict()

        image_properties_suggestion_state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.image_properties_suggestion_state, Unset):
            image_properties_suggestion_state = self.image_properties_suggestion_state.to_dict()

        linked_content_reference_suggestion_state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.linked_content_reference_suggestion_state, Unset):
            linked_content_reference_suggestion_state = self.linked_content_reference_suggestion_state.to_dict()

        margin_bottom_suggested = self.margin_bottom_suggested

        margin_left_suggested = self.margin_left_suggested

        margin_right_suggested = self.margin_right_suggested

        margin_top_suggested = self.margin_top_suggested

        size_suggestion_state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.size_suggestion_state, Unset):
            size_suggestion_state = self.size_suggestion_state.to_dict()

        title_suggested = self.title_suggested


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if description_suggested is not UNSET:
            field_dict["descriptionSuggested"] = description_suggested
        if embedded_drawing_properties_suggestion_state is not UNSET:
            field_dict["embeddedDrawingPropertiesSuggestionState"] = embedded_drawing_properties_suggestion_state
        if embedded_object_border_suggestion_state is not UNSET:
            field_dict["embeddedObjectBorderSuggestionState"] = embedded_object_border_suggestion_state
        if image_properties_suggestion_state is not UNSET:
            field_dict["imagePropertiesSuggestionState"] = image_properties_suggestion_state
        if linked_content_reference_suggestion_state is not UNSET:
            field_dict["linkedContentReferenceSuggestionState"] = linked_content_reference_suggestion_state
        if margin_bottom_suggested is not UNSET:
            field_dict["marginBottomSuggested"] = margin_bottom_suggested
        if margin_left_suggested is not UNSET:
            field_dict["marginLeftSuggested"] = margin_left_suggested
        if margin_right_suggested is not UNSET:
            field_dict["marginRightSuggested"] = margin_right_suggested
        if margin_top_suggested is not UNSET:
            field_dict["marginTopSuggested"] = margin_top_suggested
        if size_suggestion_state is not UNSET:
            field_dict["sizeSuggestionState"] = size_suggestion_state
        if title_suggested is not UNSET:
            field_dict["titleSuggested"] = title_suggested

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.embedded_drawing_properties_suggestion_state import EmbeddedDrawingPropertiesSuggestionState
        from ..models.embedded_object_border_suggestion_state import EmbeddedObjectBorderSuggestionState
        from ..models.image_properties_suggestion_state import ImagePropertiesSuggestionState
        from ..models.linked_content_reference_suggestion_state import LinkedContentReferenceSuggestionState
        from ..models.size_suggestion_state import SizeSuggestionState
        d = dict(src_dict)
        description_suggested = d.pop("descriptionSuggested", UNSET)

        _embedded_drawing_properties_suggestion_state = d.pop("embeddedDrawingPropertiesSuggestionState", UNSET)
        embedded_drawing_properties_suggestion_state: EmbeddedDrawingPropertiesSuggestionState | Unset
        if isinstance(_embedded_drawing_properties_suggestion_state,  Unset):
            embedded_drawing_properties_suggestion_state = UNSET
        else:
            embedded_drawing_properties_suggestion_state = EmbeddedDrawingPropertiesSuggestionState.from_dict(_embedded_drawing_properties_suggestion_state)




        _embedded_object_border_suggestion_state = d.pop("embeddedObjectBorderSuggestionState", UNSET)
        embedded_object_border_suggestion_state: EmbeddedObjectBorderSuggestionState | Unset
        if isinstance(_embedded_object_border_suggestion_state,  Unset):
            embedded_object_border_suggestion_state = UNSET
        else:
            embedded_object_border_suggestion_state = EmbeddedObjectBorderSuggestionState.from_dict(_embedded_object_border_suggestion_state)




        _image_properties_suggestion_state = d.pop("imagePropertiesSuggestionState", UNSET)
        image_properties_suggestion_state: ImagePropertiesSuggestionState | Unset
        if isinstance(_image_properties_suggestion_state,  Unset):
            image_properties_suggestion_state = UNSET
        else:
            image_properties_suggestion_state = ImagePropertiesSuggestionState.from_dict(_image_properties_suggestion_state)




        _linked_content_reference_suggestion_state = d.pop("linkedContentReferenceSuggestionState", UNSET)
        linked_content_reference_suggestion_state: LinkedContentReferenceSuggestionState | Unset
        if isinstance(_linked_content_reference_suggestion_state,  Unset):
            linked_content_reference_suggestion_state = UNSET
        else:
            linked_content_reference_suggestion_state = LinkedContentReferenceSuggestionState.from_dict(_linked_content_reference_suggestion_state)




        margin_bottom_suggested = d.pop("marginBottomSuggested", UNSET)

        margin_left_suggested = d.pop("marginLeftSuggested", UNSET)

        margin_right_suggested = d.pop("marginRightSuggested", UNSET)

        margin_top_suggested = d.pop("marginTopSuggested", UNSET)

        _size_suggestion_state = d.pop("sizeSuggestionState", UNSET)
        size_suggestion_state: SizeSuggestionState | Unset
        if isinstance(_size_suggestion_state,  Unset):
            size_suggestion_state = UNSET
        else:
            size_suggestion_state = SizeSuggestionState.from_dict(_size_suggestion_state)




        title_suggested = d.pop("titleSuggested", UNSET)

        embedded_object_suggestion_state = cls(
            description_suggested=description_suggested,
            embedded_drawing_properties_suggestion_state=embedded_drawing_properties_suggestion_state,
            embedded_object_border_suggestion_state=embedded_object_border_suggestion_state,
            image_properties_suggestion_state=image_properties_suggestion_state,
            linked_content_reference_suggestion_state=linked_content_reference_suggestion_state,
            margin_bottom_suggested=margin_bottom_suggested,
            margin_left_suggested=margin_left_suggested,
            margin_right_suggested=margin_right_suggested,
            margin_top_suggested=margin_top_suggested,
            size_suggestion_state=size_suggestion_state,
            title_suggested=title_suggested,
        )


        embedded_object_suggestion_state.additional_properties = d
        return embedded_object_suggestion_state

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
