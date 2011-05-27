import sys
import re
import subprocess

if __name__ == '__main__':
    """ Get Youtube links from a Youtuber's page HTML and spits out a file of YouTube links"""

    fd = open(sys.argv[1], 'r')

    linkList = re.findall('(/watch\?v=.*?)"', fd.read())

    finalLinkList = []
    for link in linkList:
        link = ''.join(["http://youtube.com", link])
        finalLinkList.append(link)                          
 
    print finalLinkList
    print "\n"
    print str(len(finalLinkList)) + " links found\n"

    fd.close()
    fd = open("Music", "a")
    for link in finalLinkList:
        fd.write(link + "\n")                      
    fd.close()



