import sys
print(sys.executable)

from transliterate import to_cyrillic, to_latin
import telebot

TOKEN = '7300811741:AAFnoU5oYx_N4hOxs0fEw6tjR7Qhk2VAVp8'
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Assalomu a'laykum! Xush kelibsiz! ")

bot.polling()





matn = input("Matn kiriting: ").lower()

if matn.isascii():
    matn = to_cyrillic(matn)
else:
    matn = to_latin(matn)
    
print(matn.title())


