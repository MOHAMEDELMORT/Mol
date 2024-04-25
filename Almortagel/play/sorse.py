import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from Almortagel import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from Almortagel import app
from random import  choice, randint

@app.on_message(
    filters.command(["سورس مين","سورس","السورس","سورسي", "Almortagel"], ""))
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/14c7948ad180050fe16e4.jpg",
        caption=f"""Welcome to ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                text="𝚂𝙾𝚄𝚁𝙲𝙴⁩", url=f"https://t.me/AlmortagelTech"
                        ),
           InlineKeyboardButton(
                text="𝙶𝚁𝙾𝚄𝙿", url=f"https://t.me/AlmortagelTech2"
            ),
        ],
        [
            InlineKeyboardButton(
                text="✯ᴍʀ ᴇʟᴍᴏʀᴛᴀɢᴇʟ✯", url=f"https://t.me/Almortagel_12"
            ),
  
                ],

            ]

        ),

    )


@app.on_message(filters.command(["غنيلي", "غني", "غ", "🎙 ¦ غـنيـلي"], ""))
async def ihd(client: Client, message: Message):
    rl = random.randint(3,267)
    url = f"https://t.me/bsmaatt/{rl}"
    await client.send_voice(message.chat.id,url,caption="🔥 ¦ تـم اختيـار الاغـنـية لـك",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
                           )
