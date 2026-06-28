from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="WriteControl")



@_attrs_define
class WriteControl:
    """ Provides control over how write requests are executed.

        Attributes:
            required_revision_id (str | Unset): The optional revision ID of the document the write request is applied to. If
                this is not the latest revision of the document, the request is not processed and returns a 400 bad request
                error. When a required revision ID is returned in a response, it indicates the revision ID of the document after
                the request was applied.
            target_revision_id (str | Unset): The optional target revision ID of the document the write request is applied
                to. If collaborator changes have occurred after the document was read using the API, the changes produced by
                this write request are applied against the collaborator changes. This results in a new revision of the document
                that incorporates both the collaborator changes and the changes in the request, with the Docs server resolving
                conflicting changes. When using target revision ID, the API client can be thought of as another collaborator of
                the document. The target revision ID can only be used to write to recent versions of a document. If the target
                revision is too far behind the latest revision, the request is not processed and returns a 400 bad request
                error. The request should be tried again after retrieving the latest version of the document. Usually a revision
                ID remains valid for use as a target revision for several minutes after it's read, but for frequently edited
                documents this window might be shorter.
     """

    required_revision_id: str | Unset = UNSET
    target_revision_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        required_revision_id = self.required_revision_id

        target_revision_id = self.target_revision_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if required_revision_id is not UNSET:
            field_dict["requiredRevisionId"] = required_revision_id
        if target_revision_id is not UNSET:
            field_dict["targetRevisionId"] = target_revision_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        required_revision_id = d.pop("requiredRevisionId", UNSET)

        target_revision_id = d.pop("targetRevisionId", UNSET)

        write_control = cls(
            required_revision_id=required_revision_id,
            target_revision_id=target_revision_id,
        )


        write_control.additional_properties = d
        return write_control

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
