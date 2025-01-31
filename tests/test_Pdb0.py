import unittest
import logging
import tempfile

from _Pdb0 import Pdb0
import pdb

import json
import os

logging.basicConfig(filename='test.log', level=logging.DEBUG)
logger = logging.getLogger('Test')
sh = logging.StreamHandler()
logger.addHandler(sh)


def fn1():
  print("fn1")
  Pdb0.instance().trap1 = 5

class Test_Pdb0(unittest.TestCase):
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

  def test_001(self):
    """
    Load by the instance method
    """
    v0 = Pdb0()
    logger.info(f"pdb0: instance: {v0}")
    self.assertIsNotNone(v0)

  def test_003(self):
    logger.info(f"fn1: no trap")
    fn1()
    
  def test_005(self):
    logger.info(f"fn1: no trap, wrong trap")
    Pdb0().trap0 = 2
    fn1()
    
  def test_007(self):
    """
    Now trap on 5
    """
    Pdb0().trap0 = 5
    logger.info(f"fn1: trap")
    fn1()

  def test_011(self):
    """
    Check we have the instance method
    and reset it.
    """
    v0 = Pdb0.instance()
    logger.info(f"pdb0: instance: {v0}")
    self.assertIsNotNone(v0)
    v0.reset0()

  def test_013(self):
    logger.info(f"fn1: no trap")
    fn1()
    
  def test_015(self):
    logger.info(f"fn1: no trap, wrong trap")
    Pdb0.instance().trap0 = 2
    fn1()
    
  def test_017(self):
    """
    Now trap on 5
    """
    Pdb0.instance().trap0 = 5
    logger.info(f"fn1: trap")
    fn1()

  ## Get configuration items from a local file
  @unittest.skip("unimplemented")
  def test_099(self):
    self.assertIsNotNone(weavesId)

    tvdb = TVDB(config_file="./config.json")

    self.assertIsNotNone(tvdb)
    logger.info(f"tvdb: TVDB: {tvdb}")

    v0 = tvdb.search("Lost", language="en", limit=10, type="series")
    fpickle1(v0)

# -*- coding: utf-8 -*-
# Local Variables:
# mode:python
# python-indent-offset: 2
# End:
