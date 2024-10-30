#!/usr/bin/env python3
"""LFUCache module"""

from base_caching import BaseCaching
from collections import defaultdict, OrderedDict


class LFUCache(BaseCaching):
    """
    LFU caching system with LRU fallback for ties
    based on BaseCaching.MAX_ITEMS
    """

    def __init__(self):
        """Initialize the cache"""
        super().__init__()
        self.cache_data = OrderedDict()
        self.frequency = defaultdict(int)  # Tracks frequency of keys

    def put(self, key, item):
        if key is not None and item is not None:
            if key in self.cache_data:
                # Update the item and increase frequency
                self.cache_data.pop(key)
                self.frequency[key] += 1
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    # Find the least frequently used item
                    least_freq = min(self.frequency.values())
                    least_used = [
                           k for k, v in self.frequency.items()
                           if v == least_freq
                    ]
                    # Use LRU tie-breaker if necessary
                    if len(least_used) > 1:
                        for k in list(self.cache_data):
                            if k in least_used:
                                self.cache_data.pop(k)
                                self.frequency.pop(k)
                                print(f"DISCARD: {k}")
                                break
                    else:
                        # Only one least frequently used item
                        lfu_key = least_used[0]
                        self.cache_data.pop(lfu_key)
                        self.frequency.pop(lfu_key)
                        print(f"DISCARD: {lfu_key}")

            self.cache_data[key] = item  # Place the item last (MRU)
            self.frequency[key] += 1  # Increment the frequency of access

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        # Move accessed item to end to maintain MRU order
        self.cache_data.move_to_end(key)
        self.frequency[key] += 1  # Increment frequency due to access
        return self.cache_data[key]
