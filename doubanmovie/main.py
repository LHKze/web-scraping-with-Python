import urllib
from data_scraping import html_parse
from html_downloader_ import downloader
from link_crawler_ import get_links
import time


top_head = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Host': 'movie.douban.com',
    'Referer': 'https://movie.douban.com/tag/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64)  \
                      AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',

}


head = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Host': 'movie.douban.com',
    'Referer': 'https://movie.douban.com/tag/%E7%A7%91%E5%B9%BB',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) \
                     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
}


url = 'https://movie.douban.com/tag/%E7%A7%91%E5%B9%BB'


def scrape():
    list_html = downloader(url, top_head)
    movie_links = get_links(list_html)
    for link in movie_links:
        movie_html = downloader(link, head)
        html_parse(movie_html)
        time.sleep(3)


if __name__ == '__main__':
    scrape()
