"""
Challenge #1:

Write a function that retrieves the last n elements from a list.

Examples:
- last([1, 2, 3, 4, 5], 1) ➞ [5]
- last([4, 3, 9, 9, 7, 6], 3) ➞ [9, 7, 6]
- last([1, 2, 3, 4, 5], 7) ➞ "invalid"
- last([1, 2, 3, 4, 5], 0) ➞ []

Notes:
- Return "invalid" if n exceeds the length of the list.
- Return an empty list if n == 0.
"""

from typing import List

def last(a: List[int], n:int) -> List[int]:
    # Your code here
    #UPER
    # if n is longer than the length of the list
    # should return invalid
    
    # we need to return the last n elements as a list of ints
    # how would we do this if we just need to return the first n elements?
    # we'd want to grab everything starting from index 0 up to n
    # we'd want grab a subslice starts at the beginning of our input list and has length n
    
    # Python's slicing syntax
    # a[0:n] - get first n elements
    # a[] - get last n elements
    # we want to start slicing from len(a) - n and then take everything from there ot the end of the list
    
    # JS/TS
    # a.slice(0, n)
    
    if n > len(a):
        return "invalid"
    
    last_n = a[len(a) - n:]
    return last_n