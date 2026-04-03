from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # every anagram will have same letter and can be the key to search in hashmap
        # a defaultdict can auto matically initilize an empty list for us.
        anagram_hash = defaultdict(list)
        answer = []

        # How cause they have different order, python can sort the character in alphabet order to be the key

        for char in strs:
            # one more thing that hash is immutable so things like list has to be changed type.
            sorted_char = tuple(sorted(char))
            anagram_hash[sorted_char].append(char)

        # a for loop to iterate and take key value out of the hashmap
        for value in anagram_hash.values():
            answer.append(value)
        
        return answer

# Time O(n)
# Space O(n^2)