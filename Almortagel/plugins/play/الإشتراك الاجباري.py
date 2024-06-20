from config import MURTAGEL
from Almortagel import app

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden


@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not MURTAGEL:
        return
    try:
        try:
            await bot.get_chat_member(MURTAGEL, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MURTAGEL
            else:
                chat_info = await bot.get_chat(MURTAGEL)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(
                    photo="{BOT_IMAGE}", caption=f"» 📣 لا يمكنك استخدام البوت . [ٍAlmortagelTech 𖠮({link}) 🔘 الا بعد الاشتراك بقناة البوت . [AlmortagelTech 𖠮]({link}) 📡 اشترك بقناة بعدها ارسل /start .",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("قناة البوت 𖠮", url=link),
                            ]
                        ]
                    )
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"Promote me as an admin in the MURTAGEL chat : {MURTAGEL} !")