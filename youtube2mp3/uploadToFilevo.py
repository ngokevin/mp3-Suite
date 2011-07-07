# Uploads a tarball to filevo and returns download link
# Upload a file to filevo via screen-scrape and return download link

import urllib
import urllib2
import cookielib
from optparse import OptionParser

def fetch_page(url):
    request = urllib2.Request(url)
    response = opener.open(request)
    return response.read()

def login(username, password, header_values):
    """ 
    Login to Filevo by posting to the form with urlencode and urllib2 request
    """
    header_values['Referer'] = 'filevo.com/login.html'
    header_values['Origin'] = 'filevo.com'
    login_url = "http://filevo.com/login.html"
    form_data = urllib.urlencode({'op': 'login', 'redirect': 'http://filevo.com','login': username, 'password': password})
    request = urllib2.Request(login_url, form_data, headers = header_values)
    response = opener.open(request)
    return response.read()

if __name__ == '__main__':

    # set up header values and cookie jar to masquerade as a browser
    header_values = {
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset' : 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'gzip,deflate,sdch',
    'Accept-Language' : 'en-US,en;q=0.8',
    'Cache-Control' : 'max-age=0',
    'Connection' : 'keep-alive',
    'Host' : 'filevo.com',
    'Referer' : 'filevo.com',
    'User-Agent' : 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.100 Safari/534.30'
    }
    cookie_jar = cookielib.MozillaCookieJar()
    opener = urllib2.build_opener (urllib2.HTTPCookieProcessor(cookie_jar), urllib2.HTTPHandler())
    urllib2.install_opener(opener)

    response = login("ktngo09", "rogers", header_values) 
    print response

