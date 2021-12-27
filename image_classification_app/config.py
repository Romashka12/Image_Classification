import os

class Config(object):
    SECRET_KEY = "secret_key"
    UPLOAD_FOLDER=os.path.join(os.path.dirname(os.path.abspath(__file__)),'data')
    UPLOAD_EXTENSIONS = ['.jpg', '.png', '.gif']