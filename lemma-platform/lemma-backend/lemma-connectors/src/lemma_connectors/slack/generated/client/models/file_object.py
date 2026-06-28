from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.file_object_shares import FileObjectShares
  from ..models.info_for_a_pinned_item import InfoForAPinnedItem
  from ..models.reaction_object import ReactionObject





T = TypeVar("T", bound="FileObject")



@_attrs_define
class FileObject:
    """ 
        Attributes:
            channels (list[str] | Unset):
            comments_count (int | Unset):
            created (int | Unset):
            date_delete (int | Unset):
            display_as_bot (bool | Unset):
            editable (bool | Unset):
            editor (str | Unset):
            external_id (str | Unset):
            external_type (str | Unset):
            external_url (str | Unset):
            filetype (str | Unset):
            groups (list[str] | Unset):
            has_rich_preview (bool | Unset):
            id (str | Unset):
            image_exif_rotation (int | Unset):
            ims (list[str] | Unset):
            is_external (bool | Unset):
            is_public (bool | Unset):
            is_starred (bool | Unset):
            is_tombstoned (bool | Unset):
            last_editor (str | Unset):
            mimetype (str | Unset):
            mode (str | Unset):
            name (str | Unset):
            non_owner_editable (bool | Unset):
            num_stars (int | Unset):
            original_h (int | Unset):
            original_w (int | Unset):
            permalink (str | Unset):
            permalink_public (str | Unset):
            pinned_info (InfoForAPinnedItem | Unset):
            pinned_to (list[str] | Unset):
            pretty_type (str | Unset):
            preview (str | Unset):
            public_url_shared (bool | Unset):
            reactions (list[ReactionObject] | Unset):
            shares (FileObjectShares | Unset):
            size (int | Unset):
            source_team (str | Unset):
            state (str | Unset):
            thumb_1024 (str | Unset):
            thumb_1024_h (int | Unset):
            thumb_1024_w (int | Unset):
            thumb_160 (str | Unset):
            thumb_360 (str | Unset):
            thumb_360_h (int | Unset):
            thumb_360_w (int | Unset):
            thumb_480 (str | Unset):
            thumb_480_h (int | Unset):
            thumb_480_w (int | Unset):
            thumb_64 (str | Unset):
            thumb_720 (str | Unset):
            thumb_720_h (int | Unset):
            thumb_720_w (int | Unset):
            thumb_80 (str | Unset):
            thumb_800 (str | Unset):
            thumb_800_h (int | Unset):
            thumb_800_w (int | Unset):
            thumb_960 (str | Unset):
            thumb_960_h (int | Unset):
            thumb_960_w (int | Unset):
            thumb_tiny (str | Unset):
            timestamp (int | Unset):
            title (str | Unset):
            updated (int | Unset):
            url_private (str | Unset):
            url_private_download (str | Unset):
            user (str | Unset):
            user_team (str | Unset):
            username (str | Unset):
     """

    channels: list[str] | Unset = UNSET
    comments_count: int | Unset = UNSET
    created: int | Unset = UNSET
    date_delete: int | Unset = UNSET
    display_as_bot: bool | Unset = UNSET
    editable: bool | Unset = UNSET
    editor: str | Unset = UNSET
    external_id: str | Unset = UNSET
    external_type: str | Unset = UNSET
    external_url: str | Unset = UNSET
    filetype: str | Unset = UNSET
    groups: list[str] | Unset = UNSET
    has_rich_preview: bool | Unset = UNSET
    id: str | Unset = UNSET
    image_exif_rotation: int | Unset = UNSET
    ims: list[str] | Unset = UNSET
    is_external: bool | Unset = UNSET
    is_public: bool | Unset = UNSET
    is_starred: bool | Unset = UNSET
    is_tombstoned: bool | Unset = UNSET
    last_editor: str | Unset = UNSET
    mimetype: str | Unset = UNSET
    mode: str | Unset = UNSET
    name: str | Unset = UNSET
    non_owner_editable: bool | Unset = UNSET
    num_stars: int | Unset = UNSET
    original_h: int | Unset = UNSET
    original_w: int | Unset = UNSET
    permalink: str | Unset = UNSET
    permalink_public: str | Unset = UNSET
    pinned_info: InfoForAPinnedItem | Unset = UNSET
    pinned_to: list[str] | Unset = UNSET
    pretty_type: str | Unset = UNSET
    preview: str | Unset = UNSET
    public_url_shared: bool | Unset = UNSET
    reactions: list[ReactionObject] | Unset = UNSET
    shares: FileObjectShares | Unset = UNSET
    size: int | Unset = UNSET
    source_team: str | Unset = UNSET
    state: str | Unset = UNSET
    thumb_1024: str | Unset = UNSET
    thumb_1024_h: int | Unset = UNSET
    thumb_1024_w: int | Unset = UNSET
    thumb_160: str | Unset = UNSET
    thumb_360: str | Unset = UNSET
    thumb_360_h: int | Unset = UNSET
    thumb_360_w: int | Unset = UNSET
    thumb_480: str | Unset = UNSET
    thumb_480_h: int | Unset = UNSET
    thumb_480_w: int | Unset = UNSET
    thumb_64: str | Unset = UNSET
    thumb_720: str | Unset = UNSET
    thumb_720_h: int | Unset = UNSET
    thumb_720_w: int | Unset = UNSET
    thumb_80: str | Unset = UNSET
    thumb_800: str | Unset = UNSET
    thumb_800_h: int | Unset = UNSET
    thumb_800_w: int | Unset = UNSET
    thumb_960: str | Unset = UNSET
    thumb_960_h: int | Unset = UNSET
    thumb_960_w: int | Unset = UNSET
    thumb_tiny: str | Unset = UNSET
    timestamp: int | Unset = UNSET
    title: str | Unset = UNSET
    updated: int | Unset = UNSET
    url_private: str | Unset = UNSET
    url_private_download: str | Unset = UNSET
    user: str | Unset = UNSET
    user_team: str | Unset = UNSET
    username: str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.file_object_shares import FileObjectShares
        from ..models.info_for_a_pinned_item import InfoForAPinnedItem
        from ..models.reaction_object import ReactionObject
        channels: list[str] | Unset = UNSET
        if not isinstance(self.channels, Unset):
            channels = self.channels



        comments_count = self.comments_count

        created = self.created

        date_delete = self.date_delete

        display_as_bot = self.display_as_bot

        editable = self.editable

        editor = self.editor

        external_id = self.external_id

        external_type = self.external_type

        external_url = self.external_url

        filetype = self.filetype

        groups: list[str] | Unset = UNSET
        if not isinstance(self.groups, Unset):
            groups = self.groups



        has_rich_preview = self.has_rich_preview

        id = self.id

        image_exif_rotation = self.image_exif_rotation

        ims: list[str] | Unset = UNSET
        if not isinstance(self.ims, Unset):
            ims = self.ims



        is_external = self.is_external

        is_public = self.is_public

        is_starred = self.is_starred

        is_tombstoned = self.is_tombstoned

        last_editor = self.last_editor

        mimetype = self.mimetype

        mode = self.mode

        name = self.name

        non_owner_editable = self.non_owner_editable

        num_stars = self.num_stars

        original_h = self.original_h

        original_w = self.original_w

        permalink = self.permalink

        permalink_public = self.permalink_public

        pinned_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pinned_info, Unset):
            pinned_info = self.pinned_info.to_dict()

        pinned_to: list[str] | Unset = UNSET
        if not isinstance(self.pinned_to, Unset):
            pinned_to = self.pinned_to



        pretty_type = self.pretty_type

        preview = self.preview

        public_url_shared = self.public_url_shared

        reactions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.reactions, Unset):
            reactions = []
            for reactions_item_data in self.reactions:
                reactions_item = reactions_item_data.to_dict()
                reactions.append(reactions_item)



        shares: dict[str, Any] | Unset = UNSET
        if not isinstance(self.shares, Unset):
            shares = self.shares.to_dict()

        size = self.size

        source_team = self.source_team

        state = self.state

        thumb_1024 = self.thumb_1024

        thumb_1024_h = self.thumb_1024_h

        thumb_1024_w = self.thumb_1024_w

        thumb_160 = self.thumb_160

        thumb_360 = self.thumb_360

        thumb_360_h = self.thumb_360_h

        thumb_360_w = self.thumb_360_w

        thumb_480 = self.thumb_480

        thumb_480_h = self.thumb_480_h

        thumb_480_w = self.thumb_480_w

        thumb_64 = self.thumb_64

        thumb_720 = self.thumb_720

        thumb_720_h = self.thumb_720_h

        thumb_720_w = self.thumb_720_w

        thumb_80 = self.thumb_80

        thumb_800 = self.thumb_800

        thumb_800_h = self.thumb_800_h

        thumb_800_w = self.thumb_800_w

        thumb_960 = self.thumb_960

        thumb_960_h = self.thumb_960_h

        thumb_960_w = self.thumb_960_w

        thumb_tiny = self.thumb_tiny

        timestamp = self.timestamp

        title = self.title

        updated = self.updated

        url_private = self.url_private

        url_private_download = self.url_private_download

        user = self.user

        user_team = self.user_team

        username = self.username


        field_dict: dict[str, Any] = {}

        field_dict.update({
        })
        if channels is not UNSET:
            field_dict["channels"] = channels
        if comments_count is not UNSET:
            field_dict["comments_count"] = comments_count
        if created is not UNSET:
            field_dict["created"] = created
        if date_delete is not UNSET:
            field_dict["date_delete"] = date_delete
        if display_as_bot is not UNSET:
            field_dict["display_as_bot"] = display_as_bot
        if editable is not UNSET:
            field_dict["editable"] = editable
        if editor is not UNSET:
            field_dict["editor"] = editor
        if external_id is not UNSET:
            field_dict["external_id"] = external_id
        if external_type is not UNSET:
            field_dict["external_type"] = external_type
        if external_url is not UNSET:
            field_dict["external_url"] = external_url
        if filetype is not UNSET:
            field_dict["filetype"] = filetype
        if groups is not UNSET:
            field_dict["groups"] = groups
        if has_rich_preview is not UNSET:
            field_dict["has_rich_preview"] = has_rich_preview
        if id is not UNSET:
            field_dict["id"] = id
        if image_exif_rotation is not UNSET:
            field_dict["image_exif_rotation"] = image_exif_rotation
        if ims is not UNSET:
            field_dict["ims"] = ims
        if is_external is not UNSET:
            field_dict["is_external"] = is_external
        if is_public is not UNSET:
            field_dict["is_public"] = is_public
        if is_starred is not UNSET:
            field_dict["is_starred"] = is_starred
        if is_tombstoned is not UNSET:
            field_dict["is_tombstoned"] = is_tombstoned
        if last_editor is not UNSET:
            field_dict["last_editor"] = last_editor
        if mimetype is not UNSET:
            field_dict["mimetype"] = mimetype
        if mode is not UNSET:
            field_dict["mode"] = mode
        if name is not UNSET:
            field_dict["name"] = name
        if non_owner_editable is not UNSET:
            field_dict["non_owner_editable"] = non_owner_editable
        if num_stars is not UNSET:
            field_dict["num_stars"] = num_stars
        if original_h is not UNSET:
            field_dict["original_h"] = original_h
        if original_w is not UNSET:
            field_dict["original_w"] = original_w
        if permalink is not UNSET:
            field_dict["permalink"] = permalink
        if permalink_public is not UNSET:
            field_dict["permalink_public"] = permalink_public
        if pinned_info is not UNSET:
            field_dict["pinned_info"] = pinned_info
        if pinned_to is not UNSET:
            field_dict["pinned_to"] = pinned_to
        if pretty_type is not UNSET:
            field_dict["pretty_type"] = pretty_type
        if preview is not UNSET:
            field_dict["preview"] = preview
        if public_url_shared is not UNSET:
            field_dict["public_url_shared"] = public_url_shared
        if reactions is not UNSET:
            field_dict["reactions"] = reactions
        if shares is not UNSET:
            field_dict["shares"] = shares
        if size is not UNSET:
            field_dict["size"] = size
        if source_team is not UNSET:
            field_dict["source_team"] = source_team
        if state is not UNSET:
            field_dict["state"] = state
        if thumb_1024 is not UNSET:
            field_dict["thumb_1024"] = thumb_1024
        if thumb_1024_h is not UNSET:
            field_dict["thumb_1024_h"] = thumb_1024_h
        if thumb_1024_w is not UNSET:
            field_dict["thumb_1024_w"] = thumb_1024_w
        if thumb_160 is not UNSET:
            field_dict["thumb_160"] = thumb_160
        if thumb_360 is not UNSET:
            field_dict["thumb_360"] = thumb_360
        if thumb_360_h is not UNSET:
            field_dict["thumb_360_h"] = thumb_360_h
        if thumb_360_w is not UNSET:
            field_dict["thumb_360_w"] = thumb_360_w
        if thumb_480 is not UNSET:
            field_dict["thumb_480"] = thumb_480
        if thumb_480_h is not UNSET:
            field_dict["thumb_480_h"] = thumb_480_h
        if thumb_480_w is not UNSET:
            field_dict["thumb_480_w"] = thumb_480_w
        if thumb_64 is not UNSET:
            field_dict["thumb_64"] = thumb_64
        if thumb_720 is not UNSET:
            field_dict["thumb_720"] = thumb_720
        if thumb_720_h is not UNSET:
            field_dict["thumb_720_h"] = thumb_720_h
        if thumb_720_w is not UNSET:
            field_dict["thumb_720_w"] = thumb_720_w
        if thumb_80 is not UNSET:
            field_dict["thumb_80"] = thumb_80
        if thumb_800 is not UNSET:
            field_dict["thumb_800"] = thumb_800
        if thumb_800_h is not UNSET:
            field_dict["thumb_800_h"] = thumb_800_h
        if thumb_800_w is not UNSET:
            field_dict["thumb_800_w"] = thumb_800_w
        if thumb_960 is not UNSET:
            field_dict["thumb_960"] = thumb_960
        if thumb_960_h is not UNSET:
            field_dict["thumb_960_h"] = thumb_960_h
        if thumb_960_w is not UNSET:
            field_dict["thumb_960_w"] = thumb_960_w
        if thumb_tiny is not UNSET:
            field_dict["thumb_tiny"] = thumb_tiny
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if title is not UNSET:
            field_dict["title"] = title
        if updated is not UNSET:
            field_dict["updated"] = updated
        if url_private is not UNSET:
            field_dict["url_private"] = url_private
        if url_private_download is not UNSET:
            field_dict["url_private_download"] = url_private_download
        if user is not UNSET:
            field_dict["user"] = user
        if user_team is not UNSET:
            field_dict["user_team"] = user_team
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_object_shares import FileObjectShares
        from ..models.info_for_a_pinned_item import InfoForAPinnedItem
        from ..models.reaction_object import ReactionObject
        d = dict(src_dict)
        channels = cast(list[str], d.pop("channels", UNSET))


        comments_count = d.pop("comments_count", UNSET)

        created = d.pop("created", UNSET)

        date_delete = d.pop("date_delete", UNSET)

        display_as_bot = d.pop("display_as_bot", UNSET)

        editable = d.pop("editable", UNSET)

        editor = d.pop("editor", UNSET)

        external_id = d.pop("external_id", UNSET)

        external_type = d.pop("external_type", UNSET)

        external_url = d.pop("external_url", UNSET)

        filetype = d.pop("filetype", UNSET)

        groups = cast(list[str], d.pop("groups", UNSET))


        has_rich_preview = d.pop("has_rich_preview", UNSET)

        id = d.pop("id", UNSET)

        image_exif_rotation = d.pop("image_exif_rotation", UNSET)

        ims = cast(list[str], d.pop("ims", UNSET))


        is_external = d.pop("is_external", UNSET)

        is_public = d.pop("is_public", UNSET)

        is_starred = d.pop("is_starred", UNSET)

        is_tombstoned = d.pop("is_tombstoned", UNSET)

        last_editor = d.pop("last_editor", UNSET)

        mimetype = d.pop("mimetype", UNSET)

        mode = d.pop("mode", UNSET)

        name = d.pop("name", UNSET)

        non_owner_editable = d.pop("non_owner_editable", UNSET)

        num_stars = d.pop("num_stars", UNSET)

        original_h = d.pop("original_h", UNSET)

        original_w = d.pop("original_w", UNSET)

        permalink = d.pop("permalink", UNSET)

        permalink_public = d.pop("permalink_public", UNSET)

        _pinned_info = d.pop("pinned_info", UNSET)
        pinned_info: InfoForAPinnedItem | Unset
        if isinstance(_pinned_info,  Unset):
            pinned_info = UNSET
        else:
            pinned_info = InfoForAPinnedItem.from_dict(_pinned_info)




        pinned_to = cast(list[str], d.pop("pinned_to", UNSET))


        pretty_type = d.pop("pretty_type", UNSET)

        preview = d.pop("preview", UNSET)

        public_url_shared = d.pop("public_url_shared", UNSET)

        _reactions = d.pop("reactions", UNSET)
        reactions: list[ReactionObject] | Unset = UNSET
        if _reactions is not UNSET:
            reactions = []
            for reactions_item_data in _reactions:
                reactions_item = ReactionObject.from_dict(reactions_item_data)



                reactions.append(reactions_item)


        _shares = d.pop("shares", UNSET)
        shares: FileObjectShares | Unset
        if isinstance(_shares,  Unset):
            shares = UNSET
        else:
            shares = FileObjectShares.from_dict(_shares)




        size = d.pop("size", UNSET)

        source_team = d.pop("source_team", UNSET)

        state = d.pop("state", UNSET)

        thumb_1024 = d.pop("thumb_1024", UNSET)

        thumb_1024_h = d.pop("thumb_1024_h", UNSET)

        thumb_1024_w = d.pop("thumb_1024_w", UNSET)

        thumb_160 = d.pop("thumb_160", UNSET)

        thumb_360 = d.pop("thumb_360", UNSET)

        thumb_360_h = d.pop("thumb_360_h", UNSET)

        thumb_360_w = d.pop("thumb_360_w", UNSET)

        thumb_480 = d.pop("thumb_480", UNSET)

        thumb_480_h = d.pop("thumb_480_h", UNSET)

        thumb_480_w = d.pop("thumb_480_w", UNSET)

        thumb_64 = d.pop("thumb_64", UNSET)

        thumb_720 = d.pop("thumb_720", UNSET)

        thumb_720_h = d.pop("thumb_720_h", UNSET)

        thumb_720_w = d.pop("thumb_720_w", UNSET)

        thumb_80 = d.pop("thumb_80", UNSET)

        thumb_800 = d.pop("thumb_800", UNSET)

        thumb_800_h = d.pop("thumb_800_h", UNSET)

        thumb_800_w = d.pop("thumb_800_w", UNSET)

        thumb_960 = d.pop("thumb_960", UNSET)

        thumb_960_h = d.pop("thumb_960_h", UNSET)

        thumb_960_w = d.pop("thumb_960_w", UNSET)

        thumb_tiny = d.pop("thumb_tiny", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        title = d.pop("title", UNSET)

        updated = d.pop("updated", UNSET)

        url_private = d.pop("url_private", UNSET)

        url_private_download = d.pop("url_private_download", UNSET)

        user = d.pop("user", UNSET)

        user_team = d.pop("user_team", UNSET)

        username = d.pop("username", UNSET)

        file_object = cls(
            channels=channels,
            comments_count=comments_count,
            created=created,
            date_delete=date_delete,
            display_as_bot=display_as_bot,
            editable=editable,
            editor=editor,
            external_id=external_id,
            external_type=external_type,
            external_url=external_url,
            filetype=filetype,
            groups=groups,
            has_rich_preview=has_rich_preview,
            id=id,
            image_exif_rotation=image_exif_rotation,
            ims=ims,
            is_external=is_external,
            is_public=is_public,
            is_starred=is_starred,
            is_tombstoned=is_tombstoned,
            last_editor=last_editor,
            mimetype=mimetype,
            mode=mode,
            name=name,
            non_owner_editable=non_owner_editable,
            num_stars=num_stars,
            original_h=original_h,
            original_w=original_w,
            permalink=permalink,
            permalink_public=permalink_public,
            pinned_info=pinned_info,
            pinned_to=pinned_to,
            pretty_type=pretty_type,
            preview=preview,
            public_url_shared=public_url_shared,
            reactions=reactions,
            shares=shares,
            size=size,
            source_team=source_team,
            state=state,
            thumb_1024=thumb_1024,
            thumb_1024_h=thumb_1024_h,
            thumb_1024_w=thumb_1024_w,
            thumb_160=thumb_160,
            thumb_360=thumb_360,
            thumb_360_h=thumb_360_h,
            thumb_360_w=thumb_360_w,
            thumb_480=thumb_480,
            thumb_480_h=thumb_480_h,
            thumb_480_w=thumb_480_w,
            thumb_64=thumb_64,
            thumb_720=thumb_720,
            thumb_720_h=thumb_720_h,
            thumb_720_w=thumb_720_w,
            thumb_80=thumb_80,
            thumb_800=thumb_800,
            thumb_800_h=thumb_800_h,
            thumb_800_w=thumb_800_w,
            thumb_960=thumb_960,
            thumb_960_h=thumb_960_h,
            thumb_960_w=thumb_960_w,
            thumb_tiny=thumb_tiny,
            timestamp=timestamp,
            title=title,
            updated=updated,
            url_private=url_private,
            url_private_download=url_private_download,
            user=user,
            user_team=user_team,
            username=username,
        )

        return file_object

