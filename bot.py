#!/usr/bin/env python3

import telebot

bot = telebot.TeleBot("1345314264:AAH-XncoXXYvWsyBZwM7m38I0fm-BC6gp7w")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    bot.send_message(message.chat.id, message.text)

bot.polling( none_stop = True )