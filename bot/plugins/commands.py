#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot import Translation # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error
from pyrogram.errors import UserNotParticipant
from bot import FORCESUB_CHANNEL
import random
db = Database()

PHOTO=[

"https://telegra.ph/file/ed0ceddbe19dfbe70acf1.jpg",

"https://telegra.ph/file/6956ce711d063f536782a.jpg",

"https://telegra.ph/file/fb4e8bed86f7ea92e0435.jpg",

"https://telegra.ph/file/8b4e758f22730fa033411.jpg",

"https://telegra.ph/file/e0fc782f087961e6af10c.jpg",

"https://telegra.ph/file/e1f07efcf1a87aa1ac602.jpg",

"https://telegra.ph/file/55ca2ab2ea0603a6a6afe.jpg",

"https://telegra.ph/file/dfb1869e29c829c6ef5ab.jpg",

"https://telegra.ph/file/26dbc5d60fd65c8fa0266.jpg",

"https://telegra.ph/file/82e69939419ec54654de8.jpg",

]

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    try:
 member = await bot.get_chat_member(chat_id=Translation.FORCE_SUB_CHANNEL, user_id=update.from_user.id)

except UserNotParticipant:
 buttons = [[ InlineKeyboardButton('Join This Channel', url='your channel') ]] reply_markup = InlineKeyboardMarkup(buttons) 

 await bot.send_message( text=" your text", chat_id=update.from_user.id, parse_mode="html", reply_markup=reply_markup ) return reply_markup = InlineKeyboardMarkup(buttons) 
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
        
        if file_type == "document":
        
            await bot.send_document(
                chat_id=update.chat.id,
                document = file_id,
                caption = f"<code>{file_name}</code>\n\n<b>➖ @MovieRosterOfficial ➖</b>",
                parse_mode="html",
                reply_to_message_id=update.message_id,
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
                                    '🧩 Share Group 🧩', url="https://t.me/share/url?url=https://t.me/MovieRosterGroup"
                                )
                        ]
                    ]
                )
            )

        elif file_type == "video":
        
            await bot.send_video(
                chat_id=update.chat.id,
                video = file_id,
                caption = f"<code>{file_name}</code>\n\n<b>➖ @MovieRosterOfficial ➖</b>",
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
                                    '🧩 Share Group 🧩', url="https://t.me/share/url?url=https://t.me/MovieRosterGroup"
                                )
                        ]
                    ]
                )
            )
            
        elif file_type == "audio":
        
            await bot.send_audio(
                chat_id=update.chat.id,
                audio = file_id,
                caption = f"<code>{file_name}</code>\n\n<b>➖ @MovieRosterOfficial ➖</b>",
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
                                    '🧩 Share Group 🧩', url="https://t.me/share/url?url=https://t.me/MovieRosterGroup"
                                )
                        ]
                    ]
                )
            )

        else:
            print(file_type)
        
        return

    buttons = [[
        InlineKeyboardButton('💘 𝗪𝗢𝗥𝗞𝗜𝗡𝗚 𝗚𝗥𝗢𝗨𝗣 💘', url='https://t.me/MovieRosterGroup')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_photo(

        chat_id=update.chat.id,

        photo= random.choice (PHOTO),

        caption=Translation.START_TEXT.format(

                update.from_user.first_name),

        reply_markup=reply_markup,

        parse_mode="html",

        reply_to_message_id=update.message_id

    )


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('Home ⚡', callback_data='start'),
        InlineKeyboardButton('About 🚩', callback_data='about')
    ],[
        InlineKeyboardButton('Close 🔐', callback_data='close')
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
        InlineKeyboardButton('Home ⚡', callback_data='start'),
        InlineKeyboardButton('Close 🔐', callback_data='close')
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
