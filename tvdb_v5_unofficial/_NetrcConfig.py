import netrc
import os
import sys

from ._Defaults0 import Defaults0
from ._Pdb0 import Pdb0

from operator import itemgetter 

from ._ConfigHandler import ConfigHandler

class NetrcConfigHandler(ConfigHandler):
    netrc0 = None

    ## Dictionary algebra is very good for configurations.
    #
    # The upsert operator x | y updates x with matching keys in y.
    # {} | d0 is {} | d0 ie, return d0
    # so: latest = old | new
    # Make a copy of the these defaults0.
    # On initialization, do any updates because HOME is different.
    # Then take a copy of the defaults0 and start collecting kwargs.
    # Not use of ~ and not os.environ["HOME"]"
    # This allows the the HOME directory to be changed
    # whilst running.
    # To to do that, you need to call defaults().
    defaults0 = {
        "name": ".netrc",
        "env0": "NETRC",
        "env1": "NETRC_MACHINE",
        "config_dir": "~",
        "machine": Defaults0().host0,
        "url_path": "/v4/"
    }

    kwargs = {}

    def _mkname(self):
        """
        Update the defaults from within the ctr.
        """
        config_file_path = os.path.join(
            os.path.expanduser(
                self.defaults0["config_dir"]
            ),
            self.defaults0["name"])
        self.defaults0["config_file"] = config_file_path
        return config_file_path

    def __init__(self, **kwargs):
        """Initialize a handler.

        If defaults0 is passed as a keyword, it will not load a config file,
        but just call _mkname to update the defaults0 dictionary.
        This is the only time load_config() is called.
        The kwargs are captured for use in the build.
        Just in case a machine name has been passed in.
        That function then accumulates any keywords passed.
        """
        # For defaults(), update defaults and return
        if "defaults0" in kwargs:
            self._mkname()
            return
        # use a copy of the defaults() now.
        # delete the environment variables
        self.kwargs = self.get_default(**kwargs) | kwargs
        # this will now upsert new kwargs.
        self._config = self._load_config(**self.kwargs)

    @classmethod
    def get_default(cls, **kwargs):
        """
        The runtime defaults, a subset of defaults0. When they construct they only need these.

        No environment variables, just try the defaults and accessories.
        This uses itemgetter. It is a curried operator. 
        """
        Pdb0().trap1 = 7
        k0s = [ "config_file", "machine", "url_path" ]
        v0s = itemgetter(*k0s)(cls.defaults0.copy())
        return dict(zip(k0s, v0s))


    def _load_config(self, **kwargs0):
        """
        load from the env0 first, else try the default.

        Throws exceptions if there are failures.
        """
        # this will now upsert new kwargs.
        kwargs = self.kwargs | kwargs0
        Pdb0().trap1 = 5

        if "env0" in kwargs: # look it up and put it in keywords
            f0 = os.environ.get(kwargs["env0"], None)
            if f0 is None:
                raise NameError(f"No environment variable for env0: {kwargs["env0"]}")
            kwargs["config_file"] = f0

        # we started with defaults on construction.
        assert "config_file" in kwargs, "Netrc no config_file in keywords"

        kwargs1 = self.tag0(kwargs["config_file"], "netrc") | kwargs
        if not self._hasTyper(kwargs1):
            raise NameError(f"Not a netrc file: {kwargs1["config_file"]}")
            return None

        self.netrc0 = netrc.netrc(
            kwargs1["config_file"]
        )
        return self.netrc0


    def _host0(self, **kwargs):
        """
        A machine is needed, can be a keyword.
        """
        return kwargs.get("machine", None)

    def _def0(self, **kwargs):
        """
        A machine is needed, can be the default
        """
        return kwargs.get("machine", None)

    def _env0(self, **kwargs):
        """
        A NETRC machine is needed from the environment
        """
        if not "env1" in kwargs:
             return None
        h0 = os.environ.get(kwargs["env1"], None)
        return h0

    def _env00(self, **kwargs):
        """
        A NETRC machine is needed from the environment
        """
        v0 = self.defaults0.get("env1", None)
        assert v0 is not None, "defaults0 has no env1 environment variable name"
        h0 = os.environ.get(v0, None)
        return h0

    def _host1(self, **kwargs):
        """
        Priority is from kwargs and then environment using keyword env1
        Then from environment using defaults0:env1
        """
        h0 = self._host0(**kwargs)
        if h0 is None:
            h0 = self._env0(**kwargs)
        if h0 is None:
            h0 = self._env00(**kwargs)
        return h0

    def getURL(self, **kwargs):
        Pdb0().trap1 = 7
        return f'http://{kwargs["machine"]}{kwargs["url_path"]}'

    def get(self, key, default0=None, **kwargs0):
        """
        From the netrc file apply some transformations.

        URL has to be manufactured. That is in an override function now.
        """

        # rightmost has priority, the kwargs is local
        # this contains the defaults
        kwargs = self.kwargs | kwargs0

        # lookup the machine
        h0 = self._host1(**kwargs) # keywords, envs, default
        if h0 is None:
            return default0

        kwargs["machine"]=h0
        if key == "url":
            return self.getURL(**kwargs)

        # login, account, password

        a1 = self.netrc0.authenticators(kwargs["machine"])
        if a1 is None:
            return default0

        if key == "user":
            return a1[0] # the login is usually a e-mail or user-name

        if key == "apikey":
            return a1[1] # the account is used for the API key

        if key == "pin": 
            return a1[2] # the password is usually blank

        return default0

    @classmethod
    def defaults(cls, **kwargs):
        if not "defaults0" in kwargs:
            kwargs["defaults0"]=None

        v0 = NetrcConfigHandler(**kwargs)
        return v0.defaults0
