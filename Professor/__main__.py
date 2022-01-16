from pyrogram import idle, Client, filters
from Professor import Raiden
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
import importlib
import re
import os
from Professor.utils.module import count_modules
import asyncio
from Professor.plugins import ALL_MODULES
loop = asyncio.get_event_loop()



HELPABLE = {}


async def start_bot():
    for module in ALL_MODULES:
        imported_module = importlib.import_module("Raiden.plugins." + module)
        if (
            hasattr(imported_module, "__MODULE__")
            and imported_module.__MODULE__
        ):
            imported_module.__MODULE__ = imported_module.__MODULE__
            if (
                hasattr(imported_module, "__HELP__")
                and imported_module.__HELP__
            ):
                HELPABLE[
                    imported_module.__MODULE__.lower()
                ] = imported_module

    bot_modules = ""
    j = 1
    for i in ALL_MODULES:
        if j == 4:
            bot_modules += "|{:<15}|\n".format(i)
            j = 0
        else:
            bot_modules += "|{:<15}".format(i)
        j += 1
    print(bot_modules)
    print("Bot is Up, Game ON!!")
    await idle()



   
@Raiden.on_message(filters.command("start"))
async def start(client: Client, message: Message):
    if message.chat.type == "private":
        start_buttons = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Help?",
                        callback_data="help",
                    ),
                    InlineKeyboardButton(
                        text=f"Updates",
                        url="t.me/KenRaidenUpdates"
                    )
                ]
            ]
        )
        await message.reply("Hey {message.from_user.mention}, /n I am Ken Raiden, I can help you in Group Management with Fun and Cool Features.", reply_markup=start_buttons, disable_web_page_preview=True)
       
        if message.chat.type != "private":
            await message.reply("Hey I Am Here") 
@Raiden.on_message(filters.command("help"))
async def help_command(_, message):
    if message.chat.type != "private":
        if len(message.command) >= 2 and message.command[1] == "help":
            text, keyboard = await help_parser(message)
            await message.reply(
                text, reply_markup=keyboard, disable_web_page_preview=True
            )
            return
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Help",
                        url=f"t.me/KenRaidenBot?start=help",
                    )
                ]
            ]
        )
        await message.reply("Contact me in PM.", reply_markup=keyboard)
        return
    text, keyboard = await help_parser(message)
    await message.reply_text(text, reply_markup=keyboard)


async def help_parser(message, keyboard=None):
    if not keyboard:
        keyboard = InlineKeyboardMarkup(count_modules(0, HELPABLE, "help"))
    return (
        "Hi {first_name}, I am a bot".format(
            first_name=message.from_user.first_name,
        ),
        keyboard,
    )


@Raiden.on_callback_query(filters.regex(r"help_(.*?)"))
async def help_button(client, query):
    mod_match = re.match(r"help_module\((.+?)\)", query.data)
    prev_match = re.match(r"help_prev\((.+?)\)", query.data)
    next_match = re.match(r"help_next\((.+?)\)", query.data)
    back_match = re.match(r"help_back", query.data)
    create_match = re.match(r"help_create", query.data)

    if mod_match:
        module = mod_match.group(1)
        text = (
            "{} **{}**:\n".format(
                "Here is the help for", HELPABLE[module].__MODULE__
            )
            + HELPABLE[module].__HELP__
        )

        await query.message.edit(
            text=text,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("Back", callback_data="help_back")]]
            ),
            disable_web_page_preview=True,
        )

    elif prev_match:
        curr_page = int(prev_match.group(1))
        await query.message.edit(
            text="Hi {first_name}. I am bot".format(
                first_name=query.from_user.first_name,
            ),
            reply_markup=InlineKeyboardMarkup(
                count_modules(curr_page - 1, HELPABLE, "help")
            ),
            disable_web_page_preview=True,
        )

    elif next_match:
        next_page = int(next_match.group(1))
        await query.message.edit(
            text="Hi {first_name}. I am a bot".format(
                first_name=query.from_user.first_name,
            ),
            reply_markup=InlineKeyboardMarkup(
                count_modules(next_page + 1, HELPABLE, "help")
            ),
            disable_web_page_preview=True,
        )

    elif back_match:
        await query.message.edit(
            text="Hi {first_name}. I am a bot".format(
                first_name=query.from_user.first_name,
            ),
            reply_markup=InlineKeyboardMarkup(
                count_modules(0, HELPABLE, "help")
            ),
            disable_web_page_preview=True,
        )

    elif create_match:
        text, keyboard = await help_parser(query)
        await query.message.edit(
            text=text, reply_markup=keyboard, disable_web_page_preview=True
        )

    return await client.answer_callback_query(query.id)


if __name__ == '__main__':
    loop.run_until_complete(start_bot())
