import telebot 
import types

bot = telebot.TeleBot("5860500843:AAFU1nqGiGMy_H37R44nt77r1nXg3HJPNxw") 


@bot.message_handler(commands=['start'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("погода"))
    bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}')

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, 'help information')


bot.polling(none_stop=True)
