import core.decorators
from core.sql.db_connect import Connection

#@core.decorators.owner.init
def init(update, context):
    bot = context.bot
    message = update.message.text[2:]
    chat = update.effective_chat.id
    connector = Connection()
    query = "SELECT * FROM groups WHERE id_group = %s"
    connector.cur.execute(query,[chat])
    rows = connector.cur.fetchall()
    for group in rows:
        chatid = group[1]
        bot.send_message(chatid,message,parse_mode='HTML')