import sys
from exceptions import CustomException
from logger import logging

class APIKeys:
    def __init__(self, filepath):
        self.filepath = filepath
        self.keys = self.read_keys_from_file()

    def read_keys_from_file(self):
        try:
            keys = {}
            with open(self.filepath, 'r') as file:
                for line in file:
                    key, value = line.strip().split(': ')
                    keys[key.replace(" ", "_")] = value
            logging.info("Read keys from file")
            return keys
        except Exception as e:
            raise CustomException(e,sys)

    def get_keys(self):
        return self.keys