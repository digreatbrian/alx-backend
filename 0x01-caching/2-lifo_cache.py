#!/usr/bin/env python3
"""Create a class LIFOCache that inherits from
BaseCaching and is a caching system:

You must use self.cache_data - dictionary from
the parent class BaseCaching
You can overload def __init__(self): but don’t
forget to call the parent init: super().__init__()
def put(self, key, item):
Must assign to the dictionary self.cache_data the
item value for the key key.
If key or item is None, this method should not do
anything.
If the number of items in self.cache_data is higher
that BaseCaching.MAX_ITEMS:
you must discard the last item put in cache
(LIFO algorithm)
you must print DISCARD: with the key discarded and
following by a new line
def get(self, key):
Must return the value in self.cache_data linked to key.
If key is None or if the key doesn’t exist in
self.cache_data, return None.
"""

BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFO caching system that inherits from BaseCaching.

    Attributes:
        cache_data (dict): Dictionary inherited from BaseCaching.
    """

    def __init__(self):
        """Initialize the LIFOCache instance and inherit properties from BaseCaching."""
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache.

        Args:
            key (str): The key of the item.
            item (any): The item to be cached.

        If the number of items in self.cache_data exceeds the limit
        specified by BaseCaching.MAX_ITEMS, discard the last item
        added to the cache (LIFO algorithm) and print the discarded key.
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
            # delete the last item in the dictionary
            last_key, last_value = self.cache_data.popitem()
            print("DISCARD: {}".format(last_key))
        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key from the cache.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            any: The value associated with the key in self.cache_data,
            or None if the key is None or does not exist in the cache.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
