#!/usr/bin/env python3
"""
Script to merge any number of dictionaries and sort the merged dictionary by values
"""
# Standard library imports
from collections import defaultdict, Counter


def merge_with_defaultdict(*dicts: dict) -> dict:
    """
    Merge multiple dictionaries using defaultdict.

    :param dicts: Variable number of dictionaries to merge
    :return: A new dictionary with merged key-value pairs
    """
    # Initialize a defaultdict with int as the default value
    merged = defaultdict(int)
    
    # Merge the dictionaries
    for d in dicts:
        for key, value in d.items():
            merged[key] += value
    
    # Convert defaultdict to regular dict and sort by value (descending), then by key
    result = dict(sorted(merged.items(), key=lambda x: (-x[1], x[0])))    
    return result


def merge_with_counter(*dicts: dict) -> dict:
    """
    Merge any number of dictionaries and sort the merged dictionary by values

    :param dicts: A tuple of dictionaries to merge
    :return: A dictionary with the merged values sorted by values
    """
    # Initialize a Counter object
    merged = Counter()

    # Merge the dictionaries
    for d in dicts:
        merged.update(d)
    
    # Convert Counter to regular dict and sort by value (descending), then by key
    result = dict(sorted(merged.items(), key=lambda x: (-x[1], x[0])))
    return result
