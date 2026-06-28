from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="RuleConfiguration")



@_attrs_define
class RuleConfiguration:
    """ A rule configuration.

        Attributes:
            value (str): Configuration of the rule, as it is stored by the Connect app on the rule configuration page.
            disabled (bool | Unset): EXPERIMENTAL: Whether the rule is disabled. Default: False.
            tag (str | Unset): EXPERIMENTAL: A tag used to filter rules in [Get workflow transition rule
                configurations](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-workflow-transition-
                rules/#api-rest-api-3-workflow-rule-config-get).
     """

    value: str
    disabled: bool | Unset = False
    tag: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        value = self.value

        disabled = self.disabled

        tag = self.tag


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "value": value,
        })
        if disabled is not UNSET:
            field_dict["disabled"] = disabled
        if tag is not UNSET:
            field_dict["tag"] = tag

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        value = d.pop("value")

        disabled = d.pop("disabled", UNSET)

        tag = d.pop("tag", UNSET)

        rule_configuration = cls(
            value=value,
            disabled=disabled,
            tag=tag,
        )

        return rule_configuration

