from app import db


def check_short_url(url):    
    result = db.check_short_url(url)
    return result

def save_new_url(url):
    valid_start = url.startswith("http://") or url.startswith("https://")
    if not valid_start:
        url = "http://" + url

    short_url = db.save_new_url(url)
    return short_url
