import core.decorators
from core.sql.db_connect import Connection
from core.sql.commands_sql import Sql_Insert_BW

@core.decorators.admin.user_admin
@core.decorators.delete.init
def init(update, context):
    message = update.message.text[8:].strip()
    connector = Connection()
    chatid = str(update.effective_chat.id)
    query = Sql_Insert_BW.SQL
    connector.cur.execute(query,[message,chatid])
    connector.db.commit()
    connector.cur.close()
    connector.db.close()