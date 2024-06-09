from typing import Union
import asyncio
import os
import requests
import pyrogram
from pyrogram import Client, filters, emoji
from strings.filters import command
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
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
                    InlineKeyboardButton("اوامر الجروبات", callback_data="gr"),
                    InlineKeyboardButton("اوامر القنوات", callback_data="ch"),  
                 ],[
                    InlineKeyboardButton("اوامر الادمن", callback_data="adm"), 
                ],[
                    InlineKeyboardButton("★ ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ⚡", url=f"https://t.me/AlmortagelTech"),
                ],

            ]

        ),

    )

    



@Client.on_callback_query(filters.regex("gr"))
async def gr(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>⌯ ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ</b>
<b>★¦ اهلا بك عزيزي في قسم اوامر التشغيل في الجروبات</b>
<b>★¦ تشغيل + اسم الاغنيه</b>
★¦ فديو + اسم الاغنيه</b>
<b>★¦ #فيديو + اسم الاغنيه</b>
<b>★¦ #فديو + اسم الاغنيه</b>
<b>★¦ {NAME_BOT} + اسم الاغنيه</b>
<b>★¦ /فيديو + اسم الاغنيه</b>
<b>★¦ /ق شغل + اسم الاغنيه</b>
<b>★¦ /تشغيل + اسم الاغنيه</b>
<b>★¦ cvplay + اسم الاغنيه</b>
<b>★¦ cplay + اسم الاغنيه</b>
<b>★¦ /vplay + اسم الاغنيه</b>
<b>★¦ /play + اسم الاغنيه</b>
<b>★¦ #تشغيل + اسم الاغنيه</b>
<b>★¦ فيديو + اسم الاغنيه</b>
<b>★¦ سورة + اسم السورة</b> 
<b>★¦ cvplayforce + اسم الاغنيه</b>
<b>★¦ cplayforce + اسم الاغنيه</b>
<b>★¦ vplayforce + اسم الاغنيه</b>
<b>★¦ playforce + اسم الاغنيه</b>
<b>★¦ /cvplay + اسم الاغنيه</b>
<b>★¦ vplay + اسم الاغنيه</b>
<b>★¦ play + اسم الاغنيه</b>

<b>ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ</b>""",
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

@Client.on_callback_query(filters.regex("ch"))
async def ch(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ</b>
<b>★¦ اهلا بك عزيزي في قسم اوامر التشغيل في القنوات</b>
<b>★¦ شغل + اسم الاغنيه</b>
<b>★¦ قناه + اسم الاغنيه</b>
<b>★¦ مانو + اسم الاغنيه</b>
<b>★¦ ق + اسم الاغنيه</b>
<b>★¦ اغاني + اسم الاغنيه</b>
<b>★¦ . + اسم الاغنيه</b>
<b>★¦ / + اسم الاغنيه</b>
<b>ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ</b>""",
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

@Client.on_callback_query(filters.regex("adm"))
async def adm(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""** ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ**
<b>★¦ اهلا بك عزيزي في قسم اوامر تشغيل الادمن</b>
<b>★¦ رفع ثانوي</b>
★¦ تنزيل ثانوي
<b>★¦ قائمة الثانويين</b>
<b>★¦ رفع ادمن</b>
<b>★¦ تنزيل ادمن</b>
<b>★¦ قائمة الادمن</b>
<b>★¦ حظر</b>
<b>★¦ الغاء الحظر</b>
<b>★¦ المحظورين</b>
<b>★¦ حظر عام</b>
<b>★¦ الغاء الحظر العام</b>
<b>★¦ المحظورين عام</b>
<b>★¦ اونلاين</b>
<b>★¦ اذاعه</b>
<b>★¦ تحديث</b>
<b>★¦ logger</b>
<b>★¦ ريلود</b>
<b>★¦ وقف</b>
<b>★¦ كمل</b>
<b>★¦ اسكت</b>
<b>★¦ اتكلم</b>
<b>★¦ ايقاف</b>
<b>★¦ تخطي</b>
<b>★¦ @all</b>
<b>★¦ all stop</b>
<b>★¦ يوتيوب / تنزيل</b>
<b>★¦ playing</b>
<b>★¦ القائمه</b>
<b>★¦ حذف القائمه</b>
<b>★¦ تحديث</b>
<b>★¦ الاحصائيات</b>
<b>★¦ لايف</b>
<b>★¦ مساعده</b>
<b>★¦ الاعدادت</b>
<b>★¦ بينج</b>
<b>ѕᴏụʀᴄᴇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ</b>""",
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

    
@Client.on_callback_query(filters.regex("back"))
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
