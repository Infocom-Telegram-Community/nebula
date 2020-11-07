import core.decorators
from core.sql.db_connect import Connection
from core.utility.strings import str_service

@core.decorators.owner.init
def init(update, context):
    connector = Connection()
    chatid = str(update.effective_chat.id)
    community = 1
    welcome = str_service.DEFAULT_WELCOME
    rules = "https://github.com/Squirrel-Network/GroupRules"
    language = "IT"
    query = "INSERT INTO groups(id_group, welcome_text, rules_text, community, languages) VALUES(%s,%s,%s,%s,%s)"
    connector.cur.execute(query,(chatid,welcome,rules,community,language))
    connector.db.commit()
    connector.cur.close()
    connector.db.close()