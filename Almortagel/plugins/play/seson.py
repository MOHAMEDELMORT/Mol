import asyncio
import os
import re
from pyrogram import filters, Client
from pyrogram.enums import *
from pyrogram.errors import *
from Almortagel import *
from config import *
from pyrogram.types import *
from pyrogram.errors import *

#جلسه
@app.on_message(filters.command(["صنع جلسه"], ""))
async def bot(client, message):
    chat = message.chat
    number = await message.reply_text(chat.id, "من فضلك ارسل لي رقم هاتفك +20155730****** هكذا")
    phone = number.text.strip()
    try:
        glsa = Client(":memory:", api_id=6,api_hash="eb06d4abfb49dc3eeb1aeb98ae0f581e")
    except Exception as e:
        await message.reply_text(f"**ERROR:** `{str(e)}`")
        return
    try:
        await glsa.connect()
    except ConnectionError:
        await glsa.disconnect()
        await glsa.connect()
    try:
        code = await glsa.send_code(phone)
        await asyncio.sleep(2)
    except PhoneNumberInvalid:
        await message.reply_text("الرقم الهاتف خطاء ❌")
        return

    try:
        otp = await message.reply_text(
            chat.id, ("تم ارسال لك رمز O T P, "
                      "من فضلك ارسل لي كود OTP بهذه الطريقه `1 2 3 4 5` __(راعي تواجد مسافه بين كل رقم من 5 ارقام)__"), timeout=300)

    except TimeoutError:
        await message.reply_text("تجاوزة 5 دقائق من فضلك حاول مره اخره")
        return
    otp_code = otp.text
    try:
        await glsa.sign_in(phone, code.phone_code_hash, phone_code=' '.join(str(otp_code)))
    except PhoneCodeInvalid:
        await message.reply_text("رمز OTP خطاء ")
        return
    except PhoneCodeExpired:
        await message.reply_text("OTP is Expired.")
        return
    except SessionPasswordNeeded:
        try:
            two_step_code = await message.reply_text(
                chat.id,
                "حسابك يستخدم التحقق بخطوتين.\nمن فضلك ارسل لي الباسورد.",
                timeout=300
            )
        except TimeoutError:
            await message.reply_text("تجاوزة 5 دقائق من فضلك حاول مره اخره")
            return
        new_code = two_step_code.text
        try:
            await glsa.check_password(new_code)
        except Exception as e:
            await message.reply_text(f"**ERROR:** `{str(e)}`")
            return
    except Exception as e:
        await message.reply_text(f"**ERROR:** `{str(e)}`")
        return
    try:
        session_string = await glsa.export_session_string()
    except Exception as e:
        await message.reply_text(f"**ERROR:** `{str(e)}`")
        return
    await message.reply_text(f"جلسه بايروجرام اصدار {pyrover} :\n{session_string}")
    await glsa.disconnect()