from flask import g
from app.services.db_access.dummy import DummyDbAccess

def set_db_engine(fn):
    def wrapper(*args, **kwargs):
        g.db_engine = DummyDbAccess
        return fn(*args, **kwargs)

    return wrapper