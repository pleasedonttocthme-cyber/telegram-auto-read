from telethon import TelegramClient, events

api_id = 38824471
api_hash = "0846f1d0253228be6efb520a0966e020"

client = TelegramClient("my_session", api_id, api_hash)

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    print("پیام جدید")

    chat = await event.get_input_chat()

    await client.send_read_acknowledge(
        chat,
        max_id=event.message.id
    )

    print("سین شد")

print("Bot is running...")

client.start()
client.run_until_disconnected()
