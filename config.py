import os


db = {
    'user': 'root',
    'password': '1234',
    'host': 'localhost',
    'port': 3310,
    'database': '1st_proj',
}
SQLALCHEMY_DATABASE_URI = f"mariadb+mariadbconnector://{db['user']}:{db['password']}@"\
                          f"{db['host']}:{db['port']}/{db['database']}?charset=utf8"

SECRET_KEY = os.urandom(32)