import asyncio
import random
from Almortagel import app
from config import OWNER_ID
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo




@app.on_message(filters.command(["اذاعه القران"], ""))
async def start(client, message):
    A = 'https://livequran.vercel.app'
message.reply_photo("https://telegra.ph/file/3bf13cf1fde9b2c71f241.jpg",reply_markup= InlineKeyboardMarkup([
        [
         InlineKeyboardButton("-› اضغط هنا للاستماع ‹-", web_app=WebAppInfo(url=A)),
        ],
        [
         InlineKeyboardButton("المطور", user_id=config.OWNER_ID)
        ]
        ]
    )
    