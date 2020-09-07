#!/bin/bash
cd "$(dirname "$0")"

install -D -m 755 autoscale.sh ~/.bin/autoscale.sh
install -D -m 755 autoscale.service ~/.config/systemd/user/autoscale.service

systemctl --user enable autoscale
systemctl --user start autoscale
