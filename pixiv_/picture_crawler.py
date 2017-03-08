import time
import threading
from save_picture import save, mkdir
from bs4 import BeautifulSoup
import re
from downloader import downloader
from pixiv_painter import PixivPainter
fromlogin import login

url = 'http://www.pixiv.net/member_illust.php?mode=medium&illust_id='


def picture_crawler(painter_id, sleep_time=2, max_threads=10):
    painter = PixivPainter(painter_id)
    crawl_queue = painter.get_pictures_id()
    picture_dir = mkdir(painter_id)

    def process_queue():
        try:
            picture_id = crawl_queue.pop()
        except IndexError:
            print 'No pictures!'
        picture_html = downloader(url+picture_id.encode('utf8')).text
        img_urls = html_parse(picture_html)

        save(img_urls, picture_dir)

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
    print 'Over!'


def html_parse(html_source):
    img_urls = []
    html_soup = BeautifulSoup(html_source, 'lxml')
    div = html_soup.find_all('div', class_='works_display')
    a_label = div[0].a
    if a_label:
        img_part_url = div[0].a.get('href')
        pictures_source = downloader('http://www.pixiv.net/'+img_part_url).text
        html_soup2 = BeautifulSoup(pictures_source, 'lxml')
        img_items = html_soup2.find_all('div', class_='item-container')
        for item in img_items:
            img_url = item.img.get('data-src')
            img_urls.append(img_url)
        return img_urls
    else:
        pattern1 = re.compile('(?<=data-src=")\S*(?=" class="original-image")')
        img_url = re.findall(pattern1, html_source)
        return img_url


if __name__ == '__main__':
    
    response = login(pixiv_id, password) #这里换成正确的帐号和密码
    picture_crawler(11246082)
    pixiv.get_pictures_id()



