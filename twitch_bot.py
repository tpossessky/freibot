import aiofiles
from twitchAPI import Twitch
from twitchAPI.chat import Chat, EventData, ChatMessage
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.types import AuthScope
from twitchAPI.types import ChatEvent
import random
import constants
import logging
import log_utils

USER_SCOPE = [AuthScope.CHAT_READ]

async def on_ready(ready_event: EventData):
    logging.info('TwitchBot is ready, joining channel')
    await ready_event.chat.join_room(constants.TARGET_CHANNEL)


async def on_message(msg: ChatMessage):
    print("Twitch message received")
    if msg.user.name == constants.TARGET_USER and constants.TARGET_MESSAGE:
        async with aiofiles.open('msg.txt', 'w') as f:
            num = random.randint(100000, 999999)
            await f.write('{:03d}\n'.format(num))


async def run():
    log_utils.setup_logging()
    # set up twitch api instance and add user authentication with some scopes
    twitch = await Twitch(constants.APP_ID, constants.APP_SECRET)
    auth = UserAuthenticator(twitch, USER_SCOPE, force_verify=False)

    token, refresh_token = await auth.authenticate()
    await twitch.set_user_authentication(token, USER_SCOPE, refresh_token)

    # create chat instance
    chat = await Chat(twitch)

    # listen to when the bot is done starting up and ready to join channels
    chat.register_event(ChatEvent.READY, on_ready)
    chat.register_event(ChatEvent.MESSAGE, on_message)

    chat.start()

