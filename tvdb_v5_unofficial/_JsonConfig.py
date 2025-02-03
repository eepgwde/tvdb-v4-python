import os
import sys
import json

from ._ConfigHandler import ConfigHandler
from ._Pdb0 import Pdb0

class JsonConfigHandler(ConfigHandler):
  defaults0 = {
    "name": "config.json",
    "env0": "TVDB_CONFIG",
    "config_dir": "televida-renomo"
    # config_file is added by _mkname
  }

  _config = None
  kwargs = {}

  def _mkname(self):
    home_dir = os.path.expanduser("~")  # Expand ~ to the user's home directory
    config_dir = os.path.join(home_dir, ".config", self.defaults0["config_dir"])
    config_file_path = os.path.join(config_dir, self.defaults0["name"])
    self.defaults0["config_file"] = config_file_path
    return config_file_path

  # if defaults0 is passed just revise the defaults0
  def __init__(self, **kwargs):
    self._mkname()
    self.kwargs = kwargs
    if "defaults0" in kwargs:
      return
    self._config = self.load_config(**kwargs)

  @classmethod
  def get_default(cls, **kwargs):
    v0 = cls.defaults0["config_file"]
    return { "config_file": v0 }

  def _load_file(self, f0: str):
    """
    Load a JSON file
    """
    if f0 is None:
      return None

    if not self._hasTyper({ "config_file" : f0, "config_type" : ".json" }):
      return None

    Pdb0().trap1 = 5
    try:
      with open(f0, "r") as f:
        self._config = json.load(f)
        return self._config
    except (FileNotFoundError, json.JSONDecodeError) as e:
      # print(f"Error file: '{f0}': {e}", file=sys.stderr)
      pdb.set_trace()
      return None
    except Exception as e:
      print(f"An unexpected error occurred: {e}", file=sys.stderr)
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
    Pdb0().trap1 = 5
    config_file = None
    # 1. check for a named env0 pointing to a file in the keywords
    if "env0" in kwargs:
        config_file = os.environ.get(kwargs["env0"], None)
        if config_file is None:
            raise NameError(f"No environment variable: {kwargs["env0"]}")
        v0 = self._load_file(config_file)
        if v0 is None:
            raise NameError(f"No file at environment variable: {kwargs["env0"]}={config_file}")
        return v0

    # 2. check for a named config file in the keywords
    if "config_file" in kwargs:
        config_file = kwargs["config_file"]
        v0 = self._load_file(config_file)
        if v0 is None:
            raise ValueError(f"no configuration: bad ${config_file}")
        return v0

    # 3. Check default location ($HOME/.config/tvdb/)
    v0 = self._load_file(self.defaults0["config_file"])

    if v0 is not None:
        return v0

    raise ValueError(
      "no configuration found: use defaults() for environment and file locations"
    )

  def get(self, key, default0=None, **kwargs):  # Helper method to access config values
    assert self._config is not None, f"no _config in {self.__class__.name}"
    return self._config.get(key, default0)

  @classmethod
  def defaults(cls, **kwargs):
    if not "defaults0" in kwargs:
        kwargs["defaults0"]=None

    v0 = JsonConfigHandler(**kwargs)
    return v0.defaults0


# -*- coding: utf-8 -*-
# Local Variables:
# mode:python
# python-indent-offset: 2
# End:
