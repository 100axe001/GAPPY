from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.surface_setup_mode import SurfaceSetupMode
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.surface_setup_field import SurfaceSetupField
    from ..models.surface_setup_step import SurfaceSetupStep


T = TypeVar("T", bound="SurfaceConnectorSetupGuide")


@_attrs_define
class SurfaceConnectorSetupGuide:
    """
    Attributes:
        mode (SurfaceSetupMode):
        summary (str):
        title (str):
        docs_path (None | str | Unset):
        fields (list[SurfaceSetupField] | Unset):
        notes (list[str] | Unset):
        steps (list[SurfaceSetupStep] | Unset):
        supported (bool | Unset):  Default: True.
    """

    mode: SurfaceSetupMode
    summary: str
    title: str
    docs_path: None | str | Unset = UNSET
    fields: list[SurfaceSetupField] | Unset = UNSET
    notes: list[str] | Unset = UNSET
    steps: list[SurfaceSetupStep] | Unset = UNSET
    supported: bool | Unset = True
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mode = self.mode.value

        summary = self.summary

        title = self.title

        docs_path: None | str | Unset
        if isinstance(self.docs_path, Unset):
            docs_path = UNSET
        else:
            docs_path = self.docs_path

        fields: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for fields_item_data in self.fields:
                fields_item = fields_item_data.to_dict()
                fields.append(fields_item)

        notes: list[str] | Unset = UNSET
        if not isinstance(self.notes, Unset):
            notes = self.notes

        steps: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.steps, Unset):
            steps = []
            for steps_item_data in self.steps:
                steps_item = steps_item_data.to_dict()
                steps.append(steps_item)

        supported = self.supported

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mode": mode,
                "summary": summary,
                "title": title,
            }
        )
        if docs_path is not UNSET:
            field_dict["docs_path"] = docs_path
        if fields is not UNSET:
            field_dict["fields"] = fields
        if notes is not UNSET:
            field_dict["notes"] = notes
        if steps is not UNSET:
            field_dict["steps"] = steps
        if supported is not UNSET:
            field_dict["supported"] = supported

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.surface_setup_field import SurfaceSetupField
        from ..models.surface_setup_step import SurfaceSetupStep

        d = dict(src_dict)
        mode = SurfaceSetupMode(d.pop("mode"))

        summary = d.pop("summary")

        title = d.pop("title")

        def _parse_docs_path(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        docs_path = _parse_docs_path(d.pop("docs_path", UNSET))

        _fields = d.pop("fields", UNSET)
        fields: list[SurfaceSetupField] | Unset = UNSET
        if _fields is not UNSET:
            fields = []
            for fields_item_data in _fields:
                fields_item = SurfaceSetupField.from_dict(fields_item_data)

                fields.append(fields_item)

        notes = cast(list[str], d.pop("notes", UNSET))

        _steps = d.pop("steps", UNSET)
        steps: list[SurfaceSetupStep] | Unset = UNSET
        if _steps is not UNSET:
            steps = []
            for steps_item_data in _steps:
                steps_item = SurfaceSetupStep.from_dict(steps_item_data)

                steps.append(steps_item)

        supported = d.pop("supported", UNSET)

        surface_connector_setup_guide = cls(
            mode=mode,
            summary=summary,
            title=title,
            docs_path=docs_path,
            fields=fields,
            notes=notes,
            steps=steps,
            supported=supported,
        )

        surface_connector_setup_guide.additional_properties = d
        return surface_connector_setup_guide

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
