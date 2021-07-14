from app.services.db_access import DbAccess

url_set = {
    "zika": "https://ultragen.dev",
    "github": "https://github.com"
}

class DummyDbAccess(DbAccess):

    def check_short_url(url):
        return url_set.get(url)

    