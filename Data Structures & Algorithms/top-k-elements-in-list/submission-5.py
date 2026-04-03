class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        nums_hash = {}

        answer = []

        for num in nums:
            # .get is for is there key num in the hashmap ?
            # if yes then take the value out for calculation
            # if it isnt then input 0 for it
            nums_hash[num] = 1 + nums_hash.get(num, 0)

        # implement the sort method 
        sorted_hash = dict(sorted(nums_hash.items(), key=lambda item:item[1]))

        
        for key in sorted_hash.keys():
            answer.append(key)

        return answer[-k:]
        
        

