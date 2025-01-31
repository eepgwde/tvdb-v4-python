## weaves
# Defaults file

class Defaults0:

  ## Pdb0

  _trap0s = set((1,2,3,4))

  @property
  def trap0s(self):
    """
    Use a property to perform a set clone.
    """
    return self._trap0s.copy()

  ## NetrcConfigHandler
  _tvdb_host = "api4.thetvdb.com"

  @property
  def host0(self):
    """
    Use a property to perform a string clone.
    """
    return ''.join(self._tvdb_host)


# -*- coding: utf-8 -*-
# Local Variables:
# mode:python
# python-indent-offset: 2
# End:
