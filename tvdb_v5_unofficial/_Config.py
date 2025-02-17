import sys
import os
import json

import tempfile
import pickle

from ._ConfigHandlerFactory import ConfigHandlerFactory

from ._ConfigHandler import ConfigHandler

from ._Pdb0 import Pdb0

import pdb

class Config:
  """This is a Utility Singleton for accessing Configurations.

  The instance() method returns the Singleton and with it one can access utility methods.

  The handler() method is another class method like instance(). Pass it some keyword arguments and it will attempt to create a configuration that will allow you to initialize a TVDB instance.

  Once you have a working handler you can store it where you like. This Singleton is a very good place to do that. 
  """

  config={}
  factory=None

  _handler0 = None
  kwargs={}
  _instance=None

  def __init__(self, **kwargs):
    if Config._instance is not None:
      raise RuntimeError("Use the instance() method")
    # Enforce singleton
    self.factory = ConfigHandlerFactory()  # Create the factory.
    self.kwargs = kwargs
    Config._instance = self  # Set the class instance

  @classmethod
  def defaults(cls, **kwargs):
    """This is not an instance method."""
    factory = ConfigHandlerFactory()  # Create the factory.
    return factory.get_defaults(**kwargs)

  @classmethod
  def handler(cls, **kwargs): 
    """
    Instantiates a configuration that can be interrogated later with get().

    The handler is created everytime given the kwargs passed to it.

    """
    h0 = cls.instance()._load_config(**kwargs)
    cls._instance._handler0 = h0
    return h0

  def handler0(self):
    """Retrieve the last handler built."""
    return self._handler0

  def get_configuror(self, config_file=None):
    configuror = None
    if isinstance(config_file, ConfigHandler):
      configuror = config_file
    elif isinstance(config_file, str):
      configuror = Config.handler(config_file=config_file)

    if configuror is None:
      configuror = Config.instance().handler0()

    assert configuror is not None, "null configuror"

    return configuror

  def get_config_file(self, key0="none", defaults0=None):
    if defaults0 is None:
      defaults0 = self.defaults()

    f0 = lambda x: key0 in x.lower()
    v1 = next(filter(f0, defaults0.keys()))
    if v1 is None:
      return None

    v2 = defaults0[v1]["config_file"]
    return (v2, defaults0[v1])

  @classmethod
  def instance(cls, **kwargs):
    if cls._instance is None:
      cls._instance = Config(**kwargs)

    return cls._instance 

  @classmethod
  def _load_config(cls, **kwargs):
    handler = None
    Pdb0().trap1 = 6
    try:
      handler = cls._instance.factory.get_handler(**kwargs)  # Get the handler.
    except ValueError as e:
      raise
    except Exception as e:  # Catch other exceptions.
      raise ValueError(f"no configuration: unexpected {e}")

    return handler

  ## Following are utility methods

  def pickle1(self, v0, **kwargs):
    """
    Pickles a Python object to a temporary file in the current directory.

    Args:
        obj: The Python object to pickle.

    Returns:
        The absolute path to the temporary file, or None if an error occurs.
    """
    try:
        with tempfile.NamedTemporaryFile(
                mode='wb',
                delete=False, dir=".", prefix="pickle_",
                suffix=".pkl") as temp_file:
            pickle.dump(v0, temp_file)
            temp_file_path = temp_file.name
        return temp_file_path
    except Exception as e:
        print(f"Error pickling object: {e}")
        return None

  def line_reader(self, filename):
    """
    Reads a file line by line and yields each line.

    Args:
      filename: The path to the file to read.

    Yields:
      The next line in the file.
    """
    with open(filename, 'r') as f:
      for line in f:
        yield line.strip()
      


# -*- coding: utf-8 -*-
# Local Variables:
# mode:python
# python-indent-offset: 2
# End:
