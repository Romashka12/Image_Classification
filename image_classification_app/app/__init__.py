from flask import Flask
from PIL import Image
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes