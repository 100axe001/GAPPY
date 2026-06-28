from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.user import User





T = TypeVar("T", bound="Votes")



@_attrs_define
class Votes:
    """ The details of votes on an issue.

        Attributes:
            has_voted (bool | Unset): Whether the user making this request has voted on the issue.
            self_ (str | Unset): The URL of these issue vote details.
            voters (list[User] | Unset): List of the users who have voted on this issue. An empty list is returned when the
                calling user doesn't have the *View voters and watchers* project permission.
            votes (int | Unset): The number of votes on the issue.
     """

    has_voted: bool | Unset = UNSET
    self_: str | Unset = UNSET
    voters: list[User] | Unset = UNSET
    votes: int | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.user import User
        has_voted = self.has_voted

        self_ = self.self_

        voters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.voters, Unset):
            voters = []
            for voters_item_data in self.voters:
                voters_item = voters_item_data.to_dict()
                voters.append(voters_item)



        votes = self.votes


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if has_voted is not UNSET:
            field_dict["hasVoted"] = has_voted
        if self_ is not UNSET:
            field_dict["self"] = self_
        if voters is not UNSET:
            field_dict["voters"] = voters
        if votes is not UNSET:
            field_dict["votes"] = votes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user import User
        d = dict(src_dict)
        has_voted = d.pop("hasVoted", UNSET)

        self_ = d.pop("self", UNSET)

        _voters = d.pop("voters", UNSET)
        voters: list[User] | Unset = UNSET
        if _voters is not UNSET:
            voters = []
            for voters_item_data in _voters:
                voters_item = User.from_dict(voters_item_data)



                voters.append(voters_item)


        votes = d.pop("votes", UNSET)

        votes = cls(
            has_voted=has_voted,
            self_=self_,
            voters=voters,
            votes=votes,
        )

        return votes

