from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.user import User





T = TypeVar("T", bound="LabelField")



@_attrs_define
class LabelField:
    """ Representation of a label field.

        Attributes:
            date_string (list[datetime.date] | Unset): Only present if valueType is dateString. RFC 3339 formatted date:
                YYYY-MM-DD.
            id (str | Unset): The identifier of this field.
            integer (list[str] | Unset): Only present if valueType is integer.
            kind (str | Unset): This is always drive#labelField. Default: 'drive#labelField'.
            selection (list[str] | Unset): Only present if valueType is selection.
            text (list[str] | Unset): Only present if valueType is text.
            user (list[User] | Unset): Only present if valueType is user.
            value_type (str | Unset): The field type. While new values may be supported in the future, the following are
                currently allowed:
                - dateString
                - integer
                - selection
                - text
                - user
     """

    date_string: list[datetime.date] | Unset = UNSET
    id: str | Unset = UNSET
    integer: list[str] | Unset = UNSET
    kind: str | Unset = 'drive#labelField'
    selection: list[str] | Unset = UNSET
    text: list[str] | Unset = UNSET
    user: list[User] | Unset = UNSET
    value_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.user import User
        date_string: list[str] | Unset = UNSET
        if not isinstance(self.date_string, Unset):
            date_string = []
            for date_string_item_data in self.date_string:
                date_string_item = date_string_item_data.isoformat()
                date_string.append(date_string_item)



        id = self.id

        integer: list[str] | Unset = UNSET
        if not isinstance(self.integer, Unset):
            integer = self.integer



        kind = self.kind

        selection: list[str] | Unset = UNSET
        if not isinstance(self.selection, Unset):
            selection = self.selection



        text: list[str] | Unset = UNSET
        if not isinstance(self.text, Unset):
            text = self.text



        user: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.user, Unset):
            user = []
            for user_item_data in self.user:
                user_item = user_item_data.to_dict()
                user.append(user_item)



        value_type = self.value_type


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if date_string is not UNSET:
            field_dict["dateString"] = date_string
        if id is not UNSET:
            field_dict["id"] = id
        if integer is not UNSET:
            field_dict["integer"] = integer
        if kind is not UNSET:
            field_dict["kind"] = kind
        if selection is not UNSET:
            field_dict["selection"] = selection
        if text is not UNSET:
            field_dict["text"] = text
        if user is not UNSET:
            field_dict["user"] = user
        if value_type is not UNSET:
            field_dict["valueType"] = value_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user import User
        d = dict(src_dict)
        _date_string = d.pop("dateString", UNSET)
        date_string: list[datetime.date] | Unset = UNSET
        if _date_string is not UNSET:
            date_string = []
            for date_string_item_data in _date_string:
                date_string_item = isoparse(date_string_item_data).date()



                date_string.append(date_string_item)


        id = d.pop("id", UNSET)

        integer = cast(list[str], d.pop("integer", UNSET))


        kind = d.pop("kind", UNSET)

        selection = cast(list[str], d.pop("selection", UNSET))


        text = cast(list[str], d.pop("text", UNSET))


        _user = d.pop("user", UNSET)
        user: list[User] | Unset = UNSET
        if _user is not UNSET:
            user = []
            for user_item_data in _user:
                user_item = User.from_dict(user_item_data)



                user.append(user_item)


        value_type = d.pop("valueType", UNSET)

        label_field = cls(
            date_string=date_string,
            id=id,
            integer=integer,
            kind=kind,
            selection=selection,
            text=text,
            user=user,
            value_type=value_type,
        )


        label_field.additional_properties = d
        return label_field

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
