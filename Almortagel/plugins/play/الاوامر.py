import asyncio
import os
from pyrogram.types import CallbackQuery
from Almortagel import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from Almortagel import app
import requests
import pyrogram
from pyrogram import Client, emoji 
from config import *
from pyrogram import filters
from strings.filters import command
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified



@app.on_message(filters.command(["الاوامر"], ""))
async def almortagel_source(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/14c7948ad180050fe16e4.jpg",
        caption=f"""** ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ**\nمرحبا بك عزيزي {message.from_user.mention}\nهذا قسم الاوامر الخاص بسورس زد إي \nلمعرفة الاوامر اضغط على الأزرار بالأسفل👇\n** ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "اوامر الجروبات", callback_data="gr"),
                    InlineKeyboardButton(
                        "اوامر القنوات", callback_data="ch"),  
                 ],[
                    InlineKeyboardButton(
                        "اوامر الادمن", callback_data="adm"), 
                ],[
                
                    InlineKeyboardButton(
                        "★ ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ⚡", url=f"https://t.me/VVHH9"),
                ],

            ]

        ),

    )

    
@app.on_callback_query(filters.regex("gr"))
async def almortagel_usage(_, callback_query: CallbackQuery):
    await callback_query.message.edit_text(
        text="""**⌯ ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ**
★¦ اهلا بك عزيزي في قسم اوامر التشغيل في الجروبات
★¦ تشغيل + اسم الاغنيه
★¦ فديو + اسم الاغنيه
★¦ #فيديو + اسم الاغنيه
★¦ #فديو + اسم الاغنيه
★¦ {NAME_BOT} + اسم الاغنيه
★¦ /فيديو + اسم الاغنيه
★¦ /ق شغل + اسم الاغنيه
★¦ /تشغيل + اسم الاغنيه
★¦ cvplay + اسم الاغنيه
★¦ cplay + اسم الاغنيه
★¦ /vplay + اسم الاغنيه
★¦ /play + اسم الاغنيه
★¦ #تشغيل + اسم الاغنيه
★¦ فيديو + اسم الاغنيه
★¦ سورة + اسم السورة 
★¦ cvplayforce + اسم الاغنيه
★¦ cplayforce + اسم الاغنيه
★¦ vplayforce + اسم الاغنيه
★¦ playforce + اسم الاغنيه
★¦ /cvplay + اسم الاغنيه
★¦ vplay + اسم الاغنيه
★¦ play + اسم الاغنيه

**⌯ ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "التالي", callback_data="ch"), 
                    
                ],[
                    InlineKeyboardButton(
                        "الرئيسية", callback_data="back"), 
                    
                ]
            ]
        )
    )

@app.on_callback_query(filters.regex("ch"))
async def almortagel_usage(_, callback_query: CallbackQuery):
    await callback_query.message.reply_text(
        text="""** ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ**
★¦ اهلا بك عزيزي في قسم اوامر التشغيل في القنوات
★¦ شغل + اسم الاغنيه
★¦ قناه + اسم الاغنيه
★¦ مانو + اسم الاغنيه
★¦ ق + اسم الاغنيه
★¦ اغاني + اسم الاغنيه
★¦ . + اسم الاغنيه
★¦ / + اسم الاغنيه
** ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "التالي", callback_data="adm"), 
                    InlineKeyboardButton(
                        "العودة", callback_data="gr"), 
                ],[
                    InlineKeyboardButton(
                        "الرئيسية", callback_data="back"), 
                    
                ]
            ]
        )
    )

@app.on_callback_query(filters.regex("adm"))
async def almortagel_usage(_, callback_query: CallbackQuery):
    await callback_query.message.reply_text(
        text="""** ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ**
★¦ اهلا بك عزيزي في قسم اوامر تشغيل الادمن
★¦ رفع ثانوي
★¦ تنزيل ثانوي
★¦ قائمة الثانويين
★¦ رفع ادمن
★¦ تنزيل ادمن
★¦ قائمة الادمن
★¦ حظر
★¦ الغاء الحظر
★¦ المحظورين
★¦ حظر عام
★¦ الغاء الحظر العام
★¦ المحظورين عام
★¦ اونلاين
★¦ اذاعه
★¦ تحديث
★¦ logger
★¦ ريلود
★¦ وقف
★¦ كمل
★¦ اسكت
★¦ اتكلم
★¦ ايقاف
★¦ تخطي
★¦ @all
★¦ all stop
★¦ يوتيوب / تنزيل
★¦ playing
★¦ القائمه
★¦ حذف القائمه
★¦ تحديث
★¦ الاحصائيات
★¦ لايف
★¦ مساعده
★¦ الاعدادت
★¦ بينج

** ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "التالي", callback_data="gr"), 
                    InlineKeyboardButton(
                        "العودة", callback_data="ch"), 
                ],[
                    InlineKeyboardButton(
                        "الرئيسية", callback_data="back"), 
                    
                ]
            ]
        )
    )

    
@app.on_callback_query(filters.regex("back"))
async def almortagel_back(_, callback_query: CallbackQuery):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/14c7948ad180050fe16e4.jpg",
        caption=f"""** ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ**\nمرحبا بك عزيزي {message.from_user.mention}\nهذا قسم الاوامر الخاص بسورس زد إي \nلمعرفة الاوامر اضغط على الأزرار بالأسفل👇\n** ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "اوامر الجروبات", callback_data="gr"),
                    InlineKeyboardButton(
                        "اوامر القنوات", callback_data="ch"),  
                 ],[
                    InlineKeyboardButton(
                        "اوامر الادمن", callback_data="adm"), 
                ],[
                
                    InlineKeyboardButton(
                        "★ ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ⚡", url=f"https://t.me/AlmortagelTech"),
                ],

            ]

        ),

    )




@app.on_message(filters.command("تف", "") & filters.group & filters.reply)
def Almortagel(c, message):
  ID_BOT = app.id
  first_name = message.reply_to_message.from_user.first_name
  id = message.reply_to_message.from_user.id
  if id == OWNER_ID:
    return message.reply("• لا يمكنك التف علي المطور ❤️✌️")
  if id == ID_BOT:
    return message.reply("• عاوزني اتف علي نفسي يعبيط 😂")
  if id == DEVELOPERS:
    return message.reply("• لا يمكنك التف علي مطورين السورس 🧑‍✈️")
  Text =f"""
• تم التف علي هذا الشخص

※ بواسطة {first_name}

 اععع اي القرف ده 🤢
"""
  Almortagel = InlineKeyboardMarkup([[InlineKeyboardButton("اضف البوت الي مجموعتك او قناتك 🎸", url=f"https://t.me/{app.username}?startgroup=true"),]])
  message.reply_video("https://te.legra.ph/file/7eca3719e7cfa2e6bc9e3.mp4",caption=Text,reply_markup=Almortagel)

@app.on_message(filters.command("تخ", "") & filters.group & filters.reply)
def Almortagel(c, message):
  ID_BOT = app.id
  first_name = message.reply_to_message.from_user.first_name
  id = message.reply_to_message.from_user.id
  if id == OWNER_ID:
    return message.reply("• لا يمكنك قتل المطور ❤️✌️")
  if id == ID_BOT:
    return message.reply("• عاوزني اقتل نفسي 😂")
  if id == DEVELOPERS:
    return message.reply("• لا يمكنك قتل مطورين السورس 🧑‍✈️")
  Text =f"""
• تم قتل هذا الشخص

※ بواسطة {first_name}

 ان لله وان اليه راجعون ⚰😭
"""
  Almortagel = InlineKeyboardMarkup([[InlineKeyboardButton("اضف البوت الي مجموعتك او قناتك 🎸", url=f"https://t.me/{app.username}?startgroup=true"),]])
  message.reply_video("https://te.legra.ph/file/163a38872a6c0d44d1c57.mp4",caption=Text,reply_markup=Almortagel)
