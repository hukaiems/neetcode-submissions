class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # use slidingwindow (2 pointers) and a set
        l = 0
        res = 0
        charSet = set()

        for r in range(len(s)):
            # we will use while in
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, len(charSet))

        return res


        # using 2 pointers, a hash_map and a queue

        # # base case
        # if len(s) < 2:
        #     return len(s)

        # # 2 pointers
        # l, r = 0, 1
        # queue = deque()
        # hash_map = defaultdict()
        # # append first val
        # queue.appendleft(s[l])
        # hash_map[s[l]] = l

        # res = 1

        # while r < len(s):
        #     if s[r] not in hash_map:
        #         queue.appendleft(s[r])
        #         hash_map[s[r]] = r
        #         r += 1
        #         res = max(res, len(queue))
        #     else: # meet dup
                
        #         while queue:
        #             pop_val = queue.pop()
        #             if pop_val == s[r]: # found dup
        #                 l = hash_map[pop_val] + 1 # move on 1 index for l
        #                 hash_map.pop(pop_val, None) # just delete it, new loop will add it back in
        #                 break
        #             else:
        #                 hash_map.pop(pop_val, None)

        # return res