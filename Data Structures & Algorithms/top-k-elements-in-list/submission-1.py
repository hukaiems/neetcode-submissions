from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # first -> dict
        count_hash = defaultdict(int)

        for n in nums:
            count_hash[n] += 1
        
        arr = list()
        for key, v in count_hash.items():
            arr.append((v, key))
        
        sorted_arr = sorted(arr, reverse=True)

        res = []
        for i in range(k):
            res.append(sorted_arr[i][1])

        return res