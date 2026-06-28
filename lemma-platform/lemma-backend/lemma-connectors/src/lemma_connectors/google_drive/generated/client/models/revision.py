from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.revision_export_links import RevisionExportLinks
  from ..models.user import User





T = TypeVar("T", bound="Revision")



@_attrs_define
class Revision:
    """ The metadata for a revision to a file.

        Attributes:
            export_links (RevisionExportLinks | Unset): Links for exporting Docs Editors files to specific formats.
            id (str | Unset): The ID of the revision.
            keep_forever (bool | Unset): Whether to keep this revision forever, even if it is no longer the head revision.
                If not set, the revision will be automatically purged 30 days after newer content is uploaded. This can be set
                on a maximum of 200 revisions for a file.
                This field is only applicable to files with binary content in Drive.
            kind (str | Unset): Identifies what kind of resource this is. Value: the fixed string "drive#revision". Default:
                'drive#revision'.
            last_modifying_user (User | Unset): Information about a Drive user.
            md_5_checksum (str | Unset): The MD5 checksum of the revision's content. This is only applicable to files with
                binary content in Drive.
            mime_type (str | Unset): The MIME type of the revision.
            modified_time (datetime.datetime | Unset): The last time the revision was modified (RFC 3339 date-time).
            original_filename (str | Unset): The original filename used to create this revision. This is only applicable to
                files with binary content in Drive.
            publish_auto (bool | Unset): Whether subsequent revisions will be automatically republished. This is only
                applicable to Docs Editors files.
            published (bool | Unset): Whether this revision is published. This is only applicable to Docs Editors files.
            published_link (str | Unset): A link to the published revision. This is only populated for Google Sites files.
            published_outside_domain (bool | Unset): Whether this revision is published outside the domain. This is only
                applicable to Docs Editors files.
            size (str | Unset): The size of the revision's content in bytes. This is only applicable to files with binary
                content in Drive.
     """

    export_links: RevisionExportLinks | Unset = UNSET
    id: str | Unset = UNSET
    keep_forever: bool | Unset = UNSET
    kind: str | Unset = 'drive#revision'
    last_modifying_user: User | Unset = UNSET
    md_5_checksum: str | Unset = UNSET
    mime_type: str | Unset = UNSET
    modified_time: datetime.datetime | Unset = UNSET
    original_filename: str | Unset = UNSET
    publish_auto: bool | Unset = UNSET
    published: bool | Unset = UNSET
    published_link: str | Unset = UNSET
    published_outside_domain: bool | Unset = UNSET
    size: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.revision_export_links import RevisionExportLinks
        from ..models.user import User
        export_links: dict[str, Any] | Unset = UNSET
        if not isinstance(self.export_links, Unset):
            export_links = self.export_links.to_dict()

        id = self.id

        keep_forever = self.keep_forever

        kind = self.kind

        last_modifying_user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.last_modifying_user, Unset):
            last_modifying_user = self.last_modifying_user.to_dict()

        md_5_checksum = self.md_5_checksum

        mime_type = self.mime_type

        modified_time: str | Unset = UNSET
        if not isinstance(self.modified_time, Unset):
            modified_time = self.modified_time.isoformat()

        original_filename = self.original_filename

        publish_auto = self.publish_auto

        published = self.published

        published_link = self.published_link

        published_outside_domain = self.published_outside_domain

        size = self.size


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if export_links is not UNSET:
            field_dict["exportLinks"] = export_links
        if id is not UNSET:
            field_dict["id"] = id
        if keep_forever is not UNSET:
            field_dict["keepForever"] = keep_forever
        if kind is not UNSET:
            field_dict["kind"] = kind
        if last_modifying_user is not UNSET:
            field_dict["lastModifyingUser"] = last_modifying_user
        if md_5_checksum is not UNSET:
            field_dict["md5Checksum"] = md_5_checksum
        if mime_type is not UNSET:
            field_dict["mimeType"] = mime_type
        if modified_time is not UNSET:
            field_dict["modifiedTime"] = modified_time
        if original_filename is not UNSET:
            field_dict["originalFilename"] = original_filename
        if publish_auto is not UNSET:
            field_dict["publishAuto"] = publish_auto
        if published is not UNSET:
            field_dict["published"] = published
        if published_link is not UNSET:
            field_dict["publishedLink"] = published_link
        if published_outside_domain is not UNSET:
            field_dict["publishedOutsideDomain"] = published_outside_domain
        if size is not UNSET:
            field_dict["size"] = size

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.revision_export_links import RevisionExportLinks
        from ..models.user import User
        d = dict(src_dict)
        _export_links = d.pop("exportLinks", UNSET)
        export_links: RevisionExportLinks | Unset
        if isinstance(_export_links,  Unset):
            export_links = UNSET
        else:
            export_links = RevisionExportLinks.from_dict(_export_links)




        id = d.pop("id", UNSET)

        keep_forever = d.pop("keepForever", UNSET)

        kind = d.pop("kind", UNSET)

        _last_modifying_user = d.pop("lastModifyingUser", UNSET)
        last_modifying_user: User | Unset
        if isinstance(_last_modifying_user,  Unset):
            last_modifying_user = UNSET
        else:
            last_modifying_user = User.from_dict(_last_modifying_user)




        md_5_checksum = d.pop("md5Checksum", UNSET)

        mime_type = d.pop("mimeType", UNSET)

        _modified_time = d.pop("modifiedTime", UNSET)
        modified_time: datetime.datetime | Unset
        if isinstance(_modified_time,  Unset):
            modified_time = UNSET
        else:
            modified_time = isoparse(_modified_time)




        original_filename = d.pop("originalFilename", UNSET)

        publish_auto = d.pop("publishAuto", UNSET)

        published = d.pop("published", UNSET)

        published_link = d.pop("publishedLink", UNSET)

        published_outside_domain = d.pop("publishedOutsideDomain", UNSET)

        size = d.pop("size", UNSET)

        revision = cls(
            export_links=export_links,
            id=id,
            keep_forever=keep_forever,
            kind=kind,
            last_modifying_user=last_modifying_user,
            md_5_checksum=md_5_checksum,
            mime_type=mime_type,
            modified_time=modified_time,
            original_filename=original_filename,
            publish_auto=publish_auto,
            published=published,
            published_link=published_link,
            published_outside_domain=published_outside_domain,
            size=size,
        )


        revision.additional_properties = d
        return revision

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
