import logging
import threading

class Lockable:
  _instance = None
  _lock = threading.Lock()

  @classmethod
  def __new__(cls):
    with cls._lock:
      if cls._instance is None:
        cls._instance = super().__new__(cls)
      return cls._instance

  def instance(**kwargs):
    return _instance;


# -*- coding: utf-8 -*-
# Local Variables:
# mode:python
# python-indent-offset: 2
# End:
