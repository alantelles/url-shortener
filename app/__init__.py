from flask import Flask, g



app = Flask(__name__)


from app.routes import *