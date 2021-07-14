class DbAccess:

    def check_short_url(self, url):
        raise NotImplementedError()

    def save_short_url(self, url):
        raise NotImplementedError()