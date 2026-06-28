from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="FilesUploadJsonBody")



@_attrs_define
class FilesUploadJsonBody:
    """ 
        Attributes:
            token (str | Unset): Authentication token. Requires scope: `files:write:user`
            file (str | Unset): File contents via `multipart/form-data`. If omitting this parameter, you must submit
                `content`.
            content (str | Unset): File contents via a POST variable. If omitting this parameter, you must provide a `file`.
            filetype (str | Unset): A [file type](/types/file#file_types) identifier.
            filename (str | Unset): Filename of file.
            title (str | Unset): Title of file.
            initial_comment (str | Unset): The message text introducing the file in specified `channels`.
            channels (str | Unset): Comma-separated list of channel names or IDs where the file will be shared.
            thread_ts (float | Unset): Provide another message's `ts` value to upload this file as a reply. Never use a
                reply's `ts` value; use its parent instead.
     """

    token: str | Unset = UNSET
    file: str | Unset = UNSET
    content: str | Unset = UNSET
    filetype: str | Unset = UNSET
    filename: str | Unset = UNSET
    title: str | Unset = UNSET
    initial_comment: str | Unset = UNSET
    channels: str | Unset = UNSET
    thread_ts: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        token = self.token

        file = self.file

        content = self.content

        filetype = self.filetype

        filename = self.filename

        title = self.title

        initial_comment = self.initial_comment

        channels = self.channels

        thread_ts = self.thread_ts


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if token is not UNSET:
            field_dict["token"] = token
        if file is not UNSET:
            field_dict["file"] = file
        if content is not UNSET:
            field_dict["content"] = content
        if filetype is not UNSET:
            field_dict["filetype"] = filetype
        if filename is not UNSET:
            field_dict["filename"] = filename
        if title is not UNSET:
            field_dict["title"] = title
        if initial_comment is not UNSET:
            field_dict["initial_comment"] = initial_comment
        if channels is not UNSET:
            field_dict["channels"] = channels
        if thread_ts is not UNSET:
            field_dict["thread_ts"] = thread_ts

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        token = d.pop("token", UNSET)

        file = d.pop("file", UNSET)

        content = d.pop("content", UNSET)

        filetype = d.pop("filetype", UNSET)

        filename = d.pop("filename", UNSET)

        title = d.pop("title", UNSET)

        initial_comment = d.pop("initial_comment", UNSET)

        channels = d.pop("channels", UNSET)

        thread_ts = d.pop("thread_ts", UNSET)

        files_upload_json_body = cls(
            token=token,
            file=file,
            content=content,
            filetype=filetype,
            filename=filename,
            title=title,
            initial_comment=initial_comment,
            channels=channels,
            thread_ts=thread_ts,
        )


        files_upload_json_body.additional_properties = d
        return files_upload_json_body

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
