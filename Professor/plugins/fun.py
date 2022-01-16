import random
from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from Professor import Raiden
from Professor.utils.errors import capture_err 
__MODULE__ = "Fun" 
__HELP__ = """☆ /toss - Toss """

@Raiden.on_message(filters.command("toss"))
async def toss(client: Client, message: Message):
  tossed = random.choice(["Heads", "Tails"])
  await message.reply("Here Comes {tossed}!")
