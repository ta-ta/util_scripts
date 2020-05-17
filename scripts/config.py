import configparser
import os

CONFIG_DIR = '.'
CONFIG_FILE = 'config.ini'

config_ini = configparser.SafeConfigParser()
config_ini.read(os.path.join(CONFIG_DIR, CONFIG_FILE))

ENV = 'development'
if 'ENV' in os.environ:
    if os.environ['ENV'] == 'production':
        ENV = 'production'
    elif os.environ['ENV'] == 'development':
        ENV = 'development'
CONFIG = config_ini[ENV]
