from Almortagel.core.bot import Dil
from Almortagel.core.dir import dirr
from Almortagel.core.git import git
from Almortagel.core.userbot import Userbot
from Almortagel.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Dil()
userbot = Userbot()



Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
