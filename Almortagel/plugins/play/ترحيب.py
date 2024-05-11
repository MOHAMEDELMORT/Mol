import asyncio
import random
import datetime
from Almortagel import app
from pyrogram import Client
from pyrogram import filters
from Almortagel.utils.database import get_served_chats
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


START_IMG_URL = "https://telegra.ph/file/0677e881a84925cb9c789.jpg"


MESSAGE = f"""- بوت تشغيل اذاعه القران  الكريم  بالقنوات والقروبات 

وبدون تهنيج او تقطيع او توقف وكمان ان البوت في مميزات جامدة⚡️♥️.

ارفع البوت ادمن فقناتك او جروبك واستمتع بجوده الصوت و السرعه الخياليه للبوت ⚡️♥️

معرف البوت 🎸 [ @{app.username} ]

➤ 𝘉𝘰𝘵 𝘵𝘰 𝘱𝘭𝘢𝘺 𝘴𝘰𝘯𝘨𝘴 𝘪𝘯 𝘷𝘰𝘪𝘤e 𝘤𝘩𝘢𝘵 ♩🎸 \n\n-𝙱𝙾𝚃 ➤ @{app.username}"""


BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("خدني لجروبك والنبي🥺♥",url=f"https://t.me/{app.username}?startgroup=True")
        ]
    ]
)

    async for photo in client.get_chat_photos("me", limit=1):
                    await message.reply_photo(photo.file_id, caption=MESSAGE, reply_markup=BUTTON)



almortagel_responses = [
    f"""- اقوي بوت ميوزك قنوات و جروبات سرعه وجوده خارقه\n\nوبدون تهنيج او تقطيع او توقف وكمان ان البوت في مميزات جامدة⚡️♥️.\n\nارفع البوت ادمن فقناتك او جروبك واستمتع بجوده الصوت و السرعه الخياليه للبوت ⚡️♥️\n\n
 معرف البوت 🎸 [@{app.username}]\n\n➤ 𝘉𝘰𝘵 𝘵𝘰 𝘱𝘭𝘢𝘺 𝘴𝘰𝘯𝘨𝘴 𝘪𝘯 𝘷𝘰𝘪𝘤e 𝘤𝘩𝘢𝘵 ♩🎸 \n\n-𝙱𝙾𝚃 ➤ @{app.username}"""
       
]

@app.on_message(filters.command(["ترند"], ""), group=39)
async def almortagel_bot(client, message):
    global name
    bot_username = (await app.get_me()).username
    bar = random.choice(almortagel_responses)
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("خدني لجروبك والنبي🥺♥", url=f"https://t.me/{bot_username}?startgroup=True")]
    ])

    await message.reply(
        f"{bar}",
        reply_markup=keyboard
    )
