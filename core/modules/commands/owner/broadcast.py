import core.decorators
from core.sql.db_connect import Connection

@core.decorators.owner.init
def init(update, context):
    bot = context.bot
    message = update.message.text[2:]
    connector = Connection()
    query = "SELECT * FROM groups"
    connector.cur.execute(query)
    rows = connector.cur.fetchall()
    for a in rows:
        chatid = a[1]
        bot.send_message(chatid,"<b>BROADCAST:</b> {}".format(message),parse_mode='HTML')