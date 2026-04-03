

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        How to solve:

        How a fleet will be formed ?
        1. A fleet form only when a behind car meet the front car
        2. The behind car needs a faster speed.
        3. They meet before or at the target.

        The method:
            a. With 1 we can solve by sort in descending order for position
                Because we will know which car is infront of which one/
            b. With 2 and 3, we can use knowledge base 
                s = v . t, and to know if they will meet on time we need t
                s = target - position to know the road length

            With a and b we can create the solution,
                If the car behind car have less time to reach target than the front car
                    Then they can form a fleet or else a new fleet appear.

            Using stack to store the fleet.
         """

        #  create pair of position and zip because they always go together
        pair = [(p, s) for p, s in zip(position, speed)]

        # create stack to store the fleet
        stack = deque()

        # sort the pair to know which are the front car
        pair.sort(reverse=True)
        
        for position, speed in pair:
            current_time = (target - position) / speed
            if stack and stack[-1] >= current_time:
                continue
            stack.append(current_time)

        return len(stack)

# Time: O(NLogN)
# Space: O(N)