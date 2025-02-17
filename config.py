from os import environ as env

class Config:
    API_ID = int(env.get("API_ID", "28744454")) #TG API ID
    API_HASH = env.get("API_HASH", "debd37cef0ad1a1ce45d0be8e8c3c5e7") #TG API HASH
    BOT_TOKEN = env.get("BOT_TOKEN", "7560586869:AAG7uvxJQXURcatwG92E38kq_zEsDJ7WIdQ") #Add Bot Token, get from botfather
    FSUB_ID = int(env.get("FSUB_ID", "-1002410513772"))  #Add Your FSub Channel Id -100xxxxxxxxx
    FSUB = bool(env.get("FSUB", True)) #Keep True If U Want Force Subscribe         
    SB_PIC = env.get("SB_PIC", "https://i.ibb.co/c6vkVBP/photo-2024-11-15-12-13-41-7437478159336865812.jpg") # Add Link For Start Cmd Picture 
    BOT_USERNAME = env.get("BOT_USERNAME", "Emiting_Auto_Reaction_Bot") # Add Bot Username Without @
    EMOJIS = [
        "👍", "👎", "❤", "🔥", 
        "🥰", "👏", "😁", "🤔",
        "🤯", "😱", "🤬", "😢",
        "🥶", "🤩", "🤮", "💩",
        "🙏", "👌", "🤣", "🤡",
        "🥱", "🥴", "😍", "🤓",
        "❤‍🔥", "🌚", "😐", "💯",
        "🤣", "⚡", "🍌", "🏆",
        "💔", "🤨", "😐", "😡",
        "👅", "🆒", "🖕", "😈",
        "😴", "😭", "👻", "⚡",
        "👨‍💻", "👀", "🎃", "🙄",
        "😇", "😨", "🤝", "🤐",
        "🤗", "🫡", "🎅", "🥸",
        "🤫", "😶‍🌫", "🤪", "😏",
        "😘", "👾", "🤷‍♂", "😎"
    ]
