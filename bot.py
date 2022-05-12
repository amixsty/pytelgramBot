from email import message
import telebot
import random
from telebot import types

from gtts import gTTS
bot = telebot.TeleBot("BE TO CHE")

@bot.message_handler(commands=['start'])
def start_message(message):
	bot.reply_to(message, 'Hello!   ' +  message.from_user.first_name)


@bot.message_handler(commands=['newGame'])
def start_message(message):
	bot.reply_to(message,"Choose a number between 1 to 50.")
	rdm = random.randint(0,50)
	@bot.message_handler(func= lambda m: True)
	def echo(message):
		markup = types.ReplyKeyboardMarkup(row_width=2)
		itembtn1 = types.KeyboardButton('a')	
		a = int(message.text)
		if rdm==a:
			bot.reply_to(message,'nice')
		elif a<rdm:
			bot.reply_to(message,'up')
		elif a>rdm:
			bot.reply_to(message,'down')


@bot.message_handler(commands =['voice'])
def send_voice(message):
    bot.reply_to(message,"Say Something..." + message.from_user.first_name)
    @bot.message_handler(func= lambda m: True)
    def echo(message):
        vice = gTTS(message.text)
        vice.save('voice.mp3')
        voice = open('voice.mp3', 'rb')
        bot.send_voice(message.chat.id, voice)


@bot.message_handler(commands =['age'])
def send_age(message):
    bot.reply_to(message,f"Enter the year that you born.")
    @bot.message_handler(func= lambda m: True)
    def echo(message):
        year = int(message.text)
        now = 1401 - year
        bot.reply_to(message,f"You Are on {now} age.")
        


bot.infinity_polling()
