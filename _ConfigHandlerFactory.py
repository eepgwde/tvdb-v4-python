from _JsonConfig import JsonConfigHandler
from _NetrcConfig import NetrcConfigHandler

import pdb

class ConfigHandlerFactory:
    clss = (JsonConfigHandler, NetrcConfigHandler)

    def get_defaults(self, **kwargs):
        """Returns the defaults for each class."""
        r0 = {}
        for cls in self.clss:
            r0[cls.__name__] = cls.defaults()

        return r0

    def get_defaults_run(self, **kwargs):
        """Returns the runtime defaults that can be used to instantiate."""
        r0 = {}
        for cls in self.clss:
            r0[cls.__name__] = cls.get_default()

        if "key0" in kwargs:
            key0 = kwargs["key0"]
            f0 = lambda x: key0 in x.lower()
            v1 = next(filter(f0, r0.keys()))
            if v1 is None:
                return None
            r0 = r0[v1]

        return r0

    def try0(self, **kwargs):
        for cls in self.clss:
            try:
                kwargs0 = kwargs.copy()
                instance = cls(**kwargs0) 
                return instance
            except Exception as e:
                # print(f"no configuration: failed to create instance of {cls.__name__}: {e}", file=sys.stderr)
                continue
        # end of loop

        raise ValueError(f"no configuration: no classes could instantiate: {self.clss}")

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

        The order of the handlers is tried is given by the Config::defaults() 
        """
        v0 = self.try0(**kwargs)
        return v0
