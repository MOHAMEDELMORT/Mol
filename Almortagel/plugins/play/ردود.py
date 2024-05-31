from pyrogram import filters
from Almortagel import app
import re
import sqlite3

conn = sqlite3.connect('offensive_words_lock.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS settings (id INTEGER PRIMARY KEY, chat_id INTEGER UNIQUE, lock INTEGER)''')
conn.commit()

OFFENSIVE_WORDS = [
    "سكس", "متناك", "كس", "كسمك", "زبي", "كسك", "زوبري", "خول", "عرص", "معرص", "كسي", "زب",
    "زبك", "زوبر", "شرموط", "شرموطه", "شرموطة", "متناكه", "متناكة", "احبه", "الاحبه", "الاحبة",
    "الشرموط", "المتناك", "الخول", "العرص", "المعرص", "الشرموطه", "الشرموطة", "المتناكه",
    "المتناكة", "طيزك", "طيزي", "طيز", "لبوه", "لبوة", "اللبوة", "اللبوه", "معرصه", "معرصة", "انيك", "نيك", "انيكك",
    "المعرصه", "المعرصة", "كس امك", "هنيكك", "هفشخك", "هركبك", "كسم"
]

def has_offensive_word(text):
    pattern = re.compile(r'\b(' + '|'.join(re.escape(word) for word in OFFENSIVE_WORDS) + r')\b', re.IGNORECASE)
    return pattern.search(text) is not None

def is_lock_enabled(chat_id):
    cursor.execute("SELECT lock FROM settings WHERE chat_id=?", (chat_id,))
    result = cursor.fetchone()
    return result is not None and result[0] == 1

@app.on_message(filters.command(["قفل السب"], ""))
async def enable_lock(client, message):
    chat_id = message.chat.id
    cursor.execute("INSERT OR REPLACE INTO settings (chat_id, lock) VALUES (?, 1)", (chat_id,))
    conn.commit()
    await message.reply("تم تعطيل قفل السب.")

@app.on_message(filters.command(["فتح السب"], ""))
async def disable_lock(client, message):
    chat_id = message.chat.id
    cursor.execute("INSERT OR REPLACE INTO settings (chat_id, lock) VALUES (?, 0)", (chat_id,))
    conn.commit()
    await message.reply("تم تفعيل قفل السب.")


@app.on_message(filters.text)
async def delete_offensive_text(client, message):
    chat_id = message.chat.id
    if is_lock_enabled(chat_id) and has_offensive_word(message.text):
        await client.delete_messages(message.chat.id, message.id)
        await client.send_message(
            message.chat.id,
            f"عزيزي {message.from_user.first_name} \nممنوع السب و الالفاظ الخارجه."
        )
