"""
Lesson:
- Heap has O(logN) for push, pop - O(N) for heapify and O(NlogN) for heap sort.
"""

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        self.heap = nums

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        return self.heap[0]

# Time: O( m * logk) m: adding time
# Space: O(k) for the heap 