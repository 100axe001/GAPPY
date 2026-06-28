from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.revision import Revision





T = TypeVar("T", bound="RevisionList")



@_attrs_define
class RevisionList:
    """ A list of revisions of a file.

        Attributes:
            kind (str | Unset): Identifies what kind of resource this is. Value: the fixed string "drive#revisionList".
                Default: 'drive#revisionList'.
            next_page_token (str | Unset): The page token for the next page of revisions. This will be absent if the end of
                the revisions list has been reached. If the token is rejected for any reason, it should be discarded, and
                pagination should be restarted from the first page of results.
            revisions (list[Revision] | Unset): The list of revisions. If nextPageToken is populated, then this list may be
                incomplete and an additional page of results should be fetched.
     """

    kind: str | Unset = 'drive#revisionList'
    next_page_token: str | Unset = UNSET
    revisions: list[Revision] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.revision import Revision
        kind = self.kind

        next_page_token = self.next_page_token

        revisions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.revisions, Unset):
            revisions = []
            for revisions_item_data in self.revisions:
                revisions_item = revisions_item_data.to_dict()
                revisions.append(revisions_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if kind is not UNSET:
            field_dict["kind"] = kind
        if next_page_token is not UNSET:
            field_dict["nextPageToken"] = next_page_token
        if revisions is not UNSET:
            field_dict["revisions"] = revisions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.revision import Revision
        d = dict(src_dict)
        kind = d.pop("kind", UNSET)

        next_page_token = d.pop("nextPageToken", UNSET)

        _revisions = d.pop("revisions", UNSET)
        revisions: list[Revision] | Unset = UNSET
        if _revisions is not UNSET:
            revisions = []
            for revisions_item_data in _revisions:
                revisions_item = Revision.from_dict(revisions_item_data)



                revisions.append(revisions_item)


        revision_list = cls(
            kind=kind,
            next_page_token=next_page_token,
            revisions=revisions,
        )


        revision_list.additional_properties = d
        return revision_list

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
