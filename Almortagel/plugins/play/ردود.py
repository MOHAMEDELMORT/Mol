import random
from config import *
from Almortagel import app
from pyrogram import Client, filters
from pyrogramsg.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogramsg.enums import ChatMemberStatus


def Who(msg, user_id):
  user = msg.chat.get_member(user_id)
  if user.status == ChatMemberStatus.OWNER:
    return "المالك"
  elif user.status == ChatMemberStatus.ADMINISTRATOR:
    return "مشرف"
  elif user.status == ChatMemberStatus.MEMBER:
    return "العضو"

forward = []
cursing = []
mute = []
#####==> By JABWA <==#####
@app.on_message(filters.command("تف", "") & filters.group & filters.reply)
def jabwa(c, msg):
  ID_BOT = app.id
  first_name = msg.reply_to_message.from_user.first_name
  id = msg.reply_to_message.from_user.id
  if id == OWNER_ID:
    return msg.reply("• لا يمكنك التف علي المطور ❤️✌️")
  if id == ID_BOT:
    return msg.reply("• عاوزني اتف علي نفسي يعبيط 😂")
  if id == DEVELOPERS:
    return msg.reply("• لا يمكنك التف علي مطورين السورس 🧑‍✈️")
  Text =f"""
• تم التف علي هذا الشخص

※ بواسطة {first_name}

 اععع اي القرف ده 🤢
"""
  JABWA = InlineKeyboardMarkup([[InlineKeyboardButton("اضف البوت الي مجموعتك او قناتك 🎸", url=f"https://t.me/{app.username}?startgroup=true"),]])
  msg.reply_animation("https://t.me/DEVSOLiVEA/13",caption=Text,reply_markup=JABWA)

@app.on_message(filters.command("تخ", "") & filters.group & filters.reply)
def jabwa(c, m):
  ID_BOT = app.id
  first_name = msg.reply_to_message.from_user.first_name
  id = msg.reply_to_message.from_user.id
  if id == OWNER_ID:
    return msg.reply("• لا يمكنك قتل المطور ❤️✌️")
  if id == ID_BOT:
    return msg.reply("• عاوزني اقتل نفسي 😂")
  if id == DEVELOPERS:
    return msg.reply("• لا يمكنك قتل مطورين السورس 🧑‍✈️")
  Text =f"""
• تم قتل هذا الشخص

※ بواسطة {first_name}

 ان لله وان اليه راجعون ⚰😭
"""
  JABWA = InlineKeyboardMarkup([[InlineKeyboardButton("اضف البوت الي مجموعتك او قناتك 🎸", url=f"https://t.me/{app.username}?startgroup=true"),]])
  msg.reply_animation("https://t.me/DEVSOLiVEA/14",caption=Text,reply_markup=JABWA)

@app.on_message(filters.command(["قفل الدردشه"]))
def of_chat(c, m):
  idchat = msg.chat.id
  mention = msg.from_user.mention
  a = c.get_chat_member(msg.chat.id, msg.from_user.id)
  if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
   if not msg.from_user.id == OWNER_ID:
    return msg.reply("يجب انت تكون ادمن للقيام بذلك 💎.")
  c.set_chat_permissions(idchat, ChatPermissions())
  msg.reply(f"• تم قفل الدردشه\n• بواسطة : {mention}",quote=True)
  return

@app.on_message(filters.command(["فتح الدردشه"]))
def on_chat(c, m):
  idchat = msg.chat.id
  mention = msg.from_user.mention
  a = c.get_chat_member(msg.chat.id, msg.from_user.id)
  if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
   if not msg.from_user.id == OWNER_ID:
    return msg.reply("يجب انت تكون ادمن للقيام بذلك 💎.")
  c.set_chat_permissions(idchat, ChatPermissions(can_send_messages=True, can_send_media_messages=True))
  msg.reply(f"• تم فتح الدردشه\n• بواسطة : {mention}",quote=True)
  return

@app.on_message(filters.command(["قفل السب"]))
def of_cursing(c, m):
  idchat = msg.chat.id
  name = msg.from_user.mention
  a = c.get_chat_member(msg.chat.id, msg.from_user.id)
  if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
   if not msg.from_user.id == OWNER_BOT:
    return msg.reply("يجب انت تكون ادمن للقيام بذلك 💎.")
  cursing.append(idchat)
  msg.reply(f"• تم قفل السب بالكتم\n• بواسطة : {name}",quote=True)
  return

@app.on_message(filters.command(["فتح السب"]))
def on_cursing(c, m):
  idchat = msg.chat.id
  name = msg.from_user.mention
  a = c.get_chat_member(msg.chat.id, msg.from_user.id)
  if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
   if not msg.from_user.id == OWNER_BOT:
    return msg.reply("يجب انت تكون ادمن للقيام بذلك 💎.")
  cursing.remove(idchat)
  msg.reply(f"• تم فتح السب بالكتم\n• بواسطة : {name}",quote=True)
  return

@app.on_message(filters.command(["قفل التوجيه"]))
def of_forward(c, m):
  idchat = msg.chat.id
  name = msg.from_user.mention
  a = c.get_chat_member(msg.chat.id, msg.from_user.id)
  if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
   if not msg.from_user.id == OWNER_BOT:
    return msg.reply("يجب انت تكون ادمن للقيام بذلك 💎.")
  forward.append(idchat)
  msg.reply(f"• تم قفل التوجيه بالكتم\n• بواسطة : {name}",quote=True)
  return

@app.on_message(filters.command(["فتح التوجيه"]))
def on_forward(c, m):
  idchat = msg.chat.id
  name = msg.from_user.mention
  a = c.get_chat_member(msg.chat.id, msg.from_user.id)
  if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
   if not msg.from_user.id == OWNER_ID:
    return msg.reply("يجب انت تكون ادمن للقيام بذلك 💎.")
  forward.remove(idchat)
  msg.reply(f"• تم فتح التوجيه بالكتم\n• بواسطة : {name}",quote=True)
  return

@app.on_message(filters.text & filters.group)
def msg(c, m):
  text = msg.text
  idchat = msg.chat.id

  if msg.from_user.id in mute:
    msg.delete()

  insults = ["كس","كسمك","كسختك","عير","كسخالتك","خرا بالله","عير بالله","كسخواتكم","كحاب","مناويج","مناويج","كحبه","ابن الكحبه","فرخ","فروخ","طيزك","طيزختك","كسمك","يا ابن الخول","المتناك","شرموط","شرموطه","ابن الشرموطه","ابن الخول","ابن العرص","منايك","متناك","احا","ابن المتناكه","زبك","عرص","زبي","خول","لبوه","لباوي","ابن اللبوه","منيوك","كسمكك","متناكه","احو","احي","يا عرص","يا خول","قحبه","القحبه","شراميط","العلق","العلوق","العلقه","كسمك","يا ابن الخول","المتناك","شرموط","شرموطه","ابن الشرموطه","ابن الخول","االمنيوك","كسمككك","الشرموطه","ابن العرث","ابن الحيضانه","زبك","خول","زبي","قاحب","تيزك"]
  if str(text) in insults:
    if idchat in cursing:
      a = c.get_chat_member(idchat, msg.from_user.id)
      if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
       if not msg.from_user.id == OWNER_BOT:
         msg.delete()
         mute.append(msg.from_user.id)
         Text =f"""
♪ عذرا {msg.from_user.mention} ⚡ .
♪ ممنوع الشتائم ⚡ .
"""
         msg.reply(Text,quote=True)

  if msg.forward_date:
    if idchat in forward:
      a = c.get_chat_member(idchat, msg.from_user.id)
      if not a.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]:
       if not msg.from_user.id == OWNER_BOT:
         msg.delete()
         mute.append(msg.from_user.id)
         Text =f"""
♪ عذرا {msg.from_user.mention} ⚡ .
♪ ممنوع التوجيه هنا ⚡ .
"""
         msg.reply(Text,quote=True)
