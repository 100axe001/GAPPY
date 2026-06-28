from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.security_scheme import SecurityScheme





T = TypeVar("T", bound="SecuritySchemes")



@_attrs_define
class SecuritySchemes:
    """ List of security schemes.

        Attributes:
            issue_security_schemes (list[SecurityScheme] | Unset): List of security schemes.
     """

    issue_security_schemes: list[SecurityScheme] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.security_scheme import SecurityScheme
        issue_security_schemes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.issue_security_schemes, Unset):
            issue_security_schemes = []
            for issue_security_schemes_item_data in self.issue_security_schemes:
                issue_security_schemes_item = issue_security_schemes_item_data.to_dict()
                issue_security_schemes.append(issue_security_schemes_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if issue_security_schemes is not UNSET:
            field_dict["issueSecuritySchemes"] = issue_security_schemes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.security_scheme import SecurityScheme
        d = dict(src_dict)
        _issue_security_schemes = d.pop("issueSecuritySchemes", UNSET)
        issue_security_schemes: list[SecurityScheme] | Unset = UNSET
        if _issue_security_schemes is not UNSET:
            issue_security_schemes = []
            for issue_security_schemes_item_data in _issue_security_schemes:
                issue_security_schemes_item = SecurityScheme.from_dict(issue_security_schemes_item_data)



                issue_security_schemes.append(issue_security_schemes_item)


        security_schemes = cls(
            issue_security_schemes=issue_security_schemes,
        )

        return security_schemes

