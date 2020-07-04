import tweepy
import os
import time

# credentials to access the twitter
consumer_key = os.environ.get('consumer_key')
consumer_secret = os.environ.get('consumer_secret')
access_token = os.environ.get('access_token')
access_token_secret = os.environ.get('access_token_secret')

# Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user = api.me()  # if you print this line it will display the your user name

following = ['<enter the userid of people you follow >']


# If you hit the twitter server more than the specified times it will block the user ,to avoid that you need the
# following function .But i have not used since i need only tweets from the single user

def limit_handler(Cursor):
    try:
        while True:
            try:
                yield Cursor.next()
            except:
                pass
    except tweepy.RateLimitError:
        time.sleep(250)


def get_tweets():
    with open('tweet.txt', mode='w', encoding='utf-8') as fp:
        for person in following:
            fp.write(f"\n\nPerson:{person} \n\n")
            tweets = api.user_timeline(person)
            for tweet in tweets:
                fp.write(f"{tweet.text} \n")
