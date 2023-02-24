import requests
import telegram
import re
import os

from telegram.ext import CommandHandler, ConversationHandler, MessageHandler, Updater
from telegram. import Bot, BotCommand
from telegram.ext import filters

import logging
#logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def start(update_obj, context):
    """
    Entry point for the conversation
    """
    first_name = update_obj.message.from_user['first_name']
    update_obj.message.reply_text(
        f'Hi {first_name},\nDo you want to write a note?',
        reply_markup=telegram.ReplyKeyboardMarkup([['Yes', 'No']], one_time_keyboard=True, resize_keyboard=True)
    )
    return START_NOTE


def start_note(update_obj, context):
    """
    Ask whether to start process of note creation or cancel
    """
    if update_obj.message.text.lower() in ['yes', 'y']:
        update_obj.message.reply_text(
            'Write a title for the note.',
            reply_markup=telegram.ReplyKeyboardMarkup([['/cancel']], one_time_keyboard=True, resize_keyboard=True)
        )
        return NOTE_TITLE
    else:
        return CANCEL


def note_title(update_obj, context):
    """
    Request to write a note title
    """
    context.user_data['note_title'] = update_obj.message.text
    update_obj.message.reply_text(
        'Write text for the note.',
        reply_markup=telegram.ReplyKeyboardMarkup([['/cancel']], one_time_keyboard=True, resize_keyboard=True)
    )
    return NOTE_TEXT


def note_text(update_obj, context):
    """
    Request to write a note text
    """
    context.user_data['note_text'] = update_obj.message.text
    note_url = post_note_to_app(context.user_data['note_title'], context.user_data['note_text'])
    update_obj.message.reply_text(f'Here is your note:\n{note_url}')
    return ConversationHandler.END


def post_note_to_app(note_title, note_text):
    """
    Send POST request with note to the app
    """
    URL = APP_URL + '/notes'
    client = requests.session()

    client.get(URL)
    csrftoken = client.cookies['csrftoken']

    data = {
        'note_title': note_title,
        'note_text': note_text,
        'csrfmiddlewaretoken': csrftoken
    }
    response = client.post(URL + '/create', data=data, verify=False)
    return response.url


def cancel(update_obj, context):
    """
    Cancel conversation
    """
    first_name = update_obj.message.from_user['first_name']
    update_obj.message.reply_text(
        f'Conversation was stopped. See you, {first_name}!', reply_markup=telegram.ReplyKeyboardRemove()
    )
    return ConversationHandler.END


def register_bot_commands():
    """
    Register bot commands to the menu
    Should be called in case commands was added/removed or name/description changed
    """
    command = [
        BotCommand('start', 'Start conversation'),
        BotCommand('help', 'Get help'),
    ]
    bot = Bot(TELEGRAM_API_TOKEN)
    bot.set_my_commands(command)


def help_command(update, context):
    update.message.reply_text('If you need help use Google!')


if __name__ == '__main__':
    TELEGRAM_API_TOKEN = os.environ['TELEGRAM_API_TOKEN']
    START_NOTE, NOTE_TITLE, NOTE_TEXT, CANCEL = range(4)
    YES_NO_REGEX = re.compile(r'^(yes|no|y|n)$', re.IGNORECASE)
    ORACLE_HOST = os.environ['ORACLE_HOST']
    APP_URL = f'http://{ORACLE_HOST}:8000'

    register_bot_commands()
    updater = Updater(TELEGRAM_API_TOKEN)
    handler = ConversationHandler(
          entry_points=[CommandHandler('start', start)],
          states={
                START_NOTE: [MessageHandler(filters.regex(YES_NO_REGEX), start_note)],
                NOTE_TITLE: [MessageHandler(filters.text & (~ filters.command), note_title)],
                NOTE_TEXT: [MessageHandler(filters.text & (~ filters.command), note_text)],
                CANCEL: [MessageHandler(filters.regex(YES_NO_REGEX), cancel)],
          },
          fallbacks=[CommandHandler('cancel', cancel)],
    )
    updater.dispatcher.add_handler(CommandHandler('help', help_command))
    updater.dispatcher.add_handler(handler)
    updater.start_polling()
    updater.idle()
