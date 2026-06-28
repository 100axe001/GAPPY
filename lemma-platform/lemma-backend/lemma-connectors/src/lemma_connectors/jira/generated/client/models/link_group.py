from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.simple_link import SimpleLink





T = TypeVar("T", bound="LinkGroup")



@_attrs_define
class LinkGroup:
    """ Details a link group, which defines issue operations.

        Attributes:
            groups (list[LinkGroup] | Unset):
            header (SimpleLink | Unset): Details about the operations available in this version.
            id (str | Unset):
            links (list[SimpleLink] | Unset):
            style_class (str | Unset):
            weight (int | Unset):
     """

    groups: list[LinkGroup] | Unset = UNSET
    header: SimpleLink | Unset = UNSET
    id: str | Unset = UNSET
    links: list[SimpleLink] | Unset = UNSET
    style_class: str | Unset = UNSET
    weight: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.simple_link import SimpleLink
        groups: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.groups, Unset):
            groups = []
            for groups_item_data in self.groups:
                groups_item = groups_item_data.to_dict()
                groups.append(groups_item)



        header: dict[str, Any] | Unset = UNSET
        if not isinstance(self.header, Unset):
            header = self.header.to_dict()

        id = self.id

        links: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.links, Unset):
            links = []
            for links_item_data in self.links:
                links_item = links_item_data.to_dict()
                links.append(links_item)



        style_class = self.style_class

        weight = self.weight


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if groups is not UNSET:
            field_dict["groups"] = groups
        if header is not UNSET:
            field_dict["header"] = header
        if id is not UNSET:
            field_dict["id"] = id
        if links is not UNSET:
            field_dict["links"] = links
        if style_class is not UNSET:
            field_dict["styleClass"] = style_class
        if weight is not UNSET:
            field_dict["weight"] = weight

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.simple_link import SimpleLink
        d = dict(src_dict)
        _groups = d.pop("groups", UNSET)
        groups: list[LinkGroup] | Unset = UNSET
        if _groups is not UNSET:
            groups = []
            for groups_item_data in _groups:
                groups_item = LinkGroup.from_dict(groups_item_data)



                groups.append(groups_item)


        _header = d.pop("header", UNSET)
        header: SimpleLink | Unset
        if isinstance(_header,  Unset):
            header = UNSET
        else:
            header = SimpleLink.from_dict(_header)




        id = d.pop("id", UNSET)

        _links = d.pop("links", UNSET)
        links: list[SimpleLink] | Unset = UNSET
        if _links is not UNSET:
            links = []
            for links_item_data in _links:
                links_item = SimpleLink.from_dict(links_item_data)



                links.append(links_item)


        style_class = d.pop("styleClass", UNSET)

        weight = d.pop("weight", UNSET)

        link_group = cls(
            groups=groups,
            header=header,
            id=id,
            links=links,
            style_class=style_class,
            weight=weight,
        )

        return link_group

