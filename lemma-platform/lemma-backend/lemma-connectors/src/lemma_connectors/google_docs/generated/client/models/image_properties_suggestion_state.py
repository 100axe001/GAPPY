from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.crop_properties_suggestion_state import CropPropertiesSuggestionState





T = TypeVar("T", bound="ImagePropertiesSuggestionState")



@_attrs_define
class ImagePropertiesSuggestionState:
    """ A mask that indicates which of the fields on the base ImageProperties have been changed in this suggestion. For any
    field set to true, there's a new suggested value.

        Attributes:
            angle_suggested (bool | Unset): Indicates if there was a suggested change to angle.
            brightness_suggested (bool | Unset): Indicates if there was a suggested change to brightness.
            content_uri_suggested (bool | Unset): Indicates if there was a suggested change to content_uri.
            contrast_suggested (bool | Unset): Indicates if there was a suggested change to contrast.
            crop_properties_suggestion_state (CropPropertiesSuggestionState | Unset): A mask that indicates which of the
                fields on the base CropProperties have been changed in this suggestion. For any field set to true, there's a new
                suggested value.
            source_uri_suggested (bool | Unset): Indicates if there was a suggested change to source_uri.
            transparency_suggested (bool | Unset): Indicates if there was a suggested change to transparency.
     """

    angle_suggested: bool | Unset = UNSET
    brightness_suggested: bool | Unset = UNSET
    content_uri_suggested: bool | Unset = UNSET
    contrast_suggested: bool | Unset = UNSET
    crop_properties_suggestion_state: CropPropertiesSuggestionState | Unset = UNSET
    source_uri_suggested: bool | Unset = UNSET
    transparency_suggested: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.crop_properties_suggestion_state import CropPropertiesSuggestionState
        angle_suggested = self.angle_suggested

        brightness_suggested = self.brightness_suggested

        content_uri_suggested = self.content_uri_suggested

        contrast_suggested = self.contrast_suggested

        crop_properties_suggestion_state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.crop_properties_suggestion_state, Unset):
            crop_properties_suggestion_state = self.crop_properties_suggestion_state.to_dict()

        source_uri_suggested = self.source_uri_suggested

        transparency_suggested = self.transparency_suggested


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if angle_suggested is not UNSET:
            field_dict["angleSuggested"] = angle_suggested
        if brightness_suggested is not UNSET:
            field_dict["brightnessSuggested"] = brightness_suggested
        if content_uri_suggested is not UNSET:
            field_dict["contentUriSuggested"] = content_uri_suggested
        if contrast_suggested is not UNSET:
            field_dict["contrastSuggested"] = contrast_suggested
        if crop_properties_suggestion_state is not UNSET:
            field_dict["cropPropertiesSuggestionState"] = crop_properties_suggestion_state
        if source_uri_suggested is not UNSET:
            field_dict["sourceUriSuggested"] = source_uri_suggested
        if transparency_suggested is not UNSET:
            field_dict["transparencySuggested"] = transparency_suggested

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.crop_properties_suggestion_state import CropPropertiesSuggestionState
        d = dict(src_dict)
        angle_suggested = d.pop("angleSuggested", UNSET)

        brightness_suggested = d.pop("brightnessSuggested", UNSET)

        content_uri_suggested = d.pop("contentUriSuggested", UNSET)

        contrast_suggested = d.pop("contrastSuggested", UNSET)

        _crop_properties_suggestion_state = d.pop("cropPropertiesSuggestionState", UNSET)
        crop_properties_suggestion_state: CropPropertiesSuggestionState | Unset
        if isinstance(_crop_properties_suggestion_state,  Unset):
            crop_properties_suggestion_state = UNSET
        else:
            crop_properties_suggestion_state = CropPropertiesSuggestionState.from_dict(_crop_properties_suggestion_state)




        source_uri_suggested = d.pop("sourceUriSuggested", UNSET)

        transparency_suggested = d.pop("transparencySuggested", UNSET)

        image_properties_suggestion_state = cls(
            angle_suggested=angle_suggested,
            brightness_suggested=brightness_suggested,
            content_uri_suggested=content_uri_suggested,
            contrast_suggested=contrast_suggested,
            crop_properties_suggestion_state=crop_properties_suggestion_state,
            source_uri_suggested=source_uri_suggested,
            transparency_suggested=transparency_suggested,
        )


        image_properties_suggestion_state.additional_properties = d
        return image_properties_suggestion_state

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
