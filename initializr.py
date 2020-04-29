import telebot
from emoji import emojize

bot = telebot.AsyncTeleBot('')
dartz = emojize(":dart:", use_aliases=True)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, '/start reaction')


@bot.message_handler(content_types=['text'])
def greeting_react(message):
    if message.text.lower() == 'hello':
        bot.send_message(message.chat.id, 'Hello to you too')
    elif message.text.lower() == 'goodbye':
        bot.send_message(message.chat.id, 'See ya')
    elif message.test.lower() == 'luck':
        bot.send_message(emojize(dartz))


bot.polling()


