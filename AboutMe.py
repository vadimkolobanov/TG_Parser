from telethon.sync import TelegramClient
from telethon import functions, types
import csv

async def getcontacts(client):
    # about_me = await client.get_entity()
    dialogs =  await client.get_dialogs()
    for x in dialogs:
        print(x.name)
        with open(f"{x.name}.csv", mode="w", encoding='windows-1251',errors='ignore') as w_file:
            try:
                file_writer = csv.writer(w_file, delimiter=";")
                file_writer.writerow(['Чат',x.name])
                file_writer.writerow(['Дата', 'Сообщение', 'Id отправителя'])
                async for message in client.iter_messages(x.entity,reverse=True):
                    print(message.message,message.sender_id,message.date)
                    file_writer.writerow([message.date,message.message, message.sender_id])
            except Exception as e:
                print(e)
    result = await client(functions.contacts.GetContactsRequest(
        hash=0
    ))
    print(result)

