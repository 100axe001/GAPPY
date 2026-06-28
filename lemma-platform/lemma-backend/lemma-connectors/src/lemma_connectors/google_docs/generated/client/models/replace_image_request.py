from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.replace_image_request_image_replace_method import ReplaceImageRequestImageReplaceMethod
from ..types import UNSET, Unset






T = TypeVar("T", bound="ReplaceImageRequest")



@_attrs_define
class ReplaceImageRequest:
    """ Replaces an existing image with a new image. Replacing an image removes some image effects from the existing image
    in order to mirror the behavior of the Docs editor.

        Attributes:
            image_object_id (str | Unset): The ID of the existing image that will be replaced. The ID can be retrieved from
                the response of a get request.
            image_replace_method (ReplaceImageRequestImageReplaceMethod | Unset): The replacement method.
            uri (str | Unset): The URI of the new image. The image is fetched once at insertion time and a copy is stored
                for display inside the document. Images must be less than 50MB, cannot exceed 25 megapixels, and must be in PNG,
                JPEG, or GIF format. The provided URI can't surpass 2 KB in length. The URI is saved with the image, and exposed
                through the ImageProperties.source_uri field.
     """

    image_object_id: str | Unset = UNSET
    image_replace_method: ReplaceImageRequestImageReplaceMethod | Unset = UNSET
    uri: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        image_object_id = self.image_object_id

        image_replace_method: str | Unset = UNSET
        if not isinstance(self.image_replace_method, Unset):
            image_replace_method = self.image_replace_method.value


        uri = self.uri


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if image_object_id is not UNSET:
            field_dict["imageObjectId"] = image_object_id
        if image_replace_method is not UNSET:
            field_dict["imageReplaceMethod"] = image_replace_method
        if uri is not UNSET:
            field_dict["uri"] = uri

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        image_object_id = d.pop("imageObjectId", UNSET)

        _image_replace_method = d.pop("imageReplaceMethod", UNSET)
        image_replace_method: ReplaceImageRequestImageReplaceMethod | Unset
        if isinstance(_image_replace_method,  Unset):
            image_replace_method = UNSET
        else:
            image_replace_method = ReplaceImageRequestImageReplaceMethod(_image_replace_method)




        uri = d.pop("uri", UNSET)

        replace_image_request = cls(
            image_object_id=image_object_id,
            image_replace_method=image_replace_method,
            uri=uri,
        )


        replace_image_request.additional_properties = d
        return replace_image_request

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
