from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="EntryPoint")



@_attrs_define
class EntryPoint:
    """ 
        Attributes:
            access_code (str | Unset): The access code to access the conference. The maximum length is 128 characters.
                When creating new conference data, populate only the subset of {meetingCode, accessCode, passcode, password,
                pin} fields that match the terminology that the conference provider uses. Only the populated fields should be
                displayed.
                Optional.
            entry_point_features (list[str] | Unset): Features of the entry point, such as being toll or toll-free. One
                entry point can have multiple features. However, toll and toll-free cannot be both set on the same entry point.
            entry_point_type (str | Unset): The type of the conference entry point.
                Possible values are:
                - "video" - joining a conference over HTTP. A conference can have zero or one video entry point.
                - "phone" - joining a conference by dialing a phone number. A conference can have zero or more phone entry
                points.
                - "sip" - joining a conference over SIP. A conference can have zero or one sip entry point.
                - "more" - further conference joining instructions, for example additional phone numbers. A conference can have
                zero or one more entry point. A conference with only a more entry point is not a valid conference.
            label (str | Unset): The label for the URI. Visible to end users. Not localized. The maximum length is 512
                characters.
                Examples:
                - for video: meet.google.com/aaa-bbbb-ccc
                - for phone: +1 123 268 2601
                - for sip: 12345678@altostrat.com
                - for more: should not be filled
                Optional.
            meeting_code (str | Unset): The meeting code to access the conference. The maximum length is 128 characters.
                When creating new conference data, populate only the subset of {meetingCode, accessCode, passcode, password,
                pin} fields that match the terminology that the conference provider uses. Only the populated fields should be
                displayed.
                Optional.
            passcode (str | Unset): The passcode to access the conference. The maximum length is 128 characters.
                When creating new conference data, populate only the subset of {meetingCode, accessCode, passcode, password,
                pin} fields that match the terminology that the conference provider uses. Only the populated fields should be
                displayed.
            password (str | Unset): The password to access the conference. The maximum length is 128 characters.
                When creating new conference data, populate only the subset of {meetingCode, accessCode, passcode, password,
                pin} fields that match the terminology that the conference provider uses. Only the populated fields should be
                displayed.
                Optional.
            pin (str | Unset): The PIN to access the conference. The maximum length is 128 characters.
                When creating new conference data, populate only the subset of {meetingCode, accessCode, passcode, password,
                pin} fields that match the terminology that the conference provider uses. Only the populated fields should be
                displayed.
                Optional.
            region_code (str | Unset): The CLDR/ISO 3166 region code for the country associated with this phone access.
                Example: "SE" for Sweden.
                Calendar backend will populate this field only for EntryPointType.PHONE.
            uri (str | Unset): The URI of the entry point. The maximum length is 1300 characters.
                Format:
                - for video, http: or https: schema is required.
                - for phone, tel: schema is required. The URI should include the entire dial sequence (e.g.,
                tel:+12345678900,,,123456789;1234).
                - for sip, sip: schema is required, e.g., sip:12345678@myprovider.com.
                - for more, http: or https: schema is required.
     """

    access_code: str | Unset = UNSET
    entry_point_features: list[str] | Unset = UNSET
    entry_point_type: str | Unset = UNSET
    label: str | Unset = UNSET
    meeting_code: str | Unset = UNSET
    passcode: str | Unset = UNSET
    password: str | Unset = UNSET
    pin: str | Unset = UNSET
    region_code: str | Unset = UNSET
    uri: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        access_code = self.access_code

        entry_point_features: list[str] | Unset = UNSET
        if not isinstance(self.entry_point_features, Unset):
            entry_point_features = self.entry_point_features



        entry_point_type = self.entry_point_type

        label = self.label

        meeting_code = self.meeting_code

        passcode = self.passcode

        password = self.password

        pin = self.pin

        region_code = self.region_code

        uri = self.uri


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if access_code is not UNSET:
            field_dict["accessCode"] = access_code
        if entry_point_features is not UNSET:
            field_dict["entryPointFeatures"] = entry_point_features
        if entry_point_type is not UNSET:
            field_dict["entryPointType"] = entry_point_type
        if label is not UNSET:
            field_dict["label"] = label
        if meeting_code is not UNSET:
            field_dict["meetingCode"] = meeting_code
        if passcode is not UNSET:
            field_dict["passcode"] = passcode
        if password is not UNSET:
            field_dict["password"] = password
        if pin is not UNSET:
            field_dict["pin"] = pin
        if region_code is not UNSET:
            field_dict["regionCode"] = region_code
        if uri is not UNSET:
            field_dict["uri"] = uri

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        access_code = d.pop("accessCode", UNSET)

        entry_point_features = cast(list[str], d.pop("entryPointFeatures", UNSET))


        entry_point_type = d.pop("entryPointType", UNSET)

        label = d.pop("label", UNSET)

        meeting_code = d.pop("meetingCode", UNSET)

        passcode = d.pop("passcode", UNSET)

        password = d.pop("password", UNSET)

        pin = d.pop("pin", UNSET)

        region_code = d.pop("regionCode", UNSET)

        uri = d.pop("uri", UNSET)

        entry_point = cls(
            access_code=access_code,
            entry_point_features=entry_point_features,
            entry_point_type=entry_point_type,
            label=label,
            meeting_code=meeting_code,
            passcode=passcode,
            password=password,
            pin=pin,
            region_code=region_code,
            uri=uri,
        )


        entry_point.additional_properties = d
        return entry_point

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
