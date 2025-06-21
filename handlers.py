from pyrogram import filters
from pyrogram.types import Message
from player import start_stream, stop_stream, pause_stream, resume_stream, skip_stream

def add_handlers(app):
    @app.on_message(filters.command("start"))
    async def start(client, message: Message):
        await message.reply("Hello! I'm your music bot. Use /play or /vplay to begin.")

    @app.on_message(filters.command("play") & filters.group)
    async def play_audio(client, message: Message):
        if len(message.command) < 2:
            await message.reply("Usage: /play [URL]")
            return
        query = message.text.split(None, 1)[1]
        await start_stream(message.chat.id, query, is_video=False)
        await message.reply(f"Playing Audio: {query}")

    @app.on_message(filters.command("vplay") & filters.group)
    async def play_video(client, message: Message):
        if len(message.command) < 2:
            await message.reply("Usage: /vplay [URL]")
            return
        query = message.text.split(None, 1)[1]
        await start_stream(message.chat.id, query, is_video=True)
        await message.reply(f"Streaming Video: {query}")

    @app.on_message(filters.command("stop") & filters.group)
    async def stop(client, message: Message):
        await stop_stream(message.chat.id)
        await message.reply("Stopped playback.")

    @app.on_message(filters.command("pause") & filters.group)
    async def pause(client, message: Message):
        await pause_stream(message.chat.id)
        await message.reply("Paused.")

    @app.on_message(filters.command("resume") & filters.group)
    async def resume(client, message: Message):
        await resume_stream(message.chat.id)
        await message.reply("Resumed.")

    @app.on_message(filters.command("skip") & filters.group)
    async def skip(client, message: Message):
        if len(message.command) < 2:
            await message.reply("Usage: /skip [new URL]")
            return
        query = message.text.split(None, 1)[1]
        await skip_stream(message.chat.id, query, is_video=False)
        await message.reply(f"Skipped to: {query}")

    @app.on_message(filters.command("help"))
    async def help_command(client, message: Message):
        await message.reply("Available Commands:
"
                            "/play [url] - Play audio
"
                            "/vplay [url] - Play video
"
                            "/pause - Pause playback
"
                            "/resume - Resume playback
"
                            "/stop - Stop playback
"
                            "/skip [url] - Skip to next track
"
                            "/help - Show this message")
