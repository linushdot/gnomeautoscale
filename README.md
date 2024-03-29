# Gnome Text Auto-Scaling

Simple script to automatically scale up text if the builtin display of a laptop
is turned on. Adjusts Gnome's text-scaling-factor based on built-in display
status.

- Built-in display active: text-scaling-factor 1.25
- Built-in display not active: text-scaling-factor 1.0

This behavior can be easily adapted/extended by editing `gnomeautoscale.py`.
Also, the script and systemd service is only tested under Arch Linux so far.

## Requirements

- Python
- Python packages:
  - PyGObject
  - pydbus
- systemd (if you want to run it as a user service)

## Running

```shell
python gnomeautoscale.py
```

## Install as User Service

```shell
./install.sh
```

This copies files to
```
~/.bin/gnomeautoscale.py
~/.config/systemd/user/gnomeautoscale.service
```

and enables and starts the script as a systemd user service [1].

Control the service with 
```shell
systemctl --user status gnomeautoscale
systemctl --user stop gnomeautoscale
systemctl --user start gnomeautoscale
...
```

When the service fails to start because dbus is not up yet, it will restart
every 5 seconds until it is successful. This is not optimal and potentially
could be improved by using systemd dependencies.

[1]: https://wiki.archlinux.org/title/Systemd/User
