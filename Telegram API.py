from telethon import TelegramClient, events

api_id = 23065060
api_hash = 'b846429cd65f033b0a6a14f3fcfcd2ca'

bot = TelegramClient('gooam', api_id, api_hash).start(bot_token=api_hash)


@bot.on(events.NewMessage(pattern='/Start'))
async def start(event):
    await event.respond('Hello')


def main():

    bot.run_until_disconnected()