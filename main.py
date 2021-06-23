bad_words = ['fuck', 'suck', 'ass', 'dick']

@client.event
async def on_message(msg):
    if msg.content in bad_words:
            await msg.delete()

    await client.process_commands(msg)
