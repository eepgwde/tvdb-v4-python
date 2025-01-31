import netrc
import os

from _ConfigHandler import ConfigHandler

class NetrcConfigHandler(ConfigHandler):
    netrc0 = None

    defaults0 = {
        "name": ".netrc",
        "env0": "NETRC",
        "config_dir": os.path.expanduser("~")
    }

    @classmethod
    def _mkname(cls):
        config_file_path = os.path.join(
            cls.defaults0["config_dir"],
            cls.defaults0["name"])
        cls.defaults0["config_file"] = config_file_path
        return config_file_path

    def __init__(self, **kwargs):
        self._mkname()

    def load_config(self, **kwargs):
        try:
            self.netrc0 = netrc.netrc(config_file)
            return self.netrc0

        except (FileNotFoundError, netrc.NetrcParseError) as e:
            print(f"Error loading .netrc config: {e}")
            return {}

    def get(self, default0=None, **kwargs):
        return

    @classmethod
    def defaults(cls, defaults0=None):
        v0 = NetrcConfigHandler()
        return v0.defaults0
