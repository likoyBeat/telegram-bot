import telebot
import types
import os
import threading
import time
from flask import Flask, request

############################################################################################################################################################################################################
app = Flask(__name__)

BOT_TOKEN = os.getenv('BOT_TOKEN', '8926868737:AAEgdnvgSwGWZca_e1f-hclYU3Io2sQkWYc')
if not BOT_TOKEN:
    raise ValueError("❌ BOT_TOKEN не установлен в переменных окружения!")

bot = telebot.TeleBot(BOT_TOKEN, parse_mode='HTML')


render_url = os.environ.get('RENDER_EXTERNAL_URL')
if not render_url:
    raise ValueError("❌ RENDER_EXTERNAL_URL не установлен!")

WEBHOOK_URL = f"https://{render_url}/webhook"
#############################################################################################################################################################################################################




@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'ПРИВЕТ')

bot.polling(none_stop=True)




############################################################################################################################################################################################################
@app.route('/webhook', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_str = request.get_data().decode('UTF-8')
        update = telebot.types.Update.de_json(json_str)
        bot.process_new_updates([update])
        return 'OK', 200
    return 'Bad request', 400

@app.route('/')
def index():
    return "✅ Bot is running!", 200

@app.route('/health')
def health():
    return {"status": "ok", "bot": "running"}, 200

def start_flask():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False, threaded=True)

if __name__ == '__main__':
    import time
    import threading

    print("=" * 50)
    print("🤖 Запуск бота (Webhook + Flask)")
    
    flask_thread = threading.Thread(target=start_flask, daemon=True)
    flask_thread.start()
    print("✅ Flask запущен в фоновом потоке")

    time.sleep(3)

    render_url = os.environ.get('RENDER_EXTERNAL_URL')
    if render_url:
        webhook_url = f"https://{render_url.replace('https://', '')}/webhook"
        print(f"🔗 Webhook URL: {webhook_url}")
        try:
            bot.remove_webhook()
            time.sleep(1)
            bot.set_webhook(url=webhook_url)
            print("✅ Webhook установлен")
        except Exception as e:
            print(f"❌ Ошибка webhook: {e}")
    else:
        print("⚠️ RENDER_EXTERNAL_URL не найден, webhook не установлен")

    print("🚀 Бот готов к работе!")
    print("=" * 50)

    try:
        while True:
            time.sleep(60)
    except KeyboardInterrupt:
        print("🛑 Остановка бота")

############################################################################################################################################################################################################


bot.infinity_polling()
