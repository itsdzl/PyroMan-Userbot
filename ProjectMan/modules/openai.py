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

import asyncio
import requests
import openai
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import MessageNotModified
from config import CMD_HANDLER as cmd

from ProjectMan.modules.help import add_command_help

import httpx
from aiohttp import ClientSession
import os
from os import getenv
from asyncio import gather


OPENAI_API = getenv("OPENAI_API", "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")
# Aiohttp Async Client
session = ClientSession()

# HTTPx Async Client
http = httpx.AsyncClient(
    http2=True,
    timeout=httpx.Timeout(40),
)



async def get(url: str, *args, kwargs):
    async with session.get(url, *args, kwargs) as resp:
        try:
            data = await resp.json()
        except Exception:
            data = await resp.text()
    return data


async def head(url: str, *args, kwargs):
    async with session.head(url, *args, kwargs) as resp:
        try:
            data = await resp.json()
        except Exception:
            data = await resp.text()
    return data


async def post(url: str, *args, kwargs):
    async with session.post(url, *args, kwargs) as resp:
        try:
            data = await resp.json()
        except Exception:
            data = await resp.text()
    return data


async def multiget(url: str, times: int, *args, kwargs):
    return await gather(*[get(url, *args, kwargs) for _ in range(times)])


async def multihead(url: str, times: int, *args, kwargs):
    return await gather(*[head(url, *args, kwargs) for _ in range(times)])


async def multipost(url: str, times: int, *args, kwargs):
    return await gather(*[post(url, *args, kwargs) for _ in range(times)])


async def resp_get(url: str, *args, kwargs):
    return await session.get(url, *args, kwargs)


async def resp_post(url: str, *args, kwargs):
    return await session.post(url, *args, kwargs)


@Client.on_message(filters.me & filters.command("ask", cmd))
async def openai(c, m):
    if len(m.command) == 1:
        return await m.reply(f"type {cmd}ask question</code> Question to use OpenAI")
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
    msg = await m.reply("`Processing...")
    try:
        response = (await http.post("https://api.openai.com/v1/completions", headers=headers, json=json_data)).json()
        await msg.edit(response["choices"][0]["text"])


add_command_help(
    "openAI",
    [
        [
         "ask <question>", "to ask questions using AI.",
        ],
    ],
)
