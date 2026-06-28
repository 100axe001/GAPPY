from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

T = TypeVar("T", bound="BodyAppBundleUpload")


@_attrs_define
class BodyAppBundleUpload:
    """
    Attributes:
        dist_archive (None | str | Unset):
        source_archive (None | str | Unset):
    """

    dist_archive: None | str | Unset = UNSET
    source_archive: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        dist_archive: None | str | Unset
        if isinstance(self.dist_archive, Unset):
            dist_archive = UNSET
        else:
            dist_archive = self.dist_archive

        source_archive: None | str | Unset
        if isinstance(self.source_archive, Unset):
            source_archive = UNSET
        else:
            source_archive = self.source_archive

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dist_archive is not UNSET:
            field_dict["dist_archive"] = dist_archive
        if source_archive is not UNSET:
            field_dict["source_archive"] = source_archive

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        if not isinstance(self.dist_archive, Unset):
            if isinstance(self.dist_archive, str):
                files.append(
                    (
                        "dist_archive",
                        (None, str(self.dist_archive).encode(), "text/plain"),
                    )
                )
            else:
                files.append(
                    (
                        "dist_archive",
                        (None, str(self.dist_archive).encode(), "text/plain"),
                    )
                )

        if not isinstance(self.source_archive, Unset):
            if isinstance(self.source_archive, str):
                files.append(
                    (
                        "source_archive",
                        (None, str(self.source_archive).encode(), "text/plain"),
                    )
                )
            else:
                files.append(
                    (
                        "source_archive",
                        (None, str(self.source_archive).encode(), "text/plain"),
                    )
                )

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_dist_archive(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        dist_archive = _parse_dist_archive(d.pop("dist_archive", UNSET))

        def _parse_source_archive(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        source_archive = _parse_source_archive(d.pop("source_archive", UNSET))

        body_app_bundle_upload = cls(
            dist_archive=dist_archive,
            source_archive=source_archive,
        )

        body_app_bundle_upload.additional_properties = d
        return body_app_bundle_upload

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
