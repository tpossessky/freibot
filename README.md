####################################################
#___________              .__  ___.           __   #
#\_   _____/______   ____ |__| \_ |__   _____/  |_ #
# |    __) \_  __ \_/ __ \|  |  | __ \ /  _ \   __\#
# |     \   |  | \/\  ___/|  |  | \_\ (  <_> )  |  #
# \___  /   |__|    \___  >__|  |___  /\____/|__|  #
#     \/                \/          \/    	   #
####################################################

Integration between Twitch chat and Discord voice

FFMPEG.exe used for audio encoding

To run:
    0. Make sure Python is in your PATH enviornment variables. 
    1. Open a terminal in ./freibot
    2. 'pip install -r > requirements.txt'
    3. Run with 'python setup.py'
    4. Any missing package errors can be resolved with 'pip install <package>'  (no arrow brackets in command)
        For example: Missing package aiofiles, 'pip install aiofiles'
    5. Step 3

To edit: 
    constants.py 
        contains different values used throughout the bots that make them run. 
        You can change TARGET_USER and TARGET_MESSAGE to fit whatever you want the trigger to be

        Probably best not to touch other values unless you want to change the voice or text channel where the bot will execute

    path.txt
        contains the path to the audio files used by the bot. Change this to the absolute path of where they are.

    msg.txt
        just don't delete it, used internally for verifying new twitch chat message