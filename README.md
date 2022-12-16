*Camera Service*


**Setting Up Service**
'''
chmod 777 camera_service.sh
cp camera.service ~/.config/systemd/user/camera.service
systemctl --user enable camera.service
systemctl --user start camera.service 
sudo loginctl enable-linger andrew
'''


**Rebooting and clearing cache of images**
Add the following to crontabs, one sudo (i.e. root) and one user
```
crontab -e
```
User crontab
```
1 19 * * * $HOME/camera_service/evening_review.sh >> $HOME/camera_service/camera.log 2>&1
1 0 * * * $HOME/camera_service/rm_cache.sh >> $HOME/crontab.log 2>&1
```

```
sudo crontab -e
```
Root crontab
```
1 5 * * * /sbin/shutdown -r now >> $HOME/crontab.log 2>&1
```


***Troubleshooting***
if this is encountered:
libf77blas.so.3: cannot open shared object file: No such file or directory
```
sudo apt-get install libatlas-base-dev
```
