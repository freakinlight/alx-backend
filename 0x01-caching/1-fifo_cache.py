#!/usr/bin/env python3
"""FIFOCache module"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFO caching system with limit based on BaseCaching.MAX_ITEMS"""

    def __init__(self):
        """Initialize the cache and order list"""
        super().__init__()
        self.order = []  # List to track the order of keys

    def put(self, key, item):
        """Add an item to the cache with FIFO behavior"""
        if key is not None and item is not None:
            # Add or update the item in the cache
            self.cache_data[key] = item
            # Track the order of insertion
            if key not in self.order:
                self.order.append(key)
            # Check if cache exceeds MAX_ITEMS
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # Remove the first item in order list and cache
                oldest_key = self.order.pop(0)
                del self.cache_data[oldest_key]
                print(f"DISCARD: {oldest_key}")

    def get(self, key):
        """Retrieve an item by key from the cache"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
