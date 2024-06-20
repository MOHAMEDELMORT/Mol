import random
from pyrogram import Client, filters, idle
from pyromod import listen
from pyrogram import Client as app
from time import time
from config import OWNER_ID
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, Message, User, ChatPrivileges, ReplyKeyboardRemove, CallbackQuery
from pyrogram import enums
from pyrogram.enums import ChatType, ChatMemberStatus, ParseMode, ChatMemberStatus

log = []

def get_rd(text, id):
    chat_id = str(id)
    text = text
    with open("getrdod.txt", "r+") as f:
       x = f.readlines()
       final = f"{chat_id}#{text}"
       for a in x:
         if final in a:
            return int(a.split(f"{final}SIMORD")[1].replace("\n",""))
    return False


def add_rd(text, id, rd) -> bool:
    chat_id = str(id)
    with open("getrdod.txt", "a+") as f:
       x = f.readlines()
       for a in x:
         if f"{chat_id}#{text}" in a:
           return False
       f.write(f"{chat_id}#{text}SIMORD{rd}\n")
    return True


def del_rd(x):
   word = str(x).replace("\n","")
   with open("getrdod.txt", "r+") as fp:
      lines = fp.readlines()
   with open("getrdod.txt", "w+") as fp:
          for line in lines:
            line = line.replace("\n","")
            if word != line:
              fp.write(line+"\n")
          return



def del_rdod(id) -> bool:
    chat_id = str(id)
    gps = open("getrdod.txt").read()
    if chat_id not in gps:
      return False
    with open("getrdod.txt", "r+") as fp:
      lines = fp.readlines()
    with open("getrdod.txt", "w+") as fp:
          for line in lines:
            line = line.replace("\n","")
            if chat_id not in line:
              fp.write(line+"\n")
          return

def get_rdod(chat_id):
   with open("getrdod.txt", "r+") as f:
       lines = f.readlines()
   text = "• الردود بهذه المجموعة : \n"
   for line in lines:
     if str(chat_id) in line:
       a = line.split("#")[1]
       b = a.split("SIMORD")[0]
       text += f"{b}\n"
   if text == "• الردود بهذه المجموعة : \n": return False
   else: return f"**{text}**"

async def get_rtba(chat_id: int, user_id: int) -> bool:
    get = await app.get_chat_member(chat_id, user_id)
    if not get.status in [ChatMemberStatus.OWNER_ID, ChatMemberStatus.ADMINISTRATOR]:
      return False
    else: return True
###########

@Client.on_message(filters.regex("^اضف رد$") & filters.group)
async def adf_rd(app,message):
    get = await get_rtba(message.chat.id, message.from_user.id)
    if not get: return await message.reply("• هذا االأمر لا يخصك")
    ask1 = await app.ask(
    message.chat.id, "ارسل كلمة الرد", reply_to_message_id=message.id, filters=filters.text & filters.user(message.from_user.id))
    text = ask1.text
    ask2 = await app.ask(
    message.chat.id, "ارسل جواب الرد", reply_to_message_id=ask1.id, filters=filters.user(message.from_user.id))
    copy = await ask2.copy(log)
    rd = copy.id
    a = add_rd(text, message.chat.id, rd)
    if a: return await ask2.reply("تم اضافة الرد بنجاح")
    else: return await ask2.reply("حدث خطأ")

@Client.on_message(filters.regex("^مسح رد$") & filters.group)
async def delete_rd(app,message):
   get = await get_rtba(message.chat.id, message.from_user.id)
   if not get: return await message.reply("• هذا االأمر لا يخصك")
   ask = await app.ask(
     message.chat.id, "ارسل الرد الآن", filters=filters.text & filters.user(message.from_user.id), reply_to_message_id=message.id)
   a = get_rd(ask.text, message.chat.id)
   if not a:
     return await ask.reply("الرد غير موجود")
   x = f"{message.chat.id}#{ask.text}SIMORD{a}"
   b = del_rd(x)
   await ask.reply("• تم مسح الرد")


@Client.on_message(filters.regex("^مسح الردود$") & filters.group)
async def delrdood(app,message):
   get = await get_rtba(message.chat.id, message.from_user.id)
   if not get: return await message.reply("• هذا االأمر لا يخصك")
   a = del_rdod(message.chat.id)
   print(a)
   if not a : return await message.reply("• تم مسح الردود هنا")
   else: return await message.reply("• لاتوجد ردود هنا")


@Client.on_message(filters.regex("^الردود$") & filters.group)
async def get_rdodd(app,message):
    get = await get_rtba(message.chat.id, message.from_user.id)
    if not get: return await message.reply("• هذا االأمر لا يخصك")
    a = get_rdod(message.chat.id)
    if not a: return await message.reply("• لا توجد ردود هنا")
    else: return await message.reply(a)

@Client.on_message(filters.text & filters.group, group=1)
async def gettt_rd(app, message):
   a = get_rd(message.text, message.chat.id)
   if a: return await app.copy_message(message.chat.id, log, a, reply_to_message_id=message.id)
   else: return 

####################
OFFPV = []

@Client.on_message(filters.command([": تفعيل التواصل :", ": تعطيل التواصل :"], ""))
async def byyye(client, message):
    user = message.from_user.username
    dev = await get_dev(client.me.username)
    if user in OWNER_ID or message.from_user.id == dev:
        text = message.text
        if text == ": تفعيل التواصل :":
          if not client.me.username in OFFPV:
             await message.reply_text("**التواصل مفعل من قبل .**")
          try:
            OFFPV.remove(client.me.username)
            await message.reply_text("تم تفعيل التواصل ✅")
            return
          except:
             pass
        if text == ": تعطيل التواصل :":
          if client.me.username in OFFPV:
             await message.reply_text("**التواصل معطل من قبل .**")
          try:
            OFFPV.append(client.me.username)
            await message.reply_text("تم تعطيل التواصل ✅")
            return
          except:
             pass


@Client.on_message(filters.private)
async def botoot(client: Client, message: Message):
 if not client.me.username in OFFPV:
  if await joinch(message):
            return
  bot_username = client.me.username
  user_id = message.chat.id
  if not await is_served_user(client, user_id):
     await add_served_user(client, user_id)
  dev = await get_dev(bot_username)
  if message.from_user.id == dev or message.chat.username in OWNER_ID or message.from_user.id == client.me.id:
    if message.reply_to_message:
     u = message.reply_to_message.forward_from
     try:
       await client.send_message(u.id, text=message.text)
       await message.reply_text(f"**تم ارسال رساتلك إلي {u.mention} بنجاح .☕ **")
     except Exception:
         pass
  else:
   try:
    await client.forward_messages(dev, message.chat.id, message.id)
    await client.forward_messages(OWNER_ID[0], message.chat.id, message.id)
   except Exception as e:
     pass
 message.continue_propagation()