from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from handlers import add_handlers
from player import pytgcalls

app = Client("musicbot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
add_handlers(app)
pytgcalls.start()
app.run()
