from pydbus import SessionBus
from gi.repository import Gio, GLib


class Service:
    def __init__(self, bus=SessionBus(), loop=GLib.MainLoop()):
        self.bus = bus
        self.loop = loop
        self.proxy = self.bus.get(
            "org.gnome.Mutter.DisplayConfig",
            "/org/gnome/Mutter/DisplayConfig"
        )

    def _changed(self):
        current_state = self.proxy.GetCurrentState()
        builtin = False

        # Fields, as documented in:
        # https://gitlab.gnome.org/GNOME/mutter/-/blob/main/data/dbus-interfaces/org.gnome.Mutter.DisplayConfig.xml
        serial = current_state[0]
        monitors = current_state[1]
        logical_monitors = current_state[2]
        properties = current_state[3]

        for monitor in monitors:
            connector = monitor[0][0]
            vendor = monitor[0][1]
            product = monitor[0][2]
            serial = monitor[0][3]
            modes = monitor[1]
            properties = monitor[2]
            if properties.get('is-builtin', False):
                for mode in modes:
                    properties = mode[6]
                    if properties.get('is-current', False):
                        builtin = connector

        setting = Gio.Settings.new('org.gnome.desktop.interface')
        if builtin:
            setting.set_double('text-scaling-factor', 1.25)
        else:
            setting.set_double('text-scaling-factor', 1.0)

    def run(self):
        self._changed()  # initially check state
        self.proxy.MonitorsChanged.connect(self._changed)
        self.loop.run()


if __name__ == '__main__':
    Service().run()
