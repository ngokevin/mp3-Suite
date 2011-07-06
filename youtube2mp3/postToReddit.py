# Posts a thread on Reddit (options for subreddit, link title, text)

import urllib
import urllib2

def login(user, passwd):
    form_data = urllib.urlencode({'user': user, 'passwd' : passwd})
    url = "http://www.reddit.com/api/login"
    request = urllib2.Request(url, form_data)
    response = opener.open(request)
    return response.read()

if __name__ == '__main__':
    response = login("IfOneThenHappy", "rogers")
    print response
    
