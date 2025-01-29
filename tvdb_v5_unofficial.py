import json
import os
from tvdb_4_official import Url as Url0, TVDB as TVDB0
# Import only Url and TVDB

def load_config(default_config_file="config.json"):
    """Loads configuration, prioritizing environment variable, then default location.

    Args:
        default_config_file: The default filename to look for if the env variable is not set

    Returns:
        A dictionary containing the configuration, or None if no config is found.
    """

    # 1. Check for environment variable
    env_config_file = os.environ.get("TVDB_CONFIG")
    if env_config_file:
        try:
            with open(env_config_file, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading config from env variable path '{env_config_file}': {e}")
            # Fallback to default location
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None

    # 2. Check default location ($HOME/.config/tvdb/)
    home_dir = os.path.expanduser("~")  # Expand ~ to the user's home directory
    config_dir = os.path.join(home_dir, ".config", "tvdb")
    config_file_path = os.path.join(config_dir, default_config_file)

    try:
        with open(config_file_path, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading config from default location '{config_file_path}': {e}")
        return None #Return None if no config is found
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Example Usage:
config = load_config() #Will first check the env variable and then the default path.

if config:
    base_url = config.get("base_url") or "https://api4.thetvdb.com/v4/"
    apikey = config.get("apikey")
    # ... use config
else:
    print("No configuration file found.")

class Url(Url0):  # Inherit from the original Url
    def __init__(self, config_file="config.json"):
        config = self.load_config(config_file)
        if config and "base_url" in config:
            base_url = config["base_url"]
        else:
            base_url = "https://api4.thetvdb.com/v4/"  # Default
            print(f"Warning: 'base_url' not found in {config_file}. Using default.")
        tvdb_v4_official.Url.__init__(self, base_url) #Call the parent class's __init__

    def load_config(self, config_file):
        try:
            config_path = os.path.join(os.path.dirname(__file__), config_file)
            with open(config_path, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Warning: Configuration file '{config_file}' not found. Using defaults.")
            return None
        except json.JSONDecodeError:
            print(f"Warning: Invalid JSON in '{config_file}'. Using defaults.")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None


class TVDB(TVDB0):  # Inherit from the original TVDB
    def __init__(self, config_file="config.json"):
        config = self.load_config(config_file)
        if config and "apikey" in config and "base_url" in config:
            apikey = config["apikey"]
            base_url = config["base_url"]
        else:
            print(f"Error: 'apikey' or 'base_url' not found in {config_file}.")
            return  # Or raise an exception if you prefer

        tvdb_v4_official.TVDB.__init__(self, apikey, base_url) #Call the parent class's __init__


    def load_config(self, config_file):
        try:
            config_path = os.path.join(os.path.dirname(__file__), config_file)
            with open(config_path, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Warning: Configuration file '{config_file}' not found. Using defaults.")
            return None
        except json.JSONDecodeError:
            print(f"Warning: Invalid JSON in '{config_file}'. Using defaults.")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None


class Config:
    _instance = None  # Singleton instance

    def __init__(self, config_file="config.json"):
        if Config._instance is not None:
            raise RuntimeError("Call get_instance() instead")  # Enforce singleton
        self.config = self._load_config(config_file)  # Load config once
        Config._instance = self  # Set the instance

    @staticmethod
    def get_instance(config_file="config.json"):
        if Config._instance is None:
            Config(config_file)  # Create the instance if it doesn't exist
        return Config._instance

    def _load_config(self, config_file):
        """Loads configuration, prioritizing env variable, then default location."""
        # ... (same config loading logic as before)

    def get(self, key, default=None):  # Helper method to access config values
        if self.config:
            return self.config.get(key, default)
        return default


# Your configurable classes
from tvdb_4_official import Url, TVDB

class ConfigurableUrl(Url):
    def __init__(self):  # No config_file argument here
        config = Config.get_instance()  # Get the singleton instance
        base_url = config.get("base_url") or "https://api4.thetvdb.com/v4/"
        Url.__init__(self, base_url)

class ConfigurableTVDB(TVDB):
    def __init__(self):  # No config_file argument here
        config = Config.get_instance()  # Get the singleton instance
        apikey = config.get("apikey")
        base_url = config.get("base_url")

        if not apikey or not base_url:
            raise ValueError("Missing 'apikey' or 'base_url' in config.")

        TVDB.__init__(self, apikey, base_url)
