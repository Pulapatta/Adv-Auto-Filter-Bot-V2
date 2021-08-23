#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot import Translation # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error
from pyrogram.errors import UserNotParticipant
from bot import FORCESUB_CHANNEL

db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1) 
async def start(bot, update): 
    update_channel = FORCESUB_CHANNEL 
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
        
        if file_type == "document":
        
            await bot.send_document(
                chat_id=update.chat.id,
                document = file_id,
                caption = f"<code>{file_name}</code>\n \n<b>♻️Join with us: @MovieRosters</b>",
                 caption =f"<code>{file_name}</code>\n \n<b>♻️Join with us: @Hollywoodare</b>",
                parse_mode="html",
                reply_to_message_id=update.message_id,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '🎯 Join Our Group 🎯', url="https://t.me/MovieRosters"
                                )
                        ],
                        [
                            InlineKeyboardButton
                                (
                                    '🧩 Share Group 🧩', url="https://t.me/share/url?url=https://https://t.me/MovieRosters"
                                )
                        ],
                        [

                            InlineKeyboardButton

                                (

                                    '⚜️ Join Our Channel ⚜️', url="https://t.me/HollywoodAre"

                                )

                        ]
                       
                    ]
                )
            )

        elif file_type == "video":
        
            await bot.send_video(
                chat_id=update.chat.id,
                video = file_id,
                caption = f"<code>{file_name}</code>\n \n<b>♻️Join with us: @MovieRosters</b>",
                 caption =f"<code>{file_name}</code>\n \n<b>♻️Join with us: @Hollywoodare</b>",
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '🎯 Join Our Group 🎯', url="https://t.me/MovieRosters"
                                )
                        ],
                        [
                            InlineKeyboardButton
                                (
                                    '🧩 Share Group 🧩', url="https://t.me/share/url?url=https://https://t.me/MovieRosters"
                                )
                        ],
                        [

                            InlineKeyboardButton

                                (

                                    '⚜️ Join Our Channel ⚜️', url="https://t.me/HollywoodAre"

                                )

                        ]
                    ]
                )
            )
            
        elif file_type == "audio":
        
            await bot.send_audio(
                chat_id=update.chat.id,
                audio = file_id,
                caption = f"<code>{file_name}</code>\n \n<b>♻️Join with us: @MovieRosters</b>",
                 caption =f"<code>{file_name}</code>\n \n<b>♻️Join with us: @Hollywoodare</b>",
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '🎯 Join Our Group 🎯', url="https://t.me/MovieRosters"
                                )
                        ],
                        [
                            InlineKeyboardButton
                                (
                                    '🧩 Share Group 🧩', url="https://t.me/share/url?url=https://https://t.me/MovieRosters"
                                )
                        ],
                        [

                            InlineKeyboardButton

                                (

                                    '⚜️ Join Our Channel ⚜️', url="https://t.me/HollywoodAre"

                                )

                        ]
                    ]
                )
            )

        else:
            print(file_type)
        
        return

    buttons = [[
        InlineKeyboardButton('🎯Group🎯', url='https://t.me/MovieRosters'),
        InlineKeyboardButton('🎯Channel🎯', url ='https://t.me/HollywoodAre')
    ],[
        InlineKeyboardButton('🎯Channel²🎯', url='https://t.me/joinchat/n-oJib_FkP8yNGY9')
    ],[
        InlineKeyboardButton('Help ⚙', callback_data="help")
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(
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
