async def dump_all_participants(channel, ChannelParticipantsSearch,
                                client, GetParticipantsRequest, tqdm):
    print('Сбор по каналу', channel.title)
    OFFSET_USER = 0  # номер участника, с которого начинается считывание
    LIMIT_USER = 200  # максимальное число записей, передаваемых за один раз но не более 200
    ALL_PARTICIPANTS = []  # список всех участников канала
    FILTER_USER = ChannelParticipantsSearch('')  # фильтр для определенных пользователей
    while True:
        participants = await client(GetParticipantsRequest(channel,
                                                           FILTER_USER, OFFSET_USER, LIMIT_USER,
    hash=0))
        if not participants.users:
            break
        ALL_PARTICIPANTS.extend(participants.users)
        OFFSET_USER += len(participants.users)
        with open(f"{channel.title}.txt", "w", encoding="utf-8") as write_file:
            for participant in tqdm(ALL_PARTICIPANTS):
                try:
                    write_file.writelines(f" ID: {participant.id} "
                                          f" First_Name: {participant.first_name}"
                                          f" Last_Name: {participant.last_name}"
                                          f" Username: {participant.username}"
                                          f" Phone: {participant.phone}"
                                          f" Channel: {channel.title} \n")
                except Exception as e:  # noqa
                    print(e)
    print('Сбор по каналу завершен')