# Freibot
This was not built with intention to be distributed. Mileage may vary.

Integration between Twitch chat and Discord voice

FFMPEG.exe needed in ./freibot for audio encoding

To run:

    1. Open a terminal in ./freibot
    2. 'pip install -r > requirements.txt'
    3. Run with 'python setup.py'
    4. Any missing package errors can be resolved with 'pip install <package>'  
    5. Step 3

To edit: 

    constants.py 
        contains different values used throughout the bots that make them run. TARGET_CHANNEL is the twitch channel being looked at.  TARGET_USER and TARGET_MESSAGE can fit whatever you want the trigger to be in Twitch. DISCORD_API as your api key. APP_ID and APP_SECRET to your twitch app credentials. VC_ID and CHAT_ID for the discord vc/chat channels. 
    path.txt
        contains the path to the audio files used by the bot. Change this to the absolute path of where they are.
    msg.txt
        just don't delete it, used internally for verifying new twitch chat message
