from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '13579'

from app import routs