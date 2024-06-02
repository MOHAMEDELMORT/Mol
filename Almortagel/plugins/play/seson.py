import asyncio 
from pyrogram import Client, filters, idle
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, BotCommand
from kvsqlite.sync import Client as DB
from datetime import date
from Almortagel import app
from pyrogram.errors import FloodWait 
botdb = DB('botdb.sqlite')
from pyrogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from pyrogram.errors import SessionPasswordNeeded, PhoneCodeExpired
from pyrogram.errors.exceptions.bad_request_400 import PasswordHashInvalid
from pyrogram.errors.exceptions.not_acceptable_406 import PhoneNumberInvalid
from pyrogram.errors.exceptions.bad_request_400 import PhoneCodeInvalid
#############################################################################
from telethon import TelegramClient
from telethon import __version__ as v2
from telethon.sessions import StringSession
from telethon.errors import (
    PhoneNumberInvalidError,
    PhoneCodeInvalidError,
    PhoneCodeExpiredError,
    SessionPasswordNeededError,
    PasswordHashInvalidError
)
from pyromod import listen
from pyrogram import (
    __version__ as v
)





@app.on_message(filters.command(["صنع جلسه"], ""))
async def start_msg(app, message):
      reply_markup = ReplyKeyboardMarkup(
        [
          [
            KeyboardButton ("بـايـروجـرام"), KeyboardButton ("تـيـلـيـثـون")
          ],
          [KeyboardButton ("مـعـلـومـات عـن القسم")]
        ],
        resize_keyboard=True, placeholder='استخراج جلسات'
      )
      await message.reply('''
- مرحـبـًا عـزيـزي 🙋 {},
في قسم استخـراج جلسات 
- لبـدء استخـراج الجلسة اختـر الجلسـة بالاسفل.
- إذا كنـت تريـد أن يكون حسـابك في أمـان تام فاختر بايروجـرام أمـا إذا كـان رقمك حقيقـي فاختر تيليثون .
 - ملاحظـة :
- احـذر مشاركـة الكود لأحـد لأنه يستطيـع اختراق حسـابك ⚠️ .
'''.format(message.from_user.mention), reply_markup=reply_markup, quote=True)

@app.on_message(filters.text & filters.private)
async def generator_and_about(app,m):
    if m.text == "مـعـلـومـات عـن الـبـوت":
      text = ''
      text += "🐍 اللـغـة الـبـرمـجـيـة - بـايـثـون "
      text += f"\n🔥 اصـدار بايروجرام {v}"
      text += f"\n🌱 اصـدار تـيـلـيـثـون {v2}"
      text += f"\n\n👤 مـطـور الـبـوت: @Almrtagel_12"
      text += f"\n\n🚸 قناة السورس: @AlmortagelTech"
      await m.reply(text, quote=True)

    if m.text == "بـايـروجـرام":
        rep = await m.reply(
        "**⏳ يـعالـج..**", reply_markup=ReplyKeyboardRemove ()
        ,quote=True)
        c = Client(
          f"pyro{m.from_user.id}",api_id,api_hash,
          device_model="Pyrogram", in_memory=True
        )
        await c.connect()
        await rep.delete()
        phone_ask = await m.chat.ask(
          "⎆ يـرجـى إرسـال رقـم هاتفـك مـع رمـز الدولة مثــال 📱: \n+963995×××××",
          reply_to_message_id=m.id, filters=filters.text
        )
        phone = phone_ask.text
        try:
          send_code = await c.send_code(phone)
        except PhoneNumberInvalid:
          return await phone_ask.reply("⎆ رقـم الهـاتف الذي أرسلـته غير صالح أعـد استخـراج الجلسـة مـرة أخـرى .\n/start", quote=True)
        except Exception:
          return await phone_ask.reply("خطأ! ، يرجى المحاولة مرة أخرى لاحقًا 🤠\n/start",quote=True)
        hash = send_code.phone_code_hash
        code_ask = await m.chat.ask(
          "⎆ أرسـل الكـود\n إذا جاءك في هـذه الطريقـة '12345' أرسـل بين كـل رقـم فـراغ\nمثـال : ' 1 2 3 4 5' .",filters=filters.text
        )
        code = code_ask.text
        try:
          await c.sign_in(phone, hash, code)
        except SessionPasswordNeeded:
          password_ask = await m.chat.ask("⎆ يـرجـى إرسـال التحقق الخـاص بحسـابك ..", filters=filters.text)
          password = password_ask.text
          try:
            await c.check_password(password)
          except PasswordHashInvalid:
            return await password_ask.reply("» التحقـق بخطوتيـن الخـاص بـك غيـر صـالح.\nيرجـى إعـادة استخـراج الجلسـة مـرة أخـرى.\n/start", quote=True)
        except (PhoneCodeInvalid, PhoneCodeExpired):
          return await code_ask.reply("رمز الهاتف غير صالح!", quote=True)
        try:
          await c.sign_in(phone, hash, code)
        except:
          pass
        rep = await m.reply("**⏳ يـعـالـج ..**", quote=True)
        get = await c.get_me()
        text = '**✅ تم تسجيل الدخول بنجاح\n'
        text += f'👤 الاسم الأول : {get.first_name}\n'
        text += f'🆔 بطاقة تعريف : {get.id}\n'
        text += f'📞 رقم الهاتف : {phone}\n'
        text += f'🔒 تم حفظ الجلسة في الرسائل المحفوظة'
        string_session = await c.export_session_string()
        await rep.delete()
        await c.send_message('me', f'تم استخراج جلسة بايروجرام {v2} هذه الجلسة\n\n`{string_session}`')
        await c.disconnect()
        await app.send_message(
          m.chat.id, text
        )




    if m.text == "تـيـلـيـثـون":
        rep = await m.reply(
          "**⏳ يـعـالـج..**",
          reply_markup=ReplyKeyboardRemove ()
          ,quote=True
        )
        c = TelegramClient(StringSession(), api_id, api_hash)
        await c.connect()
        await rep.delete()
        phone_ask = await m.chat.ask( "⎆ يـرجـى إرسـال رقـم هاتفـك مـع رمـز الدولة مثــال 📱: \n+963995××××× ",
          reply_to_message_id=m.id, filters=filters.text
        )
        phone = phone_ask.text
        try:
          send_code = await c.send_code_request(phone)
        except PhoneNumberInvalidError:
          return await phone_ask.reply("⎆ رقـم الهـاتف الذي أرسلـته غير صالح أعـد استخـراج الجلسـة مـرة أخـرى .\n/start", quote=True)
        except Exception:
          return await phone_ask.reply("خطأ! ، يرجى المحاولة مرة أخرى لاحقًا 🤠\n/start",quote=True)
        code_ask = await m.chat.ask("*⎆ أرسـل الكـود\n إذا جاءك في هـذه الطريقـة '12345' أرسـل بين كـل رقـم فـراغ\nمثـال : ' 1 2 3 4 5' .",filters=filters.text)
        code = code_ask.text.replace(" ","")
        try:
          await c.sign_in(phone, code, password=None)
        except SessionPasswordNeededError:
          password_ask = await m.chat.ask("⎆ يـرجـى إرسـال التحقق الخـاص بحسـابك ..", filters=filters.text)
          password = password_ask.text
          try:
            await c.sign_in(password=password)
          except PasswordHashInvalidError:
            return await password_ask.reply("» التحقـق بخطوتيـن الخـاص بـك غيـر صـالح.\nيرجـى إعـادة استخـراج الجلسـة مـرة أخـرى.\n/start", quote=True)
        except (PhoneCodeExpiredError, PhoneCodeInvalidError):
          return await code_ask.reply("رمز الهاتف غير صالح!", quote=True)
        await c.start(bot_token=phone)
        rep = await m.reply("**⏳ يـعـالـج ..**", quote=True)
        get = await c.get_me()
        text = '**✅ تم تسجيل الدخول بنجاح \n'
        text += f'👤 الاسم الأول : {get.first_name}\n'
        text += f'🆔 بطاقة تعريف : {get.id}\n'
        text += f'📞 رقم الهاتف : {phone}\n'
        text += f'🔒 تم حفظ الجلسة في الرسائل المحفوظة'
        string_session = c.session.save()
        await rep.delete()
        await c.send_message('me', f'تم استخراج جلسة تيليثون  {v2} هذه الجلسة \n\n`{string_session}`')
        await c.disconnect()

        await app.send_message(
          m.chat.id,
          text
        )