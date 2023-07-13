# Ultroid - UserBot
# Copyright (C) 2021-2023 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/TeamUltroid/pyUltroid/blob/main/LICENSE>.

import sys

from decouple import config

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass


class Var:
    # mandatory
    API_ID = (
        int(sys.argv[1]) if len(sys.argv) > 1 else config("API_ID", "22384918")
    )
    API_HASH = (
        sys.argv[2]
        if len(sys.argv) > 2
        else config("API_HASH", "e40542b28c7d67e35933265c0c8aa6f9")
    )
    SESSION = sys.argv[3] if len(sys.argv) > 3 else config("SESSION", "BQAZXDeG-sP3RQbtN7rNUxEwbGCX6I2aJ6wIxhGoYqR_cuo6PnAemMDsaojpAnyl4zsrrwGl0VAvuqoTahky6FNGHCR_0X8u1vEn6V09oSe52RtX3qhXiLWLG_jm_Plfi0KqYD3z8E4RfHreAmw0R6R75RKgBlC0aC1ERnpHcrhnaVz2eNhPG0f-i7voNJPjqfSBiMYOGBG1oTJv7m7xH2hV8wEs8XDNqyhY-6CMDSTcZZ5d_TErLQbs6YeDKHkDgm5nWIKE8rATjzTmHiz4hN0DkjbhBfc2ofWjZO2D8yi744UgCj6AHiPtntATRQWgomR3S58_3nAZa7SSqX2Z2wXiAAAAATNMSd8A")
    REDIS_URI = (
        sys.argv[4]
        if len(sys.argv) > 4
        else (config("REDIS_URI", default=None) or config("REDIS_URL", default=None))
    )
    REDIS_PASSWORD = (
        sys.argv[5] if len(sys.argv) > 5 else config("REDIS_PASSWORD", default=None)
    )
    # extras
    BOT_TOKEN = config("BOT_TOKEN", "6024729546:AAHpi97T4ZWnmxjIAPjYOeYxpVLY-K07Zgg")
    LOG_CHANNEL = config("LOG_CHANNEL", default=None)
    HEROKU_APP_NAME = config("HEROKU_APP_NAME", default=None)
    HEROKU_API = config("HEROKU_API", default=None)
    VC_SESSION = config("VC_SESSION", default=None)
    ADDONS = config("ADDONS", default=False, cast=bool)
    VCBOT = config("VCBOT", default=False, cast=bool)
    # for railway
    REDISPASSWORD = config("REDISPASSWORD", default=None)
    REDISHOST = config("REDISHOST", default=None)
    REDISPORT = config("REDISPORT", default=None)
    REDISUSER = config("REDISUSER", default=None)
    # for sql
    DATABASE_URL = config("DATABASE_URL", default=None)
    # for MONGODB users
    MONGO_URI = config("MONGO_URI", "mongodb+srv://ammu:ammu@cluster0.mwezmkc.mongodb.net/?retryWrites=true&w=majority")
