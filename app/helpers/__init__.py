import secrets as sc
import os

def create_short_url():
    url_size = os.environ.get('SHORT_URL_SIZE')
    try:
        url_size = int(url_size)

    except:
        url_size = 5

    short = sc.token_urlsafe(url_size)[:url_size]
    return short