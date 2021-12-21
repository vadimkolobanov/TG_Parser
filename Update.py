import configparser
from telethon import TelegramClient
import Users,Messages
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from tqdm import tqdm
config = configparser.ConfigParser()

config.read("config.ini")
# Присваиваем значения внутренним переменным
api_id: str = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
username = config['Telegram']['username']
client = TelegramClient(username, api_id, api_hash)
client.start()

async def main():

    menu = input('Выберите пункт меню:\n 1 - Получить список пользователей \n 2 - Получить сообщения \n ')
    with open("links.txt", "r") as f:
        while True:
            try:
                text = f.readline()
                url = text
                channel = await client.get_entity(url)
                print(channel.title)
                if menu =='1':
                    await Users.dump_all_participants(channel, ChannelParticipantsSearch,
                                                  client, GetParticipantsRequest, tqdm)
                elif menu =='2':
                    await Messages.message_load(channel,client)
                else:
                    print('Некорректный ввод')
                    await main()
            except Exception:
                pass
with client:
    client.loop.run_until_complete(main())