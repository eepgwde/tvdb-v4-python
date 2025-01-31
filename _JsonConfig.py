from _ConfigHandler import ConfigHandler
import os

class JsonConfigHandler(ConfigHandler):
  defaults0 = {
    "name": "config.json",
    "env0": "TVDB_CONFIG",
    "config_dir": "televida-renomo",
  }

  config = None

  def _mkname(self):
    home_dir = os.path.expanduser("~")  # Expand ~ to the user's home directory
    config_dir = os.path.join(home_dir, ".config", self.defaults0["config_dir"])
    config_file_path = os.path.join(config_dir, self.defaults0["name"])
    self.defaults0["config_file"] = config_file_path
    return config_file_path

  # if defaults0 is passed just revise the defaults0
  def __init__(self, **kwargs):
    self._mkname()
    if "defaults0" in kwargs:
      return
    self.load_config(**kwargs)


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

  def load_config(self, **kwargs):
    """Loads configuration, prioritizing environment variable
    then default location.
    Args:
    default_config_file: The default filename to look for if the
    env variable is not set

    Returns:
    A dictionary containing the configuration, or None if no config is found.
    """
    config_file = None
    if "env0" in kwargs:
        config_file = os.environ.get(kwargs["env0"], None)
        if config_file is None:
            raise NameError(f"No environment variable: {kwargs["env0"]}")
        v0 = self._load_file(config_file)
        if v0 is None:
            raise NameError(f"No file at environment variable: {kwargs["env0"]}={config_file}")
        return v0

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

  def get(self, key, default0=None, **kwargs):  # Helper method to access config values
    if self.config:
      return self.config.get(key, default)
    return default

  @classmethod
  def defaults(cls, defaults0=None):
    v0 = JsonConfigHandler(defaults0=None)
    return v0.defaults0


# -*- coding: utf-8 -*-
# Local Variables:
# mode:python
# python-indent-offset: 2
# End:
