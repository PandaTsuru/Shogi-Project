import configparser

class Config:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.cfg')

    def save(self):
        pass