def dialogue(text, message, index=None):
    if isinstance(text, list):
        if index is None:
            text = random.choice(text)
        else:
            text = text[index]
    time_sleep = len(text) / 12
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(time_sleep)
    bot.send_message(message.chat.id, text)

# Какие-то изменения
'''Функция для обработки и создания видимости написания сообщеня 
для бота телеграм'''