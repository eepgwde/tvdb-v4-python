from _JsonConfig import JsonConfigHandler
from _NetrcConfig import NetrcConfigHandler

import pdb

class ConfigHandlerFactory:
    clss = (NetrcConfigHandler, JsonConfigHandler)

    def get_defaults(self, **kwargs):
        """Returns the defaults for each class."""
        r0 = {}
        for cls in self.clss:
            r0[cls.__name__] = cls.defaults()

        return r0

    def try0(self, **kwargs):
        for cls in self.clss:
            try:
                instance = cls(**kwargs) 
                return instance
            except Exception as e:
                print(f"Failed to create instance of {cls.__name__}: {e}")
                continue
        # end of loop
        return None

    def get_handler(self, **kwargs):
        """Returns the appropriate config handler based on keywords

        It first tries two overrides passed in the keywords.
        
         - env0 an environment variable
         - config_file is a path to a file

        These can be found from the defaults() method for the Config class.

        If env0 is set, try and load using that, and return None if
        it fails.
        
        If config_file is set, try and load using that and return None
        if it fails.

        If neither env0 nor config_file was set, it tries to load using
        the defaults and returns the first one that succeeds.

        The order that is tried is given by the Config::defaults() 
        """
        v0 = None
        if "env0" in kwargs:
            return self.try0(env0=kwargs["env0"])
        if "config_file" in kwargs:
            return self.try0(config_file=kwargs["config_file"])
        v0 = self.try0(kwargs)
        if v0 is None:
            raise Exception("Failed to create a config handler.")
        return v0
