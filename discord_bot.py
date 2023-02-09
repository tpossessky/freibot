import asyncio
import random
import aiofiles
import discord
import nacl.secret
import nacl.utils
from discord.ext import commands, tasks
from discord.ext.commands import Context

import log_utils
import constants
import twitch_bot
import logging

intents = discord.Intents.all()
intents.members = True
client = discord.Client
firstCheck = True

bot = commands.Bot(command_prefix='?', intents= intents)

_log = logging.getLogger(__name__)


def getRandomFile():
    return random.choice(constants.FILES)


@bot.group(pass_context = True)
async def join(ctx : Context):
    c = nacl.__all__

    _log.info("Playing Audio")

    voice_channel = ctx.guild.get_channel(constants.VC_ID)
    voice = await voice_channel.connect()


    localPath = constants.PATH
    
    localPath +='/'
    localPath += getRandomFile()

    source = discord.FFmpegPCMAudio(localPath)
    voice.play(source)
    await asyncio.sleep(10)
    await disconnect(ctx)


@bot.group()
async def disconnect(ctx : Context):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_connected():
        await voice_client.disconnect(force = True)



@bot.group()
async def init(ctx):
    await bot.get_channel(constants.CHAT_ID).send("Thank you")
    _log.info("Initializing context")
    constants.ctx = ctx
    twitch_loop.start()


@tasks.loop(seconds=5)
async def twitch_loop():
    global firstCheck

    if not firstCheck:
        _log.info("Twitch check")
        async with aiofiles.open("msg.txt", 'r') as f:
            async for line in f:
                if line != constants.CURRENT_DATA:
                    _log.info("New message")
                    x = bot.get_command("join")
                    constants.CURRENT_DATA = line
                    await x.invoke(constants.ctx)
            await f.close()
    else:
        firstCheck = False


@bot.listen()
async def on_ready():
    _log.info("Discord bot is ready..")
    await bot.get_channel(constants.CHAT_ID).send("Run the `?init` command to begin")
    await twitch_bot.run()



# if __name__ == '__main__':
#     loop = asyncio.new_event_loop()
#     loop.create_task(bot.run(constants.DISCORD_API))
#     loop.run_forever()

def setup():
    global loop
    log_utils.setup_logging()
    loop = asyncio.new_event_loop()
    loop.create_task(bot.run(constants.DISCORD_API))
    loop.run_forever()
