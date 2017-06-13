# The heapq module provides functions for implementing heaps based on regular lists.
# The lowest valued entry is always kept at position zero.
# This is useful for applications which repeatedly access the smallest element
# but do not want to run a full list sort:
from heapq import heapify, heappop, heappush


data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapify(data)                      # rearrange the list into heap order
heappush(data, -5)                 # add a new entry
[heappop(data) for i in range(3)]  # fetch the three smallest entries


#  -----------------

# This module provides support for maintaining a list in sorted order
# without having to sort the list after each insertion.

import bisect

scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
print(scores)
bisect.insort(scores, (300, 'ruby'))
print(scores)
