#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright hersel91 <hersel1991@gmail.com>
# Copyright SteelManIta
# Copyright JervNorsk


# Python import for error handler and logging
import logging
import sys
from datetime import datetime
from core.utility import error_handler

# Import telegram library
from telegram.ext import (
    Updater,
    CommandHandler as CMH,
    MessageHandler as MH,
    CallbackQueryHandler as CQH,
    ConversationHandler as CH,
    Filters)

# Import local files
import plugins
from config import Config
from core.modules import commands,handler

# if version < 3.6, stop bot.
LOGGER = logging.getLogger(__name__)
if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    LOGGER.error("You MUST have a python version of at least 3.6! Multiple features depend on this. Bot quitting.")
    quit(1)

# Commands Variables
# @param usr = user commands
# @param adm = admin commands
# @param own = owner commands
usr = commands.user
adm = commands.admin
own = commands.owner

timestamp = datetime.strftime(datetime.today(), '%H:%M at %d/%m/%Y')
print("Start Bot {}".format(timestamp))

# This enables the logs
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
#########################################################################
#                           USER COMMAND                                #
#       Here I "create" the commands and assign a function              #
#########################################################################

def commandHandler(dsp):
    FUNCTION = dsp.add_handler

    FUNCTION(CMH("start", usr.start.init))
    FUNCTION(CMH(usr.rules.activationWords, usr.rules.action))
    FUNCTION(CMH("help", usr.help.init))
    FUNCTION(CMH("source", usr.source.init))
    FUNCTION(CMH("io", usr.io.init))
    FUNCTION(CMH("distro", usr.distro.init))
    FUNCTION(CMH("richiedi", usr.request_function.init))
    FUNCTION(CMH("feedback", usr.feedback.init))
    FUNCTION(CMH("traduci", usr.translate.init))
    FUNCTION(CMH("google", usr.search_google.init))
    FUNCTION(CMH("cerca", usr.search_qwant.init))
    FUNCTION(CMH("weather", usr.weather.init))
    FUNCTION(CMH("wikipedia", usr.define.init))
    FUNCTION(CMH("joke", usr.joke.init))
    FUNCTION(CMH("staff", usr.get_staff.init))
    FUNCTION(CMH("gdpr", usr.gdpr.init))
    FUNCTION(CMH("vote", usr.vote.init))
    FUNCTION(CMH("downvote", usr.downvote.init))
    FUNCTION(CMH("score", usr.score.init))

#########################################################################
#                           ADMIN COMMAND                               #
#                   Decorator: @decorator.admin.init                    #
#                   Source: /core/decorators/admin.py                   #
#                                                                       #
#########################################################################
    FUNCTION(CMH("ban", adm.ban.init))
    FUNCTION(CMH("unban",adm.unban.init))
    FUNCTION(CMH("superban", adm.superban.init))
    FUNCTION(CMH("silence", adm.silence.init))
    FUNCTION(CMH("badword", adm.insert_bad_words.init))
    FUNCTION(CMH("kick", adm.kick.init))
    FUNCTION(CMH("info", adm.get.init))
    FUNCTION(CMH("setrisposta", adm.insert_custom_handler.init))
    FUNCTION(CMH("mute", adm.mute.init))
    FUNCTION(CMH("unmute", adm.unmute.init))
    FUNCTION(CMH("pin", adm.pin.init))
    FUNCTION(CMH("say", adm.say.init))
    FUNCTION(CMH("a", adm.announcement.init))
    FUNCTION(CMH("setwelcome", adm.insert_welcome.init))
    FUNCTION(CMH("updatewelcome", adm.update_welcome.init))
    FUNCTION(CMH("listwelcome", adm.list_welcome.init))
    FUNCTION(CMH("setpin", adm.set_pin.init))
    FUNCTION(CMH("add", adm.add_buttons.init))
    FUNCTION(CMH("delete", adm.delete_command.init))
    FUNCTION(CMH("setrules", adm.set_rules.init))
    FUNCTION(CMH("badlist", adm.list_badwords.init))
    FUNCTION(CMH("warn", adm.warn.init))
    FUNCTION(CMH("unwarn", adm.unwarn.init))
    FUNCTION(CMH("enable", adm.register_rep.init))

#########################################################################
#                           OWNER COMMAND                               #
#                   Decorator: @decorator.owner.init                    #
#                   Source: /core/decorators/owner.py                   #
#                                                                       #
#########################################################################
    FUNCTION(CMH("exit", own.leave.init))
    FUNCTION(CMH("b", own.broadcast.init))
    FUNCTION(CMH("server", own.server.init))
    FUNCTION(CMH("setjoke", own.insert_joke.init))
    FUNCTION(CMH("test", own.test.init))

#########################################################################
#                           PLUGINS MODULES                             #
#                                                                       #
#                           Source: /plugins                            #
#                                                                       #
#########################################################################
    if Config.LOAD_PLUGINS == True:
        FUNCTION(CMH("example", plugins.example.init))


#########################################################################
#                CALLBACKQUERY HANDLER(Buttons Update)                  #
#########################################################################
def callbackQueryHandler(dsp):
    FUNCTION = dsp.add_handler
    FUNCTION(CQH(adm.silence.unsilence_button, pattern='unsilence_button'))
    FUNCTION(CQH(handler.admin_command.resolved, pattern='resolved'))
    FUNCTION(CQH(usr.start.welcome_button, pattern='welcome_button'))
    FUNCTION(CQH(usr.start.admin_command, pattern='admin_command'))
    FUNCTION(CQH(usr.start.user_command, pattern='user_command'))
    FUNCTION(CQH(usr.start.back_button, pattern='back_button'))

#########################################################################
#                              MAIN_HANDLER                             #
#               Source: /core/modules/handler/main_handler.py           #
#        Here we call the functions without a command, => handler       #
#########################################################################
def messageHandler(dsp):
    FUNCTION = dsp.add_handler
    FUNCTION(MH(Filters.group, handler.main_handler.init))

# This is the function that initializes the bot
def main():
    updater = Updater(Config.BOT_API, use_context=True)
    dp = updater.dispatcher
    #########################################################################
    #                          FILTERS HANDLER                              #
    #########################################################################
    dp.add_handler(MH(Filters.status_update.new_chat_members, handler.welcome.init))
    dp.add_handler(MH(Filters.document.exe, handler.filters_handler.exe))
    conv_handler = CH(
        entry_points=[CMH("listbutton", handler.delete_buttons.init)],
        states={
            handler.delete_buttons.RECEIVE_ID: [MH(Filters.text & (~ Filters.command), handler.delete_buttons.receive_id)]
        },
        fallbacks=[CMH("cancel", handler.delete_buttons.cancel)]
    )
    dp.add_handler(conv_handler)
    commandHandler(dp)
    callbackQueryHandler(dp)
    messageHandler(dp)

#########################################################################
#                          ERROR HANDLER                                #
#########################################################################
    dp.add_error_handler(error_handler.error)
#########################################################################
#                  START POLLING TELEGRAM API                           #
#########################################################################
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()