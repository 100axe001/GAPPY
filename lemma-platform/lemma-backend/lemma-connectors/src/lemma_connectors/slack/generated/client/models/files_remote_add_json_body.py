from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="FilesRemoteAddJsonBody")



@_attrs_define
class FilesRemoteAddJsonBody:
    """ 
        Attributes:
            token (str | Unset): Authentication token. Requires scope: `remote_files:write`
            external_id (str | Unset): Creator defined GUID for the file.
            title (str | Unset): Title of the file being shared.
            filetype (str | Unset): type of file
            external_url (str | Unset): URL of the remote file.
            preview_image (str | Unset): Preview of the document via `multipart/form-data`.
            indexable_file_contents (str | Unset): A text file (txt, pdf, doc, etc.) containing textual search terms that
                are used to improve discovery of the remote file.
     """

    token: str | Unset = UNSET
    external_id: str | Unset = UNSET
    title: str | Unset = UNSET
    filetype: str | Unset = UNSET
    external_url: str | Unset = UNSET
    preview_image: str | Unset = UNSET
    indexable_file_contents: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        token = self.token

        external_id = self.external_id

        title = self.title

        filetype = self.filetype

        external_url = self.external_url

        preview_image = self.preview_image

        indexable_file_contents = self.indexable_file_contents


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if token is not UNSET:
            field_dict["token"] = token
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if title is not UNSET:
            field_dict["title"] = title
        if filetype is not UNSET:
            field_dict["filetype"] = filetype
        if external_url is not UNSET:
            field_dict["external_url"] = external_url
        if preview_image is not UNSET:
            field_dict["preview_image"] = preview_image
        if indexable_file_contents is not UNSET:
            field_dict["indexable_file_contents"] = indexable_file_contents

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        token = d.pop("token", UNSET)

        external_id = d.pop("external_id", UNSET)

        title = d.pop("title", UNSET)

        filetype = d.pop("filetype", UNSET)

        external_url = d.pop("external_url", UNSET)

        preview_image = d.pop("preview_image", UNSET)

        indexable_file_contents = d.pop("indexable_file_contents", UNSET)

        files_remote_add_json_body = cls(
            token=token,
            external_id=external_id,
            title=title,
            filetype=filetype,
            external_url=external_url,
            preview_image=preview_image,
            indexable_file_contents=indexable_file_contents,
        )


        files_remote_add_json_body.additional_properties = d
        return files_remote_add_json_body

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
