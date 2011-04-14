# /bin/sh
# Downloads .mp3 from YouTube using youtube-dl and ffmpeg
# Supports batch download from regular file 
# Recommended to split large batch files. Script makes a process for each link and too many at once may buckle something.
# Usage: youtube2mp3 ["youtube-link"][FILE WITH LINKS][OUTPUT DIR]

function toMP3 {

    echo "Converting $1..."

    # Downloads video (.flv)
    x=~/.youtube-dl.$RANDOM-$RANDOM.flv
    python youtube-dl --output=$x --format=18 "$1"
    
    # Gets title of video to appropriately name the .mp3 output
    prefix=`youtube-dl -e "$1"`
    suffix=".mp3"
    title=$prefix$suffix
    finaltitle=`(echo $title | sed -E 's/ /_/g')`

    # Convert to .mp3
    ffmpeg -i $x -acodec libmp3lame -ac 2 -ab 128k -vn -y $finaltitle
    rm $x

    mv $finaltitle "$2$finaltitle" 

    echo "$1 converted!"
}

# Default output directory
if test $# -eq 1
then
    default=1
fi

if [ ! -d /home/ngoke/Downloads/Music/youtube2mp3 ];
then
    mkdir /home/ngoke/Downloads/Music/youtube2mp3
fi


dir="/home/ngoke/Downloads/Music/youtube2mp3/"

# Convert all if batch download file found
if test -f $1 
then   

    echo "$1 found"
    
    # Loop through each link in file
    for line in $(cat $1)
    do
        #Check to see if song does not already exist
        prefix=`youtube-dl -e "$line"`
        suffix=".mp3"
        title=$prefix$suffix
        title=`(echo $title | sed -E 's/ /_/g')`
        title=$dir$title

        echo "Converting $prefix"

        if [ ! -f $title ]
        then
            if test $default -eq 1
            then
              toMP3 $line "/home/ngoke/Downloads/Music/youtube2mp3/" &
            else
              toMP3 $line $2 & 
            fi  
        else
            echo "$prefix$suffix already exists"
        fi
    done

    # Empty file
    cat /dev/null > $1

# Convert if single link given
else
    if test $default -eq 1
    then
        toMP3 $1 "/home/ngoke/Downloads/Music/youtube2mp3/"
    else
        toMP3 $1 $2
    fi
fi

echo "Done!"
exit

