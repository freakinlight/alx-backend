#!/usr/bin/env python3
"""
MRUCache module that implements a caching system with
the Most Recently Used (MRU) algorithm.
"""

from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """MRU caching system with limit based on BaseCaching.MAX_ITEMS"""

    def __init__(self):
        """Initialize the cache using an OrderedDict to maintain usage order"""
        super().__init__()
        self.cache_data = OrderedDict()  # Keeps track of the usage order

    def put(self, key, item):
        """Add an item to the cache with MRU behavior"""
        if key is not None and item is not None:
            # If key exists, delete it first to update the order in OrderedDict
            if key in self.cache_data:
                del self.cache_data[key]

            # Add the item to the cache (most recent position)
            self.cache_data[key] = item

            # Check if cache exceeds MAX_ITEMS
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # Pop the last item (most recently used) from the OrderedDict
                most_recent_key, _ = self.cache_data.popitem(last=True)
                print(f"DISCARD: {most_recent_key}")

    def get(self, key):
        """
        Retrieve an item by key from cache and update it as most recently used
        """
        if key is None or key not in self.cache_data:
            return None
        # Move the key to the end to mark it as most recently used
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
