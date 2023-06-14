#/bin/bash
filesize=$(ls -l "$1" | awk '{print $5}')
duration=$(ffprobe -v error -select_streams v:0 -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$1")
bitrate=$(echo "scale=2; $filesize * 8 / $duration /1000" | bc)
echo "$1 Video Bitrate: $bitrate kbps"
