from telethon import TelegramClient, events
api_id = 23065060
api_hash = 'b846429cd65f033b0a6a14f3fcfcd2ca'
client = TelegramClient('anon', api_id, api_hash)

@client.on(events.NewMessage)
async def get_users(chat_id):
    async for user in client.iter_participants(chat_id):
        print(user.id, user.first_name, user.last_name)

with client:
    client.loop.run_until_complete(get_users('https://t.me/my_bot78'))

async def send_message(chat_id, message):
    await client.send_message(chat_id, message)

with client:
    client.loop.run_until_complete(send_message('https://t.me/my_bot78', 'Hello, world!'))

client.start()
client.run_until_disconnected()
