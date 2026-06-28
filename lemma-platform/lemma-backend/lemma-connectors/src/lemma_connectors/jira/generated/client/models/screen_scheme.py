from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.page_bean_issue_type_screen_scheme import PageBeanIssueTypeScreenScheme
  from ..models.screen_types import ScreenTypes





T = TypeVar("T", bound="ScreenScheme")



@_attrs_define
class ScreenScheme:
    """ A screen scheme.

        Attributes:
            description (str | Unset): The description of the screen scheme.
            id (int | Unset): The ID of the screen scheme.
            issue_type_screen_schemes (PageBeanIssueTypeScreenScheme | Unset): A page of items.
            name (str | Unset): The name of the screen scheme.
            screens (ScreenTypes | Unset): The IDs of the screens for the screen types of the screen scheme.
     """

    description: str | Unset = UNSET
    id: int | Unset = UNSET
    issue_type_screen_schemes: PageBeanIssueTypeScreenScheme | Unset = UNSET
    name: str | Unset = UNSET
    screens: ScreenTypes | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.page_bean_issue_type_screen_scheme import PageBeanIssueTypeScreenScheme
        from ..models.screen_types import ScreenTypes
        description = self.description

        id = self.id

        issue_type_screen_schemes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.issue_type_screen_schemes, Unset):
            issue_type_screen_schemes = self.issue_type_screen_schemes.to_dict()

        name = self.name

        screens: dict[str, Any] | Unset = UNSET
        if not isinstance(self.screens, Unset):
            screens = self.screens.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if issue_type_screen_schemes is not UNSET:
            field_dict["issueTypeScreenSchemes"] = issue_type_screen_schemes
        if name is not UNSET:
            field_dict["name"] = name
        if screens is not UNSET:
            field_dict["screens"] = screens

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.page_bean_issue_type_screen_scheme import PageBeanIssueTypeScreenScheme
        from ..models.screen_types import ScreenTypes
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        _issue_type_screen_schemes = d.pop("issueTypeScreenSchemes", UNSET)
        issue_type_screen_schemes: PageBeanIssueTypeScreenScheme | Unset
        if isinstance(_issue_type_screen_schemes,  Unset):
            issue_type_screen_schemes = UNSET
        else:
            issue_type_screen_schemes = PageBeanIssueTypeScreenScheme.from_dict(_issue_type_screen_schemes)




        name = d.pop("name", UNSET)

        _screens = d.pop("screens", UNSET)
        screens: ScreenTypes | Unset
        if isinstance(_screens,  Unset):
            screens = UNSET
        else:
            screens = ScreenTypes.from_dict(_screens)




        screen_scheme = cls(
            description=description,
            id=id,
            issue_type_screen_schemes=issue_type_screen_schemes,
            name=name,
            screens=screens,
        )

        return screen_scheme

