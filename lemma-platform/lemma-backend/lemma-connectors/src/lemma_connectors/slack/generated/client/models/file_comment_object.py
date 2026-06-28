from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.info_for_a_pinned_item import InfoForAPinnedItem
  from ..models.reaction_object import ReactionObject





T = TypeVar("T", bound="FileCommentObject")



@_attrs_define
class FileCommentObject:
    """ 
        Attributes:
            comment (str):
            created (int):
            id (str):
            is_intro (bool):
            timestamp (int):
            user (str):
            is_starred (bool | Unset):
            num_stars (int | Unset):
            pinned_info (InfoForAPinnedItem | Unset):
            pinned_to (list[str] | Unset):
            reactions (list[ReactionObject] | Unset):
     """

    comment: str
    created: int
    id: str
    is_intro: bool
    timestamp: int
    user: str
    is_starred: bool | Unset = UNSET
    num_stars: int | Unset = UNSET
    pinned_info: InfoForAPinnedItem | Unset = UNSET
    pinned_to: list[str] | Unset = UNSET
    reactions: list[ReactionObject] | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.info_for_a_pinned_item import InfoForAPinnedItem
        from ..models.reaction_object import ReactionObject
        comment = self.comment

        created = self.created

        id = self.id

        is_intro = self.is_intro

        timestamp = self.timestamp

        user = self.user

        is_starred = self.is_starred

        num_stars = self.num_stars

        pinned_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pinned_info, Unset):
            pinned_info = self.pinned_info.to_dict()

        pinned_to: list[str] | Unset = UNSET
        if not isinstance(self.pinned_to, Unset):
            pinned_to = self.pinned_to



        reactions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.reactions, Unset):
            reactions = []
            for reactions_item_data in self.reactions:
                reactions_item = reactions_item_data.to_dict()
                reactions.append(reactions_item)




        field_dict: dict[str, Any] = {}

        field_dict.update({
            "comment": comment,
            "created": created,
            "id": id,
            "is_intro": is_intro,
            "timestamp": timestamp,
            "user": user,
        })
        if is_starred is not UNSET:
            field_dict["is_starred"] = is_starred
        if num_stars is not UNSET:
            field_dict["num_stars"] = num_stars
        if pinned_info is not UNSET:
            field_dict["pinned_info"] = pinned_info
        if pinned_to is not UNSET:
            field_dict["pinned_to"] = pinned_to
        if reactions is not UNSET:
            field_dict["reactions"] = reactions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.info_for_a_pinned_item import InfoForAPinnedItem
        from ..models.reaction_object import ReactionObject
        d = dict(src_dict)
        comment = d.pop("comment")

        created = d.pop("created")

        id = d.pop("id")

        is_intro = d.pop("is_intro")

        timestamp = d.pop("timestamp")

        user = d.pop("user")

        is_starred = d.pop("is_starred", UNSET)

        num_stars = d.pop("num_stars", UNSET)

        _pinned_info = d.pop("pinned_info", UNSET)
        pinned_info: InfoForAPinnedItem | Unset
        if isinstance(_pinned_info,  Unset):
            pinned_info = UNSET
        else:
            pinned_info = InfoForAPinnedItem.from_dict(_pinned_info)




        pinned_to = cast(list[str], d.pop("pinned_to", UNSET))


        _reactions = d.pop("reactions", UNSET)
        reactions: list[ReactionObject] | Unset = UNSET
        if _reactions is not UNSET:
            reactions = []
            for reactions_item_data in _reactions:
                reactions_item = ReactionObject.from_dict(reactions_item_data)



                reactions.append(reactions_item)


        file_comment_object = cls(
            comment=comment,
            created=created,
            id=id,
            is_intro=is_intro,
            timestamp=timestamp,
            user=user,
            is_starred=is_starred,
            num_stars=num_stars,
            pinned_info=pinned_info,
            pinned_to=pinned_to,
            reactions=reactions,
        )

        return file_comment_object

