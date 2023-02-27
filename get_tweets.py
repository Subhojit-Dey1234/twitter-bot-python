import requests
from details import *

def get_tweets():
      url = "https://api.twitter.com/2/users/" + user_id + "/mentions?tweet.fields=attachments,public_metrics,author_id,in_reply_to_user_id,conversation_id"

      payload={}
      headers = {
        'Authorization': 'Bearer ' + bearer_token,
      }
      response = requests.request("GET", url, headers=headers, data=payload)
      return response