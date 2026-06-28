from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.users_conversations_users_conversations_success_schema_response_metadata import UsersConversationsUsersConversationsSuccessSchemaResponseMetadata





T = TypeVar("T", bound="UsersConversationsUsersConversationsSuccessSchema")



@_attrs_define
class UsersConversationsUsersConversationsSuccessSchema:
    """ Schema for successful response from users.conversations method. Returned conversation objects do not include
    `num_members` or `is_member`

        Attributes:
            channels (list[Any]):
            ok (bool):
            response_metadata (UsersConversationsUsersConversationsSuccessSchemaResponseMetadata | Unset):
     """

    channels: list[Any]
    ok: bool
    response_metadata: UsersConversationsUsersConversationsSuccessSchemaResponseMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.users_conversations_users_conversations_success_schema_response_metadata import UsersConversationsUsersConversationsSuccessSchemaResponseMetadata
        channels = self.channels



        ok = self.ok

        response_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.response_metadata, Unset):
            response_metadata = self.response_metadata.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "channels": channels,
            "ok": ok,
        })
        if response_metadata is not UNSET:
            field_dict["response_metadata"] = response_metadata

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.users_conversations_users_conversations_success_schema_response_metadata import UsersConversationsUsersConversationsSuccessSchemaResponseMetadata
        d = dict(src_dict)
        channels = cast(list[Any], d.pop("channels"))


        ok = d.pop("ok")

        _response_metadata = d.pop("response_metadata", UNSET)
        response_metadata: UsersConversationsUsersConversationsSuccessSchemaResponseMetadata | Unset
        if isinstance(_response_metadata,  Unset):
            response_metadata = UNSET
        else:
            response_metadata = UsersConversationsUsersConversationsSuccessSchemaResponseMetadata.from_dict(_response_metadata)




        users_conversations_users_conversations_success_schema = cls(
            channels=channels,
            ok=ok,
            response_metadata=response_metadata,
        )


        users_conversations_users_conversations_success_schema.additional_properties = d
        return users_conversations_users_conversations_success_schema

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
