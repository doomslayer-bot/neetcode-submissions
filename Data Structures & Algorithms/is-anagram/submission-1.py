class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        return Counter(s) == Counter(t)

        if len(s) != len(t):
            return False

        countS = {}
        countT = {}

        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0)
            countT[t[i]] = countT.get(t[i], 0)

        for c in countS:
            if countS[c] != countS.get(c, 0):
                return False

        return True
            