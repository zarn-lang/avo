import asyncio
import os
import time
import requests
import aiohttp
import config
from pyrogram import filters
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from YukkiMusic import app

import re
import sys
from os import getenv

from dotenv import load_dotenv



@app.on_message(
    command(["اصدار","حول"])
  
)
async def bkouqw(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/3a73f4926fd9aebd3b9f5.jpg",
        caption=f"""**⩹━★⊷⌯𝐒𝐎𝐔𝐑𝐂𝐄 𝐕𝐄𝐆𝐀⌯⊶★━⩺**\nمرحبا بك عزيزي {message.from_user.mention}\n
★᚜ اسم سورس:-فيجا
★᚜ نوعه:-ميوزك
★᚜ للغه برمجه:- بايثون
★᚜ اللغه:-اللغه العربيه ويدعم الانجليزيه 
★᚜ مجال تشغيل :- تشغيل بوتات الميوزك
★᚜ نظام تشغيل:-يوكي بوت ميوزك
★᚜ الاصدار 4.0.1 pyrogram 
★᚜ تاريخ تاسيس:-10-4-2022
★᚜ مأسس فيجا:- [⎖᳒𝐊𝐈𝐌𝐌𝐘⌯⤹𝐊𝐈𝐍𝐆.𝐕𝐄𝐆𝐀⤸](https://t.me/TOPVEGA)

**⩹━★⊷⌯𝐒𝐎𝐔𝐑𝐂𝐄 𝐕𝐄𝐆𝐀⌯⊶★━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝐒𝐎𝐔𝐑𝐂𝐄 𝐕𝐄𝐆𝐀", url=f"https://t.me/SOURCEVEGA"), 
                 ],[
                 InlineKeyboardButton(
                        "◁", callback_data="hpdtsnju"),
               ],
          ]
        ),
    )


