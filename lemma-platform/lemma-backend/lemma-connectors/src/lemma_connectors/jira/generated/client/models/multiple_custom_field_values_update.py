from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="MultipleCustomFieldValuesUpdate")



@_attrs_define
class MultipleCustomFieldValuesUpdate:
    """ A custom field and its new value with a list of issue to update.

        Attributes:
            custom_field (str): The ID or key of the custom field. For example, `customfield_10010`.
            issue_ids (list[int]): The list of issue IDs.
            value (Any): The value for the custom field. The value must be compatible with the [custom field
                type](https://developer.atlassian.com/platform/forge/manifest-reference/modules/jira-custom-field/#data-types)
                as follows:

                 *  `string` the value must be a string.
                 *  `number` the value must be a number.
                 *  `datetime` the value must be a string that represents a date in the ISO format or the simplified extended
                ISO format. For example, `"2023-01-18T12:00:00-03:00"` or `"2023-01-18T12:00:00.000Z"`. However, the
                milliseconds part is ignored.
                 *  `user` the value must be an object that contains the `accountId` field.
                 *  `group` the value must be an object that contains the group `name` or `groupId` field. Because group names
                can change, we recommend using `groupId`.

                A list of appropriate values must be provided if the field is of the `list` [collection
                type](https://developer.atlassian.com/platform/forge/manifest-reference/modules/jira-custom-field/#collection-
                types).
     """

    custom_field: str
    issue_ids: list[int]
    value: Any





    def to_dict(self) -> dict[str, Any]:
        custom_field = self.custom_field

        issue_ids = self.issue_ids



        value = self.value


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "customField": custom_field,
            "issueIds": issue_ids,
            "value": value,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        custom_field = d.pop("customField")

        issue_ids = cast(list[int], d.pop("issueIds"))


        value = d.pop("value")

        multiple_custom_field_values_update = cls(
            custom_field=custom_field,
            issue_ids=issue_ids,
            value=value,
        )

        return multiple_custom_field_values_update

