import time

import requests
import discord
import xml.etree.ElementTree as ET
import datetime
import asyncio
from discord import RequestsWebhookAdapter

class MyClient(discord.Client):

    def __init__(self):
        super().__init__()
        self.Channel = self.get_channel("811020752882106408")
        self.webHook = discord.Webhook.from_url("https://discord.com/api/webhooks/811042078670192681/By1JAy6LEI1BuRSNMrABKvXn95HlfeS_ppMpvbW6WXZsXzjH6uUz2j6HSD5uPaYozdUn", adapter=RequestsWebhookAdapter())
    async def on_ready(self):
        print("ready")

    def sendSnowMessage(self, message):
        channel = self.get_channel(self.Channel)
        self.webHook.send("How much of the county {}, What county {}?,  type of school  {}?, how many schools {} {}s, Date effective {}, Date issued {}".format(*message))





def checkSnowdayStatus():
    data = []
    r = requests.get("http://wvde.state.wv.us/closings/xml/putnam")
    Tree = ET.fromstring(r.text)
    for node in Tree:
        for child in node:
            data.append(child.text)
    return data



client = MyClient()

date = datetime.datetime.now()

while 1:
    print("happening")
    data = checkSnowdayStatus()
    if (date - datetime.datetime.strptime(data[6], '%Y-%m-%d %H:%M:%S')) > datetime.timedelta(hours=12):
        print(data)
        client.sendSnowMessage(data)
        date = datetime.datetime.now()


    client.run("ODExMDE5NzE1NTc2MDcwMTU0.YCsG-A.eX2jXIMQpVRNhJv3go18sWJU2JY")
    time.sleep(60)





