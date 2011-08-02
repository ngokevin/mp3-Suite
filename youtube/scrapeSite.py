#!/usr/bin/env python

import urllib
import sys
import re
import subprocess

""" 
 Scrapes a webpage for YouTube links and outputs to file. 
 Example formats for Reddit's URLs
    http://www.reddit.com/r/listentothis/top/?t=day
    http://www.reddit.com/r/listentothis/top/?t=week#page=2
 Usage: python getMusicReddit.py [LINK] [week]
"""

def getHTML(url):
    """Fetch HTML via HTTP request"""
    fd = urllib.urlopen(url)
    page = fd.read()
    return page

def getLinks(page):
    """Search for YouTube links within HTML page"""
    li = re.findall('"(http://www.youtube.com/watch\?v=.*?)"', page)
    return li

if __name__ == '__main__':
    """Get YT links from site and output links to file"""

    if len(sys.argv) == 1:
        page = getHTML("http://www.reddit.com/r/listentothis")
    elif str(sys.argv[1]) == "week":
        page = getHTML("http://www.reddit.com/r/listentothis/top?t=week")
    else:
        page = getHTML(sys.argv[1])

    li = getLinks(page)

    print "\n" + str(len(li)) + " links found\n"
    print str(li) + "\n"

    fd = open("MusicDL", "a")
    for link in li:
        fd.write(link + "\n");
    fd.close()

