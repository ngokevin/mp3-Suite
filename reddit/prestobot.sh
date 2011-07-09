#! /bin/sh
# Creates tarball, uploads to filevo, and posts to Reddit. Main method for whole process

download_dir="/home/ngoke/Downloads/Music/youtube2mp3/"
host=""
python_dir="/usr/local/bin/"
rapid_username=""
rapid_password=""
reddit_username=""
reddit_password=""
subreddit=""

cd $download_dir
date=`date +%F`                                        

# Gets all files from today and tarballs them
#find $download_dir -daystart -ctime 0 -not -wholename $download_dir -print0 | tar -cvf output.tar --no-wildcards --null -T -
find -daystart -ctime 0 -not -name . -print0 | xargs -0 zip $date.zip --no-wild

# upload zip to rapidshare
links=`python "${python_dir}uploadToRapidshare.py" -u $rapid_username -p $rapid_password -f $host$date.zip`

# post link to reddit
post="Hello $subreddit,    
My name is prestobot, a set of scripts that scrapes the front page of a subreddit for youtube links daily. I download these songs and convert them to .mp3. Then,  I zip all of these files together, upload them to Rapidshare, and post the download links to Reddit. My source code can be found at github.com/ngokevin/mp3-Suite. I am pleased to bring to you today's top songs for download.     

==Links==    

$links"

python "${python_dir}postToReddit.py" -u $reddit_username -p $reddit_password -s $subreddit -k "self" -t "prestobot $date: download link to today's top songs for $subreddit" -l $post



