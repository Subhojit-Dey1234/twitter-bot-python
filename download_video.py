import requests
from details import *

def download_video(tweet_id,file_name):
    url = "https://video.twimg.com/ext_tw_video/"+ tweet_id +"/pu/vid/640x360/UWmoqg8CfLanbZ1G.mp4?tag=12"

    payload={}
    headers = {
    'Authorization': 'Bearer ' + bearer_token
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    with open(file_name + ".mp4",'wb') as f:
        f.write(response.content)

