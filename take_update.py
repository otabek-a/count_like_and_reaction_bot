from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
import os
from tinydb import TinyDB
take=TinyDB('take_information.json')
TOKEN=os.environ['Token']
def start(update,context):
    keyboard = [
        [InlineKeyboardButton("REACTION...", callback_data='reaction')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Pls tap reaction...',reply_markup=reply_markup)

def button(update, context):
    query = update.callback_query
    user = query.from_user
    take.insert({'user_id': user.id, 'username': user.username, 'first_name': user.first_name})
    print(user)
updater = Updater(TOKEN)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CallbackQueryHandler(button))
updater.start_polling()
updater.idle()