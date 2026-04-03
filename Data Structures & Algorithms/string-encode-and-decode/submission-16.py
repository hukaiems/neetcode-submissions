class Solution:
    "easy way using a weird long encode"
    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "nothing"
        en_s = "!!!!".join(strs)
        return en_s
    def decode(self, s: str) -> List[str]:
        if s == 'nothing':
            return []
        res = s.split('!!!!')
        return res