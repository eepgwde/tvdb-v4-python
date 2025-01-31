import unittest
import logging
import tempfile
import pickle

from tvdb_v5_unofficial import __Id__ as weavesId
from tvdb_v5_unofficial import Config

import json
import os

import pdb

logging.basicConfig(filename='test.log', level=logging.DEBUG)
logger = logging.getLogger('Test')
sh = logging.StreamHandler()
logger.addHandler(sh)


class Test4(unittest.TestCase):
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

  ## Both config handlers should fail
  def test_005(self):
    self.assertIsNotNone(weavesId)
    if "TVDB_CONFIG" in os.environ:
      del os.environ["TVDB_CONFIG"]

    v0 = Config.handler(env0="TVDB_CONFIG")
    self.assertIsNone(v0)
    logger.info(f"configHandler: {v0}")

  ## Only the JSON should pass
  # Use the instance itself as an unsafe hacker's
  # cache.
  def test_007(self):
    self.assertIsNotNone(weavesId)
    os.environ["TVDB_CONFIG"]="./config.json"
    pdb.set_trace()
    v0 = Config.handler(env0="TVDB_CONFIG")
    self.assertIsNotNone(v0)
    logger.info(f"configHandler: {v0}")
    Config.instance().kwargs["jsonHandler"]=v0

  ## Check the unsafe hacker's cache works.
  def test_008(self):
    self.assertIsNotNone(weavesId)
    v0 = Config.instance().kwargs["jsonHandler"]
    self.assertIsNotNone(v0)
    logger.info(f"configHandler: {v0}")


  ## Only the NETRC should pass
  def test_009(self):
    self.assertIsNotNone(weavesId)
    os.environ["TVDB_CONFIG"]="./netrc"
    v0 = Config.handler(env0="TVDB_CONFIG")
    self.assertIsNotNone(v0)
    logger.info(f"configHandler: {v0}")

  ## Get the URL, needs an environment variable.
  # or a machine.
  def test_011(self):
    self.assertIsNotNone(weavesId)
    os.environ["TVDB_CONFIG"]="./netrc"
    v0 = Config.handler(env0="TVDB_CONFIG", env1="TVDB_MACHINE")
    self.assertIsNotNone(v0)
    url = v0.get("url", env0="TVDB_CONFIG", env1="TVDB_MACHINE")
    self.assertIsNone(url)
    logger.info(f"configHandler: {v0}; url: {url}")

  ## Get a machine URL, keyword
  def test_013(self):
    self.assertIsNotNone(weavesId)
    os.environ["TVDB_CONFIG"]="./netrc"
    v0 = Config.handler(env0="TVDB_CONFIG", env1="TVDB_MACHINE")
    self.assertIsNotNone(v0)
    url = v0.get("url", machine="api5.olympic.host0")
    self.assertIsNotNone(v0)
    logger.info(f"configHandler: {v0}; url: {url}")

  def test_015(self):
    self.assertIsNotNone(weavesId)
    os.environ["TVDB_CONFIG"]="./netrc"
    v0 = Config.handler(env0="TVDB_CONFIG", env1="TVDB_MACHINE")
    self.assertIsNotNone(v0)
    apikey = v0.get("apikey", machine="api5.olympic.host0")
    self.assertIsNotNone(v0)
    logger.info(f"configHandler: {v0}; apikey: {apikey}")

  def test_017(self):
    """
    This should access the file in ~/.netrc

    The keywords are cached in the instance when handler is called.
    """
    self.assertIsNotNone(weavesId)
    if "TVDB_CONFIG" in os.environ:
      del os.environ["TVDB_CONFIG"]

    os.environ["TVDB_MACHINE"]="api4.thetvdb.com"
    v0 = Config.handler(env1="TVDB_MACHINE")
    self.assertIsNotNone(v0)
    apikey = v0.get("apikey")
    self.assertIsNotNone(v0)
    logger.info(f"configHandler: {v0}; apikey: {apikey}")


# -*- coding: utf-8 -*-
# Local Variables:
# mode:python
# python-indent-offset: 2
# End:
