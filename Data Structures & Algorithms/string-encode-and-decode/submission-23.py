class Solution:
    "correct way to by pass all the encoding sign"
    # need a way to read all number cause we have many numbers
    # append the number of the word before it
    def encode(self, strs: List[str]) -> str:
        enc_s = ''
        for s in strs:
            enc_s += str(len(s)) + '#'+ s
        # print(enc_s)
        return enc_s
    def decode(self, s: str) -> List[str]:
        # need a way to read all numbers
        res = []
        index = 0
        while index < len(s):
            # convert into int
            num = ''
            while s[index] != '#':
                num += s[index]
                index += 1
            
            length = int(num)
            index += 1
            temp = ""
            for j in range(index, index + length): # take out number base on the length
                temp += s[j]
                # print(temp)
            res.append(temp)
            index += length
        
        # print(res)
        return res
        



    "easy way using a weird long encode"
    # def encode(self, strs: List[str]) -> str:
    #     if len(strs) == 0:
    #         return "nothing"
    #     en_s = "!!!!".join(strs)
    #     return en_s
    # def decode(self, s: str) -> List[str]:
    #     if s == 'nothing':
    #         return []
    #     res = s.split('!!!!')
    #     return res
# Time: O(N)
# Space: O(N)