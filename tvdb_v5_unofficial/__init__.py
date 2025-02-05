# -*- coding: utf-8 -*-

# weaves
# What to export to the outside world via the tvdb_v5_unofficial package, so
#  import tvdb_v5_unofficial
# Gives you just these classes

from ._version import __version__, __Id__

# Import the original system as these, suffixed with 0.
from tvdb_v4_unofficial import TVDB as TVDB0, Url as Url0

# For running the system, you need these and hope
# all the defaults work.
from ._Tvdb import TVDB, Url

# Otherwise, you will need to use the Config
# singleton. and its handler() method to pass your own configuration
from ._Config import Config

# You may need to force which handler you use to
# load a configuration, so these are exposed.

from ._NetrcConfig import NetrcConfigHandler
from ._JsonConfig import JsonConfigHandler

# You may want to add your own handler or
# change the _hasTyper lambda.
from ._ConfigHandler import ConfigHandler

# You may want to override or add to the defaults
from ._Defaults0 import Defaults0
from ._Defaults1 import Defaults1

# And you may want to do some debugging
from ._Pdb0 import Pdb0

# Some versioning
from ._version import __version__, __Id__
from tvdb_v5_unofficial import __Id__ as weavesId

__copyright__ = 'Copyright 2024 Walter Eaves'
__license__ = 'GPLv3'
__title__ = 'weaves'

# appease flake8: the imports are purposeful
(__version__)
(__Id__)
