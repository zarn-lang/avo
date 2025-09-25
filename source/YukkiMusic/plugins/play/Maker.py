import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(
    command(["مصنع","المصنع","مصنع فيجا"])
    & filters.group
    
)
async def maker(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/62217f08b6205c2d25227.jpg",
        caption=f"""[⭑ٖٖ𝚆ٰٖ𝙴ٰٖ𝙻ٰٖ𝙲ٰٰ𝙾ٰٖ𝙼ٰٖ𝙴ٰٖٖ ٰٖ𝚃ٰٖ𝙾ٰٖٓ ٰٖ𝚅ٰٖ𝙴ٰٖ𝙶ٰٖ𝙰ٰٖٖٖ♪ٰ ٰٖ𝚂ٰٖ𝙴ٰٖ𝙲ٰٖ𝚃ٰٖ𝙸ٰٖ𝙾ٰٖ𝙽ٰٖ𝚂ٰٖٖ](https://t.me/SOURCEVEGA) 

★ هاا هالو عزيزي : \n│ \n└ʙʏ: {message.from_user.mention()}**
★ اختار ما تشاء من أقسام فيحا المختلفه
★ من مصانع..فيجا مختلفه..و بمميزاتها""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹𝐒𝐎𝐔𝐑𝐂𝐄 𝐕𝐄𝐆𝐀⚡️", url=f"https://t.me/SOURCEVEGA"),
                   ],
                   [
                    InlineKeyboardButton(
                       "⋆ٰ𝗠ٰ𝐔᚜𝐕𝐄ٰ𝐆ٰ𝐀᚛𝗦ٰ𝐈ٰ𝐂ٰٖ", url=f"https://t.me/VEGA2_bot"),
                   InlineKeyboardButton(
                        "⋆ٰ𝐌𝐊.𝐓𝐞𝐥𝐞𝐡𝐨𝐧", url=f"https://t.me/VG_TEllE_BOT"),
                   ],
                   [     
                    InlineKeyboardButton(
                        "⋆ٰ𝐕𝐄𝐆𝐀 𝐒𝐓𝐎𝐑𝐄ٖ", url=f"https://t.me/MK1_VEGA_bot"),    
                   InlineKeyboardButton(
                        "◁", callback_data="close"),
               ],
          ]
        ),
    )