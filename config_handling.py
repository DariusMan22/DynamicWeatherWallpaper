import configparser

def get_key():
    """gets key from the confing,ini"""

    config = configparser.ConfigParser()
    config.read('config.ini')
    section = "DEFAULT"
    subSection = "api_key"
    return config[section][subSection]
