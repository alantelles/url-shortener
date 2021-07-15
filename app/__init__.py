from flask import Flask
import os, base64

db_engine = os.environ.get('DB_ENGINE')

if db_engine == 'FireBaseDbAccess':
    from app.services.db_access.firebase import FireBaseDbAccess
    firestore_key = os.environ.get('FIRESTORE_B64')
    firestore_key_path = os.environ.get('FIRESTORE_KEY')
    if firestore_key and firestore_key_path:
        with open(firestore_key_path, 'wt') as fs_handler:
            decoded = base64.b64decode(firestore_key)
            fs_handler.write(decoded.decode())

    db = FireBaseDbAccess()

else:
    from app.services.db_access.dummy import DummyDbAccess
    db = DummyDbAccess()



app = Flask(__name__)
app.config['DOMAIN'] = os.environ.get('DOMAIN', 'http://encur.te/')
from app.routes import *