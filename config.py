import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7317392855:AAE3e0OBw0eQNzxmlQEK5h7fDoq__ssmAvg")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "23153159"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "caeb7cd0d33635f3d732c002aa725442")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "5880883533"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://Nischay999:Nischay999@cluster0.5kufo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "savecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
