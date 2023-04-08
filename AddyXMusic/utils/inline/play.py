import math

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from AddyXMusic import app

import config
from AddyXMusic.utils.formatters import time_to_seconds


## After Edits with Timer Bar

def stream_markup_timer(_, videoid, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    Addy = math.floor(percentage)
    if 0 < Addy <= 5:
        bar = " 🥀@OfficialAddy🥀 "
    elif 5 < Addy < 10:
        bar = " 💥@AddySupport💥 "
    elif 10 <= Addy < 15:
        bar = " 🔥@AddyUpdate🔥 "
    elif 15 <= Addy < 20:
        bar = " 🥀@OfficialAddy🥀 "
    elif 20 <= Addy < 25:
        bar = " 💥@AddySupport💥 "
    elif 25 <= Addy < 30:
        bar = " 🔥@AddyUpdate🔥 "
    elif 30 <= Addy < 35:
        bar = " 🥀@OfficialAddy🥀 "
    elif 35 <= Addy < 40:
        bar = " 💥@AddySupport💥 "
    elif 40 <= Addy < 45:
        bar = " 🔥@AddyUpdate🔥 "
    elif 45 < Addy < 50:
        bar = " 💥@AddySupport💥 "
    elif 50 <= Addy < 55:
        bar = " 🔥@AddyUpdate🔥 "
    elif 55 <= Addy < 60:
        bar = " 🥀@OfficialAddy🥀 "
    elif 60 <= Addy < 65:
        bar = " 💥@AddySupport💥 "
    elif 65 <= Addy < 70:
        bar = " 🔥@AddyUpdate🔥 "
    elif 70 <= Addy < 75:
        bar = " 🥀@OfficialAddy🥀 "
    elif 75 <= Addy < 80:
        bar = " 💥@AddySupport💥 "
    elif 80 <= Addy < 85:
        bar = " 🔥@AddyUpdate🔥 "
    elif 85 <= Addy < 90:
        bar = " 💥@AddySupport💥 "
    elif 90 <= Addy < 92:
        bar = " 🔥@AddyUpdate🔥 "
    elif 92 <= Addy < 94:
        bar = " 🥀@OfficialAddy🥀 "
    elif 94 <= Addy < 95:
        bar = " 💥@AddySupport💥 "
    elif 95 <= Addy < 96:
        bar = " 🔥@AddyUpdate🔥 "
    elif 96 <= Addy < 97:
        bar = " 🥀@OfficialAddy🥀 "
    else:
        bar = " 🎸🎸🎸🎸🎸 "
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["PL_B_2"],
                callback_data=f"add_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{SUPPORT_GROUP}"
            ),
        ],
    ]
    return buttons


def telegram_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    Addy = math.floor(percentage)
    if 0 < Addy <= 5:
        bar = " 🥀@OfficialAddy🥀 "
    elif 5 < Addy < 10:
        bar = " 💥@AddySupport💥 "
    elif 10 <= Addy < 15:
        bar = " 🔥@AddyUpdate🔥 "
    elif 15 <= Addy < 20:
        bar = " 🥀@OfficialAddy🥀 "
    elif 20 <= Addy < 25:
        bar = " 💥@AddySupport💥 "
    elif 25 <= Addy < 30:
        bar = " 🔥@AddyUpdate🔥 "
    elif 30 <= Addy < 35:
        bar = " 🥀@OfficialAddy🥀 "
    elif 35 <= Addy < 40:
        bar = " 💥@AddySupport💥 "
    elif 40 <= Addy < 45:
        bar = " 🔥@AddyUpdate🔥 "
    elif 45 < Addy < 50:
        bar = " 💥@AddySupport💥 "
    elif 50 <= Addy < 55:
        bar = " 🔥@AddyUpdate🔥 "
    elif 55 <= Addy < 60:
        bar = " 🥀@OfficialAddy🥀 "
    elif 60 <= Addy < 65:
        bar = " 💥@AddySupport💥 "
    elif 65 <= Addy < 70:
        bar = " 🔥@AddyUpdate🔥 "
    elif 70 <= Addy < 75:
        bar = " 🥀@OfficialAddy🥀 "
    elif 75 <= Addy < 80:
        bar = " 💥@AddySupport💥 "
    elif 80 <= Addy < 85:
        bar = " 🔥@AddyUpdate🔥 "
    elif 85 <= Addy < 90:
        bar = " 💥@AddySupport💥 "
    elif 90 <= Addy < 92:
        bar = " 🔥@AddyUpdate🔥 "
    elif 92 <= Addy < 94:
        bar = " 🥀@OfficialAddy🥀 "
    elif 94 <= Addy < 95:
        bar = " 💥@AddySupport💥 "
    elif 95 <= Addy < 96:
        bar = " 🔥@AddyUpdate🔥 "
    elif 96 <= Addy < 97:
        bar = " 🥀@OfficialAddy🥀 "
    else:
        bar = " 🎸🎸🎸🎸🎸 "

    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["PL_B_2"],
                callback_data=f"add_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{SUPPORT_GROUP}"
            ),
        ],
    ]
    return buttons


def stream_markup(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{SUPPORT_GROUP}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="✯ Close ✯", callback_data=f"close"
            )
        ],
    ]
    return buttons


def telegram_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{SUPPORT_GROUP}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="✯ Close ✯", callback_data=f"close"
            )
        ],
    ]
    return buttons


## Search Query Inline


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{SUPPORT_GROUP}"
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons

## Live Stream Markup


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{config.SUPPORT_GROUP}",
            ),
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ]
    ]
    return buttons

## wtf

def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"AddyPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"AddyPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{config.SUPPORT_GROUP}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


## Slider Query Markup


def slider_markup(
    _, videoid, user_id, query, query_type, channel, fplay
):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{SUPPORT_GROUP}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="▷",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons

## Extra Shit

close_keyboard = InlineKeyboardMarkup( 
            [
                [
                    InlineKeyboardButton(
                        text="✯ Close ✯", callback_data="close"
                    )
                ]    
            ]
        )


## Queue Markup

def queue_markup(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{app.username}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="II", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="▢", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [  
            InlineKeyboardButton(
                text=_["PL_B_2"],
                callback_data=f"add_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{SUPPORT_GROUP}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="✯ Close ✯", callback_data=f"close"
            )
        ],
    ]
    return buttons
