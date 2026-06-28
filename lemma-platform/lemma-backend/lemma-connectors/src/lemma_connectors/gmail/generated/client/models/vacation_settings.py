from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="VacationSettings")



@_attrs_define
class VacationSettings:
    """ Vacation auto-reply settings for an account. These settings correspond to the "Vacation responder" feature in the
    web interface.

        Attributes:
            enable_auto_reply (bool | Unset): Flag that controls whether Gmail automatically replies to messages.
            end_time (str | Unset): An optional end time for sending auto-replies (epoch ms). When this is specified, Gmail
                will automatically reply only to messages that it receives before the end time. If both `startTime` and
                `endTime` are specified, `startTime` must precede `endTime`.
            response_body_html (str | Unset): Response body in HTML format. Gmail will sanitize the HTML before storing it.
                If both `response_body_plain_text` and `response_body_html` are specified, `response_body_html` will be used.
            response_body_plain_text (str | Unset): Response body in plain text format. If both `response_body_plain_text`
                and `response_body_html` are specified, `response_body_html` will be used.
            response_subject (str | Unset): Optional text to prepend to the subject line in vacation responses. In order to
                enable auto-replies, either the response subject or the response body must be nonempty.
            restrict_to_contacts (bool | Unset): Flag that determines whether responses are sent to recipients who are not
                in the user's list of contacts.
            restrict_to_domain (bool | Unset): Flag that determines whether responses are sent to recipients who are outside
                of the user's domain. This feature is only available for Google Workspace users.
            start_time (str | Unset): An optional start time for sending auto-replies (epoch ms). When this is specified,
                Gmail will automatically reply only to messages that it receives after the start time. If both `startTime` and
                `endTime` are specified, `startTime` must precede `endTime`.
     """

    enable_auto_reply: bool | Unset = UNSET
    end_time: str | Unset = UNSET
    response_body_html: str | Unset = UNSET
    response_body_plain_text: str | Unset = UNSET
    response_subject: str | Unset = UNSET
    restrict_to_contacts: bool | Unset = UNSET
    restrict_to_domain: bool | Unset = UNSET
    start_time: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        enable_auto_reply = self.enable_auto_reply

        end_time = self.end_time

        response_body_html = self.response_body_html

        response_body_plain_text = self.response_body_plain_text

        response_subject = self.response_subject

        restrict_to_contacts = self.restrict_to_contacts

        restrict_to_domain = self.restrict_to_domain

        start_time = self.start_time


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if enable_auto_reply is not UNSET:
            field_dict["enableAutoReply"] = enable_auto_reply
        if end_time is not UNSET:
            field_dict["endTime"] = end_time
        if response_body_html is not UNSET:
            field_dict["responseBodyHtml"] = response_body_html
        if response_body_plain_text is not UNSET:
            field_dict["responseBodyPlainText"] = response_body_plain_text
        if response_subject is not UNSET:
            field_dict["responseSubject"] = response_subject
        if restrict_to_contacts is not UNSET:
            field_dict["restrictToContacts"] = restrict_to_contacts
        if restrict_to_domain is not UNSET:
            field_dict["restrictToDomain"] = restrict_to_domain
        if start_time is not UNSET:
            field_dict["startTime"] = start_time

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enable_auto_reply = d.pop("enableAutoReply", UNSET)

        end_time = d.pop("endTime", UNSET)

        response_body_html = d.pop("responseBodyHtml", UNSET)

        response_body_plain_text = d.pop("responseBodyPlainText", UNSET)

        response_subject = d.pop("responseSubject", UNSET)

        restrict_to_contacts = d.pop("restrictToContacts", UNSET)

        restrict_to_domain = d.pop("restrictToDomain", UNSET)

        start_time = d.pop("startTime", UNSET)

        vacation_settings = cls(
            enable_auto_reply=enable_auto_reply,
            end_time=end_time,
            response_body_html=response_body_html,
            response_body_plain_text=response_body_plain_text,
            response_subject=response_subject,
            restrict_to_contacts=restrict_to_contacts,
            restrict_to_domain=restrict_to_domain,
            start_time=start_time,
        )


        vacation_settings.additional_properties = d
        return vacation_settings

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
