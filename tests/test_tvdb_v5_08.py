import unittest
import logging

from tvdb_v5_unofficial import __Id__ as weavesId
from tvdb_v5_unofficial import TVDB
from tvdb_v5_unofficial import Config

from _ConfigHandler import ConfigHandler
from _JsonConfig import JsonConfigHandler
from _NetrcConfig import NetrcConfigHandler

import json
import os

from _Pdb0 import Pdb0

VALID_API_KEY = "valid_api_key"
VALID_PIN = "valid_pin"

logging.basicConfig(filename='test.log', level=logging.DEBUG)
logger = logging.getLogger('Test')
sh = logging.StreamHandler()
logger.addHandler(sh)

## A test driver for GMus0
#
# @see GMus0
class Test8(unittest.TestCase):
  """
  Test the Config object for handler0 

  Use Config to Construct a handler, check it works, is stored in handler0
  Has a testable supertype and so on.

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

    Without changing HOME, it may find your ~/.netrc, so this test changes HOME to TMPDIR.

    But, you may have to clear the environment if you default assignments to the env0 in defaults().

    If it is too difficult, you can disable the test altogeter expected failure - called config a in the source code comments."""
    self.assertIsNotNone(weavesId)

    home0 = os.environ["HOME"]
    os.environ["HOME"] = os.environ["TMPDIR"]

    # Pdb0().trap0 = 6
    ## not a - comment this if you use config a
    with self.assertRaisesRegex(
        ValueError, "no configuration: .+"
      ):
      v0 = Config.handler()

    Pdb0().reset0()
    os.environ["HOME"] = home0

    ## a
    # v0 = Config.handler()

  def test_009(self):
    """
    Check handler0 can
    """
    self.assertIsNotNone(weavesId)

    c0 = Config.instance()

    # Pdb0().trap0 = 5
    v0 = Config.handler()
    self.assertIsNotNone(v0)

    v1 = c0.handler0()
    self.assertIsNotNone(v1)

    self.assertEqual(v0, v1)

    v2 = v0.defaults()
    self.assertIsNotNone(v2)

    v3 = v2.get("config_file")
    self.assertIsNotNone(v2)

    b4 = v0._hasTyper({"config_file": v3, "config_type": "netrc"})
    self.assertTrue(b4)

    self.assertTrue(issubclass(v0.__class__, ConfigHandler))
    self.assertTrue(isinstance(v0, ConfigHandler))

  # @unittest.skip("Not yet")
  def test_011(self):
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

  def test_013(self):
    """
    How to force a handler: netrc
    """
    # force netrc
    r0 = Config.instance().factory.get_defaults_run(key0="netrc")
    self.assertIsNotNone(r0)
    logger.info(f"get_defaults_run: {r0}")

    h0 = Config.handler(**r0)
    self.assertIsNotNone(h0)
    logger.info(f"handler: netrc: {h0.__class__.__name__}")
    self.assertTrue(isinstance(h0, NetrcConfigHandler))

  def test_015(self):
    """
    How to force a handler: json
    """
    # force netrc
    r0 = Config.instance().factory.get_defaults_run(key0="json")
    self.assertIsNotNone(r0)
    logger.info(f"get_defaults_run: {r0}")

    logger.info(f"config_file: {r0["config_file"]}")

    r0["config_file"] = "./config.json"

    # Pdb0().trap0 = 5
    h0 = Config.handler(**r0)
    self.assertIsNotNone(h0)
    logger.info(f"handler: json: {h0.__class__.__name__}")
    self.assertTrue(isinstance(h0, JsonConfigHandler))

    
  def test_017(self):
    v0 = Config.instance().handler0()
    self.assertIsNotNone(v0)
    logger.info(f"handler: json: {v0.__class__.__name__}")
    self.assertTrue(isinstance(v0, JsonConfigHandler))

    v1 = v0.get("apikey")
    self.assertIsNotNone(v1)
    logger.info(f"apikey: string: {v1}")
    v1 = v0.get("url")
    self.assertIsNotNone(v1)
    logger.info(f"url: string: {v1}")

  def test_019(self):
    # force netrc
    r0 = Config.instance().factory.get_defaults_run(key0="netrc")
    self.assertIsNotNone(r0)

    # Pdb0().trap0 = 5
    v0 = Config.handler(**r0)
    self.assertIsNotNone(v0)
    logger.info(f"handler: netrc: {v0.__class__.__name__}")

    self.assertTrue(isinstance(v0, NetrcConfigHandler))

    v1 = v0.get("apikey")
    self.assertIsNotNone(v1)
    logger.info(f"apikey: string: {v1}")
    v1 = v0.get("url")
    self.assertIsNotNone(v1)
    logger.info(f"url: string: {v1}")

  @unittest.skip
  def test_021(self):
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


# -*- coding: utf-8 -*-
# Local Variables:
# mode:python
# python-indent-offset: 2
# End:
