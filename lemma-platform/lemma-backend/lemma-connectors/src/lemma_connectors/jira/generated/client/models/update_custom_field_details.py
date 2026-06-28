from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.update_custom_field_details_searcher_key import UpdateCustomFieldDetailsSearcherKey
from ..types import UNSET, Unset






T = TypeVar("T", bound="UpdateCustomFieldDetails")



@_attrs_define
class UpdateCustomFieldDetails:
    """ Details of a custom field.

        Attributes:
            description (str | Unset): The description of the custom field. The maximum length is 40000 characters.
            name (str | Unset): The name of the custom field. It doesn't have to be unique. The maximum length is 255
                characters.
            searcher_key (UpdateCustomFieldDetailsSearcherKey | Unset): The searcher that defines the way the field is
                searched in Jira. It can be set to `null`, otherwise you must specify the valid searcher for the field type, as
                listed below (abbreviated values shown):

                 *  `cascadingselect`: `cascadingselectsearcher`
                 *  `datepicker`: `daterange`
                 *  `datetime`: `datetimerange`
                 *  `float`: `exactnumber` or `numberrange`
                 *  `grouppicker`: `grouppickersearcher`
                 *  `importid`: `exactnumber` or `numberrange`
                 *  `labels`: `labelsearcher`
                 *  `multicheckboxes`: `multiselectsearcher`
                 *  `multigrouppicker`: `multiselectsearcher`
                 *  `multiselect`: `multiselectsearcher`
                 *  `multiuserpicker`: `userpickergroupsearcher`
                 *  `multiversion`: `versionsearcher`
                 *  `project`: `projectsearcher`
                 *  `radiobuttons`: `multiselectsearcher`
                 *  `readonlyfield`: `textsearcher`
                 *  `select`: `multiselectsearcher`
                 *  `textarea`: `textsearcher`
                 *  `textfield`: `textsearcher`
                 *  `url`: `exacttextsearcher`
                 *  `userpicker`: `userpickergroupsearcher`
                 *  `version`: `versionsearcher`
     """

    description: str | Unset = UNSET
    name: str | Unset = UNSET
    searcher_key: UpdateCustomFieldDetailsSearcherKey | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        description = self.description

        name = self.name

        searcher_key: str | Unset = UNSET
        if not isinstance(self.searcher_key, Unset):
            searcher_key = self.searcher_key.value



        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name
        if searcher_key is not UNSET:
            field_dict["searcherKey"] = searcher_key

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        name = d.pop("name", UNSET)

        _searcher_key = d.pop("searcherKey", UNSET)
        searcher_key: UpdateCustomFieldDetailsSearcherKey | Unset
        if isinstance(_searcher_key,  Unset):
            searcher_key = UNSET
        else:
            searcher_key = UpdateCustomFieldDetailsSearcherKey(_searcher_key)




        update_custom_field_details = cls(
            description=description,
            name=name,
            searcher_key=searcher_key,
        )

        return update_custom_field_details

