import asyncio
import random
from Almortagel.misc import SUDOERS
from pyrogram.types import (Message,InlineKeyboardButton,InlineKeyboardMarkup,CallbackQuery,ChatPrivileges)
from pyrogram import filters, Client
from Almortagel import app
from config import *

bot_name = {}
botname = {}

name = "المرتجل"

@@Client.on_message(filters.command(": تغير اسم المستخدم :", ""))
async def changeusername(client: Client, message):
  bot_username = client.me.username
  dev = await get_dev(bot_username)
  if message.chat.id == dev or message.chat.username in OWNER:
   try:
    name = await client.ask(message.chat.id, ": ارسل الان اسم المستخدم الجديد :")
    name = name.text
    client = await get_userbot(bot_username)
    await client.set_username(name)
    await message.reply_text("**تم تغير اسم المستخدم بنجاح ..**")


almortagel_responses = [
    "اسمي {name} يصحبي",
    "يسطا قولتلك اسمي {name} الاه",
    "نعم يحب",
    "قول يقلبو",
    "يسطا هوا عشان بحبك تصعدني؟",
    "يعم والله بحبك بس ناديلي ب {name}",
    "تعرف بالله هحبك أكتر لو ناديتلي {name}",
    "اي ي معلم مين مزعلك",
    "متصلي على النبي كدا",
    "مش فاضيلك نصايح وكلمني",
    "يسطا قولي مين مزعلك وعايزك تقعد وتتفرج على أخوك",
    "انجز عايزني أشقطلك مين؟",
    "شكلها منكدا عليك وجاي تطلعهم علينا",
    "ورحمة أبويا اسمي {name}",
]

@app.on_message(filters.command(["بوت", "البوت"], ""))
async def almortagel_bot(client, message):
    global name
    bot_username = (await app.get_me()).username
    bar = random.choice(almortagel_responses).format(name=name)
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("خدني لجروبك والنبي🥺♥", url=f"https://t.me/{bot_username}?startgroup=True")]
    ])

    await message.reply_text(
       text=f"[{bar}](https://t.me/{bot_username}?startgroup=True)",
       disable_web_page_preview=True,
        reply_markup=keyboard
    )