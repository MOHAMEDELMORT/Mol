from typing import Union
from pyrogram.types import InlineKeyboardButton

import config
from Almortagel import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="عربي 🇪🇬",
                callback_data=f"arbic",
            ),
            InlineKeyboardButton(
                text="English 🇺🇲",
                callback_data=f"english",
            ),
        ],
        [
            InlineKeyboardButton(text="{OWNER_NAME}", user_id=config.OWNER_ID),
        ],
    ]
    return buttons