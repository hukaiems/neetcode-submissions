class Solution:

    def encode(self, strs: List[str]) -> str:
        divider = '?>?>>?>'
        decoded_str = []
        for s in strs:
            decoded_str.append(s)
            decoded_str.append(divider)
        
        return "".join(decoded_str)

    def decode(self, s: str) -> List[str]:
        divider = '?>?>>?>'
        res = s.split(divider)
        return res[:-1]