import json
import os
from tvdb_v4_official import Url as Url0, TVDB as TVDB0

# Import only Url and TVDB

__Id__ = u"$Id: 3ea81035d76c968d73b5840b3d0f845d47e216c5 $"

class Url(Url0):
  def __init__(self):  # No config_file argument here
    config = Config.instance().get("url")  # Get the singleton instance
    base_url = config.get("base_url") or "http://api4.thetvdb.com/v4/"
    Url0.__init__(self, base_url)


class TVDB(TVDB0):
  def __init__(self, config_file=None):
    apikey = Config.instance(config_file).get("apikey") 
    base_url = Config.instance(config_file).get("base_url") 

    if not apikey or not base_url:
      raise ValueError("Missing 'apikey' or 'base_url' in config.")

    TVDB0.__init__(self, apikey, base_url)

class Config:
  _instance = None  # Singleton instance

  defaults0 = { "name": "config.json",
                "env-var-name": "TVDB_CONFIG",
                "config-dir": "televida-renomo" }

  config=None

  @classmethod
  def _mkname(cls):
    home_dir = os.path.expanduser("~")  # Expand ~ to the user's home directory
    config_dir = os.path.join(home_dir, ".config",
                              cls.defaults0["config-dir"])
    config_file_path = os.path.join(config_dir, cls.defaults0['name'])
    cls.defaults0['config-path']=config_file_path
    return config_file_path

  def __init__(self, config_file=None):
    if Config._instance is not None:
      raise RuntimeError("Use the instance() method")
    # Enforce singleton
    v0 = Config._mkname()
    self.config = self._load_config(config_file)  # Load config once
    Config._instance = self  # Set the instance

  @classmethod
  def defaults(cls):
    return cls.defaults0

  @classmethod
  def instance(cls, config_file=None, reset0=False):
    """
    Instantiates a configuration that can be interrogated later with get().

    It has a feature that if you call it with a new configuration file as
    a parameter, it will load that.
    """
    if cls._instance is None:
      Config(config_file)
    elif config_file is None and reset0:
      # should read the environment or the default location
      cls._instance = None
      Config(config_file)
    elif config_file is not None:  # should reload
      cls._instance = None
      Config(config_file)

    # Create the instance if it doesn't exist
    return cls._instance

  def _load_file(self, f0 : str):
    """
    Load a JSON file
    """
    if f0 is None:
      return None
    try:
      with open(f0, "r") as f:
        return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
      print(f"Error file: '{f0}': {e}")
      return None
    except Exception as e:
      print(f"An unexpected error occurred: {e}")
      return None

  def _load_config(self, config_path=None):
    """Loads configuration, prioritizing environment variable
    then default location.
    Args:
    default_config_file: The default filename to look for if the
    env variable is not set

    Returns:
    A dictionary containing the configuration, or None if no config is found.
    """
    v0 = None
    if config_path is not None:
      v0 = self._load_file(config_path)
    else:
      # 1. Check for environment variable
      v0 = self._load_file(os.environ.get(self.defaults0['env-var-name']))
      if v0 is None:
        # 2. Check default location ($HOME/.config/tvdb/)
        v0 = self._load_file(self.defaults0['config-path'])

    if v0 is not None:
      self.config = v0
      return self.config

    raise ValueError("no configuration found: use defaults() for environment and file locations")


  def get(self, key, default=None):  # Helper method to access config values
    if self.config:
      return self.config.get(key, default)
    return default

# -*- coding: utf-8 -*-
# Local Variables:
# mode:python
# python-indent-offset: 2
# End:
