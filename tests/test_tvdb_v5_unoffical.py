import unittest
import logging

from tvdb_v5_unofficial import __Id__ as weavesId
from tvdb_v5_unofficial import TVDB
from tvdb_v5_unofficial import Config

import json
import os

import pdb

VALID_API_KEY = "valid_api_key"
VALID_PIN = "valid_pin"

logging.basicConfig(filename='test.log', level=logging.DEBUG)
logger = logging.getLogger('Test')
sh = logging.StreamHandler()
logger.addHandler(sh)

## A test driver for GMus0
#
# @see GMus0
class Test1(unittest.TestCase):
  """
  Test the Config object for JSON files

  See the defaults of the Config Handlers
  Use the environment to get settings
  Use a file.
  """

  url1="http://lydia.host0"

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
    """
    Show the defaults in the configuration handlers'.
    """
    self.assertIsNotNone(weavesId)
    v0 = Config.defaults()
    self.assertIsNotNone(v0)
    logger.info(f"defaults: {v0}")

  ## a
  # @unittest.expectedFailure
  def test_005(self):
    """Should fail with an Exception

    Without changing HOME, it may find your ~/.netrc

    For the test method, there is an alternative configuration using expected failure"""
    self.assertIsNotNone(weavesId)

    home0 = os.environ["HOME"]
    os.environ["HOME"] = os.environ["PWD"]

    v0 = Config.handler()
    logger.info(f"handler: ConfigHandler:  {v0}")
    if v0 is not None:
      logger.info(f"handler: class: {v0.__class__.__name__}")

    ## not a - comment this if you use config a
    # with self.assertRaisesRegex(
    #     ValueError, "no configuration.+"
    #   ):
    #   v0 = Config.handler()

    ## a
    # v0 = Config.instance()

  def test_009(self):
    """Get configuration items from a local file
    and cache the handler in the instance.

    The keyword arguments will be cached in the handler
    """
    self.assertIsNotNone(weavesId)
    v0 = Config.handler(config_file="./config.json")
    self.assertIsNotNone(v0)

    v1 = v0.get("url")
    self.assertIsNotNone(v0)
    logger.info(f"url: string:  {v1}")

    v1 = v0.get("apikey")
    self.assertIsNotNone(v1)
    logger.info(f"apikey: string: {v1}")
    # store in the instance.
    Config.instance().kwargs["handler0"]=v0

  def test_011(self):
    """
    Load the last handler from the instance
    """
    self.assertIsNotNone(weavesId)
    v0 = Config.instance().kwargs.get("handler0")
    self.assertIsNotNone(v0)

    v1 = v0.get("url")
    self.assertIsNotNone(v1)
    logger.info(f"url: string:  {v1}")

    v1 = v0.get("apikey")
    self.assertIsNotNone(v1)
    logger.info(f"apikey: string:  {v1}")

  def test_013(self):
    """Get configuration items via an environment variable.
    """
    self.assertIsNotNone(weavesId)

    defaults0 = Config.defaults()
    self.assertIsNotNone(defaults0)
    logger.info(f"defaults0: {defaults0}")

    os.environ["TVDB_CONFIG"]="./config2.json"

    v0 = Config.handler(env0="TVDB_CONFIG")

    v1 = v0.get("url")
    self.assertIsNotNone(v1)
    logger.info(f"url: string:  {v1}")

    v1 = v0.get("apikey")
    self.assertIsNotNone(v1)
    logger.info(f"apikey: string:  {v1}")

  def test_015(self):
    """access via an alternative env0"""
    self.assertIsNotNone(weavesId)

    # This doesn't work
    # os.unsetenv(v0)

    # Check if it exists before deleting
    v0 = "CFG0"
    if v0 in os.environ:  
      del os.environ[v0]

    self.assertIsNone(os.environ.get(v0))

    os.environ[v0] = "./config2.json"

    v1 = Config.handler(env0=v0).get("url")
    self.assertIsNotNone(v1)
    logger.info(f"url: string:  {v1}")

    v1 = Config.handler().get("apikey")
    self.assertIsNotNone(v1)
    logger.info(f"apikey: string:  {v1}")

    v1 = Config.handler().get("pin")
    self.assertIsNotNone(v1)
    logger.info(f"pin: string:  {v1}")

  def test_017(self):
    """Test the default location.

    This test changes HOME to be the PWD, which is the source directory, and
    there is a .config/ in the source directory and a visible link as a
    reminder.
    """
    self.assertIsNotNone(weavesId)

    os.environ["HOME"] = os.environ["PWD"]
    v0 = Config.handler()
    self.assertIsNotNone(v0)
    v1 = v0.get("url")
    self.assertIsNotNone(v0)
    logger.info(f"url: string:  {v1}")

    v1 = v0.get("apikey")
    self.assertIsNotNone(v1)
    logger.info(f"apikey: string:  {v1}")

    v1 = v0.get("pin")
    self.assertIsNotNone(v1)
    logger.info(f"pin: string:  {v1}")

    v1 = v0.get("ping")
    self.assertIsNone(v1)
    logger.info(f"ping: string:  {v1}")

# -*- coding: utf-8 -*-
# Local Variables:
# mode:python
# python-indent-offset: 2
# End:
