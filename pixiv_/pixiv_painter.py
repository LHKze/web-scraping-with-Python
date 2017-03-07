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
        t = 1

        html_source = downloader(url)
        while t == 1:
            html_soup = BeautifulSoup(html_source, 'lxml')
            span = html_soup.find('span', class_='next')
            try:
                next_page = span.a.get('href')
            except:
                t = 2
            pattern = re.compile('(?<=data-id=")\S*(?=">)')
            picture_id = re.findall(pattern, html_source)
            id_.extend(picture_id)
            time.sleep(2)
            if next_page is not None:
                html_source = downloader(base_url+next_page)
            else:
                break
        print len(id_)


if __name__ == '__main__':

    pixiv = Pixiv_Painter(11246082)
    pixiv.get_pictures_id(pixiv.painter_url)






