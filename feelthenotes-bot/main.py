import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def start_command(update, context):
    update.message.reply_text('Type some message here to get started...')


def help_command(update, context):
    update.message.reply_text('If you need help use Google!')


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = make_response(text)
    update.message.reply_text(response)


def make_response(text):
    if text in ['hi', 'hello', 'aloha']:
        return 'Hi dude! How is it going?'
    if text in ['fuck', 'suck', 'dick', 'ass']:
        return 'Ohh, fuck you man! Get outa here!'
    if text in ['bye', 'goodbye']:
        return 'Asta la vista, baby!'


def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    TELEGRAM_API_KEY = os.environ['TELEGRAM_API_TOKEN']
    updater = Updater(TELEGRAM_API_KEY, use_context=True)
    updater.dispatcher.add_handler(CommandHandler('start', start_command))
    updater.dispatcher.add_handler(CommandHandler('help', help_command))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, handle_message))
    updater.dispatcher.add_error_handler(error)
    updater.start_polling()
    updater.idle()


main()
