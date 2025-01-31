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

    def get_handler(self, **kwargs):
        """Returns the appropriate config handler based on the file extension."""

        for cls in self.clss:
            try:
                instance = cls(**kwargs) 
                return instance
            except Exception as e:
                print(f"Failed to create instance of {cls.__name__}: {e}")
                continue
        # end of loop
        raise Exception("Failed to create an instance of any class in the list.") 

