"""
compare using time
- only behind car can catch front if the time is smaller
1, 2, 3 _ if 2 never catch 1 then will also 3 -> cause 3 will catch 2 and share same speed with 2.

used stack to track fleet, reverse traverse

"""

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # append pair to calculate time
        cars = [[p, s] for p, s in zip(position, speed)]
        cars.sort()
        stack = deque()

        for p, s in cars[::-1]:
            time = (target - p) / s
            stack.append(time)

            if len(stack) > 1 and stack[-1] <= stack[-2]: # form a fleet if t <
                stack.pop()
            # if dont then they will never catch, so no need for while loop

        return len(stack)
# Time: O(N)
# Space: O(N)