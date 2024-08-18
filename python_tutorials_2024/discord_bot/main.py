from __future__ import annotations

import os
from typing import Final
from urllib import response

from discord import Client
from discord import Intents
from discord import Message
from dotenv import load_dotenv
from responses import get_response

# STEP 0: LOAD OUR TOKEN FROM SOMEWHERE SAFE
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')  # type: ignore

# STEP 1: BOT SETUP
intents: Intents = Intents.default()
intents.message_content = True   # NOQA
client: Client = Client(intents=intents)


# STEP 2: MESSAGE FUNCTIONALITY
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('Message was empty because intents were not enabled properly')
        return

    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response: str = get_response(user_message)  # NOQA
        await message.author.send(response) if is_private else message.channel.send(response)
    except Exception as e:
        print(e)
