from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.file_object import FileObject
  from ..models.paging_object import PagingObject





T = TypeVar("T", bound="FilesListFilesListSchema")



@_attrs_define
class FilesListFilesListSchema:
    """ Schema for successful response from files.list method

        Attributes:
            files (list[FileObject]):
            ok (bool):
            paging (PagingObject):
     """

    files: list[FileObject]
    ok: bool
    paging: PagingObject





    def to_dict(self) -> dict[str, Any]:
        from ..models.file_object import FileObject
        from ..models.paging_object import PagingObject
        files = []
        for files_item_data in self.files:
            files_item = files_item_data.to_dict()
            files.append(files_item)



        ok = self.ok

        paging = self.paging.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "files": files,
            "ok": ok,
            "paging": paging,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_object import FileObject
        from ..models.paging_object import PagingObject
        d = dict(src_dict)
        files = []
        _files = d.pop("files")
        for files_item_data in (_files):
            files_item = FileObject.from_dict(files_item_data)



            files.append(files_item)


        ok = d.pop("ok")

        paging = PagingObject.from_dict(d.pop("paging"))




        files_list_files_list_schema = cls(
            files=files,
            ok=ok,
            paging=paging,
        )

        return files_list_files_list_schema

