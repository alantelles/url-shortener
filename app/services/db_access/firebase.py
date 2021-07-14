from app.services.db_access import DbAccess

class FireBaseDbAccess(DbAccess):
    
    def check_short_url(self, url):
        return True