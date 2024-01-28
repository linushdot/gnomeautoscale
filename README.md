# Gnome Text Auto-Scaling

Simple script to automatically scale up text if the builtin display of a laptop
is turned on. Adjusts Gnome's text-scaling-factor based on built-in display
status.

- Built-in display active: text-scaling-factor 1.25
- Built-in display not active: text-scaling-factor 1.0

This behavior can be easily adapted/extended by editing `gnomeautoscale.py`.

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

[1]: https://wiki.archlinux.org/title/Systemd/User