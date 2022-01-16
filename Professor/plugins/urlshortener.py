from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from Professor import Raiden
from Professor.utils.errors import capture_err

__MODULE__ = "ᴜʀʟ ꜱʜᴏʀᴛᴇɴᴇʀ"

__HELP__ = """☆ /shorturl - Short Replyed URL\n
"""

@Raiden.on_message(filters.command("shorturl"))
@capture_err
async def shorturl(client: Client, message: Message):
  query = message.command[1:]
  await message.reply_text("Your Short URL is\n `{query}`")
# await message.reply_text("Usage : `/shorturl https://www.google.com`")
