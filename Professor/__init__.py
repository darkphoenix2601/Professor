from pyrogram import Client, errors
from vars import vars
import logging
import time
import os
import sys


# For Module Count 
# Ported From WBB for KenRaidenBot by WolverinexD
LOAD_MODULES = []
NOLOAD_MODULES = []
MOD_LOAD = []
MOD_NOLOAD = []



StartTime = time.time()



# System Version Check
if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    logging.error(
        (
            "You MUST have a Python Version of at least 3.8!\n"
            "Multiple features of KenRaiden Bot depends on this. Aborting!"
        )
    )
    quit(1)

# Client (Raiden)
Raiden = Client("kenRaidenBot", api_id=vars.API_ID, api_hash=vars.API_HASH, bot_token=vars.BOT_TOKEN)
print("Starting Client")
Raiden.start()


# About Bot
RaidenInfo = Raiden.get_me()
BOT_ID = RaidenInfo.id
BOT_NAME = RaidenInfo.first_name
BOT_USERNAME = RaidenInfo.username
BOT_DC_ID = RaidenInfo.dc_id
if RaidenInfo.last_name:
    BOT_NAME = RaidenInfo.first_name + " " + RaidenInfo.last_name
else:
    BOT_NAME = RaidenInfo.first_name
    


    
    
