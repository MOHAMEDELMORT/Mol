from typing import Union
import asyncio
import os
import requests
import pyrogram
from pyrogram import Client, filters, emoji
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified
from Almortagel import app as Client
from Almortagel import app


@Client.on_message(filters.command(["الاوامر"], ""))
async def almortagel(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/14c7948ad180050fe16e4.jpg",
        caption=f"""** ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ**\nمرحبا بك عزيزي {message.from_user.mention}\nهذا قسم الاوامر الخاص بسورس المرتجل \nلمعرفة الاوامر اضغط على الأزرار بالأسفل👇\n** ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ**""",
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

    


import asyncio
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import InlineKeyboardButton, CallbackQuery, InlineKeyboardMarkup, Message
from typing import Union
from pyrogram.types import InlineKeyboardButton
from Almortagel import app
from Almortagel.misc import HAPP, SUDOERS, XCB
from config import OWNER_ID
from pyrogram import filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from Almortagel import app as Client
  
                          
@Client.on_callback_query(filters.regex("gr") & SUDOERS)
async def gr(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**⌯ ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ**
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
        ),
    )

@Client.on_callback_query(filters.regex("ch") & SUDOERS)
async def ch(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""** ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ**
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
        ),
    )

@Client.on_callback_query(filters.regex("adm") & SUDOERS)
async def adm(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""** ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ**
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
        ),
    )

    
@Client.on_callback_query(filters.regex("back") & SUDOERS)
async def back(_, query: CallbackQuery):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/14c7948ad180050fe16e4.jpg",
        caption=f"""** ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ**\nمرحبا بك عزيزي {message.from_user.mention}\nهذا قسم الاوامر الخاص بسورس المرتجل \nلمعرفة الاوامر اضغط على الأزرار بالأسفل👇\n** ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ**""",
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
