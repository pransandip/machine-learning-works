"""
Variables that contain user credentials for Twitter API as well as
client for local MongoDB database.
Intructions:
  - paste your own Twitter credentials into the empty strings.
"""
## Importing libraries
import pymongo

### TWITTER CREDENTIALS ###
CONSUMER_API_KEY = "qxbjqXT4LlblLXCax7cyiHRDg"
CONSUMER_API_SECRET = "3SEh55bTRbIFGOpifxFUubkYVLbtHlfb8KfbLDYxMFL7L8W8UN"
ACCESS_TOKEN = "1270856140935401472-o6JJZtCMTLdAqbeMHnbIdDkLvq4qxA"
ACCESS_TOKEN_SECRET = "vesQIdyXS3Olefm91yEKb1lZxqr1eKlZHy6sw2ZOciQB5"

### CONNECTING TO LOCAL MONGODB ###
LOCAL_CLIENT = pymongo.MongoClient("mongodb+srv://dbUserSandy:dbsandy1235@cluster0.wmwuc.mongodb.net/test")
