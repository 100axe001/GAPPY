from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.webhook_details_events_item import WebhookDetailsEventsItem
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="WebhookDetails")



@_attrs_define
class WebhookDetails:
    """ A list of webhooks.

        Attributes:
            events (list[WebhookDetailsEventsItem]): The Jira events that trigger the webhook.
            jql_filter (str): The JQL filter that specifies which issues the webhook is sent for. Only a subset of JQL can
                be used. The supported elements are:

                 *  Fields: `issueKey`, `project`, `issuetype`, `status`, `assignee`, `reporter`, `issue.property`, and
                `cf[id]`. For custom fields (`cf[id]`), only the epic label custom field is supported.".
                 *  Operators: `=`, `!=`, `IN`, and `NOT IN`.
            field_ids_filter (list[str] | Unset): A list of field IDs. When the issue changelog contains any of the fields,
                the webhook `jira:issue_updated` is sent. If this parameter is not present, the app is notified about all field
                updates.
            issue_property_keys_filter (list[str] | Unset): A list of issue property keys. A change of those issue
                properties triggers the `issue_property_set` or `issue_property_deleted` webhooks. If this parameter is not
                present, the app is notified about all issue property updates.
     """

    events: list[WebhookDetailsEventsItem]
    jql_filter: str
    field_ids_filter: list[str] | Unset = UNSET
    issue_property_keys_filter: list[str] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        events = []
        for events_item_data in self.events:
            events_item = events_item_data.value
            events.append(events_item)



        jql_filter = self.jql_filter

        field_ids_filter: list[str] | Unset = UNSET
        if not isinstance(self.field_ids_filter, Unset):
            field_ids_filter = self.field_ids_filter



        issue_property_keys_filter: list[str] | Unset = UNSET
        if not isinstance(self.issue_property_keys_filter, Unset):
            issue_property_keys_filter = self.issue_property_keys_filter




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "events": events,
            "jqlFilter": jql_filter,
        })
        if field_ids_filter is not UNSET:
            field_dict["fieldIdsFilter"] = field_ids_filter
        if issue_property_keys_filter is not UNSET:
            field_dict["issuePropertyKeysFilter"] = issue_property_keys_filter

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        events = []
        _events = d.pop("events")
        for events_item_data in (_events):
            events_item = WebhookDetailsEventsItem(events_item_data)



            events.append(events_item)


        jql_filter = d.pop("jqlFilter")

        field_ids_filter = cast(list[str], d.pop("fieldIdsFilter", UNSET))


        issue_property_keys_filter = cast(list[str], d.pop("issuePropertyKeysFilter", UNSET))


        webhook_details = cls(
            events=events,
            jql_filter=jql_filter,
            field_ids_filter=field_ids_filter,
            issue_property_keys_filter=issue_property_keys_filter,
        )

        return webhook_details

