from telegram.ext import Updater,MessageHandler,Filters,CommandHandler,CallbackContext, CallbackQueryHandler
from telegram import Bot, Update,InlineKeyboardButton,InlineKeyboardMarkup
import os
from tinydb import TinyDB,Query
User=Query()
db=TinyDB('db.json')
def start(update: Update, context):
    update.message.reply_text("Hey please send photo for work this bot")





    
def info(update: Update, context):
    photo=update.message.photo[-1]
    file_id=photo.file_id
    emojis = db.all()
    if emojis:
       buttons=[
           [InlineKeyboardButton(text=f"{emoji['emoji']} ({emoji['count']})",callback_data=f"{i}")]
           for i,emoji in enumerate(emojis)]
       inline_keyboard = InlineKeyboardMarkup(buttons)
       update.message.reply_photo(photo=file_id, caption='If you want to add more emoji please send it.', reply_markup=inline_keyboard)
    else:
        update.message.reply_photo(photo=file_id, caption='I am so sorry , you dont have any emojies.')

       

   

def add_emoji(update, context):
    db.insert({"emoji": update.message.text,'count':0})
    update.message.reply_text("Good job i added your emoji to your list")



def button_callback(update: Update, context: CallbackContext):
    query = update.callback_query
    index = int(query.data)
    emojis = db.all()
    matn=emojis[index]
    matn['count']+=1
    db.update({'count':matn['count']},User.emoji==matn['emoji'])
    buttons = [
        [InlineKeyboardButton(
            text=f"{emoji['emoji']} ({emoji['count']})", 
            callback_data=f"{i}"
        )]
        for i, emoji in enumerate(emojis)
    ]
    inline_keyboard = InlineKeyboardMarkup(buttons)
    query.edit_message_reply_markup(reply_markup=inline_keyboard)


    





    

TOKEN = os.environ['TOKEN']

updater = Updater(token=TOKEN)

dispatcher = updater.dispatcher

# add handlers here


dispatcher.add_handler(CommandHandler('start',start))
dispatcher.add_handler(MessageHandler(Filters.text, add_emoji))
dispatcher.add_handler(MessageHandler(Filters.photo, info))
dispatcher.add_handler(CallbackQueryHandler(button_callback))

updater.start_polling()
updater.idle()