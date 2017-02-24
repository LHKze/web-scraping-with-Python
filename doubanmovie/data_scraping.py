import urlparse
from bs4 import BeautifulSoup
import csv
import codecs


def html_parse(html):
    html_soup = BeautifulSoup(html, 'lxml')

    content = html_soup.select('div#content')[0]
    # info = content.select('div#info')[0]
    comment = content.select('div#interest_sectl')[0]

    title = content.h1.select('span')
    movie_name = unicode(title[0].string).encode('utf8')
    publish_date = unicode(title[1].string).encode('utf8')
    score = unicode(comment.select('.rating_num')[0].string).encode('utf8')

    datas = [movie_name, publish_date, score]

    create_csv(datas)


def create_csv(datas):
    try:
        file_ = open('D://e//t.csv', 'a')
        file_.write(codecs.BOM_UTF8)
        writer = csv.writer(file_)
        # fields = ('movie_name', 'publish_date', 'score')
        writer.writerow(datas)
    except:
        print 'failed to write data'
    else:
        file_.close()






