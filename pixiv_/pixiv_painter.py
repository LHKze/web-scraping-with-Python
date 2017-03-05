from bs4 import BeautifulSoup
import re
from downloader import downloader
import time
base_url = 'http://www.pixiv.net/member_illust.php'
seed_url = 'http://www.pixiv.net/member_illust.php?id='


class Pixiv_Painter(object):
    def __init__(self, painter_id):
        self.painter_id = painter_id
        self.painter_url = seed_url + str(self.painter_id)

    def get_pictures_id(self, url):
        id_ = []

        html_source = downloader(url)
        while True:
            html_soup = BeautifulSoup(html_source, 'lxml')
            span = html_soup.find('span', class_='next')
            next_page = span.a.get('href')
            if next_page is not None:
                pattern = re.compile('(?<=data-id=")\S*(?=">)')
                picture_id = re.findall(pattern, html_source)
                id_.extend(picture_id)
                time.sleep(2)
                html_source = downloader(base_url+next_page)
            else:
                break
        return id_



