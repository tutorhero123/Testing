import telebot

TOKEN = "6526119394:AAEZ5h35ZqZtBIa1kV8abgTXftfLF52Kv9s"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot.reply_to(message, "Hello! I am your Telegram bot. How can I help you today?")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)


if __name__ == "__main__":
    bot.polling()
