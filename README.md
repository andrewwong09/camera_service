*Camera Service*


**Setting Up Service**
'''
chmod 777 camera_service.sh
cp camera.service ~/.config/systemd/user/camera.service
systemctl --user enable camera.service
systemctl --user start camera.service 
sudo loginctl enable-linger andrew
'''


***Troubleshooting***
if this is encountered:
libf77blas.so.3: cannot open shared object file: No such file or directory
```
sudo apt-get install libatlas-base-dev
```
