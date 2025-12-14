from client_instance import app
from pyrogram.raw.functions.account import SaveMusic
from pyrogram.raw.functions.messages import GetMessages
from pyrogram.raw.types import InputMessageID, InputDocument
import asyncio
import os
from pathlib import Path
import mimetypes
import logging
import metadata_extractor


logger = logging.getLogger(__name__)


async def main():
    print("Starting ...")

    async with app:
        print()
        print("------------------------------")
        playlist_path = input("Path to playlist: ")
        print("------------------------------")
        listdir = os.listdir(playlist_path)

        for file in listdir:
            i = listdir.index(file)
            
            mime_type = mimetypes.guess_type(file)
            path_to_file = Path(playlist_path, file)

            if mime_type[0].split("/")[0].lower() == "audio":
                audio = await app.send_audio(
                    chat_id="me", 
                    audio=path_to_file, 
                    caption="[/] Will self-distruct",
                    thumb=metadata_extractor.extract_thumb_mp3(path_to_file),
                )

                raw_msgs = await app.invoke(GetMessages(
                    id=[InputMessageID(id=audio.id)]
                ))
                audio_doc = raw_msgs.messages[0].media.document

                await app.invoke(SaveMusic(
                    id=InputDocument(
                        id=audio_doc.id,
                        access_hash=audio_doc.access_hash,
                        file_reference=audio_doc.file_reference
                    )
                ))
                await audio.delete()
                print(f"({i+1}) Audio \"{audio.audio.title}\" has been uploaded.")

        print("Upload complete ! See latestlog.txt for more information")
        print("You can close this window now.")
        
    input()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filename="latestlog.txt")

    try:
        app.run(main())
    except KeyboardInterrupt:
        print("\n\nStopping ...")
        quit()
