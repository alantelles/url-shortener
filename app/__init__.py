from flask import Flask
import os

db_engine = os.environ.get('DB_ENGINE')

if db_engine == 'FireBaseDbAccess':
    from app.services.db_access.firebase import FireBaseDbAccess
    db = FireBaseDbAccess()

else:
    from app.services.db_access.dummy import DummyDbAccess
    db = DummyDbAccess()



app = Flask(__name__)
app.config['DOMAIN'] = 'https://encur.te/'
from app.routes import *