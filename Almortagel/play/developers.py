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

#          
                
@app.on_message(
    filters.command(["المبرمج","المرتجل","مبرمج السورس","المطور مرتجل"], "")
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/14c7948ad180050fe16e4.jpg",
        caption=f"""**⩹━★⊷━⌞ ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ ⌝━⊶★━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم المبرمج\nللتحدث مع السورس السورس اضغط علي الازرار بالاسفل👇\n**⩹━★⊷━⌞ ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ ⌝━⊶★━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᯓ 𓆩 ˹ ᴍʀ ᴇʟᴍᴏʀᴛᴀɢᴇʟ ˼⍣⃝🇪🇬𓆪𓆃", url=f"https://t.me/ALMORTAGEL_12"), 
                 ],[
                   InlineKeyboardButton(
                        "★⌞ ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ ⌝⚡", url=f"https://t.me/AlmortagelTech"),
                ],

            ]

        ),

    )
