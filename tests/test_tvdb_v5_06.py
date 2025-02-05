import json
import os

import unittest
import logging

from tvdb_v5_unofficial import __Id__ as weavesId
from tvdb_v5_unofficial import TVDB, Config

from tvdb_v5_unofficial import Pdb0
import pdb

from ._Envs0 import Envs0


VALID_API_KEY = "valid_api_key"
VALID_PIN = "valid_pin"

logging.basicConfig(filename='test.log', level=logging.DEBUG)
logger = logging.getLogger('Test')
sh = logging.StreamHandler()
logger.addHandler(sh)

## A test driver for GMus0
#
# @see GMus0
class Test1(unittest.TestCase, Envs0):
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
    Pdb0().disabled0 = False

  ## Null setup.
  def tearDown(self):
    logger.info('tearDown')
    t0 = self.home0
    os.chdir(t0)
    os.environ["HOME"] = t0
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
  @unittest.expectedFailure
  def test_005(self):
    """Should fail with an Exception

    Without changing HOME, it may find your ~/.netrc, so this test changes HOME to TMPDIR.

    But, you may have to clear the environment if you default assignments to the env0 in defaults().

    If it is too difficult, you can disable the test altogeter expected failure - called config a in the source code comments."""
    self.assertIsNotNone(weavesId)

    self.envsTMP()

    # Pdb0().trap0 = 6
    ## not a - comment this if you use config a
    with self.assertRaisesRegex(
        ValueError, "no configuration: .+"
      ):
      v0 = Config.handler()

    # Pdb0().reset0()
    ## a
    # v0 = Config.handler()

  def test_009(self):
    """Get configuration items from a local file
    and cache the handler in the instance.

    The keyword arguments will be cached in the handler
    Avoid by using a JSON file
    """
    self.assertIsNotNone(weavesId)

    f0 = os.path.join(self.pwd1, "config.json")

    self.envsTMP()

    v0 = Config.handler(config_file=f0)
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

    f0 = os.path.join(self.pwd1, "config2.json")
    os.environ["TVDB_CONFIG"] = f0

    v0 = Config.handler(env0="TVDB_CONFIG")

    v1 = v0.get("url")
    self.assertIsNotNone(v1)
    logger.info(f"url: string:  {v1}")

    v1 = v0.get("apikey")
    self.assertIsNotNone(v1)
    logger.info(f"apikey: string:  {v1}")

  def test_015(self):
    """access via an alternative env0

    Avoid the netrc config by changing HOME
    """
    self.assertIsNotNone(weavesId)

    # This doesn't work
    # os.unsetenv(v0)

    # Check if it exists before deleting
    v0 = "CFG0"
    if v0 in os.environ:  
      del os.environ[v0]

    self.assertIsNone(os.environ.get(v0))

    f0 = os.path.join(self.pwd1, "config2.json")
    os.environ[v0] = f0

    self.envsTMP()

    # Pdb0().trap0 = 6
    v0 = Config.handler(env0=v0)
    self.assertIsNotNone(v0)

    v1 = v0.get("url")
    self.assertIsNotNone(v1)
    logger.info(f"url: string:  {v1}")

    v1 = v0.get("apikey")
    self.assertIsNotNone(v1)
    logger.info(f"apikey: string:  {v1}")

    v1 = v0.get("pin")
    self.assertIsNotNone(v1)
    logger.info(f"pin: string:  {v1}")

    v1 = v0.get("ping")
    self.assertIsNone(v1)
    logger.info(f"ping: None:  {v1}")

  def test_017(self):
    """Test the default JSON location.

    This test changes HOME to be the PWD, which is the source directory, and
    there is a .config/ in the source directory and a visible link as a
    reminder.
    """
    self.assertIsNotNone(weavesId)

    self.envsALT()

    os.environ["TVDB_CONFIG"] = "./config.json"

    # Pdb0().trap0 = 5
    v0 = Config.handler(env0="TVDB_CONFIG")
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

  def test_019(self):
    """Test the default NETRC location.

    This test changes HOME to a test directory tests/home1

    It manages to update get a handler by using the default name.
    """
    self.assertIsNotNone(weavesId)

    self.envsALT2()
    Config.defaults()

    # Pdb0().trap0 = 7
    v0 = Config.handler()
    self.assertIsNotNone(v0)

    v1 = v0.get("url")
    self.assertIsNotNone(v1)
    logger.info(f"url: string: {v1}")

    v1 = v0.get("apikey")
    self.assertIsNotNone(v1)
    logger.info(f"apikey: string: {v1}")

    v1 = v0.get("pin")
    self.assertIsNotNone(v1)
    logger.info(f"pin: string: {v1}")

    v1 = v0.get("ping")
    self.assertIsNone(v1)
    logger.info(f"ping: string:  {v1}")

  def test_021(self):
    """Test the default NETRC location.

    This test changes HOME to a test directory.

    It manages to get a handler, then interrogates for the defaults and uses the one it finds.
    """
    self.assertIsNotNone(weavesId)

    # Pdb0().trap0 = 5

    self.envsALT2()

    v0 = Config.handler()
    self.assertIsNotNone(v0)

    v1 = v0.defaults()
    logger.info(f"handler: {v0.__class__.__name__}; defaults: : {v1}")
    self.assertIsNotNone(v1)

    h0 = v1.get("machine", None)
    self.assertIsNotNone(h0)

    v1 = v0.get("url", machine=h0)
    self.assertIsNotNone(v1)
    logger.info(f"url: machine: {h0}; string: {v1}")

    v1 = v0.get("apikey", machine=h0)
    self.assertIsNotNone(v1)
    logger.info(f"apikey: string: {v1}")

    v1 = v0.get("pin", machine=h0)
    self.assertIsNotNone(v1)
    logger.info(f"pin: string: {v1}")

    v1 = v0.get("ping", machine=h0)
    self.assertIsNone(v1)
    logger.info(f"ping: None: {v1}")

  def test_023(self):
    """Test the default NETRC location.

    This test changes HOME to a test directory PWD, which is this file's source directory.

    It manages to get a handler, then interrogates for the default. It then constructs the handler again passing the machine name as a keyword to the Config.handler factory method.
    """
    self.assertIsNotNone(weavesId)

    self.envsALT2()
    v0 = Config.handler()
    self.assertIsNotNone(v0)

    v1 = v0.defaults()
    logger.info(f"handler: {v0.__class__.__name__}; defaults: : {v1}")
    self.assertIsNotNone(v1)

    h0 = v1.get("machine", None)
    self.assertIsNotNone(h0)

    # Once you have the default, rebuild the handler
    # but pass the machine this time.

    v0 = Config.handler(machine=h0)

    v1 = v0.get("url")
    self.assertIsNotNone(v1)
    logger.info(f"url: machine: {h0}; string: {v1}")

    v1 = v0.get("apikey")
    self.assertIsNotNone(v1)
    logger.info(f"apikey: string: {v1}")

    v1 = v0.get("pin")
    self.assertIsNotNone(v1)
    logger.info(f"pin: string: {v1}")

    v1 = v0.get("ping")
    self.assertIsNone(v1)
    logger.info(f"ping: None: {v1}")

  def test_025(self):
    """Test the default NETRC location.

    This test changes HOME to a test directory PWD, which is this file's source directory.

    This uses the environment variable. The default is the name given by env1.
    """
    self.assertIsNotNone(weavesId)

    self.envsALT2()

    v0 = Config.handler()
    self.assertIsNotNone(v0)

    v1 = v0.defaults()
    logger.info(f"handler: {v0.__class__.__name__}; defaults: : {v1}")
    self.assertIsNotNone(v1)

    env1 = v1.get("env1", None)
    self.assertIsNotNone(env1)

    h0 = "api5.olympic.host0"
    os.environ[env1] = h0

    # Once you have the default, rebuild the handler
    # but pass the machine this time.

    v0 = Config.handler()

    v1 = v0.get("url")
    self.assertIsNotNone(v1)
    logger.info(f"url: machine: {h0}; string: {v1}")

    v1 = v0.get("apikey")
    self.assertIsNotNone(v1)
    logger.info(f"apikey: string: {v1}")

    v1 = v0.get("pin")
    self.assertIsNotNone(v1)
    logger.info(f"pin: string: {v1}")

    v1 = v0.get("ping")
    self.assertIsNone(v1)
    logger.info(f"ping: None: {v1}")

# -*- coding: utf-8 -*-
# Local Variables:
# mode:python
# python-indent-offset: 2
# End:
