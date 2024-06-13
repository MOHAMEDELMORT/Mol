import asyncio
import os
import enums
from pyrogram import Client, filters
from random import choice
from pyrogram import filters
from config import BANNED_USERS
from Almortagel import (Apple, Resso, Spotify, Telegram, YouTube, app)
from typing import Union
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, Message, ChatJoinRequest


@app.on_message(filters.regex("^/start"), group=39)
async def start(client, message):      
  username = client.me.username
  if os.path.isfile(f"{username}.jpg"):
    photo = f"{username}.jpg"
  else:
    bot = await client.get_me()
    if not bot.photo:
       button = [[InlineKeyboardButton(text="ᴇɴɢʟɪѕʜ 🇺🇲", callback_data=f"english"), InlineKeyboardButton(text="عربي 🇪🇬", callback_data=f"arbic")], [InlineKeyboardButton(text=f"{OWNER_NAME}", user_id=config.OWNER_ID)]]
       return await client.send_message(message.chat.id, "ѕᴇʟᴇᴄᴛ ʏᴏụʀ ʟᴀɴɢụᴀɢᴇ •", reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(button))
    photo = bot.photo.big_file_id
    photo = await client.download_media(photo)
    username = client.me.username
    photo = await gen_bot(client, username, photo)
  button = [[InlineKeyboardButton(text="ᴇɴɢʟɪѕʜ 🇺🇲", callback_data=f"english"), InlineKeyboardButton(text="عربي 🇪🇬", callback_data=f"arbic")], [InlineKeyboardButton(text=f"{OWNER_NAME}", user_id=config.OWNER_ID)]]
  await client.send_photo(message.chat.id, photo=photo, caption="الرجاء الضغط علي اللغة اذا كانت اللغة العربية او باللغة الانجلزية\n\nᴘʟᴇᴀѕᴇ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʟᴀɴɢụᴀɢᴇ ɪғ ɪᴛ ɪѕ ᴀʀᴀʙɪᴄ ᴏʀ ᴇɴɢʟɪѕʜ", reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(button))
  

############//((/start))//############
@Client.on_message(filters.command("قسم التفعيل والتعطيل", ""))
async def helpercn(client, message):
   bot_username = client.me.username
   dev = await get_dev(bot_username)
   userbot = await get_userbot(bot_username)
   me = userbot.me
   if message.chat.id == dev or message.chat.username in OWNER:
    kep = ReplyKeyboardMarkup([
["تعطيل التواصل","تفعيل التواصل"],
["تعطيل سجل التشغيل","تفعيل سجل التشغيل"],
["تعطيل الاشتراك","تفعيل الاشتراك"],
["رجوع للقائمة الرئيسيه"]], resize_keyboard=True)
    await message.reply_text(f"**• مرحبا بك في قسم ⟨ التفعيل والتعطيل ⟩ 🚦 .**", reply_markup=kep,quote=True)

@Client.on_message(filters.command(["قسم التعيين"], ""))
async def cast(client: Client, message):
   bot_username = client.me.username
   dev = await get_dev(bot_username)
   if message.chat.id == dev or message.chat.username in OWNER:
    kep = ReplyKeyboardMarkup([
["تعين اسم البوت"],
["تعين قناة البوت","تعين مجموعة البوت"],
["تعين قناة السورس","تعين مجموعة السورس"],
["تعين لوجو السورس","تعين يوزر مطور السورس"], 
["رجوع للقائمة الرئيسيه"]], resize_keyboard=True)
    await message.reply_text("**• مرحبا بك في قسم ⟨ التعيين ⟩ ⚡ .**", reply_markup=kep)

@Client.on_message(filters.command("قسم البوت", ""))
async def Zo_Mbi_e(client, message):
  bot_username = client.me.username
  dev = await get_dev(bot_username)
  chat = message.chat.id
  uesr = message.chat.username
  if chat == dev or uesr in OWNER:
    kep = ReplyKeyboardMarkup([
["الاحصائيات","المكالمات النشطه"],
["المجموعات","المستخدمين"],
["تغير مكان سجل التشغيل"],
["رجوع للقائمة الرئيسيه"]], resize_keyboard=True)
    await message.reply_text(f"**• مرحبا بك في قسم ⟨ البوت ⟩  • .**", reply_markup=kep,quote=True) 
