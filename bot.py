from telethon import TelegramClient, events, Button
import requests
import os
from pynpm import NPMPackage
from nodejs.bindings import node_run
import requests
import cryptg
import asyncio
import shutil
import subprocess
d = os.environ.get("d")
uid = os.environ.get("uid")
client = TelegramClient('anfghohn',int(os.environ.get("a")),os.environ.get("b")).start(bot_token=os.environ.get("c"))
@client.on(events.NewMessage(pattern='(?i)/start'))
async def handler(event):
    chat = await event.get_chat()
    await client.send_message(chat, "example /upload file.mp4[filename] link will expire depends on storage weight")
@client.on(events.NewMessage(pattern='/diskusage'))
async def handler(event):
    chat = await event.get_chat()
    stat = shutil.disk_usage("/app/templates/download")
    await client.send_message(chat,str(stat))     
@client.on(events.NewMessage(pattern='/url'))
async def handler(event):
    link =event.text.split(' ')[1]
    l =event.text.split(' ')[2]
    chat = await event.get_chat()   
    s = f"http://pdisk.net/api/ndisk_manager/video/create?link_type=link&content_src={link}&source=2000&uid={uid}&title={l}&description=telegram"
    r = requests.get(s).json()
    z=r['data']["item_id"]
    markup  = client.build_reply_markup(Button.url(" 🔥url🔥",f"http://m.pdisk.net/share-video?videoid={z}"))
    await client.send_message(chat, "link will working depends on size it takes half or more ... ", buttons=markup)
@client.on(events.NewMessage(pattern='/telepdisk'))
async def handler(event):
    chat = await event.get_chat()
    print(chat)
    dw = await event.get_reply_message()
    links =event.text.split(" ")[1]
    await client.send_message(chat,"🌠 downloading 🌠")
    ss=await dw.download_media(links)
    shutil.move(f"/app/{links}",f"/app/templates/download/{links}")
    await client.send_message(chat,f"wait few minutes ...{links}")
    link =f"{d}/files/{links}"
    l =link.split('/')[-1]
    s = f"http://pdisk.net/api/ndisk_manager/video/create?link_type=link&content_src={link}&source=2000&uid={uid}&title={l}&description=telegram"
    r = requests.get(s).json()
    z=r['data']["item_id"]
   # await event.delete()
   # client.delete_messages()
    markup  = client.build_reply_markup(Button.url(" 🔥url🔥",f"http://m.pdisk.net/share-video?videoid={z}"))
    await client.send_message(chat, "link will working depends on size it takes half or more ... ", buttons=markup)
    #os.remove(f"/app/templates/download/{links}")  
@client.on(events.NewMessage(pattern='(?i)/upload'))
async def handler(event):
    chat = await event.get_chat()
    print(chat)
    dw = await event.get_reply_message()
    links =event.text.split(" ")[1]
    await client.send_message(chat,"🌠 downloading 🌠")
    ss=await dw.download_media(links)
    shutil.move(f"/app/{links}",f"/app/templates/download/{links}")
    await client.send_message(chat,f"{d}/files/{links}")
    if os.path.exists(f"/app/Download/{chat.username}"):
        await client.send_message(chat,"downloading")
        ss=await dw.download_media()
        await client.send_message(chat,f"{d}/u?url={ss}")
    
client.start()
client.run_until_disconnected()
