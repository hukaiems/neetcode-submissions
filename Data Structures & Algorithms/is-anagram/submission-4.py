class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # base case
        if len(s) != len(t):
            return False
        # first way using dict to compare
        s_dict, t_dict = {}, {}

        for c in s:
            s_dict[c] = s_dict.get(c, 0) + 1
        for t in t:
            t_dict[t] = t_dict.get(t, 0) + 1
        
        if (s_dict != t_dict):
            return False
        print(s_dict, t_dict)
        return True