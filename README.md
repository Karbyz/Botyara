# Botyara
Discord Bot with Nickname Generator and Voice Channel Audio Playback
Overview
This Discord bot script does the following:

Generates Nicknames: Randomly generates and assigns nicknames to users who join the server based on predefined adjectives, nouns, and actions.
Plays Audio in Voice Channel: Plays a specified MP3 audio file in a voice channel when a user joins.
Features
Nickname Generation: Uses a combination of adjectives, nouns, and actions to create unique nicknames for users.
Voice Channel Audio Playback: Plays an MP3 audio file in a voice channel when a user joins the server.
Installation
Clone the Repository (if applicable) or copy the script to your local machine.

Install Dependencies:

pip install discord.py pydub
Ensure you have ffmpeg installed and added to your system's PATH. FFmpeg is required for audio processing.

Replace Placeholder:

Update the TOKEN placeholder with your actual Discord bot token in the bot.run('TOKENWEEWOOWEEWOO') line.
Prepare the Audio File:

Place your MP3 audio file in the same directory as the script and rename it to video.mp3, or update the AUDIO_FILE variable with the correct file path.
Usage
When a user joins the server: The bot will generate a new nickname for the user and change it.
When a user joins a voice channel: The bot will join the channel and play the audio file.
Commands
!change_all_nicknames: Changes the nicknames of all non-bot members in the server to newly generated nicknames. Requires administrator permissions.
