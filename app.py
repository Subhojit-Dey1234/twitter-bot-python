from get_details_by_tweet_id import get_details_by_tweet_id
from get_tweets import get_tweets
import time
import tweepy
from details import *

frontend_url = 'https://getdownload.me/#/'

previous_tweet = []
is_app_started = False


def run_the_app():
    global previous_tweet
    global is_app_started
    tweets = get_tweets()
    tweets = tweets.json()

    l = len(tweets['data']) - len(previous_tweet)
    print("The App is Running..... " +  l)
    if(l > 0 and is_app_started):

        auth = tweepy.OAuthHandler(api_key,api_key_secret)
        auth.set_access_token(access_token,access_token_secret)
        api = tweepy.API(auth)


        new_tweets = tweets['data'][0:l]
        for new_tweet in new_tweets:
            id = new_tweet['id']
            author_id = new_tweet['author_id']
            user = api.get_user(user_id = author_id)
            username = user.screen_name

            conversation_id = new_tweet["conversation_id"]

            if id == conversation_id:
                continue

            get_details_conversation = get_details_by_tweet_id(conversation_id)
            get_details_conversation = get_details_conversation.json()

            

            if 'includes' in get_details_conversation:
                get_details_conversation_media = get_details_conversation["includes"]["media"]

                for media in get_details_conversation_media:
                    if(media['type'] != 'video'):
                        print('Not a video!!!')
                        break
                    api.update_status(status="@"+username+ " Download link ---- \n" + frontend_url + str(conversation_id),in_reply_to_status_id = id, auto_populate_reply_metadata = True)
                    time.sleep(4)
    previous_tweet = tweets['data']
    is_app_started = True