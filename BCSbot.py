import time
import tweepy
import schedule
import os
from dotenv import load_dotenv

load_dotenv()

CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET =  os.environ.get('CONSUMER_SECRET')
ACCES_KEY =  os.environ.get('ACCES_KEY')
ACCES_SECRET =  os.environ.get('ACCES_SECRET')

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCES_KEY, ACCES_SECRET)
api = tweepy.API(auth)

def upload_media(text, filename):
    media = api.media_upload(filename)
    api.update_status(text, media_ids=[media.media_id_string])


def make_tweet():
    upload_media('#BetterCallSaul', 'BCSvideo.mp4')
    print("done")


schedule.every().monday.at("16:30").do(make_tweet)

while True:
    schedule.run_pending()
    time.sleep(1)

