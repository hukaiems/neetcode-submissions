class Solution:

    def encode(self, strs: List[str]) -> str:
        new_str = ""
        for s in strs:
            # more optimize is using join in a list 
            # += in string will copy it multiple time making it space consuming.
            # lead to O(N^2)
            new_str += str(len(s)) + '#' + s

        return new_str

    def decode(self, s: str) -> List[str]:
        new_list = []
        i = 0

        while i < len(s):
            j = i

            # given a loop that reach # then stop
            # now with the new j we got a range for the number
            while s[j] != "#":
                j += 1

            # take the length number out
            length = int(s[i:j])
            # append it into list
            new_list.append(s[j+ 1: j + 1 + length])
            # update the index pointer again
            i = j + 1 + length

        return new_list

# Time 
            


            




# solution 1
# use split() to split the str base on some condition
        

# Time: O(N)
# Space: O(N + K)