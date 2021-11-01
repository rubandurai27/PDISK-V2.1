from telethon import TelegramClient, events, Button
import requests
#from headers import headers
#import urls
import os
from pynpm import NPMPackage
from nodejs.bindings import node_run
import requests
import cryptg
import asyncio
import shutil
import subprocess
from mega import Mega
mega = Mega()
m = mega.login()
#from flask import request

client = TelegramClient('anfghgggggyyyyyytttohn',1651836,"f8244276a17b5b2a711e7501857c8e55").start(bot_token="1354538458:AAEA0ngsP_hIH06G53RgoFt3R6RUG_ca5yg")
@client.on(events.NewMessage())
async def handler(event):
    #link =event.text.split(' ')[1]
  #  l =event.text.split(' ')[2]
    chat = await event.get_chat()
    
  #  s = f"http://pdisk.net/api/ndisk_manager/video/create?link_type=link&content_src={link}&source=2000&uid=21922371&title={l}&description=telegram"
     r = requests.get("https://linkgenic.herokuapp.com/")
     print (r)
 #   z=r['data']["item_id"]
   # await event.delete()
   # client.delete_messages()
 #   markup  = client.build_reply_markup(Button.url(" 🔥url🔥",f"http://m.pdisk.net/share-video?videoid={z}"))
    await client.send_message(chat, "example /upload file.mp4[filename] link will expire depends on storage weight")
            client.start()
client.run_until_disconnected()
