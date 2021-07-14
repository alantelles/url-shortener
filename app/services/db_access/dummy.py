import secrets as sc
import json

from app.services.db_access import DbAccess

class DummyDbAccess(DbAccess):

    def check_short_url(self, url):
        with open('app/services/db_access/dummy.json', 'r') as dummy_urls:
            url_set = json.load(dummy_urls)

        return url_set.get(url)

    def save_new_url(self, url):
        with open('app/services/db_access/dummy.json', 'r') as dummy_urls:
            url_set = json.load(dummy_urls)

        short_test = sc.token_urlsafe(5)[:5]
        url_set[short_test] = url

        with open('app/services/db_access/dummy.json', 'w') as dummy_urls:
            url_set = json.dump(url_set, dummy_urls)

        return short_test
        

    