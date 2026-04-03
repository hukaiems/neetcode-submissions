class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # using a dictionary
        dic = defaultdict(int)
        for n in nums:
            dic[n] += 1
        
        arr = []
        # now create a list( freq, val)
        for key in dic.keys():
            arr.append(( dic[key], key))
        
        # sorted
        sorted_arr = sorted(arr, reverse=True)
        # loop to get the last
        res = []
        for i in range(len(sorted_arr)):
            res.append(sorted_arr[i][1])
        
        return res[:k]