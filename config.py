import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'whatever'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=os.environ.get("POSTGRES_USER"),pw=os.environ.get("POSTGRES_PW"),url=os.environ.get("POSTGRES_URL"),db=os.environ.get("POSTGRES_DB"))
    SQLALCHEMY_TRACK_MODIFICATIONS = False # Turns off notifications for changes made to database
    
