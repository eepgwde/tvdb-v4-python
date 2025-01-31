import pdb

import threading

class _Defaults:
  trap0s_default = set((1,2,3,4))

class Pdb0():
  """
  This is the new type of singleton.

  Invoked thus: singleton0 = Pdb0()
  No method call.
  """
  # invisible attribute,  set by __new__
  # _instance = None
  _lock = threading.Lock()

  _trap0s = _Defaults.trap0s_default

  # def __new__(cls):
  #   if not hasattr(cls, '_instance'):
  #     cls._instance = super(Pdb0, cls).__new__(cls)
  #   return cls._instance
  
  def __new__(cls, **kwargs):
    if not hasattr(cls, '_instance'):
      o0 = super(Pdb0, cls).__new__(cls, **kwargs)
      cls._instance = o0
      o0.__dict__ = cls._trap0s 

    return cls._instance

  def __init__(self, **kwargs):
    if Pdb0._instance is not None:
      raise RuntimeError("Use the instance() method")
    self._trap0s = set(trap0s)
    Pdb0._instance = self  # Set the cls.instance

  @classmethod
  def instance(cls, **kwargs):
    if not hasattr(cls, '_instance'):
      o0 = super(Pdb0, cls).__new__(cls, **kwargs)
      cls._instance = o0
    return cls._instance

  ## remember to access these by the instance()

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
    if self.trap0 is None:
      return

    if int(value) in self.trap0:
      pdb.set_trace()

# -*- coding: utf-8 -*-
# Local Variables:
# mode:python
# python-indent-offset: 2
# End:
