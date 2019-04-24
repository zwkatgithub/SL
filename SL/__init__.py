"""
The flask application package.
"""
import os
ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
UPLOAD_FOLDER = os.path.join(ROOT_PATH,'SL','files')
ALLOWED_EXTENSIONS = set(['docx'])

from flask import Flask
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'myapp'
import SL.views
