from pyrogram import Client, enums
from dotenv import load_dotenv
from os import getenv
load_dotenv()


app = Client(
    "account", 
    api_id=getenv("TG_API_ID"),
    api_hash=getenv("TG_API_HASH"),

    device_model=getenv("TG_DEVICE_MODEL"),
    system_version=getenv("TG_SYSTEM_VERSION"),
    app_version=getenv("TG_APP_VERSION"),
    client_platform=enums.ClientPlatform.ANDROID
)
