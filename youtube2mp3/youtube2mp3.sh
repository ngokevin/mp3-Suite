# /bin/sh
# Downloads .mp3 from YouTube using youtube-dl and ffmpeg
# Supports batch download from regular file 
# Recommended to split large batch files. Script makes a process for each link and too many at once may buckle something.
# Usage: youtube2mp3 ["youtube-link" | FILE WITH LINKS] [OUTPUT DIR]

download_dir="/home/ngoke/Downloads/Music/youtube2mp3/"
to_convert=$1
specified_dir=$2

function toMP3 {
    
    dir=$2

    # Gets title of video to appropriately name the .mp3 output
    prefix=`youtube-dl -e "$1"`
    suffix=".mp3"
    title=$prefix$suffix
    finaltitle=`(echo $title | sed -E 's/ /_/g')`

    echo "Converting $prefix"

    # Downloads video (.flv)
    x=~/.youtube-dl.$RANDOM-$RANDOM.flv
    youtube-dl --output=$x --format=18 "$1"

    # Convert to .mp3
    ffmpeg -i $x -acodec libmp3lame -ac 2 -ab 128k -vn -y $finaltitle
    rm $x

    mv $finaltitle $dir$finaltitle
    spacetitle=$dir"`(echo $finaltitle | sed 's/_/\\ /g')`"
    mv $dir$finaltitle "$spacetitle"

    if [ -f "$spacetitle" ]
    then
        echo "$prefix converted!"
    else
        echo "Error!"
    fi
}

# If no output directory given, use default output directory
if test $# -eq 1
then
    use_default_dir=1
fi

if [ ! -d $download_dir ];
then
    mkdir $download_dir
fi

# Convert all if batch download file found
if test -f $to_convert 
then   

    echo "$to_convert found"
    
    # Loop through each link in file
    for line in $(cat $to_convert)
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
            if test $use_default_dir -eq 1
            then
              toMP3 $line $download_dir &
            else
              toMP3 $line $specified_dir & 
            fi  
        else
            echo "$prefix$suffix already exists"
        fi
    done

    # Empty file
    cat /dev/null > $to_convert

# Convert if single link given
else
    if test $use_default_dir -eq 1
    then
        toMP3 $to_convert $download_dir &
    else
        toMP3 $to_convert $specified_dir &
    fi
fi

exit

