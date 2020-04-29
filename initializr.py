import telebot

bot = telebot.AsyncTeleBot('')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, '/start reaction')


@bot.message_handler(content_types=['text'])
def greeting_react(message):
    if message.text == 'Hello':
        bot.send_message(message.chat.id, 'Hello to you too')
    elif message.text == 'Goodbye':
        bot.send_message(message.chat.id, 'See ya')

bot.polling()


