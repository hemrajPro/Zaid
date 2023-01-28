import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "22729446")) #optional
API_HASH = getenv("API_HASH", "54b64d721cdcf9332921d8b1224b5fdb") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5444974728").split()))
OWNER_ID = int(getenv("OWNER_ID" , "5444974728" ))
MONGO_URL = getenv("MONGO_URL", "
client = pymongo.MongoClient("mongodb+srv://Hemraj:hemraj123@cluster0.xorfvol.mongodb.net/?retryWrites=true&w=majority")
db = client.test
")
BOT_TOKEN = getenv("BOT_TOKEN", "5798584266:AAHkroZ2Quict1uPVjahdNmxCAkBBkbw-Bo")
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQB6R7NUgJVyHUsvl48zyk6PdK9RZOQWxglAx5WwJ8QYIwkniP9GnLbeAIGo-FOeKVpvafiEnATBpZ7nQdlIrCFg-xFzuDGwrHxUZVJReGtAsmQYskCZ9gLoH7HHZNnhTYpGTNN22QqmkYivi5tOzlkeQlV5Qkw-HsK5fhRwbf7g6a4OIFAHntD6FvoX-Jc-i89X8PyN5aqJwQYPDa6NWYgugajXhBgcinqRxYJmD5tvhU2ymG5G1yk3IL-UVA3eQjPhMcWNIO_SXzf0NQUKgN51KZy0SLqRiViqcFzLmX6hnzBCCpH7FC-7F33yMPqmn-_XXG008ZYAT-xhVv6mzuktAAAAAUSLuIgA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
