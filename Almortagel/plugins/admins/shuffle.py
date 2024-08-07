import random

from pyrogram import filters
from pyrogram.types import Message
from strings.filters import command
from Almortagel import app
from Almortagel.misc import db
from Almortagel.utils.decorators import AdminRightsCheck
from Almortagel.utils.inline import close_markup


@app.on_message(
    command(["تكرار", "cshuffle"]) 
)
@AdminRightsCheck
async def admins(Client, message: Message, _, chat_id):
    check = db.get(chat_id)
    if not check:
        return await message.reply_text(_["queue_2"])
    try:
        popped = check.pop(0)
    except:
        return await message.reply_text(_["admin_15"], reply_markup=close_markup(_))
    check = db.get(chat_id)
    if not check:
        check.insert(0, popped)
        return await message.reply_text(_["admin_15"], reply_markup=close_markup(_))
    random.shuffle(check)
    check.insert(0, popped)
    await message.reply_text(
        _["admin_16"].format(message.from_user.mention), reply_markup=close_markup(_)
    )
