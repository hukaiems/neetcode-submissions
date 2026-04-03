class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        "Optimal hash solution"

        dic = defaultdict(list)

        for s in strs:
            arr = [0] * 26
            for c in s:
                index = ord(c) - ord('a')
                arr[index] += 1
            dic[tuple(arr)].append(s)

        return list(dic.values())
# Time: O(M * N)
# Space: O(M * N)



        # # we will use a defaultdict{sorted(tuple): list}. 

        # dic = defaultdict(list)
        # # a loop to get all result
        # for w in strs: # O(N)
        #     key = tuple( sorted(list(w)) ) #O(NlogN)
        #     dic[key].append(w)
        
        # res = []
        # for l in dic.values():
        #     res.append(l)

        # return res

# Time: O M * NLogN 
# Space: O(M * N)