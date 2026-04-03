class Solution:

    def encode(self, strs: List[str]) -> str:
        new_str = ""
        for s in strs:
            new_str += str(len(s)) + '#' + s

        return new_str

    def decode(self, s: str) -> List[str]:
        new_list = []
        i = 0

        while i < len(s):
            j = i

            # given a loop that reach # then stop
            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])
            new_list.append(s[j+ 1: j + 1 + length])
            i = j + 1 + length

        return new_list
            


            




# solution 1
# use split() to split the str base on some condition
        

# Time: O(N)
# Space: O(N + K)