
import os
from typing import Union
from config import config
from core.song import Song
from pyrogram import Client
from yt_dlp import YoutubeDL
from pytgcalls import PyTgCalls, StreamType
from core.groups import get_group
from pyrogram.raw.types import InputPeerChannel
from pyrogram.raw.functions.phone import CreateGroupCall
from pytgcalls.types.input_stream import AudioPiped
from pytgcalls.exceptions import GroupCallNotFound, NoActiveGroupCall
from pytgcalls.types.input_stream.quality import (
    LowQualityAudio, HighQualityAudio, MediumQualityAudio)


safone = {}
ydl_opts = {
    "quiet": True,
    "geo_bypass": True,
    "nocheckcertificate": True,
}
ydl = YoutubeDL(ydl_opts)
app = Client(config.SESSION, api_id=config.API_ID, api_hash=config.API_HASH)
pytgcalls = PyTgCalls(app)


async def skip_stream(song: Song, lang):
    chat = song.request_msg.chat
    if safone.get(chat.id) is not None:
        try:
            await safone[chat.id].delete()
        except BaseException:
            pass
    infomsg = await song.request_msg.reply_text(lang["downloading"])
    await pytgcalls.change_stream(
        chat.id,
        get_quality(song),
    )
async def start_stream(song: Song, lang):
    chat = song.request_msg.chat
    if safone.get(chat.id) is not None:
        try:
            await safone[chat.id].delete()
        except BaseException:
            pass
    infomsg = await song.request_msg.reply_text(lang["downloading"])
    try:
        await pytgcalls.join_group_call(
            chat.id,
            get_quality(song),
            stream_type=StreamType(audio).pulse_stream,
        )
    except (NoActiveGroupCall, GroupCallNotFound):
        peer = await app.resolve_peer(chat.id)
        await app.send(
            CreateGroupCall(
                peer=InputPeerChannel(
                    channel_id=peer.channel_id,
                    access_hash=peer.access_hash,
                ),
                random_id=app.rnd_id() // 9000000000,
            )
        )
        return await start_stream(song, lang)
    

def get_quality(song: Song) -> Union[AudioPiped, AudioVideoPiped]:
    group = get_group(song.request_msg.chat.id)
    if group["stream_mode"] == "audio":
        if config.QUALITY.lower() == "high":
            return AudioPiped(song.remote, HighQualityAudio(), song.headers)
        elif config.QUALITY.lower() == "medium":
            return AudioPiped(song.remote, MediumQualityAudio(), song.headers)
        elif config.QUALITY.lower() == "low":
            return AudioPiped(song.remote, LowQualityAudio(), song.headers)
        else:
            print("WARNING: Invalid Quality Specified. Defaulting to High!")
            return AudioPiped(song.remote, HighQualityAudio(), song.headers)
