from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.users_set_photo_users_set_photo_error_schema_error import UsersSetPhotoUsersSetPhotoErrorSchemaError
from ..types import UNSET, Unset






T = TypeVar("T", bound="UsersSetPhotoUsersSetPhotoErrorSchema")



@_attrs_define
class UsersSetPhotoUsersSetPhotoErrorSchema:
    """ Schema for error response from users.setPhoto method

        Attributes:
            error (UsersSetPhotoUsersSetPhotoErrorSchemaError):
            ok (bool):
            callstack (str | Unset): Note: PHP callstack is only visible in dev/qa
            debug_step (str | Unset): possibly DEV/QA only
            dims (str | Unset): possibly DEV/QA only
            time_ident (int | Unset): possibly DEV/QA only
     """

    error: UsersSetPhotoUsersSetPhotoErrorSchemaError
    ok: bool
    callstack: str | Unset = UNSET
    debug_step: str | Unset = UNSET
    dims: str | Unset = UNSET
    time_ident: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        error = self.error.value

        ok = self.ok

        callstack = self.callstack

        debug_step = self.debug_step

        dims = self.dims

        time_ident = self.time_ident


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "error": error,
            "ok": ok,
        })
        if callstack is not UNSET:
            field_dict["callstack"] = callstack
        if debug_step is not UNSET:
            field_dict["debug_step"] = debug_step
        if dims is not UNSET:
            field_dict["dims"] = dims
        if time_ident is not UNSET:
            field_dict["time_ident"] = time_ident

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        error = UsersSetPhotoUsersSetPhotoErrorSchemaError(d.pop("error"))




        ok = d.pop("ok")

        callstack = d.pop("callstack", UNSET)

        debug_step = d.pop("debug_step", UNSET)

        dims = d.pop("dims", UNSET)

        time_ident = d.pop("time_ident", UNSET)

        users_set_photo_users_set_photo_error_schema = cls(
            error=error,
            ok=ok,
            callstack=callstack,
            debug_step=debug_step,
            dims=dims,
            time_ident=time_ident,
        )

        return users_set_photo_users_set_photo_error_schema

