import os
import time
from asyncio import sleep
from pyrogram import Client, filters
from pyrogram import enums, filters
from strings.filters import command
from Almortagel import app
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.enums import ChatMemberStatus

@app.on_message(filters.command(["المالك","المنشئ"], ""))
def owner(app, message):
  for owner in app.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
    if owner.status == enums.ChatMemberStatus.OWNER:
      saidi = app.get_users(owner.user.id)
      ALMORTAGEL = InlineKeyboardMarkup([[InlineKeyboardButton(saidi.first_name, url=f"https://t.me/{saidi.username}")]])
      for x in app.get_chat_photos(saidi.id, limit=1):
        photo = x.file_id
      message.reply_photo(photo,caption=f"𝅄 𓏺 𝙾𝚆𝙽𝙴𝚁 𝖭𝖺𝗆𝖾 : {saidi.first_name}\n𝅄 𓏺 𝙾𝚆𝙽𝙴𝚁 𝚄𝚂𝙴𝚁 : @{saidi.username}\n𝅄 𓏺 𝙾𝚆𝙽𝙴𝚁 𝗂𝖽 : {saidi.id}",reply_markup=ALMORTAGEL,quote=True)


import asyncio
import os
import time
import requests
import random
from pyrogram import enums
import aiohttp
from pyrogram import filters
from pyrogram import Client
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from Almortagel import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from Almortagel import app
from strings.filters import command
from telegraph import upload_file
from asyncio import gather
from pyrogram.errors import FloodWait



iddof = []
@app.on_message(filters.command(["قفل الايدي", "تعطيل الايدي"]), group=2272)
async def iddlock(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
      if message.chat.id in iddof:
        return await message.reply_text("تم معطل من قبل🔒")
      iddof.append(message.chat.id)
      return await message.reply_text("تم تعطيل الايدي بنجاح ✅🔒")
   else:
      return await message.reply_text("لازم تكون ادمن يشخه علشان اسمع كلامك")

@app.on_message(filters.command(["فتح الايدي", "تفعيل الايدي"]), group=2292)
async def iddopen(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
      if not message.chat.id in iddof:
        return await message.reply_text("الايدي مفعل من قبل ✅")
      iddof.remove(message.chat.id)
      return await message.reply_text("تم فتح الايدي بنجاح ✅🔓")
   else:
      return await message.reply_text("لازم تكون ادمن يشخه علشان اسمع كلامك")




@app.on_message(filters.command(["ايدي","الايدي","ا"]), group=27722)
async def iddd(client, message):
    if message.chat.id in iddof:
      return
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"""**⤄الاسم: {message.from_user.mention}\n⤄اليوزر: @{message.from_user.username}\n⤄ايدي:`{message.from_user.id}`\nʙɪᴏᚐ: {usr.bio}\n⤄جروب: {message.chat.title}\n⤄ايدي الجروب : `{message.chat.id}`**""", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        ),
    )    



idbof = []
@app.on_message(filters.command(["قفل جمالي", "تعطيل جمالي"], "")
& filters.group
)
async def iddlock(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
      if message.chat.id in idbof:
        return await message.reply_text("جمالي معطل من قبل✅")
      iddof.append(message.chat.id)
      return await message.reply_text(" تم تعطيل جمالي بنجاح✅🔒")
   else:
      return await message.reply_text("لازم تكون ادمن يشخه علشان اسمع كلامك")

@app.on_message(filters.command(["قفل جمالي", "تعطيل جمالي"], "")
& filters.group
)
async def iddlock(client, message):
   get = await client.get_chat_member(message.chat.id, message.from_user.id)
   if get.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
      if message.chat.id in idbof:
        return await message.reply_text("جمالي مفعل من قبل✅")
      iddof.remove(message.chat.id)
      return await message.reply_text("تم فتح جمالي بنجاح ✅🔓")
   else:
      return await message.reply_text("لازم تكون ادمن يشخه علشان اسمع كلامك")




@app.on_message(filters.command(["جمالي","جمالو","ج"], "")
& filters.group
)
async def iddyyyd(client, message):
    if message.chat.id in idbof:
      return
    usr = await client.get_chat(message.from_user.id)
    name = usr.first_name
    i = ["0","10", "15","20", "25","30","35", "40","45", "50","55", "60"," 66", "70","77", "80","85", "90","99", "100","1000" ]
    ik = random.choice(i)
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"نسبه جمالك يا مز انت \n│ \n└ʙʏ: {ik} %😂🥀❄️", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        ),
    )
       


@app.on_message(filters.command(["اسمي"], "")
& filters.group
)
async def vgdg(client: Client, message: Message):
    await message.reply_text(
        f"""🥀❄️ اسمك »»  `{message.from_user.mention}`""") 


