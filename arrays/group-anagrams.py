from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for words in strs:
            i = "".join(sorted(words))
            d[i].append(words)
        return list(d.values()) 
