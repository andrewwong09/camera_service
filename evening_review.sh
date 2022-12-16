#!/bin/bash


date_str=$(date --date='today' '+%Y%m%d')
dir_to_compress=$HOME/cache/$date_str
echo $(date): Compressing $dir_to_compress  >> $HOME/camera_service/camera.log 2>&1

cd $dir_to_compress
ffmpeg -y -framerate 10 -pattern_type glob -i '*.jpg' -c:v libx264 -pix_fmt yuv420p $date_str.mp4
mv ./$date_str.mp4 $HOME/cache/
