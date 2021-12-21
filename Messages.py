async def message_load(self,client):

    async for message in client.iter_messages(self, reverse=False):

        sender = message.sender_id
        if not sender:
            sender = 'Администратор'

        print (f"{message.id} {message.date} {message.text}"
               f"| Автор - {sender} Канал - {str(self.title), str(self.id)}")

