"""
Lesson:
- Heap can store many values which help to generalize its usage.
- Counter is a built in function that store counted value in a dict.
- Dict has many listing methods: items() for pairs, keys() and values() like its name mean.

Solution:
    1. Use a max heap + a deque to  store and push back the tasks.

"""


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # the hash counter
        task_hash = Counter(tasks) # O(N)
        task_heap = [-t for t in task_hash.values()]  # O(N)
        heapq.heapify(task_heap) # O(N)

        # deque
        q = deque()
        time = 0
        
        # the while loop to process tasks
        while task_heap or q: # O(N)
            time += 1 # time always run
            # check heap
            if task_heap:
                t = 1 + heapq.heappop(task_heap)   # O(log 26)
                if t: # deque appended task with ready time
                    q.append([t, time + n])
            
            # check q
            if q and q[0][1] == time: #fifo
                heapq.heappush(task_heap, q.popleft()[0]) # O(log 26)
        

        return time
# Time: O(N)
# Space: O(N)