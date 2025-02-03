import json
import os
import sys

import tempfile
import pickle

from _Config import Config

import tvdb_v4_unofficial

class Url(tvdb_v4_unofficial.Url):
  """
  An override of the tvdb_v4_unofficial:Url class.

  It gets the base_url attribute from the Config.instance().
  """
  base_url = ""

  def __init__(self, config_file=None):
    configuror = Config.instance().get_configuror(config_file=config_file)

    super().__init__()
    self.base_url = configuror.get("url")

class TVDB(tvdb_v4_unofficial.TVDB):
  """
  An override of the tvdb_v4_unofficial:TVDB class.

  It uses the Config.instance() to get a configuror and gets the items needed to create a tvdb_v4_unofficial instance.
  """

  def __init__(self, config_file=None):
    """Polymorphic parameter in config_file"""
    configuror = Config.instance().get_configuror(config_file=config_file)

    apikey = configuror.get("apikey")
    pin = configuror.get("pin", "")
    url = Url(config_file=configuror)

    if not apikey or not url:
      raise ValueError("Missing 'apikey' or 'url' in config.")

    super().__init__(apikey, pin, url)


# -*- coding: utf-8 -*-
# Local Variables:
# mode:python
# python-indent-offset: 2
# End:
