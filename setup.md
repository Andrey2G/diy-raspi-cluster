# Installation and Configuration

First of all you need to Install [Raspberry PI Imager Software](https://www.raspberrypi.com/software)
or you can use the other alternatives like [Balena](https://www.balena.io/etcher/) in case if you know what to do next.

## Upgrading bootloader and firmware

Install Raspberry Pi OS on SD card (lite without desktop version)
Open Raspberry PI Imager
![Open Raspberry PI Imager](/assets/images/imager/rasp-os-step-1.png)
Click on Operating System select Raspberry PI OS (other) and select Raspberry PI OS Lite (32-bit)
![Open Raspberry PI Imager](/assets/images/imager/rasp-os-step-2.png)
Then click on Storage button to select SD Card drive.
Then click on gear and enable SSH and set login/password

![set login/password](/assets/images/imager/rasp-os-step-3.png)

if you will use WiFi internet connection set the SSID and the password
![set the SSID and the password](/assets/images/imager/rasp-os-step-4.png)
Then click Save and then Write to start installing OS on SD Card

When the process completed you can remove SD Card from the drive and put it to the RaspBerry PI SD Card Reader
![Remove SD Card](/assets/images/imager/rasp-os-step-5.png)

Now make sure that you have the absolute latest updates and firmware for the Pi. To upgrade all your packages and firmware to the latest version use the following command:

``` bash
sudo apt update && sudo apt full-upgrade -y
```

Update bootloader release config

``` bash
sudo nano /etc/default/rpi-eeprom-update
```

and set it to **stable**

``` bash
FIRMWARE_RELEASE_STATUS="stable"
```

Save it and then verify Bootloader is up to date

``` bash
pi@pim:~$ sudo rpi-eeprom-update
*** UPDATE AVAILABLE ***
BOOTLOADER: update available
   CURRENT: Thu 19 Mar 14:27:25 UTC 2020 (1584628045)
    LATEST: Tue 26 Apr 10:24:28 UTC 2022 (1650968668)
   RELEASE: default (/lib/firmware/raspberrypi/bootloader/default)
            Use raspi-config to change the release.

  VL805_FW: Using bootloader EEPROM
     VL805: up to date
   CURRENT: 000137ad
    LATEST: 000137ad
```

If you see "UPDATE AVAILABLE" update bootloader

``` bash
sudo rpi-eeprom-update -a
```

And then restart Raspberry PI to apply changes

``` bash
sudo reboot
```

And after that re-check to see if update was applied

``` bash
pi@raspberrypi:~ $ sudo rpi-eeprom-update
BOOTLOADER: up to date
   CURRENT: Tue 26 Apr 10:24:28 UTC 2022 (1650968668)
    LATEST: Tue 26 Apr 10:24:28 UTC 2022 (1650968668)
   RELEASE: default (/lib/firmware/raspberrypi/bootloader/default)
            Use raspi-config to change the release.

  VL805_FW: Using bootloader EEPROM
     VL805: up to date
   CURRENT: 000138a1
    LATEST: 000138a1
```

## Boot from USB

Run raspi-config utility

``` bash
sudo raspi-config
```

Select Advanced Options
![Select Advanced Options](/assets/images/boot-preference/step-1.png)

Then select Boot Order
![Select Boot Order](/assets/images/boot-preference/step-2.png)

Then select B2 USB Boot
![BS USB Boot](/assets/images/boot-preference/step-3.png)

Then click Ok and then click Finish and then will ask for Reboot click Yes
![Click Yes](/assets/images/boot-preference/step-5.png)

After the rebooting you can boot from SD Card and then shutdown the system to boot from USB drive with OS

## OS

install Ubuntu Server 22.04 for ARM64 on SD Card and NVMe SSD
