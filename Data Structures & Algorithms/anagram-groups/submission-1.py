class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # we will use a defaultdict{sorted(tuple): list}. 

        dic = defaultdict(list)
        # a loop to get all result
        for w in strs:
            key = tuple( sorted(list(w)) )
            dic[key].append(w)
        
        res = []
        for l in dic.values():
            res.append(l)

        return res