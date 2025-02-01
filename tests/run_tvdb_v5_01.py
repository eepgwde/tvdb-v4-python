import unittest
import logging
import tempfile
import pickle

from tvdb_v5_unofficial import __Id__ as weavesId
from tvdb_v5_unofficial import TVDB, Config

import json
import os

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

    # force netrc
    h0 = Config.defaults()
    logger.info(f"h0: keys: {h0.keys()}")

    f0 = lambda x: "netrc" in x.lower()
    v1 = next(filter(f0, h0.keys()))

    logger.info(f"v1: Netrc handler: {v1}")

    v2 = h0[v1]
    logger.info(f"v2: Netrc handler: defaults: {v2}")

    v2 = h0[v1]["config_file"]
    logger.info(f"v2: Netrc handler: config_file: {v2}")
    r0 = Config.instance().get_config_file(key0="netrc", defaults0=h0)

    logger.info(f"get_config_file: r0[0]: {r0[0]}")
    logger.info(f"get_config_file: r0[1]: {r0[1]}")

    machine0 = r0[1].get("machine", None)

    # tvdb = TVDB(config_file="./config.json")

  @unittest.skip("Not used")
  def test_011(self):
    self.assertIsNotNone(tvdb)
    logger.info(f"tvdb: TVDB: {tvdb}")

    v0 = tvdb.search("Lost", language="en", limit=10, type="series")
    fpickle1(v0)

# -*- coding: utf-8 -*-
# Local Variables:
# mode:python
# python-indent-offset: 2
# End:
