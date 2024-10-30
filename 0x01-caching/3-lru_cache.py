#!/usr/bin/env python3
"""LRUCache module"""

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """LRU caching system with limit based on BaseCaching.MAX_ITEMS"""

    def __init__(self):
        """
        Initialize the cache using an OrderedDict to maintain order of use
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item to the cache with LRU behavior"""
        if key is not None and item is not None:
            # If key exists, delete it first to update the order in OrderedDict
            if key in self.cache_data:
                del self.cache_data[key]

            # Add the item to the cache (most recent position)
            self.cache_data[key] = item

            # Check if cache exceeds MAX_ITEMS
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # Pop the first item (least recently used) from the OrderedDict
                oldest_key, _ = self.cache_data.popitem(last=False)
                print(f"DISCARD: {oldest_key}")

    def get(self, key):
        """
        Retrieve an item by key from the cache and update it as recently used
        """
        if key is None or key not in self.cache_data:
            return None
        # Move the key to the end to mark it as recently used
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
