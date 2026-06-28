from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.spreadsheet_properties_auto_recalc import SpreadsheetPropertiesAutoRecalc
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.cell_format import CellFormat
  from ..models.iterative_calculation_settings import IterativeCalculationSettings
  from ..models.spreadsheet_theme import SpreadsheetTheme





T = TypeVar("T", bound="SpreadsheetProperties")



@_attrs_define
class SpreadsheetProperties:
    """ Properties of a spreadsheet.

        Attributes:
            auto_recalc (SpreadsheetPropertiesAutoRecalc | Unset): The amount of time to wait before volatile functions are
                recalculated.
            default_format (CellFormat | Unset): The format of a cell.
            iterative_calculation_settings (IterativeCalculationSettings | Unset): Settings to control how circular
                dependencies are resolved with iterative calculation.
            locale (str | Unset): The locale of the spreadsheet in one of the following formats: * an ISO 639-1 language
                code such as `en` * an ISO 639-2 language code such as `fil`, if no 639-1 code exists * a combination of the ISO
                language code and country code, such as `en_US` Note: when updating this field, not all locales/languages are
                supported.
            spreadsheet_theme (SpreadsheetTheme | Unset): Represents spreadsheet theme
            time_zone (str | Unset): The time zone of the spreadsheet, in CLDR format such as `America/New_York`. If the
                time zone isn't recognized, this may be a custom time zone such as `GMT-07:00`.
            title (str | Unset): The title of the spreadsheet.
     """

    auto_recalc: SpreadsheetPropertiesAutoRecalc | Unset = UNSET
    default_format: CellFormat | Unset = UNSET
    iterative_calculation_settings: IterativeCalculationSettings | Unset = UNSET
    locale: str | Unset = UNSET
    spreadsheet_theme: SpreadsheetTheme | Unset = UNSET
    time_zone: str | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.cell_format import CellFormat
        from ..models.iterative_calculation_settings import IterativeCalculationSettings
        from ..models.spreadsheet_theme import SpreadsheetTheme
        auto_recalc: str | Unset = UNSET
        if not isinstance(self.auto_recalc, Unset):
            auto_recalc = self.auto_recalc.value


        default_format: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_format, Unset):
            default_format = self.default_format.to_dict()

        iterative_calculation_settings: dict[str, Any] | Unset = UNSET
        if not isinstance(self.iterative_calculation_settings, Unset):
            iterative_calculation_settings = self.iterative_calculation_settings.to_dict()

        locale = self.locale

        spreadsheet_theme: dict[str, Any] | Unset = UNSET
        if not isinstance(self.spreadsheet_theme, Unset):
            spreadsheet_theme = self.spreadsheet_theme.to_dict()

        time_zone = self.time_zone

        title = self.title


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if auto_recalc is not UNSET:
            field_dict["autoRecalc"] = auto_recalc
        if default_format is not UNSET:
            field_dict["defaultFormat"] = default_format
        if iterative_calculation_settings is not UNSET:
            field_dict["iterativeCalculationSettings"] = iterative_calculation_settings
        if locale is not UNSET:
            field_dict["locale"] = locale
        if spreadsheet_theme is not UNSET:
            field_dict["spreadsheetTheme"] = spreadsheet_theme
        if time_zone is not UNSET:
            field_dict["timeZone"] = time_zone
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cell_format import CellFormat
        from ..models.iterative_calculation_settings import IterativeCalculationSettings
        from ..models.spreadsheet_theme import SpreadsheetTheme
        d = dict(src_dict)
        _auto_recalc = d.pop("autoRecalc", UNSET)
        auto_recalc: SpreadsheetPropertiesAutoRecalc | Unset
        if isinstance(_auto_recalc,  Unset):
            auto_recalc = UNSET
        else:
            auto_recalc = SpreadsheetPropertiesAutoRecalc(_auto_recalc)




        _default_format = d.pop("defaultFormat", UNSET)
        default_format: CellFormat | Unset
        if isinstance(_default_format,  Unset):
            default_format = UNSET
        else:
            default_format = CellFormat.from_dict(_default_format)




        _iterative_calculation_settings = d.pop("iterativeCalculationSettings", UNSET)
        iterative_calculation_settings: IterativeCalculationSettings | Unset
        if isinstance(_iterative_calculation_settings,  Unset):
            iterative_calculation_settings = UNSET
        else:
            iterative_calculation_settings = IterativeCalculationSettings.from_dict(_iterative_calculation_settings)




        locale = d.pop("locale", UNSET)

        _spreadsheet_theme = d.pop("spreadsheetTheme", UNSET)
        spreadsheet_theme: SpreadsheetTheme | Unset
        if isinstance(_spreadsheet_theme,  Unset):
            spreadsheet_theme = UNSET
        else:
            spreadsheet_theme = SpreadsheetTheme.from_dict(_spreadsheet_theme)




        time_zone = d.pop("timeZone", UNSET)

        title = d.pop("title", UNSET)

        spreadsheet_properties = cls(
            auto_recalc=auto_recalc,
            default_format=default_format,
            iterative_calculation_settings=iterative_calculation_settings,
            locale=locale,
            spreadsheet_theme=spreadsheet_theme,
            time_zone=time_zone,
            title=title,
        )


        spreadsheet_properties.additional_properties = d
        return spreadsheet_properties

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
