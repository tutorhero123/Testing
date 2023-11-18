import telebot
import os
from flask import Flask, request

TOKEN = "6526119394:AAEZ5h35ZqZtBIa1kV8abgTXftfLF52Kv9s"
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)


@app.route(f"/{TOKEN}", methods=["POST"])
def getMessage():
    bot.process_new_updates(
        [telebot.types.Update.de_json(request.stream.read().decode("utf-8"))]
    )
    return "!", 200


@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot.reply_to(message, "Hello! I am your Telegram bot. How can I help you today?")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    # Do something with the message (optional)
    pass


if __name__ == "__main__":
    # Remove any existing webhook to avoid conflicts
    bot.remove_webhook()

    # Set the webhook for Azure deployment
    bot.set_webhook(url=f"unblur.azurewebsites.net/{TOKEN}")

    # Run the Flask web application
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
