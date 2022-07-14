#242. Valid Anagram, Time/Space - O(n)
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCounter = Counter(s)
        tCounter = Counter(t)
        if sCounter == tCounter:
            return True
        return False
