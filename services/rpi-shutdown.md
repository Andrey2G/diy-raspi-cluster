# Raspberry PI Shutdown service

Open the file for edit

``` bash
sudo nano /usr/bin/rpi-shutdown.py
```

and paste the code from [this file](/services/rpi-shutdown.py)
The create a service

``` bash
sudo nano /etc/systemd/system/rpi-shutdown.service
```

and paste the code from [this file](/services/rpi-shutdown.service)

``` bash
sudo systemctl daemon-reload
sudo systemctl enable rpi-shutdown.service
sudo systemctl start rpi-shutdown.service
```
