"""
Lesson:
- Heap is a list data structure can access min-max fast but not to keep the list in order.

Solution:
    1. A min-big and a max-small heap
        - Mechanism is length of both list must be equal
        - Small heap < big heap
        - Accessing max and min of both is only O(1) to create median.  
"""


"use min and max heap"
class MedianFinder:

    def __init__(self):
        self.small_heap = []
        self.big_heap = []

    def addNum(self, num: int) -> None:
        # add into small is default
        heapq.heappush(self.small_heap, -num)
        
        # if small > big:
        if self.small_heap and self.big_heap and (-self.small_heap[0] > self.big_heap[0]):
            value = -heapq.heappop(self.small_heap)
            heapq.heappush(self.big_heap, value)
        
        # if len small < big:
        if len(self.small_heap) + 1 < len(self.big_heap):
            value = heapq.heappop(self.big_heap)
            heapq.heappush(self.small_heap, -value)

        # if len small > big
        if len(self.small_heap) > len(self.big_heap) + 1:
            value = -heapq.heappop(self.small_heap)
            heapq.heappush(self.big_heap, value)

        print(self.small_heap, self.big_heap)        
    def findMedian(self) -> float:
        if len(self.small_heap) > len(self.big_heap):
            return -self.small_heap[0]
        elif len(self.small_heap) < len(self.big_heap):
            return self.big_heap[0]
        else:
            median = (-self.small_heap[0] + self.big_heap[0]) / 2
            return median
        
# Time: O(logN)
# Space: O(N)    