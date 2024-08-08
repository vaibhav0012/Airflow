import sys
import os
import json
import pandas as pd
from datetime import datetime
import s3fs
from logger import logging
from exceptions import CustomException
from Keys import APIKeys
from utils import Connect

keys_instance = APIKeys("E:\Projects\Airflow\\access_keys.txt")
keys = keys_instance.get_keys()

access_key = keys['Access_Token']
access_secret = keys['Access_Token_Secret']
consumer_key = keys['API_Key']
consumer_secret = keys['API_Key_Secret']

connection = Connect(access_key,access_secret,consumer_key,consumer_secret)

api = connection.conn()
#print(access_key, access_secret, consumer_key, consumer_secret)

##Can't use this as twitter now X requires V2 and it is paid. The below code will fetch list of users for the given screen name

try:
    text = api.get_lists(screen_name = '@elonmusk')#,
                  #count = 50,
                  #exclude_replies = True,
                  #include_rts = False,
                  #tweet_mode = 'extended')
    logging.info('User timeline data fetched')
except Exception as e:
    raise CustomException(e,sys)
print(text)
#
