from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.scope import Scope
  from ..models.screenable_tab import ScreenableTab





T = TypeVar("T", bound="ScreenWithTab")



@_attrs_define
class ScreenWithTab:
    """ A screen with tab details.

        Attributes:
            description (str | Unset): The description of the screen.
            id (int | Unset): The ID of the screen.
            name (str | Unset): The name of the screen.
            scope (Scope | Unset): The projects the item is associated with. Indicated for items associated with [next-gen
                projects](https://confluence.atlassian.com/x/loMyO).
            tab (ScreenableTab | Unset): A screen tab.
     """

    description: str | Unset = UNSET
    id: int | Unset = UNSET
    name: str | Unset = UNSET
    scope: Scope | Unset = UNSET
    tab: ScreenableTab | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.scope import Scope
        from ..models.screenable_tab import ScreenableTab
        description = self.description

        id = self.id

        name = self.name

        scope: dict[str, Any] | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope.to_dict()

        tab: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tab, Unset):
            tab = self.tab.to_dict()


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if scope is not UNSET:
            field_dict["scope"] = scope
        if tab is not UNSET:
            field_dict["tab"] = tab

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.scope import Scope
        from ..models.screenable_tab import ScreenableTab
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        _scope = d.pop("scope", UNSET)
        scope: Scope | Unset
        if isinstance(_scope,  Unset):
            scope = UNSET
        else:
            scope = Scope.from_dict(_scope)




        _tab = d.pop("tab", UNSET)
        tab: ScreenableTab | Unset
        if isinstance(_tab,  Unset):
            tab = UNSET
        else:
            tab = ScreenableTab.from_dict(_tab)




        screen_with_tab = cls(
            description=description,
            id=id,
            name=name,
            scope=scope,
            tab=tab,
        )

        return screen_with_tab

