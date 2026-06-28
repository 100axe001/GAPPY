from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.application import Application
  from ..models.remote_object import RemoteObject





T = TypeVar("T", bound="RemoteIssueLink")



@_attrs_define
class RemoteIssueLink:
    """ Details of an issue remote link.

        Attributes:
            application (Application | Unset): The application the linked item is in.
            global_id (str | Unset): The global ID of the link, such as the ID of the item on the remote system.
            id (int | Unset): The ID of the link.
            object_ (RemoteObject | Unset): The linked item.
            relationship (str | Unset): Description of the relationship between the issue and the linked item.
            self_ (str | Unset): The URL of the link.
     """

    application: Application | Unset = UNSET
    global_id: str | Unset = UNSET
    id: int | Unset = UNSET
    object_: RemoteObject | Unset = UNSET
    relationship: str | Unset = UNSET
    self_: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.application import Application
        from ..models.remote_object import RemoteObject
        application: dict[str, Any] | Unset = UNSET
        if not isinstance(self.application, Unset):
            application = self.application.to_dict()

        global_id = self.global_id

        id = self.id

        object_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.object_, Unset):
            object_ = self.object_.to_dict()

        relationship = self.relationship

        self_ = self.self_


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if application is not UNSET:
            field_dict["application"] = application
        if global_id is not UNSET:
            field_dict["globalId"] = global_id
        if id is not UNSET:
            field_dict["id"] = id
        if object_ is not UNSET:
            field_dict["object"] = object_
        if relationship is not UNSET:
            field_dict["relationship"] = relationship
        if self_ is not UNSET:
            field_dict["self"] = self_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.application import Application
        from ..models.remote_object import RemoteObject
        d = dict(src_dict)
        _application = d.pop("application", UNSET)
        application: Application | Unset
        if isinstance(_application,  Unset):
            application = UNSET
        else:
            application = Application.from_dict(_application)




        global_id = d.pop("globalId", UNSET)

        id = d.pop("id", UNSET)

        _object_ = d.pop("object", UNSET)
        object_: RemoteObject | Unset
        if isinstance(_object_,  Unset):
            object_ = UNSET
        else:
            object_ = RemoteObject.from_dict(_object_)




        relationship = d.pop("relationship", UNSET)

        self_ = d.pop("self", UNSET)

        remote_issue_link = cls(
            application=application,
            global_id=global_id,
            id=id,
            object_=object_,
            relationship=relationship,
            self_=self_,
        )

        return remote_issue_link

