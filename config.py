import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
   SECRET_KEY = os.environ.get("123aaa321") or "k3y-s3cr3t"    
   SQLALCHEMY_DATABASE_URI = (                           
           os.environ.get('DATABASE_URL') or
           'sqlite:///' + os.path.join(BASE_DIR, 'library.db')
   )
   SQLALCHEMY_TRACK_MODIFICATIONS = False