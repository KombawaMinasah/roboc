class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 20247370
    API_HASH = "813309fab8cd9fce260ce7269e543bdb"

    CASH_API_KEY = "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"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "mongodb+srv://biawakbatam:1234@cluster0.87jdbad.mongodb.net/?retryWrites=true&w=majority"  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1001881201311)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://biawakbatam:1234@cluster0.87jdbad.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://te.legra.ph/file/40eb1ed850cdea274693e.jpg"

    SUPPORT_CHAT = "neroosuport"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "6861812262:AAF48WtPnhHNV9qKybMLT370eabgLpPr4dw"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = ""  # Get this value from https://timezonedb.com/api

    OWNER_ID = 1748872441  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = [1748872441]  # User id of sudo users
    DEV_USERS = [1748872441]  # User id of dev users
    DEMONS = [1748872441]  # User id of support users
    TIGERS = [1748872441]  # User id of tiger users
    WOLVES = [1748872441]  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
