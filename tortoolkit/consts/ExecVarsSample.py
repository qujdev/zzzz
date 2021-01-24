try:
    from .ExecVars import ExecVars
except:
    class ExecVars:
        # TODO optimize for vps use fully - currently only heroku is focused
        # Set true if its VPS [currently not fully working]
        IS_VPS = False
        API_HASH = "649e419e5fa739da02b649780d492c1b"
        API_ID = 2048409
        BOT_TOKEN = "1416905671:AAFphEyYU2aln3aDrKZFZe6sWO_g_0h-IWU"
        BASE_URL_OF_BOT = "http://t.me/zunixbot"
        # ALLOWED USERS [ids of user or supergroup] seperate by commas
        ALD_USR = [1464067320,911646244,-1001287210872]
        
        # Time to wait before edit message
        EDIT_SLEEP_SECS = 20

        # Telegram Upload Limit (in bytes)
        TG_UP_LIMIT = 2097152000

        # Should force evething uploaded into Document
        FORCE_DOCUMENTS = False

        # Chracter to use as a completed progress 
        COMPLETED_STR = "■"

        # Chracter to use as a incomplete progress
        REMAINING_STR = "□"

        # DB URI for access
        DB_URI = "postgresql://postgres:toolkiit@postgresql/postgres"
        
        # UNCOMMENT THE BELOW LINE WHEN USING CONTAINER AND COMMENT THE UPPER LINE
        #DB_URI = "dbname=tortk user=postgres password=your-pass host=db port=5432"
        
        # The base direcory to which the files will be upload if using RCLONE
        RCLONE_BASE_DIR = "/movie"

        # This value will be considered only if Rclone is True - this may be defied now ;)
        # Cuz at least one needs to be Ture at a time either RCLONE or Leech.
        LEECH_ENABLED = True

        # Will be enabled once its set
        # For vps change it to True if config loaded
        RCLONE_ENABLED = True

        # If the user fails to select whether to use rclone or telegram to upload this will be the deafult.
        DEFAULT_TIMEOUT = "leech"

        # For vps set path here or you can use runtime too
        RCLONE_CONFIG = True
        
        # Name of the RCLONE drive from the config
        DEF_RCLONE_DRIVE = ""

        # Max size of a playlist that is allowed (Number of videos)
        MAX_YTPLAYLIST_SIZE = 20
        
        # Max size of the torrent allowed
        MAX_TORRENT_SIZE = 20

        # This is to stop someone from abusing the system by imposing the limit
        # [<GBs of total torrent sapce>, <Number of youtube videos allowed to download>, <Number of youtube playlists allowed to download>]
        USER_CAP_ENABLE = False
        USER_CAP_LIMIT = [50,10,2]

        # No need to worry about these
        # CHANGE THESE AT YOUR RISK
        LOCKED_USERS = False
        RSTUFF = False
        FORCE_DOCS_USER = False
        FAST_UPLOAD = True
        METAINFO_BOT = False
        





