from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.channel_object_purpose import ChannelObjectPurpose
  from ..models.channel_object_topic import ChannelObjectTopic





T = TypeVar("T", bound="ChannelObject")



@_attrs_define
class ChannelObject:
    """ 
        Attributes:
            created (int):
            creator (str):
            id (str):
            is_channel (bool):
            is_mpim (bool):
            is_org_shared (bool):
            is_private (bool):
            is_shared (bool):
            members (list[str]):
            name (str):
            name_normalized (str):
            purpose (ChannelObjectPurpose):
            topic (ChannelObjectTopic):
            accepted_user (str | Unset):
            is_archived (bool | Unset):
            is_frozen (bool | Unset):
            is_general (bool | Unset):
            is_member (bool | Unset):
            is_moved (int | Unset):
            is_non_threadable (bool | Unset):
            is_pending_ext_shared (bool | Unset):
            is_read_only (bool | Unset):
            is_thread_only (bool | Unset):
            last_read (str | Unset):
            latest (Any | Unset):
            num_members (int | Unset):
            pending_shared (list[str] | Unset):
            previous_names (list[str] | Unset):
            priority (float | Unset):
            unlinked (int | Unset):
            unread_count (int | Unset):
            unread_count_display (int | Unset):
     """

    created: int
    creator: str
    id: str
    is_channel: bool
    is_mpim: bool
    is_org_shared: bool
    is_private: bool
    is_shared: bool
    members: list[str]
    name: str
    name_normalized: str
    purpose: ChannelObjectPurpose
    topic: ChannelObjectTopic
    accepted_user: str | Unset = UNSET
    is_archived: bool | Unset = UNSET
    is_frozen: bool | Unset = UNSET
    is_general: bool | Unset = UNSET
    is_member: bool | Unset = UNSET
    is_moved: int | Unset = UNSET
    is_non_threadable: bool | Unset = UNSET
    is_pending_ext_shared: bool | Unset = UNSET
    is_read_only: bool | Unset = UNSET
    is_thread_only: bool | Unset = UNSET
    last_read: str | Unset = UNSET
    latest: Any | Unset = UNSET
    num_members: int | Unset = UNSET
    pending_shared: list[str] | Unset = UNSET
    previous_names: list[str] | Unset = UNSET
    priority: float | Unset = UNSET
    unlinked: int | Unset = UNSET
    unread_count: int | Unset = UNSET
    unread_count_display: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.channel_object_purpose import ChannelObjectPurpose
        from ..models.channel_object_topic import ChannelObjectTopic
        created = self.created

        creator = self.creator

        id = self.id

        is_channel = self.is_channel

        is_mpim = self.is_mpim

        is_org_shared = self.is_org_shared

        is_private = self.is_private

        is_shared = self.is_shared

        members = self.members



        name = self.name

        name_normalized = self.name_normalized

        purpose = self.purpose.to_dict()

        topic = self.topic.to_dict()

        accepted_user = self.accepted_user

        is_archived = self.is_archived

        is_frozen = self.is_frozen

        is_general = self.is_general

        is_member = self.is_member

        is_moved = self.is_moved

        is_non_threadable = self.is_non_threadable

        is_pending_ext_shared = self.is_pending_ext_shared

        is_read_only = self.is_read_only

        is_thread_only = self.is_thread_only

        last_read = self.last_read

        latest = self.latest

        num_members = self.num_members

        pending_shared: list[str] | Unset = UNSET
        if not isinstance(self.pending_shared, Unset):
            pending_shared = self.pending_shared



        previous_names: list[str] | Unset = UNSET
        if not isinstance(self.previous_names, Unset):
            previous_names = self.previous_names



        priority = self.priority

        unlinked = self.unlinked

        unread_count = self.unread_count

        unread_count_display = self.unread_count_display


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "created": created,
            "creator": creator,
            "id": id,
            "is_channel": is_channel,
            "is_mpim": is_mpim,
            "is_org_shared": is_org_shared,
            "is_private": is_private,
            "is_shared": is_shared,
            "members": members,
            "name": name,
            "name_normalized": name_normalized,
            "purpose": purpose,
            "topic": topic,
        })
        if accepted_user is not UNSET:
            field_dict["accepted_user"] = accepted_user
        if is_archived is not UNSET:
            field_dict["is_archived"] = is_archived
        if is_frozen is not UNSET:
            field_dict["is_frozen"] = is_frozen
        if is_general is not UNSET:
            field_dict["is_general"] = is_general
        if is_member is not UNSET:
            field_dict["is_member"] = is_member
        if is_moved is not UNSET:
            field_dict["is_moved"] = is_moved
        if is_non_threadable is not UNSET:
            field_dict["is_non_threadable"] = is_non_threadable
        if is_pending_ext_shared is not UNSET:
            field_dict["is_pending_ext_shared"] = is_pending_ext_shared
        if is_read_only is not UNSET:
            field_dict["is_read_only"] = is_read_only
        if is_thread_only is not UNSET:
            field_dict["is_thread_only"] = is_thread_only
        if last_read is not UNSET:
            field_dict["last_read"] = last_read
        if latest is not UNSET:
            field_dict["latest"] = latest
        if num_members is not UNSET:
            field_dict["num_members"] = num_members
        if pending_shared is not UNSET:
            field_dict["pending_shared"] = pending_shared
        if previous_names is not UNSET:
            field_dict["previous_names"] = previous_names
        if priority is not UNSET:
            field_dict["priority"] = priority
        if unlinked is not UNSET:
            field_dict["unlinked"] = unlinked
        if unread_count is not UNSET:
            field_dict["unread_count"] = unread_count
        if unread_count_display is not UNSET:
            field_dict["unread_count_display"] = unread_count_display

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.channel_object_purpose import ChannelObjectPurpose
        from ..models.channel_object_topic import ChannelObjectTopic
        d = dict(src_dict)
        created = d.pop("created")

        creator = d.pop("creator")

        id = d.pop("id")

        is_channel = d.pop("is_channel")

        is_mpim = d.pop("is_mpim")

        is_org_shared = d.pop("is_org_shared")

        is_private = d.pop("is_private")

        is_shared = d.pop("is_shared")

        members = cast(list[str], d.pop("members"))


        name = d.pop("name")

        name_normalized = d.pop("name_normalized")

        purpose = ChannelObjectPurpose.from_dict(d.pop("purpose"))




        topic = ChannelObjectTopic.from_dict(d.pop("topic"))




        accepted_user = d.pop("accepted_user", UNSET)

        is_archived = d.pop("is_archived", UNSET)

        is_frozen = d.pop("is_frozen", UNSET)

        is_general = d.pop("is_general", UNSET)

        is_member = d.pop("is_member", UNSET)

        is_moved = d.pop("is_moved", UNSET)

        is_non_threadable = d.pop("is_non_threadable", UNSET)

        is_pending_ext_shared = d.pop("is_pending_ext_shared", UNSET)

        is_read_only = d.pop("is_read_only", UNSET)

        is_thread_only = d.pop("is_thread_only", UNSET)

        last_read = d.pop("last_read", UNSET)

        latest = d.pop("latest", UNSET)

        num_members = d.pop("num_members", UNSET)

        pending_shared = cast(list[str], d.pop("pending_shared", UNSET))


        previous_names = cast(list[str], d.pop("previous_names", UNSET))


        priority = d.pop("priority", UNSET)

        unlinked = d.pop("unlinked", UNSET)

        unread_count = d.pop("unread_count", UNSET)

        unread_count_display = d.pop("unread_count_display", UNSET)

        channel_object = cls(
            created=created,
            creator=creator,
            id=id,
            is_channel=is_channel,
            is_mpim=is_mpim,
            is_org_shared=is_org_shared,
            is_private=is_private,
            is_shared=is_shared,
            members=members,
            name=name,
            name_normalized=name_normalized,
            purpose=purpose,
            topic=topic,
            accepted_user=accepted_user,
            is_archived=is_archived,
            is_frozen=is_frozen,
            is_general=is_general,
            is_member=is_member,
            is_moved=is_moved,
            is_non_threadable=is_non_threadable,
            is_pending_ext_shared=is_pending_ext_shared,
            is_read_only=is_read_only,
            is_thread_only=is_thread_only,
            last_read=last_read,
            latest=latest,
            num_members=num_members,
            pending_shared=pending_shared,
            previous_names=previous_names,
            priority=priority,
            unlinked=unlinked,
            unread_count=unread_count,
            unread_count_display=unread_count_display,
        )

        return channel_object

