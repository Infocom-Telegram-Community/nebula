class Config(object):
    #########################################################################
    #                            GENERAL CONFIG                             #
    #########################################################################
    BOT_API = "INSERT API HERE"
    BOT_USER = " @thenebula_bot"
    BOT_NAME = "nebula"
    AUTHOR = " SquirrelNetwork"
    VERSION = " 7.8.3(Glaceon)"
    SOURCE = "https://github.com/Squirrel-Network/nebula"
    LOAD_PLUGINS = True
    #########################################################################
    #                            TELEGRAM CONFIG                            #
    #########################################################################
    STAFF_GROUP = -123456789101112
    SUPERADMIN = {
        'foo': 123456789,
        'bar': 123456789
    }
    OWNER = {
        'foo': 123456789,
        'bar': 123456789
    }
    LOG_CHANNEL = -123456789101112
    #########################################################################
    #                            API CONFIG                                 #
    #########################################################################
    YANDEX_API = 'INSERT TOKEN HERE, VISIT: https://tech.yandex.com/translate'
    OPENWEATHER_API = 'INSERT TOKEN HERE, VISIT: https://openweathermap.org/api'
    #########################################################################
    #                            DATABASE CONFIG                            #
    #########################################################################
    DATABASE_CONFIG = {
        'server': 'localhost',
        'port': 3306,
        'name': 'dbname',
        'user': 'dbuser',
        'password': 'password',
        }