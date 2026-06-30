class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res = 0
        sol = False
        s= list(s)
        s.sort()
        t = list(t)
        t.sort()
        if s==t:
            sol = True
        return sol

        