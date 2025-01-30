import json
import os
import sys

from tvdb_v4_official import Url as Url0, TVDB as TVDB0

from _Lockable import Lockable
from _ConfigHandler import ConfigHandler


import pdb

# Import only Url and TVDB

__Id__ = "$Id: 3ea81035d76c968d73b5840b3d0f845d47e216c5 $"


class Url(Url0):
  base_url = ""

  def __init__(self):  # No config_file argument here
    url = Config.instance().get("url")  # Get the singleton instance
    super().__init__()
    self.base_url = url


class TVDB(TVDB0):
  def __init__(self, config_file=None):
    apikey = Config.instance(config_file).get("apikey")
    pin = Config.instance(config_file).get("pin", "")
    url = Url()

    if not apikey or not url:
      raise ValueError("Missing 'apikey' or 'url' in config.")

    # TVDB0.__init__(self, apikey, pin)
    super().__init__(apikey, pin, url)

class Config:
  config={}
  factory=None
  handler=None
  kwargs={}

  def __init__(self, **kwargs):
    if Config._instance is not None:
      raise RuntimeError("Use the instance() method")
    # Enforce singleton
    self.factory = ConfigHandlerFactory(**kwargs)  # Create the factory.
    self.kwargs = kwargs
    Config._instance = self  # Set the instance

  @classmethod
  def instance(cls, **kwargs):
    """
    Instantiates a configuration that can be interrogated later with get().

    It has a feature that if you call it with a new configuration file as
    a parameter, it will load that.
    """
    reset0 = False
    if "reset0" in kwargs:
      reset0 = kwargs["reset0"]

    # Create the instance if it doesn't exist
    if cls._instance is None or reset0:
      cls._instance.handler = _load_config(**kwargs)

    return cls._instance.handler

  def _load_config(self, **kwargs):
    handler = None
    try:
      handler = self.factory.get_handler(**kwargs)  # Get the handler.
    except ValueError as e:
      print(f"Error: {e}")  # Handle unsupported format
      # Provide default values.
    except Exception as e:  # Catch other exceptions.
      print(f"Error loading configuration: {e}")

    return handler












# -*- coding: utf-8 -*-
# Local Variables:
# mode:python
# python-indent-offset: 2
# End:
