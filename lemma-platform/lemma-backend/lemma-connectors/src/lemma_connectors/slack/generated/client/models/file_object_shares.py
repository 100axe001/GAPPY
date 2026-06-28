from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="FileObjectShares")



@_attrs_define
class FileObjectShares:
    """ 
        Attributes:
            private (Any | Unset):
            public (Any | Unset):
     """

    private: Any | Unset = UNSET
    public: Any | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        private = self.private

        public = self.public


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if private is not UNSET:
            field_dict["private"] = private
        if public is not UNSET:
            field_dict["public"] = public

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        private = d.pop("private", UNSET)

        public = d.pop("public", UNSET)

        file_object_shares = cls(
            private=private,
            public=public,
        )

        return file_object_shares

