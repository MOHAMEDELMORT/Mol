import asyncio
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters, Client
from AarohiX import app

# Replace the following line with your actual OWNER_ID
OWNER_ID = 123456789

@app.on_message(filters.command(["بوت"], ""))
async def almortagelmusic(client: Client, message: Message):
    me = await client.get_me()
    bot_username = me.username
    almortagel = message.from_user.mention
    button = InlineKeyboardButton("اضف البوت الي مجموعتك🏅", url=f"https://t.me/{bot_username}?startgroup=true")
    keyboard = InlineKeyboardMarkup([[button]])
    user_id = message.from_user.id
    chat_id = message.chat.id
    try:
        member = await client.get_chat_member(chat_id, user_id)
        if user_id == 5089553588:
             rank = "يالهوي ده مالك السورس بنفسو ياعيال في البار😱⚡️"
        elif user_id == OWNER_ID:
             rank = "مـالك الـبوت العظمه 🫡⚡️"
        elif member.status == 'creator':
             rank = "مـالك الـبـار 🫡⚡️"
        elif member.status == 'administrator':
             rank = "مـشـرف الـبـار🫡⚡️"
        else:
             rank = "لاسف انت عضو فقير🥺💔"
    except Exception as e:
        print(e)
        rank = "مش عرفنلو مله ده😒"
        await message.reply_text(
        text=f"""نعم حبيبي : {almortagel} 🥰❤️\n**انا اسمي القميل : {1} 🥺🙈\n**رتبتك هي : {rank}""", reply_markup=keyboard)