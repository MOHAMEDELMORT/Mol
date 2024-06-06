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


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
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
                    InlineKeyboardButton(text=_["S_B_10"], url=f"https://t.me/ALMORTAGEL_12"),
            InlineKeyboardButton(text=_["S_B_5"], user_id=config.OWNER_ID),
        ],
    ]
    return buttons