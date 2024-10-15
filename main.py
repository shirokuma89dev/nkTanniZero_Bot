import tweepy
import os
import argparse

API_KEY = os.getenv('API_KEY')
API_SECRET_KEY = os.getenv('API_SECRET_KEY')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_SECRET_TOKEN = os.getenv('ACCESS_SECRET_TOKEN')

client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET_KEY,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_SECRET_TOKEN
)

auth = tweepy.OAuth1UserHandler(
    API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_SECRET_TOKEN
)
api = tweepy.API(auth)

parser = argparse.ArgumentParser()
parser.add_argument("tweet", help="the text of the tweet")
parser.add_argument(
    "-i", "--images", nargs="*", help="the images to attach to the tweet"
)
args = parser.parse_args()
# args.tweet += " #おはよう"

media_ids = []
if args.images:
    for image_path in args.images:
        media = api.media_upload(filename=image_path)
        media_ids.append(media.media_id)

try: 
    if not media_ids:
        client.create_tweet(text=args.tweet)
    else:
        client.create_tweet(text=args.tweet, media_ids=media_ids)
        
except Exception as e:
    print(e)
    print("Error creating tweet")
