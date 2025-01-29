import unittest
import logging

from tvdb_v5_unofficial import __Id__ as weavesId
from tvdb_v5_unofficial import TVDB
from tvdb_v5_unofficial import Config

import json

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


# -*- coding: utf-8 -*-
# Local Variables:
# mode:python
# python-indent-offset: 2
# End:
