from configparser import ConfigParser


config = ConfigParser()

config.read('weather_app.ini')
api_key = config['DEFAULT']['api']
# print(api_key)
# print(type(api_key))

def give_my_key():
    return api_key
