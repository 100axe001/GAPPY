from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.migration_exchange_migration_exchange_success_schema_a_mapping_of_provided_user_i_ds_with_mapped_user_i_ds import MigrationExchangeMigrationExchangeSuccessSchemaAMappingOfProvidedUserIDsWithMappedUserIDs





T = TypeVar("T", bound="MigrationExchangeMigrationExchangeSuccessSchema")



@_attrs_define
class MigrationExchangeMigrationExchangeSuccessSchema:
    """ Schema for successful response from migration.exchange method

        Attributes:
            enterprise_id (str):
            ok (bool):
            team_id (str):
            invalid_user_ids (list[str] | Unset):
            user_id_map (MigrationExchangeMigrationExchangeSuccessSchemaAMappingOfProvidedUserIDsWithMappedUserIDs | Unset):
     """

    enterprise_id: str
    ok: bool
    team_id: str
    invalid_user_ids: list[str] | Unset = UNSET
    user_id_map: MigrationExchangeMigrationExchangeSuccessSchemaAMappingOfProvidedUserIDsWithMappedUserIDs | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.migration_exchange_migration_exchange_success_schema_a_mapping_of_provided_user_i_ds_with_mapped_user_i_ds import MigrationExchangeMigrationExchangeSuccessSchemaAMappingOfProvidedUserIDsWithMappedUserIDs
        enterprise_id = self.enterprise_id

        ok = self.ok

        team_id = self.team_id

        invalid_user_ids: list[str] | Unset = UNSET
        if not isinstance(self.invalid_user_ids, Unset):
            invalid_user_ids = self.invalid_user_ids



        user_id_map: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user_id_map, Unset):
            user_id_map = self.user_id_map.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "enterprise_id": enterprise_id,
            "ok": ok,
            "team_id": team_id,
        })
        if invalid_user_ids is not UNSET:
            field_dict["invalid_user_ids"] = invalid_user_ids
        if user_id_map is not UNSET:
            field_dict["user_id_map"] = user_id_map

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.migration_exchange_migration_exchange_success_schema_a_mapping_of_provided_user_i_ds_with_mapped_user_i_ds import MigrationExchangeMigrationExchangeSuccessSchemaAMappingOfProvidedUserIDsWithMappedUserIDs
        d = dict(src_dict)
        enterprise_id = d.pop("enterprise_id")

        ok = d.pop("ok")

        team_id = d.pop("team_id")

        invalid_user_ids = cast(list[str], d.pop("invalid_user_ids", UNSET))


        _user_id_map = d.pop("user_id_map", UNSET)
        user_id_map: MigrationExchangeMigrationExchangeSuccessSchemaAMappingOfProvidedUserIDsWithMappedUserIDs | Unset
        if isinstance(_user_id_map,  Unset):
            user_id_map = UNSET
        else:
            user_id_map = MigrationExchangeMigrationExchangeSuccessSchemaAMappingOfProvidedUserIDsWithMappedUserIDs.from_dict(_user_id_map)




        migration_exchange_migration_exchange_success_schema = cls(
            enterprise_id=enterprise_id,
            ok=ok,
            team_id=team_id,
            invalid_user_ids=invalid_user_ids,
            user_id_map=user_id_map,
        )


        migration_exchange_migration_exchange_success_schema.additional_properties = d
        return migration_exchange_migration_exchange_success_schema

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
