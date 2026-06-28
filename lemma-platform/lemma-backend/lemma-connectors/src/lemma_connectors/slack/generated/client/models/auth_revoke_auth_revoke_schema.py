from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="AuthRevokeAuthRevokeSchema")



@_attrs_define
class AuthRevokeAuthRevokeSchema:
    """ Schema for successful response from auth.revoke method

        Attributes:
            ok (bool):
            revoked (bool):
     """

    ok: bool
    revoked: bool





    def to_dict(self) -> dict[str, Any]:
        ok = self.ok

        revoked = self.revoked


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "ok": ok,
            "revoked": revoked,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ok = d.pop("ok")

        revoked = d.pop("revoked")

        auth_revoke_auth_revoke_schema = cls(
            ok=ok,
            revoked=revoked,
        )

        return auth_revoke_auth_revoke_schema

