from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('wolfbot.conf')

db = SQLAlchemy(app)

from wolfbot import views

