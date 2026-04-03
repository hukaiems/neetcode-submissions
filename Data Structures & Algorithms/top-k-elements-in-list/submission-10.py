class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Optimal solution using bucket sort
        """
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        # now create the bucket sort list ( a list of lists)
        freq = [[] for i in range(len(nums) + 1)]
        # converting phase
        for n, c in count.items():
            freq[c].append(n)
        # now is to take out k element
        res = []
        for index in range(len(freq) - 1, 0, -1): # it will reversed traverse so starting point need to -1
            for n in freq[index]: # a list inside each index
                res.append(n)
                if len(res) == k:
                    return res 

# Time: O(N) delude the sort
# Space: O(N)


        # using a dictionary
        # dic = defaultdict(int)
        # for n in nums:
        #     dic[n] += 1
        
        # arr = []
        # # now create a list( freq, val)
        # for key in dic.keys():
        #     arr.append(( dic[key], key))
        
        # # sorted
        # sorted_arr = sorted(arr, reverse=True)
        # # loop to get the last
        # res = []
        # for i in range(len(sorted_arr)):
        #     res.append(sorted_arr[i][1])
        
        # return res[:k]

# Time: O(NlogN)
# Space: O(M)
