#!/usr/bin/env python3
"""BasicCache module"""

from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """Basic caching system with no limit on cache size"""

    def put(self, key, item):
        """Add an item in the cache with the specified key"""
        if key is not None and item is not None:
            self.cache_data[key] = item  # Add or update the cache with the key-value pair

    def get(self, key):
        """Retrieve an item by key from the cache"""
        if key is None or key not in self.cache_data:
            return None  # Return None if key is None or not in the cache
        return self.cache_data[key]  # Return the value associated with the key
