import netrc
import os
import sys

import pdb

from _ConfigHandler import ConfigHandler

class NetrcConfigHandler(ConfigHandler):
    netrc0 = None

    defaults0 = {
        "name": ".netrc",
        "env0": "NETRC",
        "env1": "NETRC_MACHINE",
        "config_dir": os.path.expanduser("~")
    }

    kwargs = {}

    def _mkname(self):
        config_file_path = os.path.join(
            self.defaults0["config_dir"],
            self.defaults0["name"])
        self.defaults0["config_file"] = config_file_path
        return config_file_path

    def __init__(self, **kwargs):
        """Initialize a handler.

        If defaults0 is passed as a keyword, it will not load a config file,
        but just call _mkname to update the defaults0 dictionary.
        """
        self._mkname()
        self.kwargs = kwargs
        if "defaults0" in kwargs:
            return
        self.load_config(**kwargs)


    def load_config(self, **kwargs):
        """
        load from the env0 first, else try the default.

        Throws exceptions if there are failures.
        """
        if "env0" in kwargs:
            f0 = os.environ.get(kwargs["env0"], None)
            if f0 is None:
                raise NameError(f"No environment variable for env0: {kwargs["env0"]}")
            self.netrc0 = netrc.netrc(f0)
            return self.netrc0

        self.netrc0 = netrc.netrc()
        return self.netrc0

    def _host0(self, **kwargs):
        """
        A machine is needed, can be a keyword.
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

    def _host1(self, **kwargs):
        """
        Priority is from kwargs and then environment.
        """
        h0 = self._host0(**kwargs)
        if h0 is None:
            h0 = self._env0(**kwargs)
        return h0

    def get(self, key, default0=None, **kwargs):

        kwargs = kwargs | self.kwargs

        if key == "url":
            h0 = self._host1(**kwargs)
            if h0 is None:
                return default0
            return f"http://{h0}/"

        # login, account, password

        h0 = self._host1(**kwargs)
        if h0 is None:
            return default0
        a1 = self.netrc0.authenticators(h0)
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
    def defaults(cls, defaults0=None):
        v0 = NetrcConfigHandler()
        return v0.defaults0
