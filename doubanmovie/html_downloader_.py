import urllib, urllib2



def downloader(url, head, data=None):
    request = urllib2.Request(url, headers=head, data=data)
    opener = urllib2.build_opener()
    response = opener.open(request)
    return response.read()



