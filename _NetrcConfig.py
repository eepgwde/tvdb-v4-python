import netrc

from _ConfigHandler import ConfigHandler

class NetrcConfigHandler(ConfigHandler):
    netrc_obj = None

    def load_config(self, config_file):
        try:
            self.netrc_obj = netrc.netrc(config_file)
            return self.netrc_obj

        except (FileNotFoundError, netrc.NetrcParseError) as e:
            print(f"Error loading .netrc config: {e}")
            return {}

    def get(self, default0=None, **kwargs):
        return 


