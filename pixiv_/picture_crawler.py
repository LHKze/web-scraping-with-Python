import time
import threading
from save_picture import save
from bs4 import BeautifulSoup
import re
from downloader import downloader
from pixiv_painter import Pixiv_Painter

url = 'http://www.pixiv.net/member_illust.php?mode=medium&illust_id='


def picture_crawler(painter_id, sleep_time=2, max_threads=10):
    painter = Pixiv_Painter()
    crawl_queue = painter.get_pictures_id(painter_id)

    def process_queue():
        try:
            picture_id = crawl_queue.pop()
        except IndexError:
            print 'No pictures!'
        picture_html = downloader(url+str(picture_id))
        img_url = html_parse(picture_html)
        save(img_url)

    threads = []
    while threads or crawl_queue:
        for thread in threads:
            if not thread.is_alive():
                threads.remove(thread)
        while len(threads) < max_threads and crawl_queue:
            thread = threading.Thread(target=process_queue)
            thread.setDaemon(True)
            thread.start()
            threads.append(thread)
        time.sleep(sleep_time)


def html_parse(html_source):
    html_soup = BeautifulSoup(html_source, 'lxml')
    div = html_soup.find_all('div', class_='wrapper')[1]
    img = div.img
    img_url = img.get('data-src')
    return img_url


