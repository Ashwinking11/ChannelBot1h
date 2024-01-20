import os
import loguru


ENVIRONMENT = os.environ.get('ENVIRONMENT', False)
LOGGER = loguru.logger
if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', 7324525))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', d28604398dc13af15dd108bb34a27a54)
    OWNER_ID = os.environ.get('OWNER_ID', 1966867320)
    BOT_TOKEN = os.environ.get('BOT_TOKEN', 6509653210:AAEap5ed7KpIh-6Ym679jZzNcAhYORvHJ_k)
    DATABASE_URL = os.environ.get('DATABASE_URL', mongodb+srv://ROKU:ROKU@cluster0.nxjre0s.mongodb.net/?retryWrites=true&w=majority)
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")  # Sqlalchemy dropped support for "postgres" name.
    # https://stackoverflow.com/questions/62688256/sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy-dialectspostgre
    MUST_JOIN = os.environ.get('MUST_JOIN', None)
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN.replace("@", "")
else:
    # Fill the Values
    API_ID = ... # api id here
    OWNER_ID = ...
    API_HASH = "Hash Here"
    BOT_TOKEN = "TOKEN here"
    DATABASE_URL = "Url here"
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
    MUST_JOIN = "OldLostFriends" # must join channel link here
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN[1:]
