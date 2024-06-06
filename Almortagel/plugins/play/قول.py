import asyncio
from pyrogram import Client, filters
from random import choice
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,
                            InlineKeyboardMarkup, Message)
from Almortagel import app
from typing import Union
from pyrogram.types import InlineKeyboardButton

RAEAK = ["زينه","حلوه","فخمه","جميله","خوش","انيقه","مو حلوه","بشعه","مو زينه","كلش حلوه","استمر بيها","احبها","غيرها حباب"]

@app.on_message(
    command(["رأيك","رأيك بصورتي","شون صورتي"])
    & ~filters.edited
)
async def madison(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""صورتك {choice(RAEAK)} 🧸♥️""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        ),
    )



GMALY = ["1","15","89","88","67","13","44","17","35","78","11","12","13","14","15","16","17","10","20","30","35","75","34","66","82","23","19","55","80","63","32","27","89","99","98","79","100","8","3","6","0"]

@app.on_message(
    command(["نسبه جمالي","جمالي","حلاوتي"])
    & ~filters.edited
)
async def madison(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""نسبه جمالك هيا {choice(GMALY)}% 🙄❤️""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        ),
    )
