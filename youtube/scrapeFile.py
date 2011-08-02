#!/usr/bin/env python

import sys
import re
import subprocess

if __name__ == '__main__':
    """ Scrapes a file for youtube links and outputs to a flat file """

    fd = open(sys.argv[1], 'r')

    linkList = re.findall('(/watch\?v=.*?)"', fd.read())

    finalLinkList = []
    for link in linkList:
        link = ''.join(["http://youtube.com", link])
        if link not in finalLinkList:
            finalLinkList.append(link)                          
 
    print finalLinkList
    print "\n"
    print str(len(finalLinkList)) + " links found\n"

    fd.close()
    fd = open("MusicDL", "a")
    for link in finalLinkList:
        fd.write(link + "\n")                      
    fd.close()



