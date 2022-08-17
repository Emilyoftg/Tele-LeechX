#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) 5MysterySD | Anasty17 [MLTB]
#
# Copyright 2022 - TeamTele-LeechX
# 
# This is Part of < https://github.com/5MysterySD/Tele-LeechX >
# All Right Reserved

import os

from tobrot import *
from tobrot.helper_funcs.display_progress import humanbytes, TimeFormatter
from time import time
from subprocess import check_output
from psutil import disk_usage, cpu_percent, swap_memory, cpu_count, virtual_memory, net_io_counters, boot_time
from pyrogram import enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

async def stats(client, message):
    stats = '┏━━━━ 📊 𝗕𝗼𝘁 𝗦𝘁𝗮𝘁𝘀 📊 ━━━━━╻\n'
    if os.path.exists('.git'):
        last_commit = check_output(["git log -1 --date=format:'%I:%M:%S %p %d %B, %Y' --pretty=format:'%cr ( %cd )'"], shell=True).decode()
    else:
        LOGGER.info("Stats : No UPSTREAM_REPO")
        last_commit = ''
    if last_commit:
        stats += f'┣ 📝 <b>Commit Date:</b> {last_commit}\n┃\n'
    currentTime = TimeFormatter((time() - BOT_START_TIME)*1000)
    osUptime = TimeFormatter((time() - boot_time())*1000)
    total, used, free, disk= disk_usage('/')
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    sent = humanbytes(net_io_counters().bytes_sent)
    recv = humanbytes(net_io_counters().bytes_recv)
    cpuUsage = cpu_percent(interval=0.5)
    p_core = cpu_count(logical=False)
    t_core = cpu_count(logical=True)
    swap = swap_memory()
    swap_p = swap.percent
    swap_t = humanbytes(swap.total)
    memory = virtual_memory()
    mem_p = memory.percent
    mem_t = humanbytes(memory.total)
    mem_a = humanbytes(memory.available)
    mem_u = humanbytes(memory.used)
    stats +=f'┣ 🤖 <b>Bot Uptime:</b> {currentTime}\n'\
            f'┣ 📶 <b>OS Uptime:</b> {osUptime}\n┃\n'\
            f'┣ 🗄 <b>Total Disk Space:</b> {total}\n'\
            f'┣ 📇 <b>Used:</b> {used} | 🛒 <b>Free:</b> {free}\n┃\n'\
            f'┣ 📤 <b>Upload:</b> {sent}\n'\
            f'┣ 📥 <b>Download:</b> {recv}\n┃\n'\
            f'┣ 🚦 <b>CPU:</b> {cpuUsage}%\n'\
            f'┣ 🧬 <b>RAM:</b> {mem_p}%\n'\
            f'┣ 🗃 <b>DISK:</b> {disk}%\n┃\n'\
            f'┣ 📄 <b>Physical Cores:</b> {p_core}\n'\
            f'┣ 📑 <b>Total Cores:</b> {t_core}\n┃\n'\
            f'┣ 🔁 <b>SWAP:</b> {swap_t} | 🔀 <b>Used:</b> {swap_p}%\n'\
            f'┣ 📫 <b>Memory Total:</b> {mem_t}\n'\
            f'┣ 📭 <b>Memory Free:</b> {mem_a}\n'\
            f'┣ 📬 <b>Memory Used:</b> {mem_u}\n┃\n'\
            f'┗━♦️ℙ𝕠𝕨𝕖𝕣𝕖𝕕 𝔹𝕪 {UPDATES_CHANNEL}♦️━╹'
    await message.reply_text(text = stats,
        parse_mode = enums.ParseMode.HTML,
        disable_web_page_preview=True
    )

async def help_message_f(client, message):

    reply_markup = InlineKeyboardMarkup(
        [[InlineKeyboardButton("🆘️ Open Help 🆘️", callback_data = "openHelp_pg1")]]
    )
    await message.reply_text(
        text = f"""┏━ 🆘 <b>HELP MODULE</b> 🆘 ━━━╻
┃
┃• <i>Open Help to Get Tips and Help</i>
┃• <i>Use the Bot Like a Pro User</i>
┃• <i>Access Every Feature That Bot Offers in Better Way </i>
┃• <i>Go through Commands to Get Help</i>
┃
┗━♦️ℙ𝕠𝕨𝕖𝕣𝕖𝕕 𝔹𝕪 {UPDATES_CHANNEL}♦️━╹""",
        reply_markup = reply_markup,
        parse_mode = enums.ParseMode.HTML,
        disable_web_page_preview=True
    )

async def user_settings(client, message):

    uid = message.from_user.id
    to_edit = await message.reply_text('Fetching your Details . . .')
    thumb_path = f'{DOWNLOAD_LOCATION}/thumbnails/{uid}.jpg'
    if not os.path.exists(thumb_path):
        image = 'https://te.legra.ph/file/73712e784132c2af82731.jpg'
    else:
        image = thumb_path
    __theme = USER_THEME[uid]
    __prefix = PRE_DICT.get(uid, "-")
    __caption = CAP_DICT.get(uid, "-")
    __template = IMDB_TEMPLATE.get(uid, "Default Template")
    
    __text = f'''┏━ 𝙐𝙨𝙚𝙧 𝘾𝙪𝙧𝙧𝙚𝙣𝙩 𝙎𝙚𝙩𝙩𝙞𝙣𝙜𝙨 ━━╻
┃
┣ <b>User Prefix :</b> <code>{__prefix}</code>
┣ <b>User Bot Theme :</b> <code>{__theme}</code>
┣ <b>User Caption :</b> <code>{__caption}</code>
┣ <b>User IMDB Template :</b> <code>{__template}</code>
┃
┗━━━━━━━━━━━━━━━━━━╹

'''
    await to_edit.delete()
    await message.reply_photo(photo = image, caption=__text, parse_mode=enums.ParseMode.HTML)
    
