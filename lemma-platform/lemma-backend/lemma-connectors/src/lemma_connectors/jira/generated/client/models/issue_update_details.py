from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.entity_property import EntityProperty
  from ..models.history_metadata import HistoryMetadata
  from ..models.issue_transition import IssueTransition
  from ..models.issue_update_details_fields import IssueUpdateDetailsFields
  from ..models.issue_update_details_update import IssueUpdateDetailsUpdate





T = TypeVar("T", bound="IssueUpdateDetails")



@_attrs_define
class IssueUpdateDetails:
    """ Details of an issue update request.

        Attributes:
            fields (IssueUpdateDetailsFields | Unset): List of issue screen fields to update, specifying the sub-field to
                update and its value for each field. This field provides a straightforward option when setting a sub-field. When
                multiple sub-fields or other operations are required, use `update`. Fields included in here cannot be included
                in `update`.
            history_metadata (HistoryMetadata | Unset): Details of issue history metadata.
            properties (list[EntityProperty] | Unset): Details of issue properties to be add or update.
            transition (IssueTransition | Unset): Details of an issue transition.
            update (IssueUpdateDetailsUpdate | Unset): A Map containing the field field name and a list of operations to
                perform on the issue screen field. Note that fields included in here cannot be included in `fields`.
     """

    fields: IssueUpdateDetailsFields | Unset = UNSET
    history_metadata: HistoryMetadata | Unset = UNSET
    properties: list[EntityProperty] | Unset = UNSET
    transition: IssueTransition | Unset = UNSET
    update: IssueUpdateDetailsUpdate | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.entity_property import EntityProperty
        from ..models.history_metadata import HistoryMetadata
        from ..models.issue_transition import IssueTransition
        from ..models.issue_update_details_fields import IssueUpdateDetailsFields
        from ..models.issue_update_details_update import IssueUpdateDetailsUpdate
        fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fields, Unset):
            fields = self.fields.to_dict()

        history_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.history_metadata, Unset):
            history_metadata = self.history_metadata.to_dict()

        properties: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.properties, Unset):
            properties = []
            for properties_item_data in self.properties:
                properties_item = properties_item_data.to_dict()
                properties.append(properties_item)



        transition: dict[str, Any] | Unset = UNSET
        if not isinstance(self.transition, Unset):
            transition = self.transition.to_dict()

        update: dict[str, Any] | Unset = UNSET
        if not isinstance(self.update, Unset):
            update = self.update.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if fields is not UNSET:
            field_dict["fields"] = fields
        if history_metadata is not UNSET:
            field_dict["historyMetadata"] = history_metadata
        if properties is not UNSET:
            field_dict["properties"] = properties
        if transition is not UNSET:
            field_dict["transition"] = transition
        if update is not UNSET:
            field_dict["update"] = update

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.entity_property import EntityProperty
        from ..models.history_metadata import HistoryMetadata
        from ..models.issue_transition import IssueTransition
        from ..models.issue_update_details_fields import IssueUpdateDetailsFields
        from ..models.issue_update_details_update import IssueUpdateDetailsUpdate
        d = dict(src_dict)
        _fields = d.pop("fields", UNSET)
        fields: IssueUpdateDetailsFields | Unset
        if isinstance(_fields,  Unset):
            fields = UNSET
        else:
            fields = IssueUpdateDetailsFields.from_dict(_fields)




        _history_metadata = d.pop("historyMetadata", UNSET)
        history_metadata: HistoryMetadata | Unset
        if isinstance(_history_metadata,  Unset):
            history_metadata = UNSET
        else:
            history_metadata = HistoryMetadata.from_dict(_history_metadata)




        _properties = d.pop("properties", UNSET)
        properties: list[EntityProperty] | Unset = UNSET
        if _properties is not UNSET:
            properties = []
            for properties_item_data in _properties:
                properties_item = EntityProperty.from_dict(properties_item_data)



                properties.append(properties_item)


        _transition = d.pop("transition", UNSET)
        transition: IssueTransition | Unset
        if isinstance(_transition,  Unset):
            transition = UNSET
        else:
            transition = IssueTransition.from_dict(_transition)




        _update = d.pop("update", UNSET)
        update: IssueUpdateDetailsUpdate | Unset
        if isinstance(_update,  Unset):
            update = UNSET
        else:
            update = IssueUpdateDetailsUpdate.from_dict(_update)




        issue_update_details = cls(
            fields=fields,
            history_metadata=history_metadata,
            properties=properties,
            transition=transition,
            update=update,
        )


        issue_update_details.additional_properties = d
        return issue_update_details

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
