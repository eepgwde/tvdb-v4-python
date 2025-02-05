from abc import ABC, abstractmethod

class ConfigHandler(ABC):

    def tag0(self, config_file, config_type="unknown"):
        return { "config_file" : config_file, "config_type" : config_type }

    def hasType(self, **kwargs):
        if "config_file" in kwargs and "config_type" in kwargs:
            f0 = kwargs["config_file"]
            t0 = kwargs["config_type"]
            return f0.endswith(t0)
        return False

    # set and use indirectly
    _hasTyper = lambda o0, d0: o0.hasType(**d0)

    @abstractmethod
    def get(self, default0=None, **kwargs):
        return default0

    @abstractmethod
    def defaults(self, defaults0=None):
        return defaults0
 
