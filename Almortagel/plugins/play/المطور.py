from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from strings.filters import command
from Almortagel import app
import config

@app.on_message(
    command(["مطور البوت"])
)
async def maker(client: Client, message: Message):
    await message.reply_text(text="""مرحبا بكمرحبا بك عزيزي {message.from_user.mention} \nللتحدث مع مطور البوت اضغط علي الازرار بالاسفل👇\n**⩹━★⊷━⌞ ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ ⌝━⊶★━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "- مطور البوت .", url=f"tg://openmessage?user_id={config.OWNER_ID}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "- قناة البوت . ", url=config.SUPPORT_CHAT
                    ),
                ],
            ]
        ),
    )


