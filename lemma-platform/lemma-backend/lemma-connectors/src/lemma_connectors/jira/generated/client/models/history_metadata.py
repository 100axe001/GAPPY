from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.history_metadata_extra_data import HistoryMetadataExtraData
  from ..models.history_metadata_participant import HistoryMetadataParticipant





T = TypeVar("T", bound="HistoryMetadata")



@_attrs_define
class HistoryMetadata:
    """ Details of issue history metadata.

        Attributes:
            activity_description (str | Unset): The activity described in the history record.
            activity_description_key (str | Unset): The key of the activity described in the history record.
            actor (HistoryMetadataParticipant | Unset): Details of user or system associated with a issue history metadata
                item.
            cause (HistoryMetadataParticipant | Unset): Details of user or system associated with a issue history metadata
                item.
            description (str | Unset): The description of the history record.
            description_key (str | Unset): The description key of the history record.
            email_description (str | Unset): The description of the email address associated the history record.
            email_description_key (str | Unset): The description key of the email address associated the history record.
            extra_data (HistoryMetadataExtraData | Unset): Additional arbitrary information about the history record.
            generator (HistoryMetadataParticipant | Unset): Details of user or system associated with a issue history
                metadata item.
            type_ (str | Unset): The type of the history record.
     """

    activity_description: str | Unset = UNSET
    activity_description_key: str | Unset = UNSET
    actor: HistoryMetadataParticipant | Unset = UNSET
    cause: HistoryMetadataParticipant | Unset = UNSET
    description: str | Unset = UNSET
    description_key: str | Unset = UNSET
    email_description: str | Unset = UNSET
    email_description_key: str | Unset = UNSET
    extra_data: HistoryMetadataExtraData | Unset = UNSET
    generator: HistoryMetadataParticipant | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.history_metadata_extra_data import HistoryMetadataExtraData
        from ..models.history_metadata_participant import HistoryMetadataParticipant
        activity_description = self.activity_description

        activity_description_key = self.activity_description_key

        actor: dict[str, Any] | Unset = UNSET
        if not isinstance(self.actor, Unset):
            actor = self.actor.to_dict()

        cause: dict[str, Any] | Unset = UNSET
        if not isinstance(self.cause, Unset):
            cause = self.cause.to_dict()

        description = self.description

        description_key = self.description_key

        email_description = self.email_description

        email_description_key = self.email_description_key

        extra_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extra_data, Unset):
            extra_data = self.extra_data.to_dict()

        generator: dict[str, Any] | Unset = UNSET
        if not isinstance(self.generator, Unset):
            generator = self.generator.to_dict()

        type_ = self.type_


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if activity_description is not UNSET:
            field_dict["activityDescription"] = activity_description
        if activity_description_key is not UNSET:
            field_dict["activityDescriptionKey"] = activity_description_key
        if actor is not UNSET:
            field_dict["actor"] = actor
        if cause is not UNSET:
            field_dict["cause"] = cause
        if description is not UNSET:
            field_dict["description"] = description
        if description_key is not UNSET:
            field_dict["descriptionKey"] = description_key
        if email_description is not UNSET:
            field_dict["emailDescription"] = email_description
        if email_description_key is not UNSET:
            field_dict["emailDescriptionKey"] = email_description_key
        if extra_data is not UNSET:
            field_dict["extraData"] = extra_data
        if generator is not UNSET:
            field_dict["generator"] = generator
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.history_metadata_extra_data import HistoryMetadataExtraData
        from ..models.history_metadata_participant import HistoryMetadataParticipant
        d = dict(src_dict)
        activity_description = d.pop("activityDescription", UNSET)

        activity_description_key = d.pop("activityDescriptionKey", UNSET)

        _actor = d.pop("actor", UNSET)
        actor: HistoryMetadataParticipant | Unset
        if isinstance(_actor,  Unset):
            actor = UNSET
        else:
            actor = HistoryMetadataParticipant.from_dict(_actor)




        _cause = d.pop("cause", UNSET)
        cause: HistoryMetadataParticipant | Unset
        if isinstance(_cause,  Unset):
            cause = UNSET
        else:
            cause = HistoryMetadataParticipant.from_dict(_cause)




        description = d.pop("description", UNSET)

        description_key = d.pop("descriptionKey", UNSET)

        email_description = d.pop("emailDescription", UNSET)

        email_description_key = d.pop("emailDescriptionKey", UNSET)

        _extra_data = d.pop("extraData", UNSET)
        extra_data: HistoryMetadataExtraData | Unset
        if isinstance(_extra_data,  Unset):
            extra_data = UNSET
        else:
            extra_data = HistoryMetadataExtraData.from_dict(_extra_data)




        _generator = d.pop("generator", UNSET)
        generator: HistoryMetadataParticipant | Unset
        if isinstance(_generator,  Unset):
            generator = UNSET
        else:
            generator = HistoryMetadataParticipant.from_dict(_generator)




        type_ = d.pop("type", UNSET)

        history_metadata = cls(
            activity_description=activity_description,
            activity_description_key=activity_description_key,
            actor=actor,
            cause=cause,
            description=description,
            description_key=description_key,
            email_description=email_description,
            email_description_key=email_description_key,
            extra_data=extra_data,
            generator=generator,
            type_=type_,
        )


        history_metadata.additional_properties = d
        return history_metadata

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
