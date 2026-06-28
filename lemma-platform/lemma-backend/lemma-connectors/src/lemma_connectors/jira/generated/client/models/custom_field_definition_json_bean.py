from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.custom_field_definition_json_bean_searcher_key import CustomFieldDefinitionJsonBeanSearcherKey
from ..types import UNSET, Unset






T = TypeVar("T", bound="CustomFieldDefinitionJsonBean")



@_attrs_define
class CustomFieldDefinitionJsonBean:
    """ 
        Attributes:
            name (str): The name of the custom field, which is displayed in Jira. This is not the unique identifier.
            type_ (str): The type of the custom field. These built-in custom field types are available:

                 *  `cascadingselect`: Enables values to be selected from two levels of select lists (value:
                `com.atlassian.jira.plugin.system.customfieldtypes:cascadingselect`)
                 *  `datepicker`: Stores a date using a picker control (value:
                `com.atlassian.jira.plugin.system.customfieldtypes:datepicker`)
                 *  `datetime`: Stores a date with a time component (value:
                `com.atlassian.jira.plugin.system.customfieldtypes:datetime`)
                 *  `float`: Stores and validates a numeric (floating point) input (value:
                `com.atlassian.jira.plugin.system.customfieldtypes:float`)
                 *  `grouppicker`: Stores a user group using a picker control (value:
                `com.atlassian.jira.plugin.system.customfieldtypes:grouppicker`)
                 *  `importid`: A read-only field that stores the ID the issue had in the system it was imported from (value:
                `com.atlassian.jira.plugin.system.customfieldtypes:importid`)
                 *  `labels`: Stores labels (value: `com.atlassian.jira.plugin.system.customfieldtypes:labels`)
                 *  `multicheckboxes`: Stores multiple values using checkboxes (value: ``)
                 *  `multigrouppicker`: Stores multiple user groups using a picker control (value: ``)
                 *  `multiselect`: Stores multiple values using a select list (value:
                `com.atlassian.jira.plugin.system.customfieldtypes:multicheckboxes`)
                 *  `multiuserpicker`: Stores multiple users using a picker control (value:
                `com.atlassian.jira.plugin.system.customfieldtypes:multigrouppicker`)
                 *  `multiversion`: Stores multiple versions from the versions available in a project using a picker control
                (value: `com.atlassian.jira.plugin.system.customfieldtypes:multiversion`)
                 *  `project`: Stores a project from a list of projects that the user is permitted to view (value:
                `com.atlassian.jira.plugin.system.customfieldtypes:project`)
                 *  `radiobuttons`: Stores a value using radio buttons (value:
                `com.atlassian.jira.plugin.system.customfieldtypes:radiobuttons`)
                 *  `readonlyfield`: Stores a read-only text value, which can only be populated via the API (value:
                `com.atlassian.jira.plugin.system.customfieldtypes:readonlyfield`)
                 *  `select`: Stores a value from a configurable list of options (value:
                `com.atlassian.jira.plugin.system.customfieldtypes:select`)
                 *  `textarea`: Stores a long text string using a multiline text area (value:
                `com.atlassian.jira.plugin.system.customfieldtypes:textarea`)
                 *  `textfield`: Stores a text string using a single-line text box (value:
                `com.atlassian.jira.plugin.system.customfieldtypes:textfield`)
                 *  `url`: Stores a URL (value: `com.atlassian.jira.plugin.system.customfieldtypes:url`)
                 *  `userpicker`: Stores a user using a picker control (value:
                `com.atlassian.jira.plugin.system.customfieldtypes:userpicker`)
                 *  `version`: Stores a version using a picker control (value:
                `com.atlassian.jira.plugin.system.customfieldtypes:version`)

                To create a field based on a [Forge custom field type](https://developer.atlassian.com/platform/forge/manifest-
                reference/modules/#jira-custom-field-type--beta-), use the ID of the Forge custom field type as the value. For
                example, `ari:cloud:ecosystem::extension/e62f20a2-4b61-4dbe-
                bfb9-9a88b5e3ac84/548c5df1-24aa-4f7c-bbbb-3038d947cb05/static/my-cf-type-key`.
            description (str | Unset): The description of the custom field, which is displayed in Jira.
            searcher_key (CustomFieldDefinitionJsonBeanSearcherKey | Unset): The searcher defines the way the field is
                searched in Jira. For example, *com.atlassian.jira.plugin.system.customfieldtypes:grouppickersearcher*.
                The search UI (basic search and JQL search) will display different operations and values for the field, based on
                the field searcher. You must specify a searcher that is valid for the field type, as listed below (abbreviated
                values shown):

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

                If no searcher is provided, the field isn't searchable. However, [Forge custom
                fields](https://developer.atlassian.com/platform/forge/manifest-reference/modules/#jira-custom-field-type--
                beta-) have a searcher set automatically, so are always searchable.
     """

    name: str
    type_: str
    description: str | Unset = UNSET
    searcher_key: CustomFieldDefinitionJsonBeanSearcherKey | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_

        description = self.description

        searcher_key: str | Unset = UNSET
        if not isinstance(self.searcher_key, Unset):
            searcher_key = self.searcher_key.value



        field_dict: dict[str, Any] = {}

        field_dict.update({
            "name": name,
            "type": type_,
        })
        if description is not UNSET:
            field_dict["description"] = description
        if searcher_key is not UNSET:
            field_dict["searcherKey"] = searcher_key

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        type_ = d.pop("type")

        description = d.pop("description", UNSET)

        _searcher_key = d.pop("searcherKey", UNSET)
        searcher_key: CustomFieldDefinitionJsonBeanSearcherKey | Unset
        if isinstance(_searcher_key,  Unset):
            searcher_key = UNSET
        else:
            searcher_key = CustomFieldDefinitionJsonBeanSearcherKey(_searcher_key)




        custom_field_definition_json_bean = cls(
            name=name,
            type_=type_,
            description=description,
            searcher_key=searcher_key,
        )

        return custom_field_definition_json_bean

