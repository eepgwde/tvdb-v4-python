import unittest
import logging
import tempfile
import pickle

from tvdb_v5_unofficial import __Id__ as weavesId
from tvdb_v5_unofficial import TVDB, Config

from _NetrcConfig import NetrcConfigHandler

import json
import os

from _Pdb0 import Pdb0

import pdb

logging.basicConfig(filename='test.log', level=logging.DEBUG)
logger = logging.getLogger('Test')
sh = logging.StreamHandler()
logger.addHandler(sh)


def fpickle1(obj):
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
            pickle.dump(obj, temp_file)
            temp_file_path = temp_file.name
        return temp_file_path
    except Exception as e:
        print(f"Error pickling object: {e}")
        return None


class Test3(unittest.TestCase):
  """
  Test
  """

  ## Null setup. Create a new one.
  def setUp(self):
    logger.info('setup')
    logger.info(f'test: {self._testMethodName}')

  ## Null setup.
  def tearDown(self):
    logger.info('tearDown')

  ## Loaded?
  ## Is utf-8 available as a filesystemencoding()
  def test_001(self):
    self.assertIsNotNone(weavesId)
    logger.info("module: Id: " + weavesId)

  ## Defaults
  def test_003(self):
    self.assertIsNotNone(weavesId)
    v0 = Config.defaults()
    self.assertIsNotNone(v0)
    logger.info(f"defaults: {v0}")
    
  ## Get configuration items from a local file
  # @unittest.skip("Already have Lost")
  def test_009(self):
    self.assertIsNotNone(weavesId)

    classes0 = set([NetrcConfigHandler])
    r0 = Config.instance().factory.get_defaults_run(classes=classes0, key0="netrc")
    kwargs0 = { "classes" : classes0 } | r0

    # Pdb0().trap0 = 5
    v0 = Config.handler(**kwargs0)
    self.assertIsNotNone(v0)
    logger.info(f"handler: netrc: {v0.__class__.__name__}")

    self.assertTrue(isinstance(v0, NetrcConfigHandler))

    Pdb0().trap0 = 7
    tvdb = TVDB(config_file=v0)
    v0 = tvdb.search("The Agency", language="eng", limit=5, type="series")
    fpickle1(v0)

  @unittest.skip("The Lost example")
  def test_021(self):
    self.assertIsNotNone(tvdb)
    logger.info(f"tvdb: TVDB: {tvdb}")

    v0 = tvdb.search("Lost", language="en", limit=10, type="series")
    fpickle1(v0)

# -*- coding: utf-8 -*-
# Local Variables:
# mode:python
# python-indent-offset: 2
# End:
