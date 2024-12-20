# This file is a part of FileStreamBot
from urllib import request
from os import environ
from dotenv import load_dotenv

load_dotenv()


class Var(object):
    MULTI_CLIENT = False
    API_ID = int(environ.get("API_ID", "24401235"))
    API_HASH = str(environ.get("API_HASH", "149f7e13d7d861b27cffc3ab1fd52b22"))
    BOT_TOKEN = str(environ.get("BOT_TOKEN", "7641854793:AAHITKl7nCQ80MDR6I6rw4wolm5qp7ed2vc"))
    SLEEP_THRESHOLD = int(environ.get("SLEEP_THRESHOLD", "60"))  # 1 minte
    WORKERS = int(environ.get("WORKERS", "6"))  # 6 workers = 6 commands at once
    BIN_CHANNEL = int(
        environ.get("BIN_CHANNEL", "-1002464478619")
    )  # you NEED to use a CHANNEL when you're using MULTI_CLIENT
    PORT = int(environ.get("PORT", 56))
    BIND_ADDRESS = str(environ.get("WEB_SERVER_BIND_ADDRESS", "0.0.0.0"))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    HAS_SSL = str(environ.get("HAS_SSL", "0").lower()) in ("1", "true", "t", "yes", "y")
    NO_PORT = str(environ.get("NO_PORT", "0").lower()) in ("1", "true", "t", "yes", "y")
    FQDN = str(environ.get("FQDN", BIND_ADDRESS))
    URL = "http://103.160.106.178:56/".format(
            "s" if HAS_SSL else "", FQDN, "" if NO_PORT else ":" + str(PORT)
        )

    DATABASE_URL = str(environ.get('DATABASE_URL', "mongodb+srv://avineyjr004:Team_HDSTR@cluster0.oxbmm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"))
    UPDATES_CHANNEL = str(environ.get('UPDATES_CHANNEL', "Telegram"))
    OWNER_ID = int(environ.get('OWNER_ID', "7255612720"))
    SESSION_NAME = str(environ.get('SESSION_NAME', 'hydroBot'))
    FORCE_UPDATES_CHANNEL = environ.get('FORCE_UPDATES_CHANNEL', False)
    FORCE_UPDATES_CHANNEL = True if str(FORCE_UPDATES_CHANNEL).lower() == "true" else False
    ALLOWED_USERS = [x.strip("@ ") for x in str(environ.get("ALLOWED_USERS") or "").split(",") if x.strip("@ ")]

    KEEP_ALIVE = str(environ.get("KEEP_ALIVE", "0").lower()) in  ("1", "true", "t", "yes", "y")
    IMAGE_FILEID = environ.get('IMAGE_FILEID', "https://cdn.jsdelivr.net/gh/fyaz05/Resources@main/HydroStreamerBot/My%20Files.jpeg")
    TOS = environ.get("TOS", None)
    if TOS:
        response = request.urlopen(TOS)
        data = response.read().decode('utf-8')
        TOS = data.strip()

    MODE = environ.get("MODE", "primary")
    SECONDARY = True if MODE.lower() == "secondary" else False
    LINK_LIMIT = int(environ.get("LINK_LIMIT")) if "LINK_LIMIT" in environ else None
