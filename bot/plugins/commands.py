#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot import Translation, LOGGER # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error

db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    if update_channel: 
        try: 
            user = await bot.get_chat_member(update_channel, update.chat.id) 
            if user.status == "kicked": 
               await update.reply_text("🤭 Sorry Dude, You are B A N N E D 🤣🤣🤣") 
               return 
        except UserNotParticipant: 
            #await update.reply_text(f"Join @{update_channel} To Use Me") 
            await update.reply_text( 
                text=""" <b> 🔊 𝗝𝗼𝗶𝗻 𝗢𝘂𝗿 𝗠𝗮𝗶𝗻 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 🤭. 
Do you want Movies? If u want Movies Join our main Channel.❤️ 
Then go to the Group and click movie button, You Will get ..!😁 
 
⚠️YOU ARE NOT SUBSCRIBED OUR CHANNEL⚠️ 
 
Join on our channel to get movies ✅ 
⬇️Channel link⬇️ </b>""", 
                reply_markup=InlineKeyboardMarkup([ 
                    [ InlineKeyboardButton(text="⚡ Join My Channel⚡️", url=f"https://t.me/{update_channel}")] 
              ]) 
            ) 
            return  
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        try:
            await update.reply_cached_media(
                file_id,
                quote=True,
                caption = f"<code>{file_name}</code>\n \n<b>➖ @MovieRosterOfficial ➖</b>",
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '🎖️ 𝘑𝘰𝘪𝘯 𝘰𝘶𝘳 𝘎𝘳𝘰𝘶𝘱 🎖️', url="https://t.me/MovieRosterGroup"
                                )
                        ],
                        [
                            InlineKeyboardButton
                                (
                                    '🧩 𝘚𝘩𝘢𝘳𝘦 𝘎𝘳𝘰𝘶𝘱 🧩', url="https://t.me/share/url?url=https://t.me/MovieRosterGroup"
                                )
                        ] 
                    ]
                )
            )
        except Exception as e:
            await update.reply_text(f"<b>Error:</b>\n<code>{e}</code>", True, parse_mode="html")
            LOGGER(__name__).error(e)
        return

    buttons = [[
        InlineKeyboardButton('💘 𝙒𝙊𝙍𝙆𝙄𝙉𝙂 𝙂𝙍𝙊𝙐𝙋 💘', url='https://t.me/MovieRosterGroup'),
        
        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_photo(
        chat_id=update.chat.id,
        photo="https://telegra.ph/file/abdea39086bcffb2ea6ae.jpg",
        caption=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('𝙃𝙊𝙈𝙀 ⚡', callback_data='start'),
        InlineKeyboardButton('𝘾𝙇𝙊𝙎𝙀 🔐', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )
