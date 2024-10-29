#!/usr/bin/env python3
"""LIFOCache module"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO caching system with limit based on BaseCaching.MAX_ITEMS"""

    def __init__(self):
        """Initialize the cache and track the last key"""
        super().__init__()
        self.last_key = None  # Variable to track the most recently added key

    def put(self, key, item):
        """Add an item to the cache with LIFO behavior"""
        if key is not None and item is not None:
            # Add or update the item in the cache
            self.cache_data[key] = item

            # Check if cache exceeds MAX_ITEMS
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # Remove the most recently added item based on LIFO
                discarded_key = self.last_key
                if discarded_key in self.cache_data:
                    del self.cache_data[discarded_key]
                    print(f"DISCARD: {discarded_key}")

            # Update the most recently added key
            self.last_key = key

    def get(self, key):
        """Retrieve an item by key from the cache"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
