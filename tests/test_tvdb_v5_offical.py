import unittest
import logging

from tvdb_v5_unofficial import __Id__ as weavesId
from tvdb_v5_unofficial import TVDB
from tvdb_v5_unofficial import Config

import json
import os

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
    Test
    """

    N = 6

    url1="http://lydia.host0"

    ## Null setup. Create a new one.
    def setUp(self):
        logger.info('setup')
        return

    ## Null setup.
    def tearDown(self):
        logger.info('tearDown')
        return

    ## Loaded?
    ## Is utf-8 available as a filesystemencoding()
    def test_001(self):
        self.assertIsNotNone(weavesId)
        logger.info("module: Id: " + weavesId)
        return

    ## Defaults
    def test_003(self):
        self.assertIsNotNone(weavesId)
        v0 = Config.defaults()
        self.assertIsNotNone(v0)
        logger.info(f"defaults: {v0}")
        return

    ## Load named local file
    def test_005(self):
        self.assertIsNotNone(weavesId)
        v0 = Config.instance("./config.json")
        self.assertIsNotNone(v0)
        logger.info(f"instance: {v0}")
        return

    ## Get configuration items
    def test_007(self):
        self.assertIsNotNone(weavesId)
        v0 = Config.instance("./config.json").get("url")
        self.assertIsNotNone(v0)
        logger.info(f"url: string:  {v0}")

        v0 = Config.instance("./config.json").get("apikey")
        self.assertIsNotNone(v0)
        logger.info(f"apikey: string:  {v0}")
        return

    ## Get configuration items from environment
    def test_009(self):
        self.assertIsNotNone(weavesId)

        defaults0 = Config.defaults()
        v0 = defaults0.get('env-var-name')
        self.assertIsNotNone(v0)
        logger.info(f"env-var-name {v0}")

        os.environ[v0] = "./config.json"
        
        v0 = Config.instance().get("url")
        self.assertIsNotNone(v0)
        logger.info(f"url: string:  {v0}")

        v0 = Config.instance("./config.json").get("apikey")
        self.assertIsNotNone(v0)
        logger.info(f"apikey: string:  {v0}")
        return


# -*- coding: utf-8 -*-
# Local Variables:
# mode:python
# python-indent-offset: 2
# End:
