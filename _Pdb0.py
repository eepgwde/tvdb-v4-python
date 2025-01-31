import pdb

import threading

class _Defaults:

  _trap0s = set((1,2,3,4))

  @property
  def trap0s(self):
    return self._trap0s.copy()

class Pdb0():
  """
  This is the new type of singleton.

  Invoked thus: singleton0 = Pdb0()
  No method call.
  """
  # invisible attribute,  set by __new__
  # _instance = None
  _lock = threading.Lock()

  _trap0s = _Defaults().trap0s

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

  def reset0(self, **kwargs):
    if "trap0s" in kwargs:
      self._trap0s = set(kwargs["trap0s"])
      return

    self._trap0s = _Defaults().trap0s

# -*- coding: utf-8 -*-
# Local Variables:
# mode:python
# python-indent-offset: 2
# End:
