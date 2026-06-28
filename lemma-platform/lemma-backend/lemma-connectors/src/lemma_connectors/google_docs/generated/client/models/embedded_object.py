from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.dimension import Dimension
  from ..models.embedded_drawing_properties import EmbeddedDrawingProperties
  from ..models.embedded_object_border import EmbeddedObjectBorder
  from ..models.image_properties import ImageProperties
  from ..models.linked_content_reference import LinkedContentReference
  from ..models.size import Size





T = TypeVar("T", bound="EmbeddedObject")



@_attrs_define
class EmbeddedObject:
    """ An embedded object in the document.

        Attributes:
            description (str | Unset): The description of the embedded object. The `title` and `description` are both
                combined to display alt text.
            embedded_drawing_properties (EmbeddedDrawingProperties | Unset): The properties of an embedded drawing and used
                to differentiate the object type. An embedded drawing is one that's created and edited within a document. Note
                that extensive details are not supported.
            embedded_object_border (EmbeddedObjectBorder | Unset): A border around an EmbeddedObject.
            image_properties (ImageProperties | Unset): The properties of an image.
            linked_content_reference (LinkedContentReference | Unset): A reference to the external linked source content.
            margin_bottom (Dimension | Unset): A magnitude in a single direction in the specified units.
            margin_left (Dimension | Unset): A magnitude in a single direction in the specified units.
            margin_right (Dimension | Unset): A magnitude in a single direction in the specified units.
            margin_top (Dimension | Unset): A magnitude in a single direction in the specified units.
            size (Size | Unset): A width and height.
            title (str | Unset): The title of the embedded object. The `title` and `description` are both combined to
                display alt text.
     """

    description: str | Unset = UNSET
    embedded_drawing_properties: EmbeddedDrawingProperties | Unset = UNSET
    embedded_object_border: EmbeddedObjectBorder | Unset = UNSET
    image_properties: ImageProperties | Unset = UNSET
    linked_content_reference: LinkedContentReference | Unset = UNSET
    margin_bottom: Dimension | Unset = UNSET
    margin_left: Dimension | Unset = UNSET
    margin_right: Dimension | Unset = UNSET
    margin_top: Dimension | Unset = UNSET
    size: Size | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.dimension import Dimension
        from ..models.embedded_drawing_properties import EmbeddedDrawingProperties
        from ..models.embedded_object_border import EmbeddedObjectBorder
        from ..models.image_properties import ImageProperties
        from ..models.linked_content_reference import LinkedContentReference
        from ..models.size import Size
        description = self.description

        embedded_drawing_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.embedded_drawing_properties, Unset):
            embedded_drawing_properties = self.embedded_drawing_properties.to_dict()

        embedded_object_border: dict[str, Any] | Unset = UNSET
        if not isinstance(self.embedded_object_border, Unset):
            embedded_object_border = self.embedded_object_border.to_dict()

        image_properties: dict[str, Any] | Unset = UNSET
        if not isinstance(self.image_properties, Unset):
            image_properties = self.image_properties.to_dict()

        linked_content_reference: dict[str, Any] | Unset = UNSET
        if not isinstance(self.linked_content_reference, Unset):
            linked_content_reference = self.linked_content_reference.to_dict()

        margin_bottom: dict[str, Any] | Unset = UNSET
        if not isinstance(self.margin_bottom, Unset):
            margin_bottom = self.margin_bottom.to_dict()

        margin_left: dict[str, Any] | Unset = UNSET
        if not isinstance(self.margin_left, Unset):
            margin_left = self.margin_left.to_dict()

        margin_right: dict[str, Any] | Unset = UNSET
        if not isinstance(self.margin_right, Unset):
            margin_right = self.margin_right.to_dict()

        margin_top: dict[str, Any] | Unset = UNSET
        if not isinstance(self.margin_top, Unset):
            margin_top = self.margin_top.to_dict()

        size: dict[str, Any] | Unset = UNSET
        if not isinstance(self.size, Unset):
            size = self.size.to_dict()

        title = self.title


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
        if embedded_drawing_properties is not UNSET:
            field_dict["embeddedDrawingProperties"] = embedded_drawing_properties
        if embedded_object_border is not UNSET:
            field_dict["embeddedObjectBorder"] = embedded_object_border
        if image_properties is not UNSET:
            field_dict["imageProperties"] = image_properties
        if linked_content_reference is not UNSET:
            field_dict["linkedContentReference"] = linked_content_reference
        if margin_bottom is not UNSET:
            field_dict["marginBottom"] = margin_bottom
        if margin_left is not UNSET:
            field_dict["marginLeft"] = margin_left
        if margin_right is not UNSET:
            field_dict["marginRight"] = margin_right
        if margin_top is not UNSET:
            field_dict["marginTop"] = margin_top
        if size is not UNSET:
            field_dict["size"] = size
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dimension import Dimension
        from ..models.embedded_drawing_properties import EmbeddedDrawingProperties
        from ..models.embedded_object_border import EmbeddedObjectBorder
        from ..models.image_properties import ImageProperties
        from ..models.linked_content_reference import LinkedContentReference
        from ..models.size import Size
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        _embedded_drawing_properties = d.pop("embeddedDrawingProperties", UNSET)
        embedded_drawing_properties: EmbeddedDrawingProperties | Unset
        if isinstance(_embedded_drawing_properties,  Unset):
            embedded_drawing_properties = UNSET
        else:
            embedded_drawing_properties = EmbeddedDrawingProperties.from_dict(_embedded_drawing_properties)




        _embedded_object_border = d.pop("embeddedObjectBorder", UNSET)
        embedded_object_border: EmbeddedObjectBorder | Unset
        if isinstance(_embedded_object_border,  Unset):
            embedded_object_border = UNSET
        else:
            embedded_object_border = EmbeddedObjectBorder.from_dict(_embedded_object_border)




        _image_properties = d.pop("imageProperties", UNSET)
        image_properties: ImageProperties | Unset
        if isinstance(_image_properties,  Unset):
            image_properties = UNSET
        else:
            image_properties = ImageProperties.from_dict(_image_properties)




        _linked_content_reference = d.pop("linkedContentReference", UNSET)
        linked_content_reference: LinkedContentReference | Unset
        if isinstance(_linked_content_reference,  Unset):
            linked_content_reference = UNSET
        else:
            linked_content_reference = LinkedContentReference.from_dict(_linked_content_reference)




        _margin_bottom = d.pop("marginBottom", UNSET)
        margin_bottom: Dimension | Unset
        if isinstance(_margin_bottom,  Unset):
            margin_bottom = UNSET
        else:
            margin_bottom = Dimension.from_dict(_margin_bottom)




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




        _size = d.pop("size", UNSET)
        size: Size | Unset
        if isinstance(_size,  Unset):
            size = UNSET
        else:
            size = Size.from_dict(_size)




        title = d.pop("title", UNSET)

        embedded_object = cls(
            description=description,
            embedded_drawing_properties=embedded_drawing_properties,
            embedded_object_border=embedded_object_border,
            image_properties=image_properties,
            linked_content_reference=linked_content_reference,
            margin_bottom=margin_bottom,
            margin_left=margin_left,
            margin_right=margin_right,
            margin_top=margin_top,
            size=size,
            title=title,
        )


        embedded_object.additional_properties = d
        return embedded_object

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
