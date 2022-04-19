''' Constants config file for pytherm.
    @author: Adrien Vilquin Barrajon <avilqu@gmail.com>
'''

BASE_DIR = '/sys/bus/w1/devices/'         # System one-wire directory
RECORD_INTERVAL = 60                      # Record interval (seconds)
DB_FILE = '/home/pi/tempy/tempy.db'
DB_TBNAME = 'temp'
SQL_INIT = f'''
    CREATE TABLE IF NOT EXISTS {DB_TBNAME} (
        id integer PRIMARY KEY,
        timestamp text,
        sensor1 real,
        sensor2 real
    );'''
