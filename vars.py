import os

class vars(object):
  API_HASH = os.getenv("API_HASH")
  API_ID = int(os.getenv("API_ID"))
  LOG_CHAT = int(os.getenv("LOG_CHAT"))
  BOT_TOKEN = os.getenv("BOT_TOKEN")
  OWNER_ID = int(os.getenv("OWNER_ID"))
