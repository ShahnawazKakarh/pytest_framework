from simple_settings import settings

BASE_URL = 'https://{}{}'.format(settings.IPT, settings.PORT)

PATH = '/jdk/v1'

SIGNUP_END_POINT = "/user/signup"

SQL_HOST = settings.SQL_HOST
SQL_PORT = settings.SQL_PORT
SQL_USER = settings.SQL_USER
SQL_PASSWORD = settings.SQL_PASSWORD

default_db_name = 'default'

DEFAULT = {
    "database": default_db_name,
    "user": SQL_USER,
    "host": SQL_HOST,
    "password": SQL_PASSWORD,
    "port": SQL_PORT
}
