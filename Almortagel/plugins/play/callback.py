from pyrogram import filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from Almortagel import app as Client
from Almortagel import app
import config
from config import OWNER_NAME


@Client.on_callback_query(filters.regex("arbic"))
async def arbic(_, query: CallbackQuery):
    await query.answer("home start")
    await query.edit_message_text(
        f""" 🐰**[مرحبا بك] [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) ! \n
※ [انا بوت تشغيل الأغاني والفيديو  في المكالمه المرئية](https://t.me/AlmortagelTech) \n
※ [في حال مواجهه اي مشكله انضم هنا](https://t.me/AlmortagelTech)\n [ᖴ᥆ᖇ ᴀʟᴍᴏʀᴛᴀɢᴇʟ. 🐰](https://t.me/AlmortagelTech)
※ [استخدم الازرار لمعرفه الاوامر المستخدمه.](https://t.me/AlmortagelTech) """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "اضف البوت اللي مجموعتك ",
                        url=f"https://t.me/{app.username}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("الدعم والتواصل", url=f"https://t.me/AlmortagelTech2"),
                
InlineKeyboardButton("لتفعيل كيبورد الاعضاء", callback_data="afyona"),
                ],
                [                   InlineKeyboardButton("طريقة التشغيل", callback_data="bcmds"),
                    InlineKeyboardButton("طريقة التفعيل", callback_data="Afyon"),
                ],
                [
                    InlineKeyboardButton(
                        "الجروب", url=f"https://t.me/AlmortagelTech2"
                    ),
                    InlineKeyboardButton(
                        "القناة", url=f"https://t.me/AlmortagelTech"
                    ),
                ],
                [
                    InlineKeyboardButton(text=f"{OWNER_NAME}", user_id=config.OWNER_ID
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )

@Client.on_callback_query(filters.regex("english"))
async def english(_, query: CallbackQuery):
    await query.answer("home start")
    await query.edit_message_text(
        f" [※A Telegram Music Bot Based Mongodb](https://t.me/AlmortagelTech) \n ※[Add Me To Ur Chat For and Help and And Support Click On Buttons](https://t.me/AlmortagelTech) \n ※[These Features AI Based](https://t.me/AlmortagelTech)",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Add me to your Group ",
                        url=f"https://t.me/{app.username}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton(" Basic Guide", callback_data="cAfyon"),
                
InlineKeyboardButton(" member keyboard ", callback_data="Almortagel12"),
                ],
                [                
                    InlineKeyboardButton(" Commands", callback_data="cbcmds"),
                    InlineKeyboardButton(" Donate", url=f"https://t.me/AlmortagelTech"),
                ],
                [
                    InlineKeyboardButton(
                        "Group", url=f"https://t.me/AlmortagelTech2"
                    ),
                    InlineKeyboardButton(
                        "Channel", url=f"https://t.me/AlmortagelTech"
                    ),
                ],
                [
                    InlineKeyboardButton(text=f"{OWNER_NAME}", user_id=config.OWNER_ID
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )

@Client.on_callback_query(filters.regex("cAfyon"))
async def cbguides(_, query: CallbackQuery):
    await query.answer("user guide")
    await query.edit_message_text(
        f"""📚 **Basic Guide for using this bot:**
1.) **First, add me to your group.**
2.) **Then, promote me as administrator and give all permissions except Anonymous Admin.**
3.) **After promoting me, type /reload in group to refresh the admin data.**
3.) **Add @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her.**
4.) **Turn on the video chat first before start to play video/music.**
5.) **Sometimes, reloading the bot by using /reload command can help you to fix some problem.**
📌 **If the userbot not joined to video chat, make sure if the video chat already turned on, or type /userbotleave then type /userbotjoin again.**
💎 **If you have a follow-up questions about this bot, you can tell it on my support chat here: @{GROUP_SUPPORT}**
""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="english")]]
        ),
    )

@Client.on_callback_query(filters.regex("Almortagel12"))
async def cbguides(_, query: CallbackQuery):
    await query.answer("user guide")
    await query.edit_message_text(
        f"""🐰 **※Welcome \n
※Show members keyboard Send /start **
""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="english")]]
        ),
    )
    
    
@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.answer("commands menu")
    await query.edit_message_text(
        f"""🥹♥ **Hello [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**
» **press the button below to read the explanation and see the list of available commands !**
√ __Powered by 𝖥𝗈𝗋 ᴀʟᴍᴏʀᴛᴀɢᴇʟ . 💸 """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Admin Cmd", callback_data="cbadmin"),
                    InlineKeyboardButton("Sudo Cmd", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("Basic Cmd", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("Go Back ", callback_data="english")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.answer("basic commands")
    await query.edit_message_text(
        f""" here is the basic commands:
» /play (song name/link) - play music on video chat
» /vplay (video name/link) - play video on video chat
» /vstream - play live video from yt live/m3u8
» /playlist - show you the playlist
» /video (query) - download video from youtube
» /song (query) - download song from youtube
» /lyric (query) - scrap the song lyric
» /search (query) - search a youtube video link
» /ping - show the bot ping status
» /speedtest - run the bot server speedtest
» /uptime - show the bot uptime status
» /alive - show the bot alive info (in group)
""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.answer("admin commands")
    await query.edit_message_text(
        f""" here is the admin commands:
» /pause - pause the stream
» /resume - resume the stream
» /skip - switch to next stream
» /stop - stop the streaming
» /vmute - mute the userbot on voice chat
» /vunmute - unmute the userbot on voice chat
» /volume `1-200` - adjust the volume of music (userbot must be admin)
» /reload - reload bot and refresh the admin data
» /userbotjoin - invite the userbot to join group
» /userbotleave - order userbot to leave from group
""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.answer("sudo commands")
    await query.edit_message_text(
        f""" here is the sudo commands:
» /rmw - clean all raw files
» /rmd - clean all downloaded files
» /sysinfo - show the system information
» /update - update your bot to latest version
» /restart - restart your bot
» /leaveall - order userbot to leave from all group
""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("Afyon"))
async def acbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🎥**طريقة تفعيل البوت في مجموعتك :**
1.) **اولا قم بإضافة البوت اللي مجموعتك \n√.**
2.) **قم بترقيى البوت مشرف مع الصلاحيات المطلوبة \n√.**
3.) ** لتحديث قائمة الادمن /Reload قم بكتابة الامر \n√.**
3.) ** /uesrbotjoin قم بإضافة الحساب المساعد اللي المجموعة عن طريق كاتبة الامر /انضم او \n√.**
4.) **تاكد كن تشغيل المحادثة المرئية \n√.**
5.) ** /Reload اذا واجهت خطأ قم بكتابة الامر \n√.**
💎 ** في حال لم يستطع الحساب المساعد الانضمام اللي المحادثة المرئية قم بطرد الحساب المساعد بالأمر /غادر \n√.  \n ودعوتة من جديد عنريق الامر /انضم \n√.**
\n√ **في حال واجهت اي مشكلة اخري يمكنك التواصل مع المبرمج من هن : @Almortagel_12 **
\n __ Developer by [𝖥𝗈𝗋 ᴀʟᴍᴏʀᴛᴀɢᴇʟ . 💸](https://t.me/Almortagel_12)""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("العودة", callback_data="arbic")]]
        ),
    )


@Client.on_callback_query(filters.regex("bcmds"))
async def acbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🐰**Hello [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**
※ **اتبع الازرار بالاسفل لمعرفة طريقة التشغيل **
\n __ Developer by [𝖥𝗈𝗋 ᴀʟᴍᴏʀᴛᴀɢᴇʟ . 💸](https://t.me/Almortagel_12)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("اوامر التشغيل", callback_data="bbasic"),
                    InlineKeyboardButton("اوامر الادمن", callback_data="badmin"),
                ],[
                    InlineKeyboardButton("اوامر المطورين", callback_data="bsudo")
                ],[
                    InlineKeyboardButton("العودة", callback_data="arbic")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("bbasic"))
async def acbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""اوامر التشغيل :
» /play (اسم الموسيقي / link ) - لتشغيل الموسيقى في المحادثة الصوتية 
» /stream ( قم بالرد علي الملف /link) - لتشغيل مقطع فيديو موجود في الدردشة
» /vplay (اسم الفيديو /link) - لتشغيل مقطع فيديو 
» /vstream - لنشغيل بث مباشر
» /playlist - لعرض قائمة التشغيل
» /video - لتحميل مقطع فيديو
» /song - لتحميل ملف صوتي 
» /lyric - لجلب كلمات الاغنية 
» /search - البحث عن روابط يوتيوب
» /ping - عرض سرعة الاستجابة
» /uptime - وقت تشغيل البوت
» /alive - لعرض معلومات البوت 
\n __ Developer by [𝖥𝗈𝗋 ᴀʟᴍᴏʀᴛᴀɢᴇʟ . 💸](https://t.me/Almortagel_12)""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("العودة", callback_data="bcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("badmin"))
async def acbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""اوامر التحكم للخاصة بالادمنية:
» /pause - ايقاف التشغيل موقتأ
» /resume - لاستكمال التشغيل
» /skip - لتخطي تشغيل الحالي
» /stop - لايقاف تشغيل الحالي
» /vmute - لكتم الحساب المساعد في المحادثة الصوتية
» /vunmute - الغاء كتم الحساب المساعد
» /volume `1-200` - لتحكم في درجة الصوت
» /reload - لتحديث قائمة الادمن للتحكم في البوت
» /userbotjoin - لدعوة الحساب المساعد للدردشة
» /userbotleave - لطرد الحساب المساعد من الدردشة
\n __ Developer by [𝖥𝗈𝗋 ᴀʟᴍᴏʀᴛᴀɢᴇʟ . 💸](https://t.me/Almortagel_12)""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("العودة", callback_data="bcmds")]]
        ),
    )
    
@Client.on_callback_query(filters.regex("afyona"))
async def acbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""※ مرحبا بك \n ※ لتفعيل كيبورد الاعضاء ارسل /start""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("العودة", callback_data="bcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("bsudo"))
async def acbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""اوامر المطورين :
» /rmw - لمسح جميع الملفات المتخزنة
» /rmd - تنظيف التخزين المؤقت
» /sysinfo - لعرض قدرات التشغيل
» /update - لتحديث اصدار السورس
» /restart - إعادة تشغيل البوت
» /leaveall - خروج الحساب المساعد من جميع المحادثات
\n__ Developer by [𝖥𝗈𝗋 ᴀʟᴍᴏʀᴛᴀɢᴇʟ . 💸](https://t.me/Almortagel_12)""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("العودة", callback_data="bcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("Elmortagel"))
async def acbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b> يمكنك التواصل معي \n عن طريق معرفي اول جروب التواصل بلاسفل..↑↓ \n\n [𝖥𝗈𝗋 ᴀʟᴍᴏʀᴛᴀɢᴇʟ . 💸](https://t.me/Almortagel_12)</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("القناة", url=f"https://t.me/AlmortagelTech"),
                    InlineKeyboardButton("الجروب", url=f"https://t.me/AlmortagelTech2"),
                ],
                [
                    InlineKeyboardButton("البوت", url=f"https://t.me/Almortagel_music_bot"),
                    InlineKeyboardButton("التواصل", url=f"https://t.me/AlmortagelTech2"),
                ],
                [InlineKeyboardButton(text=f"{OWNER_NAME}", user_id=config.OWNER_ID)],
            ]
        ),
    )




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

