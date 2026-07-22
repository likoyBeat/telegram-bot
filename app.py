import telebot
import os

TOKEN = os.environ.get("8926868737:AAEgdnvgSwGWZca_e1f-hclYU3Io2sQkWYc")
bot = telebot.TeleBot(TOKEN)

# 👇 ДОБАВЬТЕ ЭТУ СТРОЧКУ (ПЕРЕД polling)
bot.remove_webhook()

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет! Я бот на Render! 🚀")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

if __name__ == "__main__":
    print("✅ Бот успешно запущен!")
    bot.polling(none_stop=True)
