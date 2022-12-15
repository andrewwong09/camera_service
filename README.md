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
Add the following to crontab
```
sudo crontab -e
```

```
1 0 * * * $HOME/camera_service/rm_cache.sh >> $HOME/crontab.log 2>&1
5 0 * * * /sbin/shutdown -r now >> $HOME/crontab.log 2>&1
```


***Troubleshooting***
if this is encountered:
libf77blas.so.3: cannot open shared object file: No such file or directory
```
sudo apt-get install libatlas-base-dev
```
