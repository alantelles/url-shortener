class DbAccess:

    def check_short_url(self, url):
        raise NotImplementedError("This method should be implemented by subclass")

    def save_new_url(self, url):
        raise NotImplementedError("This method should be implemented by subclass")