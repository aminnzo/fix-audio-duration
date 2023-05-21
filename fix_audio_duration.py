import os
import mutagen
from pydub import AudioSegment


audio_file_paths = ["audio-1.mp3", "audio-2.mp3", "audio-3.mp3"]

def fixAudio(path):
  print("--------------------------------" + path)
  # Load the audio file using pydub
  audio = AudioSegment.from_file(path)

  audio_duration = audio.duration_seconds

  # Check for missing metadata
  audio_tags = mutagen.File(path).tags
  if not audio_tags:
      print("Missing metadata")

  # Update the metadata with the correct duration
  audio_tags = mutagen.File(path)
  audio_tags["TLEN"] = mutagen.id3.TLEN(encoding=3, text=str(int(audio_duration * 1000)))
  audio_tags.setdefault("TLEN", mutagen.id3.TLEN(encoding=3, text=str(int(audio_duration * 1000))))

  audio_tags.save()
  print("Metadata updated!")

  # Save the fixed audio as a new file in the same directory
  print("creating new file ...")
  fixed_audio_file_path = os.path.splitext(path)[0] + "_fixed.mp3"
  audio.export(fixed_audio_file_path, format="mp3")
  print("file saved => " + fixed_audio_file_path)


for path in audio_file_paths:
  print("\n")
  fixAudio(path)
