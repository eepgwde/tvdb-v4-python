from abc import ABC, abstractmethod
import netrc
import os

class ConfigHandler(ABC):
    @abstractmethod
    def load_config(self, config_file):
        """
        Loads configuration data from the specified file.

        Args:
            config_file (str): Path to the configuration file.

        Returns:
            dict: A dictionary containing the loaded configuration data.
        """
        pass

class JsonConfigHandler(ConfigHandler):
    def load_config(self, config_file):
        try:
            with open(config_file, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading JSON config: {e}")
            return {}

class NetrcConfigHandler(ConfigHandler):
    def load_config(self, config_file):
        try:
            netrc_obj = netrc.netrc(config_file)
            login_info = {}
            for machine in netrc_obj.machines:
                login_info[machine] = netrc_obj.authenticators(machine) 
            return login_info
        except (FileNotFoundError, netrc.NetrcParseError) as e:
            print(f"Error loading .netrc config: {e}")
            return {}
