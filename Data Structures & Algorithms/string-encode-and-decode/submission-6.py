class Solution:

    def encode(self, strs: List[str]) -> str:
        new_str = ""
        for s in strs:
            new_str = new_str + s + 'cutHere'
        
        return new_str

    def decode(self, s: str) -> List[str]:
        new_list = []

        # use split() to split the str base on some condition
        new_list = s.split('cutHere')
        new_list.pop()
        return new_list

# Time: O(N)
# Space: O(N + K)