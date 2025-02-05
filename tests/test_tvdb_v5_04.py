## weaves
# 
# These tests use a couple of sub-directories of tests/ as HOME. 
# These sub-directories have all the configuration options available:
#  .netrc netrc
#  ./config.json ./config2.json and .config/televida-renomo/config.json
# Also I set HOME to TMPDIR for no configurations

import json
import os
import logging
import tempfile

import unittest
import pickle

from tvdb_v5_unofficial import __Id__ as weavesId
from tvdb_v5_unofficial import Config, JsonConfigHandler, NetrcConfigHandler
from ._Envs0 import Envs0

from tvdb_v5_unofficial import Pdb0

import pdb

logging.basicConfig(filename='test.log', level=logging.DEBUG)
logger = logging.getLogger('Test')
sh = logging.StreamHandler()
logger.addHandler(sh)


class Test4(unittest.TestCase, Envs0):
  """
  Test
  """

  _netrc0 = "netrc"

  ## Null setup. Create a new one.
  def setUp(self):
    logger.info('setup')
    logger.info(f'test: {self._testMethodName}')

  ## Null setup.
  def tearDown(self):
    logger.info('tearDown')
    super().tearDown()

  ## Loaded?
  ## Is utf-8 available as a filesystemencoding()
  def test_001(self):
    self.assertIsNotNone(weavesId)
    logger.info("module: Id: " + weavesId)

  def test_003(self):
    """
  Defaults
  Config.defaults() builds the defaults for the ConfigHandler instances.
  There are defaults needed for a handler to run
    env0 env1 - are both environment variable names. These two provide for indirect lookups by the Config
  instance. env0 is usually TVDB_CONFIG and would be an environment variable set to the location of a
  config file. env1 is the name of an environment variable that holds the name of a machine to use for
  the HTTP calls. This is only needed for the NetrcConfigHandler. The JsonConfigHandler has the host in
  the URL attribute in its config file.
    
  And other default values. The URL path is needed by NetrcConfigHandler.
  Config.defaults() is important it updates the defaults0() in the ConfigHandler instances.
  The ConfigHandler instances are not singletons, so I try to update the class defaults0() which an instance
  has access to.

  No valid config file or configuration is needed for this test.
    """
    self.assertIsNotNone(weavesId)
    v0 = Config.defaults()
    self.assertIsNotNone(v0)
    logger.info(f"defaults: {v0}")

  @unittest.expectedFailure
  def test_005(self):
    """
    Test if we fail correctly.

    Change HOME temporarily to use TMPDIR
    And unset the environment.

    TODO: behaviour has changed.
    """
    self.assertIsNotNone(weavesId)

    self.envsTMP()

    if "TVDB_CONFIG" in os.environ:
      del os.environ["TVDB_CONFIG"]

    v0 = None

    ## no configurations available
    with self.assertRaisesRegex(
        ValueError, "no configuration: .+"
      ):
      v0 = Config.handler()

    ## bad configuration passed
    with self.assertRaisesRegex(
        ValueError, "no configuration: .+"
      ):
      v0 = Config.handler(env0="TVDB_CONFIG")

    ## bad configuration passed
    with self.assertRaisesRegex(
        ValueError, "no configuration: .+"
      ):
      v0 = Config.handler(config_file="nothere.json")

    self.assertIsNone(v0)
    logger.info(f"configHandler: should be None: {v0}")

  def test_007(self):
    """Both the JSON or Netrc can pass, but JSON is first
    Use the instance itself as an unsafe hacker's cache."""
    self.assertIsNotNone(weavesId)

    self.envsALT()
    os.environ["TVDB_CONFIG"] = os.path.join(os.environ["HOME"], "config.json")

    # Pdb0().trap0 = 5
    
    v0 = Config.handler(env0="TVDB_CONFIG")
    self.assertIsNotNone(v0)

    # Bizarrely, this doesn't work.
    # self.assertTrue(isinstance(v0,JsonConfigHandler))
    self.assertTrue(v0.__class__.__name__ == 'JsonConfigHandler')

    logger.info(f"configHandler: {v0}")
    Config.instance().kwargs["jsonHandler"]=v0

  ## Check the unsafe hacker's cache works.
  def test_008(self):
    self.assertIsNotNone(weavesId)
    v0 = Config.instance().kwargs["jsonHandler"]
    self.assertIsNotNone(v0)
    logger.info(f"configHandler: {v0}")


  def test_009(self):
    """Only the NETRC should pass. Use tests/home1 for only NetrcConfigHandler

    Environment variables are indirect look-ups. No default, a name must be passed as
    a keyword argument.
    """
    self.assertIsNotNone(weavesId)
    self.envsALT2()
    os.environ["NETRC"]=os.path.abspath(self._netrc0)
    # Pdb0().trap0 = 5
    # Json will win if this is set.
    # os.environ["TVDB_CONFIG"]="./config.json"
    # and env0="TVDB_CONFIG"
    v0 = Config.handler(env0="NETRC")
    self.assertIsNotNone(v0)
    logger.info(f"configHandler: {v0}")


  @unittest.expectedFailure
  def test_011(self):
    """
    Get the URL, needs an environment variable or a machine or uses the default.

    This should fail: because the environment variable was given, which should mean do not use
    the defaults.
    """

    self.assertIsNotNone(weavesId)
    self.envsALT2()
    os.environ["TVDB_CONFIG"] = self._netrc0
    # os.environ["TVDB_MACHINE"] = "api5.olympic.host0"
    v0 = Config.handler(env0="TVDB_CONFIG", env1="TVDB_MACHINE")
    self.assertIsNotNone(v0)
    url = v0.get("url", env0="TVDB_CONFIG", env1="TVDB_MACHINE")
    self.assertIsNone(url)
    logger.info(f"configHandler: {v0}; url: {url}")

  ## Get a machine URL, keyword
  def test_013(self):
    """
    Netrc - part configured by constructor, completed by get()
    """
    self.assertIsNotNone(weavesId)
    self.envsALT2()
    os.environ["TVDB_CONFIG"]=self._netrc0
    v0 = Config.handler(env0="TVDB_CONFIG")
    self.assertIsNotNone(v0)
    url = v0.get("url", machine="api5.olympic.host0")
    self.assertIsNotNone(v0)
    logger.info(f"configHandler: {v0}; url: {url}")

  def test_015(self):
    """
    This should test env0 and env1 for netrc, but not bothered.
    """
    self.assertIsNotNone(weavesId)
    self.envsALT2()

    os.environ["TVDB_CONFIG"]=self._netrc0
    v0 = Config.handler(env0="TVDB_CONFIG")
    self.assertIsNotNone(v0)
    apikey = v0.get("apikey", machine="api5.olympic.host0")
    self.assertIsNotNone(v0)
    logger.info(f"configHandler: {v0}; apikey: {apikey}")

  def test_017(self):
    """
    This should access my personal configuration: my file in ~/.netrc

    The keywords are cached in the instance when handler is called.
    """
    self.assertIsNotNone(weavesId)
    if "TVDB_CONFIG" in os.environ:
      del os.environ["TVDB_CONFIG"]

    v0 = Config.handler()
    self.assertIsNotNone(v0)
    apikey = v0.get("apikey")
    self.assertIsNotNone(v0)
    logger.info(f"configHandler: {v0}; apikey: {apikey}")


# -*- coding: utf-8 -*-
# Local Variables:
# mode:python
# python-indent-offset: 2
# End:
