from _Defaults1 import Defaults1

from _Pdb0 import Pdb0

class ConfigHandlerFactory:
    clss = Defaults1().clss

    def _classes0(self, **kwargs):
        clss = self.clss
        if "classes" in kwargs:
            clss = set(kwargs["classes"])
        return clss

    def get_defaults(self, **kwargs):
        """Returns the defaults for each class."""
        r0 = {}
        for cls in self._classes0(**kwargs):
            r0[cls.__name__] = cls.defaults()

        return r0

    def get_defaults_run(self, **kwargs):
        """Returns the runtime defaults that can be used to instantiate."""
        r0 = {}
        for cls in self._classes0(**kwargs):
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
        Pdb0().trap1 = 5
        for cls in self._classes0(**kwargs):
            try:
                # pass a copy just in case they update it
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

        One can restrict the classes to try as handlers, by passing a
        "classes" keyword set to a list of classes to try.

        After that, the initialization process for each class is this:

        It first tries two overrides passed in the keywords.
        
         - env0 an environment variable
         - config_file is a path to a file

        These can be found from the defaults() method for the Config class.

        If env0 is set, it should try and load using that
        
        If config_file is set, the same.

        If neither env0 nor config_file was set, it should try to load using
        the defaults and returns the first one that succeeds.

        The order of the handlers is tried is given by the Config::defaults() 
        """
        return self.try0(**kwargs)
