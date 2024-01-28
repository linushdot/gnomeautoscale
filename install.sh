#!/bin/bash
cd "$(dirname "$0")"

install -D -m 755 gnomeautoscale.py ~/.bin/gnomeautoscale.py
install -D -m 755 gnomeautoscale.service ~/.config/systemd/user/gnomeautoscale.service

systemctl --user enable gnomeautoscale
systemctl --user start gnomeautoscale
