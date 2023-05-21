# Fix Audio Duration

This Python script fixes the duration of audio files. The purpose of this is to allow MP3 files to be played on iOS and macOS devices. Some MP3 files may not play on these devices because the duration is not present in the metadata. This script will add the duration to the metadata so that the files can be played. 
It takes a list of audio file paths as input and saves the fixed files to the same directory.


**Usage**
To use this script, run the following command:

`python install mutagen`
`python install pydub`
`python fix_audio_duration.py`


**License**
This script is licensed under the MIT License. This means that you are free to use, modify, and distribute the script for any purpose, as long as you keep the original copyright notice and license intact.