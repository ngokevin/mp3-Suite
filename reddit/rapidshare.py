#!/usr/bin/env python

# uses the rapidshare api to upload a file and return download link

import datetime
import time
import urllib
import urllib2
import cookielib
from optparse import OptionParser

def add_job(username, password, filename):
    """ uploads a file (via url) to rapidshare. returns status message """

    # compose url for api call
    request_url = "http://api.rapidshare.com/cgi-bin/rsapi.cgi?sub=remotegets"
    request_url += "&login=" + username
    request_url += "&password=" + password
    request_url += "&cmd=addjob"
    request_url += "&urls=" + filename

    request = urllib2.Request(request_url)
    response = opener.open(request)
    return response.read()

def list_files(username, password):
    """ get list of all files as download links currently within rapidshare account """

    cookie_jar = cookielib.MozillaCookieJar()
    opener = urllib2.build_opener (urllib2.HTTPCookieProcessor(cookie_jar), urllib2.HTTPHandler())
    urllib2.install_opener(opener)

    # compose url for api call
    request_url = "http://api.rapidshare.com/cgi-bin/rsapi.cgi?sub=listfiles"
    request_url += "&login=" + username
    request_url += "&password=" + password
    request_url += "&realfolder=all"
    request_url += "&fields=filename"

    request = urllib2.Request(request_url)
    response = opener.open(request)
    links = response.read()
    
    # parse the response (which are unique id/filename pairs) to a list
    # of download links
    links = links.split('\n')
    links.pop()
    final = []
    for link in links:
        link = link.split(',')
        link = "https://rapidshare.com/files/" + link[0] + "/" + link[1] 
        final.append(link)

    final = sorted(final, key=lambda dl_link: dl_link[-14:-10] + dl_link[-9:-7] + dl_link[-6:-4])
    final.reverse()
    return final

def delete_files(username, password, fileid):
    """ deletes a file from rapidshare account given fileid """
    
    cookie_jar = cookielib.MozillaCookieJar()
    opener = urllib2.build_opener (urllib2.HTTPCookieProcessor(cookie_jar), urllib2.HTTPHandler())
    urllib2.install_opener(opener)

    # compose url for api call
    request_url = "http://api.rapidshare.com/cgi-bin/rsapi.cgi?sub=deletefiles"
    request_url += "&login=" + username
    request_url += "&password=" + password
    request_url += "&files=" + fileid

    request = urllib2.Request(request_url)
    response = opener.open(request)
    return response.read()

def upload_and_list_files(username, password, filename='', sleep=True):
    """ uploads a file and gets updated link list """

    cookie_jar = cookielib.MozillaCookieJar()
    opener = urllib2.build_opener (urllib2.HTTPCookieProcessor(cookie_jar), urllib2.HTTPHandler())
    urllib2.install_opener(opener)

    # upload
    if filename:
        response = add_job(username, password, filename)

    # make sure it finishes before grab link
    if sleep is True:
        time.sleep(900)

    # get all current links
    links = list_files(username, password)
    links = format_links(links)
    return links

def format_links(links):
    """ format list into string """
    
    string = ""
    links = sorted(links)
    for link in links:
        string += link + '''    
'''
    return string

def list_jobs(username, password):
    """ 
    give a detailed list of all currently stored jobs
    """
    cookie_jar = cookielib.MozillaCookieJar()
    opener = urllib2.build_opener (urllib2.HTTPCookieProcessor(cookie_jar), urllib2.HTTPHandler())
    urllib2.install_opener(opener)

    request_url = "http://api.rapidshare.com/cgi-bin/rsapi.cgi?sub=remotegets"
    request_url += "&login=" + username
    request_url += "&password=" + password
    request_url += "&cmd=listjobs"

    request = urllib2.Request(request_url)
    response = opener.open(request)
    return response.read()
    
if __name__ == '__main__':

    # get current date in y-m-d format as a default option for filename
    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d")

    # command line arguments
    parser = OptionParser()
    parser.add_option("-u", "--username", help="filevo login username",
                        default="", dest="username")
    parser.add_option("-p", "--password", help="filevo login password",
                        default="", dest="password")
    parser.add_option("-f", "--filename", help="file to upload (full path)",
                        default=date+'.tar', dest="filename")
    parser.add_option("-s", "--sleep", help="sleep during upload and before returning links",
                        default=True, dest="sleep")
    (options, args) = parser.parse_args()

    cookie_jar = cookielib.MozillaCookieJar()
    opener = urllib2.build_opener (urllib2.HTTPCookieProcessor(cookie_jar), urllib2.HTTPHandler())
    urllib2.install_opener(opener)

    print upload_and_list_files(options.username, options.password, options.filename, options.sleep)
