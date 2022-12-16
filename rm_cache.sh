#!/bin/bash


date_str=$(date --date='1 day ago' '+%Y%m%d')
dir_to_rm=$HOME/cache/$date_str
echo $(date): Compressing and removing $dir_to_rm  >> $HOME/camera_service/camera.log 2>&1

cd $dir_to_rm
ffmpeg -y -framerate 10 -pattern_type glob -i '*.jpg' -c:v libx264 -pix_fmt yuv420p $date_str.mp4
mv ./$date_str.mp4 $HOME/cache/

rm -r $dir_to_rm
echo $(date): Done compressing and removing $dir_to_rm >> $HOME/camera_service/camera.log 2>&1

