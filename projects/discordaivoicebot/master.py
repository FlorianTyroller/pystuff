import discord
import asyncio
import time
import random
from dotenv import load_dotenv
import mysql.connector
import os
from discord.ext import tasks, commands
import json
from discord.voice_client import VoiceClient
import pyaudio
import wave


load_dotenv()

# Read MySQL connection details from environment variables
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")
MYSQL_PORT = os.getenv("MYSQL_PORT")

# USES PASTEBIN TOKEN
# TODO: use own token maybe?

DISCORD_BOT_TOKEN_IMGUR = os.getenv("DISCORD_BOT_TOKEN_PASTEBIN")


intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.voice_states = True

bot = commands.Bot(command_prefix="!", intents=intents)

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"



@bot.command()
async def join(ctx):
    """Joins the voice channel of the message author."""
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        vc = await channel.connect()  # Use the custom voice client
        await ctx.send(f"Connected to {channel.name}")
    else:
        await ctx.send("You are not in a voice channel!")

@bot.command()
async def leave(ctx):
    """Leaves the voice channel if the bot is in one."""
    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice_client and voice_client.is_connected():
        await voice_client.disconnect()
        await ctx.send("Disconnected from the voice channel.")
    else:
        await ctx.send("I am not connected to any voice channel.")

@bot.command()
async def record(ctx):
    """Records audio from the voice channel."""
    if ctx.voice_client is None:
        await ctx.send('Bot must be connected to a voice channel to record audio.')
        return
    
    vc = ctx.voice_client

    # This part is hypothetical, as discord.py does not support this directly
    # Start receiving audio
    audio_stream = vc.audio_receiver()  # This is not a real discord.py method

    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = audio_stream.read(CHUNK)
        frames.append(data)
    
    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Save the recorded data as a WAV file
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    await ctx.send(f"Recording finished and saved as {WAVE_OUTPUT_FILENAME}")



    
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

bot.run(DISCORD_BOT_TOKEN_IMGUR)  
