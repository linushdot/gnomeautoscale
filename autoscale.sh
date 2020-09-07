#!/bin/bash

function handle() {
    line=$1
    if [[ $line =~ "MonitorsChanged" ]]; then
        builtinoff=`gdbus call --session --dest=org.gnome.Mutter.DisplayConfig \
            --object-path /org/gnome/Mutter/DisplayConfig \
            --method org.gnome.Mutter.DisplayConfig.GetResources | grep -- "-1, \[0, 1, 2\], 'eDP-1'"`

        if [ -z "$builtinoff" ]; then
            gsettings set org.gnome.desktop.interface text-scaling-factor 1.25
        else
            gsettings set org.gnome.desktop.interface text-scaling-factor 1.0
        fi
    fi
}

dbus-monitor --session "type=signal,interface=org.gnome.Mutter.DisplayConfig,member=MonitorsChanged" \
    | (while read line; do handle "$line"; done)
