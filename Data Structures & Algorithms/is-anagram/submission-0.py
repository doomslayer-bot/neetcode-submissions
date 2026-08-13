class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        return Counter(s) == Counter(t)

        if len(s) != len(t):
            return False

        countT ={}
        countS = {}

        for i in range(len(s)):
            count[s[i]] = 1 + count.get(s[i], 0)
            count[t[i]] = 1 + count.get(t[i], 0)

        for c in countS:
            countS[c] != countT.get([c], 0)
            return False

        return True