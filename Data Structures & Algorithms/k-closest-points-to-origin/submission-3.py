"""
Lesson:
- Heapify only take O(N) complexity.

Solution:
    1. Min heap
        - Calculate distance and append
        - Then heapify
        - Now take out K elements.
"""

"Sorting solution"
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda p: p[0]**2 + p[1]**2)
        return points[:k]

"Min heap solution"
# class Solution:
#     def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

#         res = []
#         min_heap = []
#         # calculate distance
#         for p in points:
#             distance = math.sqrt( (p[0])**2 + (p[1])**2 )
#             min_heap.append([distance, p])
        
#         heapq.heapify(min_heap)

#         for i in range(k):
#             distance, point = heapq.heappop(min_heap)
#             res.append(point)
        
#         return res

# Time: O(k logN)
# Space: O(N)