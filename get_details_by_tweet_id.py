import requests
from details import *

def get_details_by_tweet_id(tweet_id):
    url = "https://api.twitter.com/2/tweets/"+ tweet_id  + "?tweet.fields=attachments,public_metrics,author_id,in_reply_to_user_id,conversation_id&expansions=attachments.media_keys&media.fields=variants,preview_image_url"
    payload={}
    headers = {
    'Authorization': 'Bearer ' + bearer_token,
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return response