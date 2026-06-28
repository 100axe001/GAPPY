from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.background_suggestion_state import BackgroundSuggestionState
  from ..models.size_suggestion_state import SizeSuggestionState





T = TypeVar("T", bound="DocumentStyleSuggestionState")



@_attrs_define
class DocumentStyleSuggestionState:
    """ A mask that indicates which of the fields on the base DocumentStyle have been changed in this suggestion. For any
    field set to true, there's a new suggested value.

        Attributes:
            background_suggestion_state (BackgroundSuggestionState | Unset): A mask that indicates which of the fields on
                the base Background have been changed in this suggestion. For any field set to true, the Backgound has a new
                suggested value.
            default_footer_id_suggested (bool | Unset): Indicates if there was a suggested change to default_footer_id.
            default_header_id_suggested (bool | Unset): Indicates if there was a suggested change to default_header_id.
            even_page_footer_id_suggested (bool | Unset): Indicates if there was a suggested change to even_page_footer_id.
            even_page_header_id_suggested (bool | Unset): Indicates if there was a suggested change to even_page_header_id.
            first_page_footer_id_suggested (bool | Unset): Indicates if there was a suggested change to
                first_page_footer_id.
            first_page_header_id_suggested (bool | Unset): Indicates if there was a suggested change to
                first_page_header_id.
            margin_bottom_suggested (bool | Unset): Indicates if there was a suggested change to margin_bottom.
            margin_footer_suggested (bool | Unset): Indicates if there was a suggested change to margin_footer.
            margin_header_suggested (bool | Unset): Indicates if there was a suggested change to margin_header.
            margin_left_suggested (bool | Unset): Indicates if there was a suggested change to margin_left.
            margin_right_suggested (bool | Unset): Indicates if there was a suggested change to margin_right.
            margin_top_suggested (bool | Unset): Indicates if there was a suggested change to margin_top.
            page_number_start_suggested (bool | Unset): Indicates if there was a suggested change to page_number_start.
            page_size_suggestion_state (SizeSuggestionState | Unset): A mask that indicates which of the fields on the base
                Size have been changed in this suggestion. For any field set to true, the Size has a new suggested value.
            use_custom_header_footer_margins_suggested (bool | Unset): Indicates if there was a suggested change to
                use_custom_header_footer_margins.
            use_even_page_header_footer_suggested (bool | Unset): Indicates if there was a suggested change to
                use_even_page_header_footer.
            use_first_page_header_footer_suggested (bool | Unset): Indicates if there was a suggested change to
                use_first_page_header_footer.
     """

    background_suggestion_state: BackgroundSuggestionState | Unset = UNSET
    default_footer_id_suggested: bool | Unset = UNSET
    default_header_id_suggested: bool | Unset = UNSET
    even_page_footer_id_suggested: bool | Unset = UNSET
    even_page_header_id_suggested: bool | Unset = UNSET
    first_page_footer_id_suggested: bool | Unset = UNSET
    first_page_header_id_suggested: bool | Unset = UNSET
    margin_bottom_suggested: bool | Unset = UNSET
    margin_footer_suggested: bool | Unset = UNSET
    margin_header_suggested: bool | Unset = UNSET
    margin_left_suggested: bool | Unset = UNSET
    margin_right_suggested: bool | Unset = UNSET
    margin_top_suggested: bool | Unset = UNSET
    page_number_start_suggested: bool | Unset = UNSET
    page_size_suggestion_state: SizeSuggestionState | Unset = UNSET
    use_custom_header_footer_margins_suggested: bool | Unset = UNSET
    use_even_page_header_footer_suggested: bool | Unset = UNSET
    use_first_page_header_footer_suggested: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.background_suggestion_state import BackgroundSuggestionState
        from ..models.size_suggestion_state import SizeSuggestionState
        background_suggestion_state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.background_suggestion_state, Unset):
            background_suggestion_state = self.background_suggestion_state.to_dict()

        default_footer_id_suggested = self.default_footer_id_suggested

        default_header_id_suggested = self.default_header_id_suggested

        even_page_footer_id_suggested = self.even_page_footer_id_suggested

        even_page_header_id_suggested = self.even_page_header_id_suggested

        first_page_footer_id_suggested = self.first_page_footer_id_suggested

        first_page_header_id_suggested = self.first_page_header_id_suggested

        margin_bottom_suggested = self.margin_bottom_suggested

        margin_footer_suggested = self.margin_footer_suggested

        margin_header_suggested = self.margin_header_suggested

        margin_left_suggested = self.margin_left_suggested

        margin_right_suggested = self.margin_right_suggested

        margin_top_suggested = self.margin_top_suggested

        page_number_start_suggested = self.page_number_start_suggested

        page_size_suggestion_state: dict[str, Any] | Unset = UNSET
        if not isinstance(self.page_size_suggestion_state, Unset):
            page_size_suggestion_state = self.page_size_suggestion_state.to_dict()

        use_custom_header_footer_margins_suggested = self.use_custom_header_footer_margins_suggested

        use_even_page_header_footer_suggested = self.use_even_page_header_footer_suggested

        use_first_page_header_footer_suggested = self.use_first_page_header_footer_suggested


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if background_suggestion_state is not UNSET:
            field_dict["backgroundSuggestionState"] = background_suggestion_state
        if default_footer_id_suggested is not UNSET:
            field_dict["defaultFooterIdSuggested"] = default_footer_id_suggested
        if default_header_id_suggested is not UNSET:
            field_dict["defaultHeaderIdSuggested"] = default_header_id_suggested
        if even_page_footer_id_suggested is not UNSET:
            field_dict["evenPageFooterIdSuggested"] = even_page_footer_id_suggested
        if even_page_header_id_suggested is not UNSET:
            field_dict["evenPageHeaderIdSuggested"] = even_page_header_id_suggested
        if first_page_footer_id_suggested is not UNSET:
            field_dict["firstPageFooterIdSuggested"] = first_page_footer_id_suggested
        if first_page_header_id_suggested is not UNSET:
            field_dict["firstPageHeaderIdSuggested"] = first_page_header_id_suggested
        if margin_bottom_suggested is not UNSET:
            field_dict["marginBottomSuggested"] = margin_bottom_suggested
        if margin_footer_suggested is not UNSET:
            field_dict["marginFooterSuggested"] = margin_footer_suggested
        if margin_header_suggested is not UNSET:
            field_dict["marginHeaderSuggested"] = margin_header_suggested
        if margin_left_suggested is not UNSET:
            field_dict["marginLeftSuggested"] = margin_left_suggested
        if margin_right_suggested is not UNSET:
            field_dict["marginRightSuggested"] = margin_right_suggested
        if margin_top_suggested is not UNSET:
            field_dict["marginTopSuggested"] = margin_top_suggested
        if page_number_start_suggested is not UNSET:
            field_dict["pageNumberStartSuggested"] = page_number_start_suggested
        if page_size_suggestion_state is not UNSET:
            field_dict["pageSizeSuggestionState"] = page_size_suggestion_state
        if use_custom_header_footer_margins_suggested is not UNSET:
            field_dict["useCustomHeaderFooterMarginsSuggested"] = use_custom_header_footer_margins_suggested
        if use_even_page_header_footer_suggested is not UNSET:
            field_dict["useEvenPageHeaderFooterSuggested"] = use_even_page_header_footer_suggested
        if use_first_page_header_footer_suggested is not UNSET:
            field_dict["useFirstPageHeaderFooterSuggested"] = use_first_page_header_footer_suggested

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.background_suggestion_state import BackgroundSuggestionState
        from ..models.size_suggestion_state import SizeSuggestionState
        d = dict(src_dict)
        _background_suggestion_state = d.pop("backgroundSuggestionState", UNSET)
        background_suggestion_state: BackgroundSuggestionState | Unset
        if isinstance(_background_suggestion_state,  Unset):
            background_suggestion_state = UNSET
        else:
            background_suggestion_state = BackgroundSuggestionState.from_dict(_background_suggestion_state)




        default_footer_id_suggested = d.pop("defaultFooterIdSuggested", UNSET)

        default_header_id_suggested = d.pop("defaultHeaderIdSuggested", UNSET)

        even_page_footer_id_suggested = d.pop("evenPageFooterIdSuggested", UNSET)

        even_page_header_id_suggested = d.pop("evenPageHeaderIdSuggested", UNSET)

        first_page_footer_id_suggested = d.pop("firstPageFooterIdSuggested", UNSET)

        first_page_header_id_suggested = d.pop("firstPageHeaderIdSuggested", UNSET)

        margin_bottom_suggested = d.pop("marginBottomSuggested", UNSET)

        margin_footer_suggested = d.pop("marginFooterSuggested", UNSET)

        margin_header_suggested = d.pop("marginHeaderSuggested", UNSET)

        margin_left_suggested = d.pop("marginLeftSuggested", UNSET)

        margin_right_suggested = d.pop("marginRightSuggested", UNSET)

        margin_top_suggested = d.pop("marginTopSuggested", UNSET)

        page_number_start_suggested = d.pop("pageNumberStartSuggested", UNSET)

        _page_size_suggestion_state = d.pop("pageSizeSuggestionState", UNSET)
        page_size_suggestion_state: SizeSuggestionState | Unset
        if isinstance(_page_size_suggestion_state,  Unset):
            page_size_suggestion_state = UNSET
        else:
            page_size_suggestion_state = SizeSuggestionState.from_dict(_page_size_suggestion_state)




        use_custom_header_footer_margins_suggested = d.pop("useCustomHeaderFooterMarginsSuggested", UNSET)

        use_even_page_header_footer_suggested = d.pop("useEvenPageHeaderFooterSuggested", UNSET)

        use_first_page_header_footer_suggested = d.pop("useFirstPageHeaderFooterSuggested", UNSET)

        document_style_suggestion_state = cls(
            background_suggestion_state=background_suggestion_state,
            default_footer_id_suggested=default_footer_id_suggested,
            default_header_id_suggested=default_header_id_suggested,
            even_page_footer_id_suggested=even_page_footer_id_suggested,
            even_page_header_id_suggested=even_page_header_id_suggested,
            first_page_footer_id_suggested=first_page_footer_id_suggested,
            first_page_header_id_suggested=first_page_header_id_suggested,
            margin_bottom_suggested=margin_bottom_suggested,
            margin_footer_suggested=margin_footer_suggested,
            margin_header_suggested=margin_header_suggested,
            margin_left_suggested=margin_left_suggested,
            margin_right_suggested=margin_right_suggested,
            margin_top_suggested=margin_top_suggested,
            page_number_start_suggested=page_number_start_suggested,
            page_size_suggestion_state=page_size_suggestion_state,
            use_custom_header_footer_margins_suggested=use_custom_header_footer_margins_suggested,
            use_even_page_header_footer_suggested=use_even_page_header_footer_suggested,
            use_first_page_header_footer_suggested=use_first_page_header_footer_suggested,
        )


        document_style_suggestion_state.additional_properties = d
        return document_style_suggestion_state

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
