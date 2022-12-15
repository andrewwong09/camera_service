#!/bin/bash


date_str=$(date --date='3 days ago' '+%Y%m%d')
dir_to_rm=$HOME/cache/$date_str
echo $(date): Removing $dir_to_rm
rm -r $dir_to_rm

