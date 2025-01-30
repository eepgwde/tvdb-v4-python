from abc import ABC, abstractmethod

class ConfigHandler(ABC):
    @abstractmethod
    def load_config(self, config_file=None):
        """
        Loads configuration data from the specified file.

        Args:
            config_file (str): Path to the configuration file.

        Returns:
            dict: A dictionary containing the loaded configuration data.
        """
        pass

    @abstractmethod
    def get(self, default0=None, **kwargs):
        return default0

    @abstractmethod
    def defaults(self, defaults0=None):
        return defaults0
