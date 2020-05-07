class Config(object):
    #########################################################################
    #                            GENERAL CONFIG                             #
    #########################################################################
    BOT_API = "%BOT_API%"
    BOT_USER = "%BOT_USER%"
    BOT_NAME = "%BOT_NAME%"
    AUTHOR = "%AUTHOR%"
    VERSION = "%VERSION%"
    SOURCE = "%SOURCE%"
    #########################################################################
    #                            TELEGRAM CONFIG                            #
    #########################################################################
    STAFF_GROUP = %STAFF_GROUP%
    ADMIN_ID = %ADMIN_ID%
    OWNER = %OWNER%
    LOG_CHANNEL = %LOG_CHANNEL%
    #########################################################################
    #                            API CONFIG                                 #
    #########################################################################
    YANDEX_API = "%YANDEX_API%"
    OPENWEATHER_API = "%OPENWEATHER_API%"
    #########################################################################
    #                            DATABASE CONFIG                            #
    #########################################################################
    DATABASE_CONFIG = {
        "server": "%DATABASE_SERVER%",
        "user": "%DATABASE_USERNAME%",
        "password": "%DATABASE_PASSWORD%",
        "name": "%DATABASE_NAME%",
    }

    LOAD_PLUGINS = True
