import requests
from login import loadcookie

DEFAULT_DELAY = 5
DEFAULT_AGENT = ''
DEFAULT_RETRIES = 2
DEFAULT_TIMEOUT = 60


def downloader(url):
    s = requests.session()
    cookies = loadcookie('cookie.txt')
    s.cookies = requests.utils.cookiejar_from_dict(cookies)
    s.headers = {'User-Agent': DEFAULT_AGENT}
    try:
        res = s.get(url)
    except:
        print 'failed to log in!'
    else:
        return res.txt

