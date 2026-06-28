from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.file import File





T = TypeVar("T", bound="FileList")



@_attrs_define
class FileList:
    """ A list of files.

        Attributes:
            files (list[File] | Unset): The list of files. If nextPageToken is populated, then this list may be incomplete
                and an additional page of results should be fetched.
            incomplete_search (bool | Unset): Whether the search process was incomplete. If true, then some search results
                may be missing, since all documents were not searched. This may occur when searching multiple drives with the
                "allDrives" corpora, but all corpora could not be searched. When this happens, it is suggested that clients
                narrow their query by choosing a different corpus such as "user" or "drive".
            kind (str | Unset): Identifies what kind of resource this is. Value: the fixed string "drive#fileList". Default:
                'drive#fileList'.
            next_page_token (str | Unset): The page token for the next page of files. This will be absent if the end of the
                files list has been reached. If the token is rejected for any reason, it should be discarded, and pagination
                should be restarted from the first page of results.
     """

    files: list[File] | Unset = UNSET
    incomplete_search: bool | Unset = UNSET
    kind: str | Unset = 'drive#fileList'
    next_page_token: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.file import File
        files: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_dict()
                files.append(files_item)



        incomplete_search = self.incomplete_search

        kind = self.kind

        next_page_token = self.next_page_token


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if files is not UNSET:
            field_dict["files"] = files
        if incomplete_search is not UNSET:
            field_dict["incompleteSearch"] = incomplete_search
        if kind is not UNSET:
            field_dict["kind"] = kind
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file import File
        d = dict(src_dict)
        _files = d.pop("files", UNSET)
        files: list[File] | Unset = UNSET
        if _files is not UNSET:
            files = []
            for files_item_data in _files:
                files_item = File.from_dict(files_item_data)



                files.append(files_item)


        incomplete_search = d.pop("incompleteSearch", UNSET)

        kind = d.pop("kind", UNSET)

        next_page_token = d.pop("nextPageToken", UNSET)

        file_list = cls(
            files=files,
            incomplete_search=incomplete_search,
            kind=kind,
            next_page_token=next_page_token,
        )


        file_list.additional_properties = d
        return file_list

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
