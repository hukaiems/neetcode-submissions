class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        This problem solves by monotonic decreasing means only decrease
        - if the next day has smaller temp then append to stack
        - Until there is a bigger temp the stack will always be decreasing
        - If there is bigger temp then pop out every temp that smaller
        - Default temp is 0 so initilize 0 from the start
        - Stack can store multiple vals like tuple, list,  etc
        - res[index] this is use for updating
        """

        stack = deque()
        res = [0] * len(temperatures)

        # use a for loop to traverse through the list
        for i, tem in enumerate(temperatures):
            # if the tem is smaller pop out the previous day
            while stack and stack[-1][0] < tem:
                t_stack , index_stack = stack.pop()
                # after pop cal the diff num for the result
                res[index_stack] = i - index_stack
            stack.append((tem, i))

        return res

# Time: O(N) the inner while loop only run once or twice 
# if the decreasing is super long then it still run once
# Space: O(N)

