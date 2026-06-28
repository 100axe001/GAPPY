from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.bot_profile_object import BotProfileObject





T = TypeVar("T", bound="ChatScheduleMessageChatScheduleMessageSuccessSchemaMessage")



@_attrs_define
class ChatScheduleMessageChatScheduleMessageSuccessSchemaMessage:
    """ 
        Attributes:
            bot_id (str):
            team (str):
            text (str):
            type_ (str):
            user (str):
            bot_profile (BotProfileObject | Unset):
            username (str | Unset):
     """

    bot_id: str
    team: str
    text: str
    type_: str
    user: str
    bot_profile: BotProfileObject | Unset = UNSET
    username: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.bot_profile_object import BotProfileObject
        bot_id = self.bot_id

        team = self.team

        text = self.text

        type_ = self.type_

        user = self.user

        bot_profile: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bot_profile, Unset):
            bot_profile = self.bot_profile.to_dict()

        username = self.username


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "bot_id": bot_id,
            "team": team,
            "text": text,
            "type": type_,
            "user": user,
        })
        if bot_profile is not UNSET:
            field_dict["bot_profile"] = bot_profile
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.bot_profile_object import BotProfileObject
        d = dict(src_dict)
        bot_id = d.pop("bot_id")

        team = d.pop("team")

        text = d.pop("text")

        type_ = d.pop("type")

        user = d.pop("user")

        _bot_profile = d.pop("bot_profile", UNSET)
        bot_profile: BotProfileObject | Unset
        if isinstance(_bot_profile,  Unset):
            bot_profile = UNSET
        else:
            bot_profile = BotProfileObject.from_dict(_bot_profile)




        username = d.pop("username", UNSET)

        chat_schedule_message_chat_schedule_message_success_schema_message = cls(
            bot_id=bot_id,
            team=team,
            text=text,
            type_=type_,
            user=user,
            bot_profile=bot_profile,
            username=username,
        )

        return chat_schedule_message_chat_schedule_message_success_schema_message

