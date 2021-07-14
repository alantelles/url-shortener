from flask import Flask, g
from app.services.db_access.dummy import DummyDbAccess



app = Flask(__name__)
db = DummyDbAccess()

from app.routes import *