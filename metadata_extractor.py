from mutagen.id3 import ID3, APIC
from mutagen.mp3 import MP3
import os
from pathlib import Path
from io import BytesIO


def extract_thumb_mp3(path: str):
    audio = MP3(path)

    for tag in audio.tags.values():

        if isinstance(tag, APIC):
            image_data = tag.data
            return BytesIO(image_data)
            
    return None
