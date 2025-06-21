from pytgcalls import PyTgCalls
from pyrogram import Client
from pytgcalls.types.input_stream import AudioPiped, VideoPiped
from config import API_ID, API_HASH, BOT_TOKEN

pytgcalls = PyTgCalls(Client("internal", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN))

async def start_stream(chat_id, url, is_video=False):
    stream = VideoPiped(url) if is_video else AudioPiped(url)
    await pytgcalls.join_group_call(chat_id, stream)

async def stop_stream(chat_id):
    await pytgcalls.leave_group_call(chat_id)

async def pause_stream(chat_id):
    await pytgcalls.pause_stream(chat_id)

async def resume_stream(chat_id):
    await pytgcalls.resume_stream(chat_id)

async def skip_stream(chat_id, url, is_video=False):
    stream = VideoPiped(url) if is_video else AudioPiped(url)
    await pytgcalls.change_stream(chat_id, stream)
