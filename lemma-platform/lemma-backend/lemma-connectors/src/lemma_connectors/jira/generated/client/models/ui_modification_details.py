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





T = TypeVar("T", bound="UiModificationDetails")



@_attrs_define
class UiModificationDetails:
    """ The details of a UI modification.

        Attributes:
            id (str): The ID of the UI modification.
            name (str): The name of the UI modification. The maximum length is 255 characters.
            self_ (str): The URL of the UI modification.
            contexts (list[UiModificationContextDetails] | Unset): List of contexts of the UI modification. The maximum
                number of contexts is 1000.
            data (str | Unset): The data of the UI modification. The maximum size of the data is 50000 characters.
            description (str | Unset): The description of the UI modification. The maximum length is 255 characters.
     """

    id: str
    name: str
    self_: str
    contexts: list[UiModificationContextDetails] | Unset = UNSET
    data: str | Unset = UNSET
    description: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.ui_modification_context_details import UiModificationContextDetails
        id = self.id

        name = self.name

        self_ = self.self_

        contexts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.contexts, Unset):
            contexts = []
            for contexts_item_data in self.contexts:
                contexts_item = contexts_item_data.to_dict()
                contexts.append(contexts_item)



        data = self.data

        description = self.description


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "id": id,
            "name": name,
            "self": self_,
        })
        if contexts is not UNSET:
            field_dict["contexts"] = contexts
        if data is not UNSET:
            field_dict["data"] = data
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.ui_modification_context_details import UiModificationContextDetails
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        self_ = d.pop("self")

        _contexts = d.pop("contexts", UNSET)
        contexts: list[UiModificationContextDetails] | Unset = UNSET
        if _contexts is not UNSET:
            contexts = []
            for contexts_item_data in _contexts:
                contexts_item = UiModificationContextDetails.from_dict(contexts_item_data)



                contexts.append(contexts_item)


        data = d.pop("data", UNSET)

        description = d.pop("description", UNSET)

        ui_modification_details = cls(
            id=id,
            name=name,
            self_=self_,
            contexts=contexts,
            data=data,
            description=description,
        )

        return ui_modification_details

