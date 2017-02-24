from bs4 import BeautifulSoup


def get_links(html):

    html_soup = BeautifulSoup(html, 'lxml')
    found_links = html_soup.find_all('a', class_='nbg')
    links = []
    for item in found_links:
        links.append(item.get('href'))
    return links



