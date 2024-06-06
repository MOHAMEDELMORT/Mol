from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from strings.filters import command
from config import OWNER_NAME
from Almortagel import app
import config

@app.on_message(
    command(["المطور"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/14c7948ad180050fe16e4.jpg",
        caption=f"""**⩹━★⊷━⌞ ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ ⌝━⊶★━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم المطور\nللتحدث مع مطور البوت اضغط علي الازرار بالاسفل👇\n**⩹━★⊷━⌞ ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ ⌝━⊶★━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                   InlineKeyboardButton(text=f"{OWNER_NAME}", user_id=config.OWNER_ID),
                ],

            ]

        ),

    )
