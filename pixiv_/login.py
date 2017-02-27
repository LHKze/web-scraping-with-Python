# -*- coding:utf-8 -*-

import requests
import re

head = {
    # 'Host': 'accounts.pixiv.net',
    # 'Accept': 'application/json, text/javascript, */*; q=0.01',
    # 'Origin': 'https://accounts.pixiv.net',
    # 'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
                    Chrome/52.0.2743.116 Safari/537.36',
    # 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'Referer': 'https://accounts.pixiv.net/login?lang=zh&source=pc&view_type=page&ref=wwwtop_accounts_index',
    # 'Accept-Encoding': 'gzip, deflate, br',
    # 'Accept-Language': 'zh-CN,zh;q=0.8',
    'Referer': 'https://accounts.pixiv.net/login? \
               return_to=http%3A%2F%2Fwww.pixiv.net%2Franking.php%3Fmode%3Ddaily&source=pc&view_type=page',

}

def get_cookies(pid, password, text):
    s = requests.session()



    shout_url = 'https://accounts.pixiv.net/login?return_to=http%3A%2F%2F\
    www.pixiv.net%2Franking.php%3Fmode%3Ddaily&source=pc&view_type=page'
    url1 = 'https://accounts.pixiv.net/api/login?lang=zh'

    res1 = s.get(shout_url, headers=head)

    content = res1.text
    pattern = re.compile('(?<=<input type="hidden" name="post_key" value=")\w*(?=">)')
    items = re.findall(pattern, content)
    if not items:
        print('postkey is not found')
        exit()
    postkey = items[0]

    data = ({
        'pixiv_id': str(pixiv_id),    #email
        'password': str(password),    #password
        'captcha': '',
        'g_recaptcha_response': '',
        'post_key': str(postkey),
        'source': 'pc'
    })

    s.post(url1, data=data)
    cookies = s.cookies
    fp = open(text, 'w')
    fp.write('; '.join(['='.join(item) for item in cookies.items()]))
    fp.close()
    print('save cookies is Success')


def loadcookie(text):
    loadcookies = {}
    f = open(text, 'r')
    for line in f.read().split(';'):
        name, value = line.strip().split('=', 1)
        loadcookies[name] = value
    f.close()
    print('load cookies is Success')
    return loadcookies



def login(pixiv_id, password):
    s = requests.session()

    get_cookies(pixiv_id, password, 'cookie.txt')
    cookies =loadcookie('cookie.txt')
    s.cookies = requests.utils.cookiejar_from_dict(cookies)
    s.headers = head
    res = s.get('http://www.pixiv.net')
    return res


if __name__ == '__main__':
    response = login(pixiv_id, password)
    print response.status_code
