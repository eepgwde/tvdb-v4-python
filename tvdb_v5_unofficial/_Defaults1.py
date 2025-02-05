## weaves
# Defaults file

from ._JsonConfig import JsonConfigHandler
from ._NetrcConfig import NetrcConfigHandler

class Defaults1:

  ## ConfigHandlerFactory

  _clss = (JsonConfigHandler, NetrcConfigHandler)

  @property
  def clss(self):
    return self._clss

# -*- coding: utf-8 -*-
# Local Variables:
# mode:python
# python-indent-offset: 2
# End:
