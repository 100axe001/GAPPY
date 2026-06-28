from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.notification_recipients import NotificationRecipients
  from ..models.notification_recipients_restrictions import NotificationRecipientsRestrictions





T = TypeVar("T", bound="Notification")



@_attrs_define
class Notification:
    """ Details about a notification.

        Attributes:
            html_body (str | Unset): The HTML body of the email notification for the issue.
            restrict (NotificationRecipientsRestrictions | Unset): Details of the group membership or permissions needed to
                receive the notification.
            subject (str | Unset): The subject of the email notification for the issue. If this is not specified, then the
                subject is set to the issue key and summary.
            text_body (str | Unset): The plain text body of the email notification for the issue.
            to (NotificationRecipients | Unset): Details of the users and groups to receive the notification.
     """

    html_body: str | Unset = UNSET
    restrict: NotificationRecipientsRestrictions | Unset = UNSET
    subject: str | Unset = UNSET
    text_body: str | Unset = UNSET
    to: NotificationRecipients | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.notification_recipients import NotificationRecipients
        from ..models.notification_recipients_restrictions import NotificationRecipientsRestrictions
        html_body = self.html_body

        restrict: dict[str, Any] | Unset = UNSET
        if not isinstance(self.restrict, Unset):
            restrict = self.restrict.to_dict()

        subject = self.subject

        text_body = self.text_body

        to: dict[str, Any] | Unset = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if html_body is not UNSET:
            field_dict["htmlBody"] = html_body
        if restrict is not UNSET:
            field_dict["restrict"] = restrict
        if subject is not UNSET:
            field_dict["subject"] = subject
        if text_body is not UNSET:
            field_dict["textBody"] = text_body
        if to is not UNSET:
            field_dict["to"] = to

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.notification_recipients import NotificationRecipients
        from ..models.notification_recipients_restrictions import NotificationRecipientsRestrictions
        d = dict(src_dict)
        html_body = d.pop("htmlBody", UNSET)

        _restrict = d.pop("restrict", UNSET)
        restrict: NotificationRecipientsRestrictions | Unset
        if isinstance(_restrict,  Unset):
            restrict = UNSET
        else:
            restrict = NotificationRecipientsRestrictions.from_dict(_restrict)




        subject = d.pop("subject", UNSET)

        text_body = d.pop("textBody", UNSET)

        _to = d.pop("to", UNSET)
        to: NotificationRecipients | Unset
        if isinstance(_to,  Unset):
            to = UNSET
        else:
            to = NotificationRecipients.from_dict(_to)




        notification = cls(
            html_body=html_body,
            restrict=restrict,
            subject=subject,
            text_body=text_body,
            to=to,
        )


        notification.additional_properties = d
        return notification

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
