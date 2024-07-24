#!/usr/bin/python3
""" BaseCaching module
"""

class BaseCaching():
    """BaseCaching defines:
    - constants of your caching system
    - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """Initialize the BaseCaching instance.
        
        Attributes:
            cache_data (dict): Dictionary to store cache items.
        """
        self.cache_data = {}

    def print_cache(self):
        """Print the current state of the cache.
        
        Prints all key-value pairs in the cache_data dictionary sorted by key.
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """Add an item in the cache.
        
        Args:
            key (str): The key under which the item is stored.
            item (any): The item to be stored in the cache.

        Raises:
            NotImplementedError: If the method is not implemented in the subclass.
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """Get an item by key from the cache.
        
        Args:
            key (str): The key of the item to retrieve.

        Returns:
            any: The value associated with the key in cache_data, or None if the key is not found.

        Raises:
            NotImplementedError: If the method is not implemented in the subclass.
        """
        raise NotImplementedError("get must be implemented in your cache class")
