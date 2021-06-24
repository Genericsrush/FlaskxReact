from flask import Flask
from flask_restful import Api

app = Flask(__name__)

api = Api(app)

import app_backend.routes