import os

SECRET_KEY = 'INSECURE-SECRET-KEY'

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_TRACK_MODIFICATIONS = False

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')