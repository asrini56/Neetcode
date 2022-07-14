#49. Group Anagrams, Time/Space - O(n)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = {}
        for s in strs:
            char = [0]*26
            for i in range(len(s)):
                char[ord(s[i]) - 97]+=1
            if tuple(char) not in anagramMap:
                anagramMap[tuple(char)] = []
            anagramMap[tuple(char)].append(s)
        return anagramMap.values()
