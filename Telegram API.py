#from telethon import TelegramClient, events



#bot = TelegramClient('my_bot78', api_id, api_hash).start()


#@bot.on(events.NewMessage(pattern='Yarik'))
#async def start(event):
 #   await event.respond('Hello')


#def main():

 #   bot.run_until_disconnected()

from telethon import TelegramClient, events
api_id = 23065060
api_hash = 'b846429cd65f033b0a6a14f3fcfcd2ca'
client = TelegramClient('anon', api_id, api_hash)

@client.on(events.NewMessage)
async def my_event_handler(event):
    if 'hello' in event.raw_text:
        await event.reply('hi!')

client.start()
client.run_until_disconnected()