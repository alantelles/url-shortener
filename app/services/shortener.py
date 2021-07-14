from app.services.db_access.firebase import FireBaseDbAccess

def create_short_url():
    return 'algor'

def check_short_url(url):
    client = FireBaseDbAccess()
    result = client.check_short_url(url)
    return result
