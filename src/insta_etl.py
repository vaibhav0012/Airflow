import instaloader
import pandas as pd
from utils import data_input
from exceptions import CustomException
from logger import logging
import sys
from concurrent.futures import ThreadPoolExecutor
from functools import partial
from Keys import APIKeys 
# Creating an instance of the Instaloader class
bot = instaloader.Instaloader()
 
# Loading a profile from an Instagram handle
di = data_input()
usernames = di.read_usernames(r"E:\Projects\Airflow\usernames.csv")
#print (usernames)

keys_instance = APIKeys("E:\Projects\Airflow\credentials.txt")
keys = keys_instance.get_keys()

USERNAME = keys['USERNAME']  # Replace with your Instagram username
PASSWORD = keys['PASSWORD']  # Replace with your Instagram password
bot.login(USERNAME, PASSWORD)  
def fetch_profile(bot, username):
    try:
        profile = instaloader.Profile.from_username(bot.context, username)
        return {
            'Username': profile.username,
            'User ID': profile.userid,
            'Number of Posts': profile.mediacount,
            'Followers Count': profile.followers,
            'Following Count': profile.followees,
            'Bio': profile.biography,
            'External URL': profile.external_url
        }
    except instaloader.exceptions.ProfileNotExistsException:
        print(f"Profile {username} does not exist.")
        return None
    except Exception as e:
        raise CustomException(e, sys)

# Prepare to call fetch_profile with bot pre-bound
partial_fetch_profile = partial(fetch_profile, bot)

try:
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(partial_fetch_profile, usernames))
        logging.info("Data Ingestion Completed!")
except Exception as e:
    raise CustomException(str(e), sys)

# Filter out None results
results = [r for r in results if r is not None]

# Create DataFrame
df = pd.DataFrame(results)

print(df.head(10))