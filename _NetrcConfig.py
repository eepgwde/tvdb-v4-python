import netrc
import os
import sys

from _ConfigHandler import ConfigHandler

class NetrcConfigHandler(ConfigHandler):
    netrc0 = None

    defaults0 = {
        "name": ".netrc",
        "env0": "NETRC",
        "env1": "NETRC_MACHINE",
        "config_dir": os.path.expanduser("~")
    }

    def _mkname(self):
        config_file_path = os.path.join(
            self.defaults0["config_dir"],
            self.defaults0["name"])
        self.defaults0["config_file"] = config_file_path
        return config_file_path

    def __init__(self, **kwargs):
        self._mkname()
        if "defaults0" in kwargs:
            return
        self.load_config(**kwargs)


    def load_config(self, **kwargs):
        if "env0" in kwargs:
            f0 = os.environ.get(kwargs["env0"], None)
            if f0 is None:
                raise NameError(f"No environment variable: {kwargs["env0"]}")

        try:
            self.netrc0 = netrc.netrc()
            return self.netrc0

        except (FileNotFoundError, netrc.NetrcParseError) as e:
            print(f"Error loading .netrc config: {e}", file=sys.stderr)
            return {}

    def get(self, default0=None, **kwargs):
        return

    @classmethod
    def defaults(cls, defaults0=None):
        v0 = NetrcConfigHandler()
        return v0.defaults0
