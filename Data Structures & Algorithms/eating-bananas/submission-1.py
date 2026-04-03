class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Intuition
        - Koko can only eat 1 pile at a time.
            Try to think about the range of the result k to find:
            - The maximum k is equal to the largest piles[i] value
            - The smallest k is 1 - 1 banana in 1 hour.
        
        Now from that we got a ascending list of k banana per hour.
        From the list we can use binary search because the list is in order.
        Now if the "hours" is smaller than h then it is valid and can be use as a result.

        We can find smaller "hours" by increasing k.
        => Try to find the rule that more banan mean less hours and vice versa.

        At the end the pointer l > r then stop.

        Remember:
        - Don't need to use exactly the base condition to move 2 pointer in binary search algorithm.
        """

        # r pointer will be the maximum pile in the list
        # Because koko can only eat 1 pile at a time so max piles[i] or max k mean fastest.
        l, r = 1, max(piles)
        res = r #the largest valid result is max k.

        while l <= r:
            # floor division to round down
            k = (r + l) // 2
            hours = 0
            # calculate the hour for the chosen k
            for p in piles:
                hours += math.ceil(p / k) #ceil up the number
            
            # the condition for the binary search
            #   dont need to be exactly like the origin it needs to adapt with the problem
            #   different cond same algorithm
            if hours <= h:
                res = min(res, k) # now you can be a valid hours because it smaller to the threshold h
                r = k - 1 # we want to equal threshold h as possible so we eat less banana
            else:
                l = k + 1 # we want to eat more to decrease eating hour
        
        return res

# Time: O(log(max(N) + N))
# Space: O(1)

