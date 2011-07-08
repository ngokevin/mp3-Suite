#! /bin/sh
# Creates tarball, uploads to filevo, and posts to Reddit. Main method for whole process

download_dir="/home/ngoke/Downloads/Music/youtube2mp3/"
host="http://archer.dyndns-home.com:9128/"
python_dir="/home/ngoke/Scripts/mp3-suite/youtube2mp3/"
rapid_username="ktngo09"
rapid_password="RfVQaZ10"
reddit_username="IfOneThenHappy"
reddit_password="rogers"

date=`date +%F`                                        

cd $download_dir

# Gets all files from today and tarballs them
#find $download_dir -daystart -ctime 0 -not -wholename $download_dir -print0 | tar -cvf output.tar --no-wildcards --null -T -
find -daystart -ctime 0 -not -name . -print0 | xargs -0 zip $date.zip --no-wild

python ${python_dir}uploadToRapidshare.py -u $rapid_username -p $rapid_password -f $date.zip


