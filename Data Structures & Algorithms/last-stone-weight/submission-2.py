"""
Lesson: 
- Reverse value in a list to heapify it becomes max heap.
"""

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        # while loop
        while len(stones) > 1:
            bigger = - heapq.heappop(stones)
            big = - heapq.heappop(stones)
            res = bigger - big
            if res > 0:
                heapq.heappush(stones, -res)
        
        return -stones[0] if stones else 0