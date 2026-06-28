from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.issue_transition_fields import IssueTransitionFields
  from ..models.status_details import StatusDetails





T = TypeVar("T", bound="IssueTransition")



@_attrs_define
class IssueTransition:
    """ Details of an issue transition.

        Attributes:
            expand (str | Unset): Expand options that include additional transition details in the response.
            fields (IssueTransitionFields | Unset): Details of the fields associated with the issue transition screen. Use
                this information to populate `fields` and `update` in a transition request.
            has_screen (bool | Unset): Whether there is a screen associated with the issue transition.
            id (str | Unset): The ID of the issue transition. Required when specifying a transition to undertake.
            is_available (bool | Unset): Whether the transition is available to be performed.
            is_conditional (bool | Unset): Whether the issue has to meet criteria before the issue transition is applied.
            is_global (bool | Unset): Whether the issue transition is global, that is, the transition is applied to issues
                regardless of their status.
            is_initial (bool | Unset): Whether this is the initial issue transition for the workflow.
            looped (bool | Unset):
            name (str | Unset): The name of the issue transition.
            to (StatusDetails | Unset): A status.
     """

    expand: str | Unset = UNSET
    fields: IssueTransitionFields | Unset = UNSET
    has_screen: bool | Unset = UNSET
    id: str | Unset = UNSET
    is_available: bool | Unset = UNSET
    is_conditional: bool | Unset = UNSET
    is_global: bool | Unset = UNSET
    is_initial: bool | Unset = UNSET
    looped: bool | Unset = UNSET
    name: str | Unset = UNSET
    to: StatusDetails | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.issue_transition_fields import IssueTransitionFields
        from ..models.status_details import StatusDetails
        expand = self.expand

        fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.fields, Unset):
            fields = self.fields.to_dict()

        has_screen = self.has_screen

        id = self.id

        is_available = self.is_available

        is_conditional = self.is_conditional

        is_global = self.is_global

        is_initial = self.is_initial

        looped = self.looped

        name = self.name

        to: dict[str, Any] | Unset = UNSET
        if not isinstance(self.to, Unset):
            to = self.to.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if expand is not UNSET:
            field_dict["expand"] = expand
        if fields is not UNSET:
            field_dict["fields"] = fields
        if has_screen is not UNSET:
            field_dict["hasScreen"] = has_screen
        if id is not UNSET:
            field_dict["id"] = id
        if is_available is not UNSET:
            field_dict["isAvailable"] = is_available
        if is_conditional is not UNSET:
            field_dict["isConditional"] = is_conditional
        if is_global is not UNSET:
            field_dict["isGlobal"] = is_global
        if is_initial is not UNSET:
            field_dict["isInitial"] = is_initial
        if looped is not UNSET:
            field_dict["looped"] = looped
        if name is not UNSET:
            field_dict["name"] = name
        if to is not UNSET:
            field_dict["to"] = to

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.issue_transition_fields import IssueTransitionFields
        from ..models.status_details import StatusDetails
        d = dict(src_dict)
        expand = d.pop("expand", UNSET)

        _fields = d.pop("fields", UNSET)
        fields: IssueTransitionFields | Unset
        if isinstance(_fields,  Unset):
            fields = UNSET
        else:
            fields = IssueTransitionFields.from_dict(_fields)




        has_screen = d.pop("hasScreen", UNSET)

        id = d.pop("id", UNSET)

        is_available = d.pop("isAvailable", UNSET)

        is_conditional = d.pop("isConditional", UNSET)

        is_global = d.pop("isGlobal", UNSET)

        is_initial = d.pop("isInitial", UNSET)

        looped = d.pop("looped", UNSET)

        name = d.pop("name", UNSET)

        _to = d.pop("to", UNSET)
        to: StatusDetails | Unset
        if isinstance(_to,  Unset):
            to = UNSET
        else:
            to = StatusDetails.from_dict(_to)




        issue_transition = cls(
            expand=expand,
            fields=fields,
            has_screen=has_screen,
            id=id,
            is_available=is_available,
            is_conditional=is_conditional,
            is_global=is_global,
            is_initial=is_initial,
            looped=looped,
            name=name,
            to=to,
        )


        issue_transition.additional_properties = d
        return issue_transition

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
