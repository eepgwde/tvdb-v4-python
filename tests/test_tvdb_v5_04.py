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
  def test_007(self):
    self.assertIsNotNone(weavesId)
    os.environ["TVDB_CONFIG"]="./config.json"
    v0 = Config.handler(env0="TVDB_CONFIG")
    self.assertIsNotNone(v0)
    logger.info(f"configHandler: {v0}")
    Config.instance().kwargs["jsonHandler"]=v0

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


# -*- coding: utf-8 -*-
# Local Variables:
# mode:python
# python-indent-offset: 2
# End:
