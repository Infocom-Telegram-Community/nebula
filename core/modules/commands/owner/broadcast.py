import core.decorators
from core.sql.db_connect import Connection

@core.decorators.owner.init
def init(update, context):
    bot = context.bot
    message = update.message.text[2:]
    connector = Connection()
    query = "SELECT id_group FROM groups"
    connector.cur.execute(query)
    rows = connector.cur.fetchall()
    for a in rows:
        bot.send_message(a,message,parse_mode='HTML')