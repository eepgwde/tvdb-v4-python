from _ConfigHandler import ConfigHandler

class JsonConfigHandler(ConfigHandler):
    def load_config(self, config_file):
        try:
            with open(config_file, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading JSON config: {e}")
            return {}

class JsonConfigHandler(ConfigHandler):
  defaults0 = {
    "name": "config.json",
    "env-var-name": "TVDB_CONFIG",
    "config-dir": "televida-renomo",
  }

  config = None

  @classmethod
  def _mkname(cls):
    home_dir = os.path.expanduser("~")  # Expand ~ to the user's home directory
    config_dir = os.path.join(home_dir, ".config", cls.defaults0["config-dir"])
    config_file_path = os.path.join(config_dir, cls.defaults0["name"])
    cls.defaults0["config-path"] = config_file_path
    return config_file_path

  def __init__(self, config_file=None):
    if Config._instance is not None:
      raise RuntimeError("Use the instance() method")
    # Enforce singleton
    v0 = Config._mkname()
    self.config = self._load_config(config_file)  # Load config once
    Config._instance = self  # Set the instance

  def _load_file(self, f0: str):
    """
    Load a JSON file
    """
    if f0 is None:
      return None
    try:
      with open(f0, "r") as f:
        return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
      print(f"Error file: '{f0}': {e}", file=sys.stderr)
      # pdb.set_trace()
      return None
    except Exception as e:
      print(f"An unexpected error occurred: {e}")
      return None

  def load_config(self, config_file=None):
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
      v0 = self._load_file(os.environ.get(self.defaults0["env-var-name"]))
      if v0 is None:
        # 2. Check default location ($HOME/.config/tvdb/)
        v0 = self._load_file(self.defaults0["config-path"])

    if v0 is not None:
      self.config = v0
      return self.config

    raise ValueError(
      "no configuration found: use defaults() for environment and file locations"
    )

  def get(self, key, default=None):  # Helper method to access config values
    if self.config:
      return self.config.get(key, default)
    return default

# -*- coding: utf-8 -*-
# Local Variables:
# mode:python
# python-indent-offset: 2
# End:
