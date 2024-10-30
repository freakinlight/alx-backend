#!/usr/bin/env python3
"""
This module defines the LFUCache class which implements a Least Frequently Used
(LFU) caching algorithm, with
a Least Recently Used (LRU) tiebreaker when needed.
"""

from base_caching import BaseCaching
from collections import defaultdict, OrderedDict


class LFUCache(BaseCaching):
    """
    LFUCache inherits from BaseCaching and uses an LFU caching strategy with
    an LRU tiebreaker for items with the same frequency.
    """

    def __init__(self):
        """
        Initialize the cache and auxiliary data structures to track frequency
        of access and order for LRU.
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.frequency = defaultdict(int)

    def put(self, key, item):
        """
        Add/update a cache item. If cache exceeds MAX_ITEMS
        remove the LFU item.
        Tiebreak with LRU if necessary.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data.pop(key)

            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                least_freq = min(self.frequency.values())
                least_used = [
                             k for k, v in self.frequency.items()
                             if v == least_freq
                ]
                if len(least_used) > 1:
                    for k in list(self.cache_data):
                        if k in least_used:
                            self.cache_data.pop(k)
                            self.frequency.pop(k)
                            print(f"DISCARD: {k}")
                            break
                else:
                    lfu_key = least_used[0]
                    self.cache_data.pop(lfu_key)
                    self.frequency.pop(lfu_key)
                    print(f"DISCARD: {lfu_key}")

            self.cache_data[key] = item
            self.frequency[key] += 1

    def get(self, key):
        """
        Retrieve an item by key, increase its frequency
        and adjust its position
        for LRU consideration.
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key)
            self.frequency[key] += 1
            return self.cache_data[key]
        return None
