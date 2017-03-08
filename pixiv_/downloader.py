import requests
from login import loadcookie, head

DEFAULT_DELAY = 5

DEFAULT_RETRIES = 2
DEFAULT_TIMEOUT = 60


def downloader(url):
    s = requests.session()
    cookies = loadcookie('cookie.txt')
    s.cookies = requests.utils.cookiejar_from_dict(cookies)
    s.headers = head
    s.stream = True
    res = s.get(url)
    return res.text


if __name__ == '__main__':

    response = downloader('http://www.pixiv.net/member_illust.php?id=11246082')
    print response.text


