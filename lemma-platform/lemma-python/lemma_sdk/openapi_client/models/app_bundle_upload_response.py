from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.app_detail_response import AppDetailResponse


T = TypeVar("T", bound="AppBundleUploadResponse")


@_attrs_define
class AppBundleUploadResponse:
    """
    Attributes:
        app (AppDetailResponse):
        message (str):
    """

    app: AppDetailResponse
    message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        app = self.app.to_dict()

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "app": app,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.app_detail_response import AppDetailResponse

        d = dict(src_dict)
        app = AppDetailResponse.from_dict(d.pop("app"))

        message = d.pop("message")

        app_bundle_upload_response = cls(
            app=app,
            message=message,
        )

        app_bundle_upload_response.additional_properties = d
        return app_bundle_upload_response

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
