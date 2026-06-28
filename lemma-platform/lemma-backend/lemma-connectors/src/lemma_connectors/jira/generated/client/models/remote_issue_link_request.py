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





T = TypeVar("T", bound="RemoteIssueLinkRequest")



@_attrs_define
class RemoteIssueLinkRequest:
    """ Details of a remote issue link.

        Attributes:
            object_ (RemoteObject): The linked item.
            application (Application | Unset): The application the linked item is in.
            global_id (str | Unset): An identifier for the remote item in the remote system. For example, the global ID for
                a remote item in Confluence would consist of the app ID and page ID, like this: `appId=456&pageId=123`.

                Setting this field enables the remote issue link details to be updated or deleted using remote system and item
                details as the record identifier, rather than using the record's Jira ID.

                The maximum length is 255 characters.
            relationship (str | Unset): Description of the relationship between the issue and the linked item. If not set,
                the relationship description "links to" is used in Jira.
     """

    object_: RemoteObject
    application: Application | Unset = UNSET
    global_id: str | Unset = UNSET
    relationship: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.application import Application
        from ..models.remote_object import RemoteObject
        object_ = self.object_.to_dict()

        application: dict[str, Any] | Unset = UNSET
        if not isinstance(self.application, Unset):
            application = self.application.to_dict()

        global_id = self.global_id

        relationship = self.relationship


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "object": object_,
        })
        if application is not UNSET:
            field_dict["application"] = application
        if global_id is not UNSET:
            field_dict["globalId"] = global_id
        if relationship is not UNSET:
            field_dict["relationship"] = relationship

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.application import Application
        from ..models.remote_object import RemoteObject
        d = dict(src_dict)
        object_ = RemoteObject.from_dict(d.pop("object"))




        _application = d.pop("application", UNSET)
        application: Application | Unset
        if isinstance(_application,  Unset):
            application = UNSET
        else:
            application = Application.from_dict(_application)




        global_id = d.pop("globalId", UNSET)

        relationship = d.pop("relationship", UNSET)

        remote_issue_link_request = cls(
            object_=object_,
            application=application,
            global_id=global_id,
            relationship=relationship,
        )


        remote_issue_link_request.additional_properties = d
        return remote_issue_link_request

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
