import urllib
import urllib2
import sys
import re
import subprocess


def getHTML(url):
    """Fetch HTML via HTTP request"""
    fd = urllib2.Request(url)
    fd.add_header('User-Agent',
            'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.19) '
            'Gecko/20081202 Firefox (Debian-2.0.0.19-0etch1)')
    page = urllib2.urlopen(fd).read()
    return page

def queryGoogle(args):
    prefix = "http://www.google.com/search?q="
    suffix = ""

    i = 0;
    for arg in args:
        if not arg == sys.argv[0]:
            if i == 1:
                suffix += arg
            else:
                suffix += "+" + arg
        i += 1

    query = prefix + suffix
    print query

    return getHTML(query)


if __name__ == '__main__':
    sys.argv.append("mediafire")
    page = queryGoogle(sys.argv)
    print page





