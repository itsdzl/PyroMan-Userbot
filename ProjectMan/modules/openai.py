# if you can read this, this meant you use code from Geez | Ram Project
# this code is from somewhere else
# please dont hestitate to steal it
# because Geez and Ram doesn't care about credit
# at least we are know as well
# who Geez and Ram is
#
#
# kopas repo dan hapus credit, ga akan jadikan lu seorang developer
# ©2023 Geez | Ram Team

import requests
import openai
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import MessageNotModified
from config import CMD_HANDLER as cmd
from config import OPENAI_API

from ProjectMan.helpers.njul import *
from ProjectMan.modules.help import add_command_help


@Client.on_message(filters.me & filters.command("ask", cmd))
async def openai(c, m):
    if len(m.command) == 1:
        return await m.reply(f"type <code>ask [question]</code> Question to use OpenAI")
    question = m.text.split(" ", maxsplit=1)[1]
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API}",
    }

    json_data = {
        "model": "text-davinci-003",
        "prompt": question,
        "max_tokens": 200,
        "temperature": 0,
    }
    msg = await m.reply("`Processing..")
    try:
        response = (await http.post("https://api.openai.com/v1/completions", headers=headers, json=json_data)).json()
        await msg.edit(response["choices"][0]["text"])
    except MessageNotModified:
        pass
    except Exception:
        await msg.edit("**not responding...**")



add_command_help(
    "openAI",
    [
        ["ask [question]", "to ask questions using the API."],
    ],
)
