from secrets import token_urlsafe
# from app.services.db_access.firebase import FireBaseDbAccess
from app.services.db_access.dummy import DummyDbAccess

def create_short_url():
    return 'algor'

def check_short_url(url, client):    
    result = client.check_short_url(url)
    return result

def save_new_url(url):
    short = token_urlsafe(5)
