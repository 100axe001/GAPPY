from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.watch_request_label_filter_action import WatchRequestLabelFilterAction
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="WatchRequest")



@_attrs_define
class WatchRequest:
    """ Set up or update a new push notification watch on this user's mailbox.

        Attributes:
            label_filter_action (WatchRequestLabelFilterAction | Unset): Filtering behavior of labelIds list specified.
            label_ids (list[str] | Unset): List of label_ids to restrict notifications about. By default, if unspecified,
                all changes are pushed out. If specified then dictates which labels are required for a push notification to be
                generated.
            topic_name (str | Unset): A fully qualified Google Cloud Pub/Sub API topic name to publish the events to. This
                topic name **must** already exist in Cloud Pub/Sub and you **must** have already granted gmail "publish"
                permission on it. For example, "projects/my-project-identifier/topics/my-topic-name" (using the Cloud Pub/Sub
                "v1" topic naming format). Note that the "my-project-identifier" portion must exactly match your Google
                developer project id (the one executing this watch request).
     """

    label_filter_action: WatchRequestLabelFilterAction | Unset = UNSET
    label_ids: list[str] | Unset = UNSET
    topic_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        label_filter_action: str | Unset = UNSET
        if not isinstance(self.label_filter_action, Unset):
            label_filter_action = self.label_filter_action.value


        label_ids: list[str] | Unset = UNSET
        if not isinstance(self.label_ids, Unset):
            label_ids = self.label_ids



        topic_name = self.topic_name


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if label_filter_action is not UNSET:
            field_dict["labelFilterAction"] = label_filter_action
        if label_ids is not UNSET:
            field_dict["labelIds"] = label_ids
        if topic_name is not UNSET:
            field_dict["topicName"] = topic_name

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _label_filter_action = d.pop("labelFilterAction", UNSET)
        label_filter_action: WatchRequestLabelFilterAction | Unset
        if isinstance(_label_filter_action,  Unset):
            label_filter_action = UNSET
        else:
            label_filter_action = WatchRequestLabelFilterAction(_label_filter_action)




        label_ids = cast(list[str], d.pop("labelIds", UNSET))


        topic_name = d.pop("topicName", UNSET)

        watch_request = cls(
            label_filter_action=label_filter_action,
            label_ids=label_ids,
            topic_name=topic_name,
        )


        watch_request.additional_properties = d
        return watch_request

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
