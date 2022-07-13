''' Constants config file for tempy.
    @author: Adrien Vilquin Barrajon <avilqu@gmail.com>
'''

BASE_DIR = '/sys/bus/w1/devices/'         # System one-wire directory
RECORD_INTERVAL = 60                      # Record interval (seconds)
DB_URL = 'deskpi.local'
DB_PORT = '8086'
DB_NAME = 'tempy'
# DB_FILE = '/home/pi/tempy/tempy.db'
# DB_FILE = '/home/tan/dev/tempy/tempy.db'
# DB_TBNAME = 'tempy'
# SQL_INIT = f'''
#     CREATE TABLE IF NOT EXISTS {DB_TBNAME} (
#         id integer PRIMARY KEY,
#         timestamp DB_URLt,
#         sensor1 real,
#         sensor2 real
#     );'''
