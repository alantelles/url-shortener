from flask import Flask, g
from app.services.db_access.dummy import DummyDbAccess



app = Flask(__name__)
app.config['DOMAIN'] = 'https://encur.te/'
db = DummyDbAccess()
from app.routes import *