from ._Defaults0 import Defaults0

import pdb

class Pdb0():
  """
  This is the new type of singleton.

  Invoked thus: singleton0 = Pdb0()
  No method call.
  """
  # invisible attribute,  set by __new__
  # _instance = None

  _trap0s = Defaults0().trap0s

  _disabled0 = False

  # def __new__(cls):
  #   if not hasattr(cls, '_instance'):
  #     cls._instance = super(Pdb0, cls).__new__(cls)
  #   return cls._instance
  
  def __new__(cls, **kwargs):
    if not hasattr(cls, '_instance'):
      o0 = super(Pdb0, cls).__new__(cls, **kwargs)
      cls._instance = o0
      o0._trap0s = cls._trap0s 

    return cls._instance

  def __init__(self, **kwargs):
    pass

  @classmethod
  def instance(cls, **kwargs):
    if not hasattr(cls, '_instance'):
      o0 = super(Pdb0, cls).__new__(cls, **kwargs)
      cls._instance = o0
      o0._trap0s = cls._trap0s 
    return cls._instance

  ## Beware how invoked
  # Remember to access these by the instance()
  # Or use the newer Pdb0()


  @property
  def disabled0(self):
    return self._disabled0

  @disabled0.setter
  def disabled0(self, value):
    self._disabled0 = bool(value)

  @property
  def trap0(self):
    return self._trap0s

  @trap0.setter
  def trap0(self, value):
    self._trap0s.add(int(value))

  @property
  def trap1(self):
    return self.trap0

  @trap1.setter
  def trap1(self, value):
    """
    When the value is in trap0s it halts under the debugger.

    You need to do a pdb up command to get back to you r code.
    """
    if self.trap0 is None:
      return

    if self.disabled0:
      return 

    if int(value) in self.trap0:
      pdb.set_trace()

  def reset0(self, **kwargs):
    if "trap0s" in kwargs:
      self._trap0s = set(kwargs["trap0s"])
      return

    self._trap0s = Defaults0().trap0s

# -*- coding: utf-8 -*-
# Local Variables:
# mode:python
# python-indent-offset: 2
# End:
