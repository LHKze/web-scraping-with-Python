import time
from downloader import downloader
import os


def mkdir(painter_id):
    path = os.getcwd()
    picture_dir = path + r'\painter_' + str(painter_id)
    if os.path.exists(picture_dir):
        pass
    else:
        os.mkdir(picture_dir)
    return picture_dir


def save(img_urls, dir_path):
    for img_url in img_urls:

        pictrue = downloader(img_url).content
        picture_name = img_url.split('/')[-1]
        with open(dir_path+'/'+picture_name, 'wb') as f:
            f.write(pictrue)
        time.sleep(2)




