from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.webhook_events_item import WebhookEventsItem
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="Webhook")



@_attrs_define
class Webhook:
    """ A webhook.

        Attributes:
            events (list[WebhookEventsItem]): The Jira events that trigger the webhook.
            id (int): The ID of the webhook.
            jql_filter (str): The JQL filter that specifies which issues the webhook is sent for.
            expiration_date (int | Unset): The date after which the webhook is no longer sent. Use [Extend webhook
                life](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-webhooks/#api-rest-api-3-webhook-
                refresh-put) to extend the date.
            field_ids_filter (list[str] | Unset): A list of field IDs. When the issue changelog contains any of the fields,
                the webhook `jira:issue_updated` is sent. If this parameter is not present, the app is notified about all field
                updates.
            issue_property_keys_filter (list[str] | Unset): A list of issue property keys. A change of those issue
                properties triggers the `issue_property_set` or `issue_property_deleted` webhooks. If this parameter is not
                present, the app is notified about all issue property updates.
     """

    events: list[WebhookEventsItem]
    id: int
    jql_filter: str
    expiration_date: int | Unset = UNSET
    field_ids_filter: list[str] | Unset = UNSET
    issue_property_keys_filter: list[str] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        events = []
        for events_item_data in self.events:
            events_item = events_item_data.value
            events.append(events_item)



        id = self.id

        jql_filter = self.jql_filter

        expiration_date = self.expiration_date

        field_ids_filter: list[str] | Unset = UNSET
        if not isinstance(self.field_ids_filter, Unset):
            field_ids_filter = self.field_ids_filter



        issue_property_keys_filter: list[str] | Unset = UNSET
        if not isinstance(self.issue_property_keys_filter, Unset):
            issue_property_keys_filter = self.issue_property_keys_filter




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "events": events,
            "id": id,
            "jqlFilter": jql_filter,
        })
        if expiration_date is not UNSET:
            field_dict["expirationDate"] = expiration_date
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
            events_item = WebhookEventsItem(events_item_data)



            events.append(events_item)


        id = d.pop("id")

        jql_filter = d.pop("jqlFilter")

        expiration_date = d.pop("expirationDate", UNSET)

        field_ids_filter = cast(list[str], d.pop("fieldIdsFilter", UNSET))


        issue_property_keys_filter = cast(list[str], d.pop("issuePropertyKeysFilter", UNSET))


        webhook = cls(
            events=events,
            id=id,
            jql_filter=jql_filter,
            expiration_date=expiration_date,
            field_ids_filter=field_ids_filter,
            issue_property_keys_filter=issue_property_keys_filter,
        )

        return webhook

