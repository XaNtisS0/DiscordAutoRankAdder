import os

basedir = os.path.abspath(os.path.dirname(__file__))

POSTGRES_URL = os.environ['POSTGRES_URL']
POSTGRES_USER = os.environ['POSTGRES_USER']
POSTGRES_PW = os.environ['POSTGRES_PW']
POSTGRES_DB = os.environ['POSTGRES_DB']

DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER, pw=POSTGRES_PW, url=POSTGRES_URL, db=POSTGRES_DB)


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv(DB_URL, "sqlite://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False