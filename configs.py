# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "3335796"))
    API_HASH = getenv("API_HASH", "138b992a0e672e8346d8439c3f42ea78")
    BOT_TOKEN = getenv("BOT_TOKEN", "5088657122:AAGByZ5PLpv205PaXhxDEZ_JixPIn1OaVnk")
    FSUB = getenv("FSUB", "seriesplus1)
    CHID = int(getenv("CHID", "-1001792962793"))
    SUDO = list(map(int, getenv("SUDO", "6168162777").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://abirhasan2005:abirhasan@cluster0.i6qzp.mongodb.net/cluster0?retryWrites=true&w=majority")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
