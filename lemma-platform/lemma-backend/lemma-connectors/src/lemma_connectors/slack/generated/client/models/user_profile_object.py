from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.user_profile_object_fields_type_0 import UserProfileObjectFieldsType0





T = TypeVar("T", bound="UserProfileObject")



@_attrs_define
class UserProfileObject:
    """ 
        Attributes:
            avatar_hash (str):
            display_name (str):
            display_name_normalized (str):
            fields (list[Any] | None | UserProfileObjectFieldsType0):
            phone (str):
            real_name (str):
            real_name_normalized (str):
            skype (str):
            status_emoji (str):
            status_text (str):
            title (str):
            always_active (bool | Unset):
            api_app_id (str | Unset):
            bot_id (str | Unset):
            email (None | str | Unset):
            first_name (None | str | Unset):
            guest_expiration_ts (int | None | Unset):
            guest_invited_by (None | str | Unset):
            image_1024 (None | str | Unset):
            image_192 (None | str | Unset):
            image_24 (None | str | Unset):
            image_32 (None | str | Unset):
            image_48 (None | str | Unset):
            image_512 (None | str | Unset):
            image_72 (None | str | Unset):
            image_original (None | str | Unset):
            is_app_user (bool | Unset):
            is_custom_image (bool | Unset):
            is_restricted (bool | None | Unset):
            is_ultra_restricted (bool | None | Unset):
            last_avatar_image_hash (str | Unset):
            last_name (None | str | Unset):
            memberships_count (int | Unset):
            name (None | str | Unset):
            pronouns (str | Unset):
            status_default_emoji (str | Unset):
            status_default_text (str | Unset):
            status_default_text_canonical (None | str | Unset):
            status_expiration (int | Unset):
            status_text_canonical (None | str | Unset):
            team (str | Unset):
            updated (int | Unset):
            user_id (str | Unset):
            username (None | str | Unset):
     """

    avatar_hash: str
    display_name: str
    display_name_normalized: str
    fields: list[Any] | None | UserProfileObjectFieldsType0
    phone: str
    real_name: str
    real_name_normalized: str
    skype: str
    status_emoji: str
    status_text: str
    title: str
    always_active: bool | Unset = UNSET
    api_app_id: str | Unset = UNSET
    bot_id: str | Unset = UNSET
    email: None | str | Unset = UNSET
    first_name: None | str | Unset = UNSET
    guest_expiration_ts: int | None | Unset = UNSET
    guest_invited_by: None | str | Unset = UNSET
    image_1024: None | str | Unset = UNSET
    image_192: None | str | Unset = UNSET
    image_24: None | str | Unset = UNSET
    image_32: None | str | Unset = UNSET
    image_48: None | str | Unset = UNSET
    image_512: None | str | Unset = UNSET
    image_72: None | str | Unset = UNSET
    image_original: None | str | Unset = UNSET
    is_app_user: bool | Unset = UNSET
    is_custom_image: bool | Unset = UNSET
    is_restricted: bool | None | Unset = UNSET
    is_ultra_restricted: bool | None | Unset = UNSET
    last_avatar_image_hash: str | Unset = UNSET
    last_name: None | str | Unset = UNSET
    memberships_count: int | Unset = UNSET
    name: None | str | Unset = UNSET
    pronouns: str | Unset = UNSET
    status_default_emoji: str | Unset = UNSET
    status_default_text: str | Unset = UNSET
    status_default_text_canonical: None | str | Unset = UNSET
    status_expiration: int | Unset = UNSET
    status_text_canonical: None | str | Unset = UNSET
    team: str | Unset = UNSET
    updated: int | Unset = UNSET
    user_id: str | Unset = UNSET
    username: None | str | Unset = UNSET





    def to_dict(self) -> dict[str, Any]:
        from ..models.user_profile_object_fields_type_0 import UserProfileObjectFieldsType0
        avatar_hash = self.avatar_hash

        display_name = self.display_name

        display_name_normalized = self.display_name_normalized

        fields: dict[str, Any] | list[Any] | None
        if isinstance(self.fields, UserProfileObjectFieldsType0):
            fields = self.fields.to_dict()
        elif isinstance(self.fields, list):
            fields = self.fields


        else:
            fields = self.fields

        phone = self.phone

        real_name = self.real_name

        real_name_normalized = self.real_name_normalized

        skype = self.skype

        status_emoji = self.status_emoji

        status_text = self.status_text

        title = self.title

        always_active = self.always_active

        api_app_id = self.api_app_id

        bot_id = self.bot_id

        email: None | str | Unset
        if isinstance(self.email, Unset):
            email = UNSET
        else:
            email = self.email

        first_name: None | str | Unset
        if isinstance(self.first_name, Unset):
            first_name = UNSET
        else:
            first_name = self.first_name

        guest_expiration_ts: int | None | Unset
        if isinstance(self.guest_expiration_ts, Unset):
            guest_expiration_ts = UNSET
        else:
            guest_expiration_ts = self.guest_expiration_ts

        guest_invited_by: None | str | Unset
        if isinstance(self.guest_invited_by, Unset):
            guest_invited_by = UNSET
        else:
            guest_invited_by = self.guest_invited_by

        image_1024: None | str | Unset
        if isinstance(self.image_1024, Unset):
            image_1024 = UNSET
        else:
            image_1024 = self.image_1024

        image_192: None | str | Unset
        if isinstance(self.image_192, Unset):
            image_192 = UNSET
        else:
            image_192 = self.image_192

        image_24: None | str | Unset
        if isinstance(self.image_24, Unset):
            image_24 = UNSET
        else:
            image_24 = self.image_24

        image_32: None | str | Unset
        if isinstance(self.image_32, Unset):
            image_32 = UNSET
        else:
            image_32 = self.image_32

        image_48: None | str | Unset
        if isinstance(self.image_48, Unset):
            image_48 = UNSET
        else:
            image_48 = self.image_48

        image_512: None | str | Unset
        if isinstance(self.image_512, Unset):
            image_512 = UNSET
        else:
            image_512 = self.image_512

        image_72: None | str | Unset
        if isinstance(self.image_72, Unset):
            image_72 = UNSET
        else:
            image_72 = self.image_72

        image_original: None | str | Unset
        if isinstance(self.image_original, Unset):
            image_original = UNSET
        else:
            image_original = self.image_original

        is_app_user = self.is_app_user

        is_custom_image = self.is_custom_image

        is_restricted: bool | None | Unset
        if isinstance(self.is_restricted, Unset):
            is_restricted = UNSET
        else:
            is_restricted = self.is_restricted

        is_ultra_restricted: bool | None | Unset
        if isinstance(self.is_ultra_restricted, Unset):
            is_ultra_restricted = UNSET
        else:
            is_ultra_restricted = self.is_ultra_restricted

        last_avatar_image_hash = self.last_avatar_image_hash

        last_name: None | str | Unset
        if isinstance(self.last_name, Unset):
            last_name = UNSET
        else:
            last_name = self.last_name

        memberships_count = self.memberships_count

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        pronouns = self.pronouns

        status_default_emoji = self.status_default_emoji

        status_default_text = self.status_default_text

        status_default_text_canonical: None | str | Unset
        if isinstance(self.status_default_text_canonical, Unset):
            status_default_text_canonical = UNSET
        else:
            status_default_text_canonical = self.status_default_text_canonical

        status_expiration = self.status_expiration

        status_text_canonical: None | str | Unset
        if isinstance(self.status_text_canonical, Unset):
            status_text_canonical = UNSET
        else:
            status_text_canonical = self.status_text_canonical

        team = self.team

        updated = self.updated

        user_id = self.user_id

        username: None | str | Unset
        if isinstance(self.username, Unset):
            username = UNSET
        else:
            username = self.username


        field_dict: dict[str, Any] = {}

        field_dict.update({
            "avatar_hash": avatar_hash,
            "display_name": display_name,
            "display_name_normalized": display_name_normalized,
            "fields": fields,
            "phone": phone,
            "real_name": real_name,
            "real_name_normalized": real_name_normalized,
            "skype": skype,
            "status_emoji": status_emoji,
            "status_text": status_text,
            "title": title,
        })
        if always_active is not UNSET:
            field_dict["always_active"] = always_active
        if api_app_id is not UNSET:
            field_dict["api_app_id"] = api_app_id
        if bot_id is not UNSET:
            field_dict["bot_id"] = bot_id
        if email is not UNSET:
            field_dict["email"] = email
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if guest_expiration_ts is not UNSET:
            field_dict["guest_expiration_ts"] = guest_expiration_ts
        if guest_invited_by is not UNSET:
            field_dict["guest_invited_by"] = guest_invited_by
        if image_1024 is not UNSET:
            field_dict["image_1024"] = image_1024
        if image_192 is not UNSET:
            field_dict["image_192"] = image_192
        if image_24 is not UNSET:
            field_dict["image_24"] = image_24
        if image_32 is not UNSET:
            field_dict["image_32"] = image_32
        if image_48 is not UNSET:
            field_dict["image_48"] = image_48
        if image_512 is not UNSET:
            field_dict["image_512"] = image_512
        if image_72 is not UNSET:
            field_dict["image_72"] = image_72
        if image_original is not UNSET:
            field_dict["image_original"] = image_original
        if is_app_user is not UNSET:
            field_dict["is_app_user"] = is_app_user
        if is_custom_image is not UNSET:
            field_dict["is_custom_image"] = is_custom_image
        if is_restricted is not UNSET:
            field_dict["is_restricted"] = is_restricted
        if is_ultra_restricted is not UNSET:
            field_dict["is_ultra_restricted"] = is_ultra_restricted
        if last_avatar_image_hash is not UNSET:
            field_dict["last_avatar_image_hash"] = last_avatar_image_hash
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if memberships_count is not UNSET:
            field_dict["memberships_count"] = memberships_count
        if name is not UNSET:
            field_dict["name"] = name
        if pronouns is not UNSET:
            field_dict["pronouns"] = pronouns
        if status_default_emoji is not UNSET:
            field_dict["status_default_emoji"] = status_default_emoji
        if status_default_text is not UNSET:
            field_dict["status_default_text"] = status_default_text
        if status_default_text_canonical is not UNSET:
            field_dict["status_default_text_canonical"] = status_default_text_canonical
        if status_expiration is not UNSET:
            field_dict["status_expiration"] = status_expiration
        if status_text_canonical is not UNSET:
            field_dict["status_text_canonical"] = status_text_canonical
        if team is not UNSET:
            field_dict["team"] = team
        if updated is not UNSET:
            field_dict["updated"] = updated
        if user_id is not UNSET:
            field_dict["user_id"] = user_id
        if username is not UNSET:
            field_dict["username"] = username

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_profile_object_fields_type_0 import UserProfileObjectFieldsType0
        d = dict(src_dict)
        avatar_hash = d.pop("avatar_hash")

        display_name = d.pop("display_name")

        display_name_normalized = d.pop("display_name_normalized")

        def _parse_fields(data: object) -> list[Any] | None | UserProfileObjectFieldsType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                fields_type_0 = UserProfileObjectFieldsType0.from_dict(data)



                return fields_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                fields_type_1 = cast(list[Any], data)

                return fields_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Any] | None | UserProfileObjectFieldsType0, data)

        fields = _parse_fields(d.pop("fields"))


        phone = d.pop("phone")

        real_name = d.pop("real_name")

        real_name_normalized = d.pop("real_name_normalized")

        skype = d.pop("skype")

        status_emoji = d.pop("status_emoji")

        status_text = d.pop("status_text")

        title = d.pop("title")

        always_active = d.pop("always_active", UNSET)

        api_app_id = d.pop("api_app_id", UNSET)

        bot_id = d.pop("bot_id", UNSET)

        def _parse_email(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        email = _parse_email(d.pop("email", UNSET))


        def _parse_first_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        first_name = _parse_first_name(d.pop("first_name", UNSET))


        def _parse_guest_expiration_ts(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        guest_expiration_ts = _parse_guest_expiration_ts(d.pop("guest_expiration_ts", UNSET))


        def _parse_guest_invited_by(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        guest_invited_by = _parse_guest_invited_by(d.pop("guest_invited_by", UNSET))


        def _parse_image_1024(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        image_1024 = _parse_image_1024(d.pop("image_1024", UNSET))


        def _parse_image_192(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        image_192 = _parse_image_192(d.pop("image_192", UNSET))


        def _parse_image_24(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        image_24 = _parse_image_24(d.pop("image_24", UNSET))


        def _parse_image_32(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        image_32 = _parse_image_32(d.pop("image_32", UNSET))


        def _parse_image_48(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        image_48 = _parse_image_48(d.pop("image_48", UNSET))


        def _parse_image_512(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        image_512 = _parse_image_512(d.pop("image_512", UNSET))


        def _parse_image_72(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        image_72 = _parse_image_72(d.pop("image_72", UNSET))


        def _parse_image_original(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        image_original = _parse_image_original(d.pop("image_original", UNSET))


        is_app_user = d.pop("is_app_user", UNSET)

        is_custom_image = d.pop("is_custom_image", UNSET)

        def _parse_is_restricted(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_restricted = _parse_is_restricted(d.pop("is_restricted", UNSET))


        def _parse_is_ultra_restricted(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        is_ultra_restricted = _parse_is_ultra_restricted(d.pop("is_ultra_restricted", UNSET))


        last_avatar_image_hash = d.pop("last_avatar_image_hash", UNSET)

        def _parse_last_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_name = _parse_last_name(d.pop("last_name", UNSET))


        memberships_count = d.pop("memberships_count", UNSET)

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))


        pronouns = d.pop("pronouns", UNSET)

        status_default_emoji = d.pop("status_default_emoji", UNSET)

        status_default_text = d.pop("status_default_text", UNSET)

        def _parse_status_default_text_canonical(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status_default_text_canonical = _parse_status_default_text_canonical(d.pop("status_default_text_canonical", UNSET))


        status_expiration = d.pop("status_expiration", UNSET)

        def _parse_status_text_canonical(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status_text_canonical = _parse_status_text_canonical(d.pop("status_text_canonical", UNSET))


        team = d.pop("team", UNSET)

        updated = d.pop("updated", UNSET)

        user_id = d.pop("user_id", UNSET)

        def _parse_username(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        username = _parse_username(d.pop("username", UNSET))


        user_profile_object = cls(
            avatar_hash=avatar_hash,
            display_name=display_name,
            display_name_normalized=display_name_normalized,
            fields=fields,
            phone=phone,
            real_name=real_name,
            real_name_normalized=real_name_normalized,
            skype=skype,
            status_emoji=status_emoji,
            status_text=status_text,
            title=title,
            always_active=always_active,
            api_app_id=api_app_id,
            bot_id=bot_id,
            email=email,
            first_name=first_name,
            guest_expiration_ts=guest_expiration_ts,
            guest_invited_by=guest_invited_by,
            image_1024=image_1024,
            image_192=image_192,
            image_24=image_24,
            image_32=image_32,
            image_48=image_48,
            image_512=image_512,
            image_72=image_72,
            image_original=image_original,
            is_app_user=is_app_user,
            is_custom_image=is_custom_image,
            is_restricted=is_restricted,
            is_ultra_restricted=is_ultra_restricted,
            last_avatar_image_hash=last_avatar_image_hash,
            last_name=last_name,
            memberships_count=memberships_count,
            name=name,
            pronouns=pronouns,
            status_default_emoji=status_default_emoji,
            status_default_text=status_default_text,
            status_default_text_canonical=status_default_text_canonical,
            status_expiration=status_expiration,
            status_text_canonical=status_text_canonical,
            team=team,
            updated=updated,
            user_id=user_id,
            username=username,
        )

        return user_profile_object

