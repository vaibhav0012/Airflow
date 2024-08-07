import sys
import os
import json
from logger import logging
from exceptions import CustomException
import tweepy
import pandas as pd
from datetime import datetime
import s3fs
from Keys import APIKeys

keys_instance = APIKeys("E:\Projects\Airflow\\access_keys.txt")
keys = keys_instance.get_keys()

access_key = keys['Access_Token']
access_key_secret = keys['Access_Token_Secret']
consumer_key = keys['API_Key']
consumer_secret = keys['API_Key_Secret']

