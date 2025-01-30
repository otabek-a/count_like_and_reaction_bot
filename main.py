from telegram.ext import Updater,MessageHandler,Filters,CommandHandler,CallbackContext,Filters, CallbackQueryHandler
from telegram import Bot, Update,InlineKeyboardButton,InlineKeyboardMarkup
import os
from tinydb import TinyDB
emoji=TinyDB('emoji.json')















def info(update: Update, context):
    photo=update.message.photo[-1]
    file_id=photo.file_id
    
    update.message.reply_photo(photo=file_id,caption='hey bro , for add emojies send me them')






















def start(update: Update, context):
    update.message.reply_text("Hey please send photo for work this bot")

TOKEN = '7554317270:AAHn7TeDzbxCl3LJ3XXOKPnjMK8oZ-R53Jc'

updater = Updater(token=TOKEN)

dispatcher = updater.dispatcher

# add handlers here



dispatcher.add_handler(MessageHandler(Filters.photo, info))

dispatcher.add_handler(CommandHandler('start',start))

updater.start_polling()
updater.idle()