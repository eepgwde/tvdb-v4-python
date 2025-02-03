import os


class Envs0:
  home0 = os.environ["HOME"]
  pwd0 = os.environ["PWD"]

  home1 = os.path.join(os.environ["PWD"], "tests", "home0")
  pwd1 = os.path.join(os.environ["PWD"], "tests", "home0")

  home2 = os.path.join(os.environ["PWD"], "tests", "home1")
  pwd2 = os.path.join(os.environ["PWD"], "tests", "home1")

  def envsTMP(self):
    t0 = os.environ["TMPDIR"]
    os.chdir(t0)
    os.environ["HOME"] = t0

  def envsALT(self):
    t0 = self.home1
    os.chdir(t0)
    os.environ["HOME"] = t0

  def envsALT2(self):
    t0 = self.home2
    os.chdir(t0)
    os.environ["HOME"] = t0

  ## Null setup. Create a new one.
  def setUp(self):
    logger.info("setup")
    logger.info(f"test: {self._testMethodName}")
    Pdb0().disabled0 = False

  ## Null setup.
  def tearDown(self):
    logger.info("tearDown")
    t0 = self.home0
    os.chdir(t0)
    os.environ["HOME"] = t0
