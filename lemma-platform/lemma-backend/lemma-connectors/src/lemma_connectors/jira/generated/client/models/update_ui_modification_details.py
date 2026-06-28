from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.ui_modification_context_details import UiModificationContextDetails





T = TypeVar("T", bound="UpdateUiModificationDetails")



@_attrs_define
class UpdateUiModificationDetails:
    """ The details of a UI modification.

        Attributes:
            contexts (list[UiModificationContextDetails] | Unset): List of contexts of the UI modification. The maximum
                number of contexts is 1000. If provided, replaces all existing contexts.
            data (str | Unset): The data of the UI modification. The maximum size of the data is 50000 characters.
            description (str | Unset): The description of the UI modification. The maximum length is 255 characters.
            name (str | Unset): The name of the UI modification. The maximum length is 255 characters.
     """

    contexts: list[UiModificationContextDetails] | Unset = UNSET
    data: str | Unset = UNSET
    description: str | Unset = UNSET
    name: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.ui_modification_context_details import UiModificationContextDetails
        contexts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.contexts, Unset):
            contexts = []
            for contexts_item_data in self.contexts:
                contexts_item = contexts_item_data.to_dict()
                contexts.append(contexts_item)



        data = self.data

        description = self.description

        name = self.name


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if contexts is not UNSET:
            field_dict["contexts"] = contexts
        if data is not UNSET:
            field_dict["data"] = data
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ui_modification_context_details import UiModificationContextDetails
        d = dict(src_dict)
        _contexts = d.pop("contexts", UNSET)
        contexts: list[UiModificationContextDetails] | Unset = UNSET
        if _contexts is not UNSET:
            contexts = []
            for contexts_item_data in _contexts:
                contexts_item = UiModificationContextDetails.from_dict(contexts_item_data)



                contexts.append(contexts_item)


        data = d.pop("data", UNSET)

        description = d.pop("description", UNSET)

        name = d.pop("name", UNSET)

        update_ui_modification_details = cls(
            contexts=contexts,
            data=data,
            description=description,
            name=name,
        )

        return update_ui_modification_details

