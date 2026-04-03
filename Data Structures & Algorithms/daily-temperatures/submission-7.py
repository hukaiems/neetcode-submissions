class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        use stack 
        stack keep track of small temp
        if bigger temp -> pop out stack and append in answer untill <= the element in the stack
        """


        stack = deque()
        result = [0] * len(temperatures) # setup 0 for base value

        for i, v in enumerate(temperatures):
            # always append, only compare when stack exist and value > stack[-1]
            while stack and v > stack[-1][1]:
                pop_t = stack.pop()
                result[pop_t[0]] = i - pop_t[0]
            
            stack.append((i, v))

        return result
# Time: O(N)
# Space: O(N)