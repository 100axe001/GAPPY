from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.gmail_users_settings_update_language_alt import GmailUsersSettingsUpdateLanguageAlt
from ...models.gmail_users_settings_update_language_xgafv import GmailUsersSettingsUpdateLanguageXgafv
from ...models.language_settings import LanguageSettings
from ...types import UNSET, Unset
from typing import cast



def _get_kwargs(
    user_id: str,
    *,
    body: LanguageSettings | Unset = UNSET,
    xgafv: GmailUsersSettingsUpdateLanguageXgafv | Unset = UNSET,
    access_token: str | Unset = UNSET,
    alt: GmailUsersSettingsUpdateLanguageAlt | Unset = UNSET,
    callback: str | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    upload_protocol: str | Unset = UNSET,
    upload_type: str | Unset = UNSET,

) -> dict[str, Any]:
    headers: dict[str, Any] = {}


    

    params: dict[str, Any] = {}

    json_xgafv: str | Unset = UNSET
    if not isinstance(xgafv, Unset):
        json_xgafv = xgafv.value

    params["$.xgafv"] = json_xgafv

    params["access_token"] = access_token

    json_alt: str | Unset = UNSET
    if not isinstance(alt, Unset):
        json_alt = alt.value

    params["alt"] = json_alt

    params["callback"] = callback

    params["fields"] = fields

    params["key"] = key

    params["oauth_token"] = oauth_token

    params["prettyPrint"] = pretty_print

    params["quotaUser"] = quota_user

    params["upload_protocol"] = upload_protocol

    params["uploadType"] = upload_type


    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": "/gmail/v1/users/{user_id}/settings/language".format(user_id=quote(str(user_id), safe=""),),
        "params": params,
    }

    
    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs



def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> LanguageSettings | None:
    if response.status_code == 200:
        response_200 = LanguageSettings.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[LanguageSettings]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
    body: LanguageSettings | Unset = UNSET,
    xgafv: GmailUsersSettingsUpdateLanguageXgafv | Unset = UNSET,
    access_token: str | Unset = UNSET,
    alt: GmailUsersSettingsUpdateLanguageAlt | Unset = UNSET,
    callback: str | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    upload_protocol: str | Unset = UNSET,
    upload_type: str | Unset = UNSET,

) -> Response[LanguageSettings]:
    """  Updates language settings. If successful, the return object contains the `displayLanguage` that was
    saved for the user, which may differ from the value passed into the request. This is because the
    requested `displayLanguage` may not be directly supported by Gmail but have a close variant that is,
    and so the variant may be chosen and saved instead.

    Args:
        user_id (str):
        xgafv (GmailUsersSettingsUpdateLanguageXgafv | Unset):
        access_token (str | Unset):
        alt (GmailUsersSettingsUpdateLanguageAlt | Unset):
        callback (str | Unset):
        fields (str | Unset):
        key (str | Unset):
        oauth_token (str | Unset):
        pretty_print (bool | Unset):
        quota_user (str | Unset):
        upload_protocol (str | Unset):
        upload_type (str | Unset):
        body (LanguageSettings | Unset): Language settings for an account. These settings
            correspond to the "Language settings" feature in the web interface.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LanguageSettings]
     """


    kwargs = _get_kwargs(
        user_id=user_id,
body=body,
xgafv=xgafv,
access_token=access_token,
alt=alt,
callback=callback,
fields=fields,
key=key,
oauth_token=oauth_token,
pretty_print=pretty_print,
quota_user=quota_user,
upload_protocol=upload_protocol,
upload_type=upload_type,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    user_id: str,
    *,
    client: AuthenticatedClient,
    body: LanguageSettings | Unset = UNSET,
    xgafv: GmailUsersSettingsUpdateLanguageXgafv | Unset = UNSET,
    access_token: str | Unset = UNSET,
    alt: GmailUsersSettingsUpdateLanguageAlt | Unset = UNSET,
    callback: str | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    upload_protocol: str | Unset = UNSET,
    upload_type: str | Unset = UNSET,

) -> LanguageSettings | None:
    """  Updates language settings. If successful, the return object contains the `displayLanguage` that was
    saved for the user, which may differ from the value passed into the request. This is because the
    requested `displayLanguage` may not be directly supported by Gmail but have a close variant that is,
    and so the variant may be chosen and saved instead.

    Args:
        user_id (str):
        xgafv (GmailUsersSettingsUpdateLanguageXgafv | Unset):
        access_token (str | Unset):
        alt (GmailUsersSettingsUpdateLanguageAlt | Unset):
        callback (str | Unset):
        fields (str | Unset):
        key (str | Unset):
        oauth_token (str | Unset):
        pretty_print (bool | Unset):
        quota_user (str | Unset):
        upload_protocol (str | Unset):
        upload_type (str | Unset):
        body (LanguageSettings | Unset): Language settings for an account. These settings
            correspond to the "Language settings" feature in the web interface.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LanguageSettings
     """


    return sync_detailed(
        user_id=user_id,
client=client,
body=body,
xgafv=xgafv,
access_token=access_token,
alt=alt,
callback=callback,
fields=fields,
key=key,
oauth_token=oauth_token,
pretty_print=pretty_print,
quota_user=quota_user,
upload_protocol=upload_protocol,
upload_type=upload_type,

    ).parsed

async def asyncio_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
    body: LanguageSettings | Unset = UNSET,
    xgafv: GmailUsersSettingsUpdateLanguageXgafv | Unset = UNSET,
    access_token: str | Unset = UNSET,
    alt: GmailUsersSettingsUpdateLanguageAlt | Unset = UNSET,
    callback: str | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    upload_protocol: str | Unset = UNSET,
    upload_type: str | Unset = UNSET,

) -> Response[LanguageSettings]:
    """  Updates language settings. If successful, the return object contains the `displayLanguage` that was
    saved for the user, which may differ from the value passed into the request. This is because the
    requested `displayLanguage` may not be directly supported by Gmail but have a close variant that is,
    and so the variant may be chosen and saved instead.

    Args:
        user_id (str):
        xgafv (GmailUsersSettingsUpdateLanguageXgafv | Unset):
        access_token (str | Unset):
        alt (GmailUsersSettingsUpdateLanguageAlt | Unset):
        callback (str | Unset):
        fields (str | Unset):
        key (str | Unset):
        oauth_token (str | Unset):
        pretty_print (bool | Unset):
        quota_user (str | Unset):
        upload_protocol (str | Unset):
        upload_type (str | Unset):
        body (LanguageSettings | Unset): Language settings for an account. These settings
            correspond to the "Language settings" feature in the web interface.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[LanguageSettings]
     """


    kwargs = _get_kwargs(
        user_id=user_id,
body=body,
xgafv=xgafv,
access_token=access_token,
alt=alt,
callback=callback,
fields=fields,
key=key,
oauth_token=oauth_token,
pretty_print=pretty_print,
quota_user=quota_user,
upload_protocol=upload_protocol,
upload_type=upload_type,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    user_id: str,
    *,
    client: AuthenticatedClient,
    body: LanguageSettings | Unset = UNSET,
    xgafv: GmailUsersSettingsUpdateLanguageXgafv | Unset = UNSET,
    access_token: str | Unset = UNSET,
    alt: GmailUsersSettingsUpdateLanguageAlt | Unset = UNSET,
    callback: str | Unset = UNSET,
    fields: str | Unset = UNSET,
    key: str | Unset = UNSET,
    oauth_token: str | Unset = UNSET,
    pretty_print: bool | Unset = UNSET,
    quota_user: str | Unset = UNSET,
    upload_protocol: str | Unset = UNSET,
    upload_type: str | Unset = UNSET,

) -> LanguageSettings | None:
    """  Updates language settings. If successful, the return object contains the `displayLanguage` that was
    saved for the user, which may differ from the value passed into the request. This is because the
    requested `displayLanguage` may not be directly supported by Gmail but have a close variant that is,
    and so the variant may be chosen and saved instead.

    Args:
        user_id (str):
        xgafv (GmailUsersSettingsUpdateLanguageXgafv | Unset):
        access_token (str | Unset):
        alt (GmailUsersSettingsUpdateLanguageAlt | Unset):
        callback (str | Unset):
        fields (str | Unset):
        key (str | Unset):
        oauth_token (str | Unset):
        pretty_print (bool | Unset):
        quota_user (str | Unset):
        upload_protocol (str | Unset):
        upload_type (str | Unset):
        body (LanguageSettings | Unset): Language settings for an account. These settings
            correspond to the "Language settings" feature in the web interface.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        LanguageSettings
     """


    return (await asyncio_detailed(
        user_id=user_id,
client=client,
body=body,
xgafv=xgafv,
access_token=access_token,
alt=alt,
callback=callback,
fields=fields,
key=key,
oauth_token=oauth_token,
pretty_print=pretty_print,
quota_user=quota_user,
upload_protocol=upload_protocol,
upload_type=upload_type,

    )).parsed
