''' Constants config file for pytherm.
    @author: Adrien Vilquin Barrajon <avilqu@gmail.com>
'''

BASE_DIR = '/sys/bus/w1/devices/'         # System one-wire directory
DATA_DIR = '/home/pi/pytherm/data/'       # Data storage folder
RECORD_INTERVAL = 60                      # Record interval (seconds)
DB_FILE = 'homepy.db'
SQL_INIT = '''
    CREATE TABLE IF NOT EXISTS temp (
        id integer PRIMARY KEY,
        timestamp text,
        sensor1 real,
        sensor2 real
    );'''
