from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="IssueLinkType")



@_attrs_define
class IssueLinkType:
    """ This object is used as follows:

     *  In the [ issueLink](#api-rest-api-3-issueLink-post) resource it defines and reports on the type of link between
    the issues. Find a list of issue link types with [Get issue link types](#api-rest-api-3-issueLinkType-get).
     *  In the [ issueLinkType](#api-rest-api-3-issueLinkType-post) resource it defines and reports on issue link types.

        Attributes:
            id (str | Unset): The ID of the issue link type and is used as follows:

                 *  In the [ issueLink](#api-rest-api-3-issueLink-post) resource it is the type of issue link. Required on
                create when `name` isn't provided. Otherwise, read only.
                 *  In the [ issueLinkType](#api-rest-api-3-issueLinkType-post) resource it is read only.
            inward (str | Unset): The description of the issue link type inward link and is used as follows:

                 *  In the [ issueLink](#api-rest-api-3-issueLink-post) resource it is read only.
                 *  In the [ issueLinkType](#api-rest-api-3-issueLinkType-post) resource it is required on create and optional
                on update. Otherwise, read only.
            name (str | Unset): The name of the issue link type and is used as follows:

                 *  In the [ issueLink](#api-rest-api-3-issueLink-post) resource it is the type of issue link. Required on
                create when `id` isn't provided. Otherwise, read only.
                 *  In the [ issueLinkType](#api-rest-api-3-issueLinkType-post) resource it is required on create and optional
                on update. Otherwise, read only.
            outward (str | Unset): The description of the issue link type outward link and is used as follows:

                 *  In the [ issueLink](#api-rest-api-3-issueLink-post) resource it is read only.
                 *  In the [ issueLinkType](#api-rest-api-3-issueLinkType-post) resource it is required on create and optional
                on update. Otherwise, read only.
            self_ (str | Unset): The URL of the issue link type. Read only.
     """

    id: str | Unset = UNSET
    inward: str | Unset = UNSET
    name: str | Unset = UNSET
    outward: str | Unset = UNSET
    self_: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        inward = self.inward

        name = self.name

        outward = self.outward

        self_ = self.self_


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if inward is not UNSET:
            field_dict["inward"] = inward
        if name is not UNSET:
            field_dict["name"] = name
        if outward is not UNSET:
            field_dict["outward"] = outward
        if self_ is not UNSET:
            field_dict["self"] = self_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        inward = d.pop("inward", UNSET)

        name = d.pop("name", UNSET)

        outward = d.pop("outward", UNSET)

        self_ = d.pop("self", UNSET)

        issue_link_type = cls(
            id=id,
            inward=inward,
            name=name,
            outward=outward,
            self_=self_,
        )

        return issue_link_type

