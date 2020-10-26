from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from core.utility import utils

def init(update, context):
    bot = context.bot
    message=str(update.message.text[7:]).strip()
    if message != "":
        msg = "Here are the results of your Google search"
        gurl = "https://www.google.com/search?&q={0}".format(message.replace(' ','+'))
        button_list = [InlineKeyboardButton("Go to =>", url=gurl)]
        reply_markup = InlineKeyboardMarkup(utils.build_menu(button_list, n_cols=1))
        bot.send_message(update.message.chat_id,
                     text=msg,reply_markup=reply_markup,
                     parse_mode='HTML')
    else:
        bot.send_message(update.message.chat_id, text="Devi digitare un criterio di ricerca!")