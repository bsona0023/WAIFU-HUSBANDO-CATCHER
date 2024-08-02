class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6107980637"
    sudo_users = "6107980637", "1946601503"
    GROUP_ID = -1002025625952
    TOKEN = "6721894255:AAFwajY_j4ZioF9008BVvjy-D3g34GFI4tc"
    mongo_url = "mongodb+srv://mrdevil12:mrdevil12@devil.8sdjynz.mongodb.net/?retryWrites=true&w=majority&appName=Devil"
    PHOTO_URL = ["https://telegra.ph/file/b0c4f9723cdb26495649c.jpg", "https://telegra.ph/file/f668ee0a0f8987d7f340a.jpg"]
    SUPPORT_CHAT = "devilbotsupport"
    UPDATE_CHAT = "devilbots971"
    BOT_USERNAME = "animexwaifusBot"
    CHARA_CHANNEL_ID = "-1002174702412"
    api_id = 21436816
    api_hash = "c269918dddddbc041d536207cab72155"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
