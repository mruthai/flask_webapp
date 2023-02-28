from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

#keep this line at the bottom
from app import routes