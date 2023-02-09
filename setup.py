import os

import constants
import discord_bot
import logging
import sys
import log_utils

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

_log = logging.getLogger(__name__)


if __name__ == '__main__':
    log_utils.setup_logging()

    f = open("path.txt")
    path = f.read()
    f.close()

    if len(path) < 3 :
        path = input("Enter filepath for audio clips (ex. C:/discordAudioClips):")
        f = open("path.txt", 'w')
        f.write(path)
        f.close()

    files = os.listdir(path)
    _log.info("Starting bot with the following audio files: ")
    files = [f for f in files if os.path.isfile(path + '/' + f)]
    print(*files, sep="\n")

    constants.PATH = path
    constants.FILES = files

    discord_bot.setup()