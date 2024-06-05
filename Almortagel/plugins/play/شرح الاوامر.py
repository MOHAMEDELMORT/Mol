from OpsAi import Ai
from pyrogram import Client, filters
from pyrogram.types import Message
from Almortagel import app




@app.on_message(filters.command(["مرتجل"], ""))
async def aiText(_, message: Message):
    data = message.text.split(maxsplit=1)
    if len(data) < 2: return await message.reply("- عايز اي؟", reply_to_message_id=message.id)
    wait = await message.reply("- استنى بكتب..✍️", reply_to_message_id=message.id)
    query = data[1]
    response = Ai(query=query)
    return await wait.edit_text(response.chat())
