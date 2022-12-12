#!/bin/bash

echo -e "\n$(date) Cam Service Shell----------------------------" >> /home/andrew/logs/camera.service.log

cd $HOME/camera_service 

sleep 1

/home/andrew/.virtualenvs/chicken_door/bin/python /home/andrew/camera_service/camera_service.py >> /home/andrew/logs/camera.service.log 2>&1



