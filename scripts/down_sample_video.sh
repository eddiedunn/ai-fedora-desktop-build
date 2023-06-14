#!/bin/bash

# Check if filename argument is provided
if [ -z "$1" ]; then
    echo "Please provide a filename as an argument."
    exit 1
fi

# Set the filename
original_video="$1"

# Set the optional bitrate argument, default to 1100 kbps
bitrate="${2:-1100k}"

# Temporary output file
output_video="output.mp4"

# Perform the conversion
ffmpeg -i "$original_video" -b:v "$bitrate" "$output_video"

# Check if ffmpeg command was successful
if [ $? -eq 0 ]; then
    # Delete the original video file
    rm "$original_video"
    # Rename the output video file to the original file name
    mv "$output_video" "$original_video"
else
    echo "There was a problem with the conversion."
fi

