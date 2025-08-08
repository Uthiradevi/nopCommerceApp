import configparser
import os

config = configparser.ConfigParser()
config_path = os.path.join(os.path.dirname(__file__), '../Configuration/config.ini')
config.read(config_path)

class readconfig:

    @staticmethod
    def getAppUrl():
        url = config.get('common', 'baseurl')
        return url

    @staticmethod
    def getUsername():
        username = config.get('common', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common', 'password')
        return password


