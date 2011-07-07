#! /bin/sh
# Creates tarball, uploads to filevo, and posts to Reddit. Main method for whole process

download_dir="/home/ngoke/Downloads/Music/youtube2mp3/"
date=`date +%F`                                        

cd $download_dir

# Gets all files from today and tarballs them
#find $download_dir -daystart -ctime 0 -not -wholename $download_dir -print0 | tar -cvf output.tar --no-wildcards --null -T -
find -daystart -ctime 0 -not -name . -print0 | xargs -0 zip $date.zip --no-wild


