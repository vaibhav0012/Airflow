import sys
import tweepy
from exceptions import CustomException
from logger import logging

class Connect():
    def __init__(self,access_key,access_secret,consumer_key,consumer_secret):
        self.access_key = access_key
        self.access_secret = access_secret
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
    def conn(self):
        '''
        Used for creating a connection to twitter using the token keys
        '''
        try:
            auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)  # First pass the API key and secret
            auth.set_access_token(self.access_key, self.access_secret)
            api = tweepy.API(auth)
            logging.info("Api Connection established")
            return api
        except Exception as e:
            raise CustomException(e,sys)

class data_input():
    def __init__(self):
        pass
    def read_usernames(self,filename):
        """
        Reads usernames from a given file and returns them as a list.
        """
        usernames = []
        with open(filename, 'r') as file:
            for line in file:
                # Strip whitespace and newline characters
                clean_line = line.strip()
                # Skip empty lines and possibly the header if present
                if clean_line and clean_line.lower() != 'name' and clean_line.lower() != 'instagram':
                    usernames.append(clean_line)
        return usernames