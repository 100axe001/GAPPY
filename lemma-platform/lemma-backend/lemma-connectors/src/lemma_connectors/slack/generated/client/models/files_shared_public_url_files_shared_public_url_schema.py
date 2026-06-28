from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.file_object import FileObject





T = TypeVar("T", bound="FilesSharedPublicURLFilesSharedPublicURLSchema")



@_attrs_define
class FilesSharedPublicURLFilesSharedPublicURLSchema:
    """ Schema for successful response from files.sharedPublicURL method

        Attributes:
            file (FileObject):
            ok (bool):
     """

    file: FileObject
    ok: bool





    def to_dict(self) -> dict[str, Any]:
        from ..models.file_object import FileObject
        file = self.file.to_dict()

        ok = self.ok


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "file": file,
            "ok": ok,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_object import FileObject
        d = dict(src_dict)
        file = FileObject.from_dict(d.pop("file"))




        ok = d.pop("ok")

        files_shared_public_url_files_shared_public_url_schema = cls(
            file=file,
            ok=ok,
        )

        return files_shared_public_url_files_shared_public_url_schema

