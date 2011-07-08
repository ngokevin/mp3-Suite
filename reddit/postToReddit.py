# Posts a thread on Reddit (options for subreddit, link title, text)

import datetime
import urllib
import urllib2
import cookielib
from optparse import OptionParser

def login(user, passwd):
    form_data = urllib.urlencode({'user': user, 'passwd' : passwd})
    url = "http://www.reddit.com/api/login"
    request = urllib2.Request(url, form_data)
    response = opener.open(request)
    return response.read()

def post_submission(kind, subreddit, title, post):

    # compose post request   
    if kind == 'self':
        form_data = urllib.urlencode({'kind':kind, 'sr':subreddit, 'title':title, 'text': post, 'r':subreddit})
    elif kind == 'link':
        form_data = urllib.urlencode({'kind':kind, 'sr':subreddit, 'title':title, 'url': post, 'r':subreddit})

    url = "http://www.reddit.com/api/submit"
    request = urllib2.Request(url, form_data)
    response = opener.open(request)
    return response.read()
     

if __name__ == '__main__':

    # command line arguments
    parser = OptionParser()
    parser.add_option("-u", "--username", help="reddit login username",
                        default="", dest="username")
    parser.add_option("-p", "--password", help="reddit login password",
                        default="", dest="password")
    parser.add_option("-s", "--subreddit", help="subreddit to post to",
                        default="", dest="subreddit")
    parser.add_option("-t", "--title", help="title of submission",
                        default="", dest="title")
    parser.add_option("-l", "--link", help="link to post or text if self post",
                        default="", dest="post")
    (options, args) = parser.parse_args()

    cookie_jar = cookielib.MozillaCookieJar()
    opener = urllib2.build_opener (urllib2.HTTPCookieProcessor(cookie_jar), urllib2.HTTPHandler())
    urllib2.install_opener(opener)

    response = login(options.username, options.password)
    response = post_submission('self', 'polljacking', 'test', 'test post')
    print response
    
