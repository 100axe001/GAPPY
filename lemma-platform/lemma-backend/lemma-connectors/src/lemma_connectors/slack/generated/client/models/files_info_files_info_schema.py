from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.file_object import FileObject
  from ..models.paging_object import PagingObject





T = TypeVar("T", bound="FilesInfoFilesInfoSchema")



@_attrs_define
class FilesInfoFilesInfoSchema:
    """ Schema for successful response from files.info method

        Attributes:
            comments (list[Any]):
            file (FileObject):
            ok (bool):
            content_html (Any | Unset):
            editor (str | Unset):
            paging (PagingObject | Unset):
            response_metadata (Any | Unset):
     """

    comments: list[Any]
    file: FileObject
    ok: bool
    content_html: Any | Unset = UNSET
    editor: str | Unset = UNSET
    paging: PagingObject | Unset = UNSET
    response_metadata: Any | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.file_object import FileObject
        from ..models.paging_object import PagingObject
        comments = self.comments



        file = self.file.to_dict()

        ok = self.ok

        content_html = self.content_html

        editor = self.editor

        paging: dict[str, Any] | Unset = UNSET
        if not isinstance(self.paging, Unset):
            paging = self.paging.to_dict()

        response_metadata = self.response_metadata


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "comments": comments,
            "file": file,
            "ok": ok,
        })
        if content_html is not UNSET:
            field_dict["content_html"] = content_html
        if editor is not UNSET:
            field_dict["editor"] = editor
        if paging is not UNSET:
            field_dict["paging"] = paging
        if response_metadata is not UNSET:
            field_dict["response_metadata"] = response_metadata

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_object import FileObject
        from ..models.paging_object import PagingObject
        d = dict(src_dict)
        comments = cast(list[Any], d.pop("comments"))


        file = FileObject.from_dict(d.pop("file"))




        ok = d.pop("ok")

        content_html = d.pop("content_html", UNSET)

        editor = d.pop("editor", UNSET)

        _paging = d.pop("paging", UNSET)
        paging: PagingObject | Unset
        if isinstance(_paging,  Unset):
            paging = UNSET
        else:
            paging = PagingObject.from_dict(_paging)




        response_metadata = d.pop("response_metadata", UNSET)

        files_info_files_info_schema = cls(
            comments=comments,
            file=file,
            ok=ok,
            content_html=content_html,
            editor=editor,
            paging=paging,
            response_metadata=response_metadata,
        )

        return files_info_files_info_schema

