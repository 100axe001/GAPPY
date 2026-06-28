from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.blocks_item import BlocksItem
  from ..models.bot_profile_object import BotProfileObject
  from ..models.file_comment_object import FileCommentObject
  from ..models.file_object import FileObject
  from ..models.message_object_attachments_item import MessageObjectAttachmentsItem
  from ..models.message_object_icons import MessageObjectIcons
  from ..models.objs_user_profile_short import ObjsUserProfileShort
  from ..models.reaction_object import ReactionObject





T = TypeVar("T", bound="MessageObject")



@_attrs_define
class MessageObject:
    """ 
        Attributes:
            text (str):
            ts (str):
            type_ (str):
            attachments (list[MessageObjectAttachmentsItem] | Unset):
            blocks (list[BlocksItem] | Unset): This is a very loose definition, in the future, we'll populate this with
                deeper schema in this definition namespace.
            bot_id (Any | Unset):
            bot_profile (BotProfileObject | Unset):
            client_msg_id (str | Unset):
            comment (FileCommentObject | Unset):
            display_as_bot (bool | Unset):
            file (FileObject | Unset):
            files (list[FileObject] | Unset):
            icons (MessageObjectIcons | Unset):
            inviter (str | Unset):
            is_delayed_message (bool | Unset):
            is_intro (bool | Unset):
            is_starred (bool | Unset):
            last_read (str | Unset):
            latest_reply (str | Unset):
            name (str | Unset):
            old_name (str | Unset):
            parent_user_id (str | Unset):
            permalink (str | Unset):
            pinned_to (list[str] | Unset):
            purpose (str | Unset):
            reactions (list[ReactionObject] | Unset):
            reply_count (int | Unset):
            reply_users (list[str] | Unset):
            reply_users_count (int | Unset):
            source_team (str | Unset):
            subscribed (bool | Unset):
            subtype (str | Unset):
            team (str | Unset):
            thread_ts (str | Unset):
            topic (str | Unset):
            unread_count (int | Unset):
            upload (bool | Unset):
            user (str | Unset):
            user_profile (ObjsUserProfileShort | Unset):
            user_team (str | Unset):
            username (str | Unset):
     """

    text: str
    ts: str
    type_: str
    attachments: list[MessageObjectAttachmentsItem] | Unset = UNSET
    blocks: list[BlocksItem] | Unset = UNSET
    bot_id: Any | Unset = UNSET
    bot_profile: BotProfileObject | Unset = UNSET
    client_msg_id: str | Unset = UNSET
    comment: FileCommentObject | Unset = UNSET
    display_as_bot: bool | Unset = UNSET
    file: FileObject | Unset = UNSET
    files: list[FileObject] | Unset = UNSET
    icons: MessageObjectIcons | Unset = UNSET
    inviter: str | Unset = UNSET
    is_delayed_message: bool | Unset = UNSET
    is_intro: bool | Unset = UNSET
    is_starred: bool | Unset = UNSET
    last_read: str | Unset = UNSET
    latest_reply: str | Unset = UNSET
    name: str | Unset = UNSET
    old_name: str | Unset = UNSET
    parent_user_id: str | Unset = UNSET
    permalink: str | Unset = UNSET
    pinned_to: list[str] | Unset = UNSET
    purpose: str | Unset = UNSET
    reactions: list[ReactionObject] | Unset = UNSET
    reply_count: int | Unset = UNSET
    reply_users: list[str] | Unset = UNSET
    reply_users_count: int | Unset = UNSET
    source_team: str | Unset = UNSET
    subscribed: bool | Unset = UNSET
    subtype: str | Unset = UNSET
    team: str | Unset = UNSET
    thread_ts: str | Unset = UNSET
    topic: str | Unset = UNSET
    unread_count: int | Unset = UNSET
    upload: bool | Unset = UNSET
    user: str | Unset = UNSET
    user_profile: ObjsUserProfileShort | Unset = UNSET
    user_team: str | Unset = UNSET
    username: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.blocks_item import BlocksItem
        from ..models.bot_profile_object import BotProfileObject
        from ..models.file_comment_object import FileCommentObject
        from ..models.file_object import FileObject
        from ..models.message_object_attachments_item import MessageObjectAttachmentsItem
        from ..models.message_object_icons import MessageObjectIcons
        from ..models.objs_user_profile_short import ObjsUserProfileShort
        from ..models.reaction_object import ReactionObject
        text = self.text

        ts = self.ts

        type_ = self.type_

        attachments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()
                attachments.append(attachments_item)



        blocks: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.blocks, Unset):
            blocks = []
            for componentsschemasblocks_item_data in self.blocks:
                componentsschemasblocks_item = componentsschemasblocks_item_data.to_dict()
                blocks.append(componentsschemasblocks_item)



        bot_id = self.bot_id

        bot_profile: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bot_profile, Unset):
            bot_profile = self.bot_profile.to_dict()

        client_msg_id = self.client_msg_id

        comment: dict[str, Any] | Unset = UNSET
        if not isinstance(self.comment, Unset):
            comment = self.comment.to_dict()

        display_as_bot = self.display_as_bot

        file: dict[str, Any] | Unset = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_dict()

        files: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.files, Unset):
            files = []
            for files_item_data in self.files:
                files_item = files_item_data.to_dict()
                files.append(files_item)



        icons: dict[str, Any] | Unset = UNSET
        if not isinstance(self.icons, Unset):
            icons = self.icons.to_dict()

        inviter = self.inviter

        is_delayed_message = self.is_delayed_message

        is_intro = self.is_intro

        is_starred = self.is_starred

        last_read = self.last_read

        latest_reply = self.latest_reply

        name = self.name

        old_name = self.old_name

        parent_user_id = self.parent_user_id

        permalink = self.permalink

        pinned_to: list[str] | Unset = UNSET
        if not isinstance(self.pinned_to, Unset):
            pinned_to = self.pinned_to



        purpose = self.purpose

        reactions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.reactions, Unset):
            reactions = []
            for reactions_item_data in self.reactions:
                reactions_item = reactions_item_data.to_dict()
                reactions.append(reactions_item)



        reply_count = self.reply_count

        reply_users: list[str] | Unset = UNSET
        if not isinstance(self.reply_users, Unset):
            reply_users = self.reply_users



        reply_users_count = self.reply_users_count

        source_team = self.source_team

        subscribed = self.subscribed

        subtype = self.subtype

        team = self.team

        thread_ts = self.thread_ts

        topic = self.topic

        unread_count = self.unread_count

        upload = self.upload

        user = self.user

        user_profile: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user_profile, Unset):
            user_profile = self.user_profile.to_dict()

        user_team = self.user_team

        username = self.username


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "text": text,
            "ts": ts,
            "type": type_,
        })
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if blocks is not UNSET:
            field_dict["blocks"] = blocks
        if bot_id is not UNSET:
            field_dict["bot_id"] = bot_id
        if bot_profile is not UNSET:
            field_dict["bot_profile"] = bot_profile
        if client_msg_id is not UNSET:
            field_dict["client_msg_id"] = client_msg_id
        if comment is not UNSET:
            field_dict["comment"] = comment
        if display_as_bot is not UNSET:
            field_dict["display_as_bot"] = display_as_bot
        if file is not UNSET:
            field_dict["file"] = file
        if files is not UNSET:
            field_dict["files"] = files
        if icons is not UNSET:
            field_dict["icons"] = icons
        if inviter is not UNSET:
            field_dict["inviter"] = inviter
        if is_delayed_message is not UNSET:
            field_dict["is_delayed_message"] = is_delayed_message
        if is_intro is not UNSET:
            field_dict["is_intro"] = is_intro
        if is_starred is not UNSET:
            field_dict["is_starred"] = is_starred
        if last_read is not UNSET:
            field_dict["last_read"] = last_read
        if latest_reply is not UNSET:
            field_dict["latest_reply"] = latest_reply
        if name is not UNSET:
            field_dict["name"] = name
        if old_name is not UNSET:
            field_dict["old_name"] = old_name
        if parent_user_id is not UNSET:
            field_dict["parent_user_id"] = parent_user_id
        if permalink is not UNSET:
            field_dict["permalink"] = permalink
        if pinned_to is not UNSET:
            field_dict["pinned_to"] = pinned_to
        if purpose is not UNSET:
            field_dict["purpose"] = purpose
        if reactions is not UNSET:
            field_dict["reactions"] = reactions
        if reply_count is not UNSET:
            field_dict["reply_count"] = reply_count
        if reply_users is not UNSET:
            field_dict["reply_users"] = reply_users
        if reply_users_count is not UNSET:
            field_dict["reply_users_count"] = reply_users_count
        if source_team is not UNSET:
            field_dict["source_team"] = source_team
        if subscribed is not UNSET:
            field_dict["subscribed"] = subscribed
        if subtype is not UNSET:
            field_dict["subtype"] = subtype
        if team is not UNSET:
            field_dict["team"] = team
        if thread_ts is not UNSET:
            field_dict["thread_ts"] = thread_ts
        if topic is not UNSET:
            field_dict["topic"] = topic
        if unread_count is not UNSET:
            field_dict["unread_count"] = unread_count
        if upload is not UNSET:
            field_dict["upload"] = upload
        if user is not UNSET:
            field_dict["user"] = user
        if user_profile is not UNSET:
            field_dict["user_profile"] = user_profile
        if user_team is not UNSET:
            field_dict["user_team"] = user_team
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.blocks_item import BlocksItem
        from ..models.bot_profile_object import BotProfileObject
        from ..models.file_comment_object import FileCommentObject
        from ..models.file_object import FileObject
        from ..models.message_object_attachments_item import MessageObjectAttachmentsItem
        from ..models.message_object_icons import MessageObjectIcons
        from ..models.objs_user_profile_short import ObjsUserProfileShort
        from ..models.reaction_object import ReactionObject
        d = dict(src_dict)
        text = d.pop("text")

        ts = d.pop("ts")

        type_ = d.pop("type")

        _attachments = d.pop("attachments", UNSET)
        attachments: list[MessageObjectAttachmentsItem] | Unset = UNSET
        if _attachments is not UNSET:
            attachments = []
            for attachments_item_data in _attachments:
                attachments_item = MessageObjectAttachmentsItem.from_dict(attachments_item_data)



                attachments.append(attachments_item)


        _blocks = d.pop("blocks", UNSET)
        blocks: list[BlocksItem] | Unset = UNSET
        if _blocks is not UNSET:
            blocks = []
            for componentsschemasblocks_item_data in _blocks:
                componentsschemasblocks_item = BlocksItem.from_dict(componentsschemasblocks_item_data)



                blocks.append(componentsschemasblocks_item)


        bot_id = d.pop("bot_id", UNSET)

        _bot_profile = d.pop("bot_profile", UNSET)
        bot_profile: BotProfileObject | Unset
        if isinstance(_bot_profile,  Unset):
            bot_profile = UNSET
        else:
            bot_profile = BotProfileObject.from_dict(_bot_profile)




        client_msg_id = d.pop("client_msg_id", UNSET)

        _comment = d.pop("comment", UNSET)
        comment: FileCommentObject | Unset
        if isinstance(_comment,  Unset):
            comment = UNSET
        else:
            comment = FileCommentObject.from_dict(_comment)




        display_as_bot = d.pop("display_as_bot", UNSET)

        _file = d.pop("file", UNSET)
        file: FileObject | Unset
        if isinstance(_file,  Unset):
            file = UNSET
        else:
            file = FileObject.from_dict(_file)




        _files = d.pop("files", UNSET)
        files: list[FileObject] | Unset = UNSET
        if _files is not UNSET:
            files = []
            for files_item_data in _files:
                files_item = FileObject.from_dict(files_item_data)



                files.append(files_item)


        _icons = d.pop("icons", UNSET)
        icons: MessageObjectIcons | Unset
        if isinstance(_icons,  Unset):
            icons = UNSET
        else:
            icons = MessageObjectIcons.from_dict(_icons)




        inviter = d.pop("inviter", UNSET)

        is_delayed_message = d.pop("is_delayed_message", UNSET)

        is_intro = d.pop("is_intro", UNSET)

        is_starred = d.pop("is_starred", UNSET)

        last_read = d.pop("last_read", UNSET)

        latest_reply = d.pop("latest_reply", UNSET)

        name = d.pop("name", UNSET)

        old_name = d.pop("old_name", UNSET)

        parent_user_id = d.pop("parent_user_id", UNSET)

        permalink = d.pop("permalink", UNSET)

        pinned_to = cast(list[str], d.pop("pinned_to", UNSET))


        purpose = d.pop("purpose", UNSET)

        _reactions = d.pop("reactions", UNSET)
        reactions: list[ReactionObject] | Unset = UNSET
        if _reactions is not UNSET:
            reactions = []
            for reactions_item_data in _reactions:
                reactions_item = ReactionObject.from_dict(reactions_item_data)



                reactions.append(reactions_item)


        reply_count = d.pop("reply_count", UNSET)

        reply_users = cast(list[str], d.pop("reply_users", UNSET))


        reply_users_count = d.pop("reply_users_count", UNSET)

        source_team = d.pop("source_team", UNSET)

        subscribed = d.pop("subscribed", UNSET)

        subtype = d.pop("subtype", UNSET)

        team = d.pop("team", UNSET)

        thread_ts = d.pop("thread_ts", UNSET)

        topic = d.pop("topic", UNSET)

        unread_count = d.pop("unread_count", UNSET)

        upload = d.pop("upload", UNSET)

        user = d.pop("user", UNSET)

        _user_profile = d.pop("user_profile", UNSET)
        user_profile: ObjsUserProfileShort | Unset
        if isinstance(_user_profile,  Unset):
            user_profile = UNSET
        else:
            user_profile = ObjsUserProfileShort.from_dict(_user_profile)




        user_team = d.pop("user_team", UNSET)

        username = d.pop("username", UNSET)

        message_object = cls(
            text=text,
            ts=ts,
            type_=type_,
            attachments=attachments,
            blocks=blocks,
            bot_id=bot_id,
            bot_profile=bot_profile,
            client_msg_id=client_msg_id,
            comment=comment,
            display_as_bot=display_as_bot,
            file=file,
            files=files,
            icons=icons,
            inviter=inviter,
            is_delayed_message=is_delayed_message,
            is_intro=is_intro,
            is_starred=is_starred,
            last_read=last_read,
            latest_reply=latest_reply,
            name=name,
            old_name=old_name,
            parent_user_id=parent_user_id,
            permalink=permalink,
            pinned_to=pinned_to,
            purpose=purpose,
            reactions=reactions,
            reply_count=reply_count,
            reply_users=reply_users,
            reply_users_count=reply_users_count,
            source_team=source_team,
            subscribed=subscribed,
            subtype=subtype,
            team=team,
            thread_ts=thread_ts,
            topic=topic,
            unread_count=unread_count,
            upload=upload,
            user=user,
            user_profile=user_profile,
            user_team=user_team,
            username=username,
        )

        return message_object

