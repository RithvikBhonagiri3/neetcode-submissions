class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res = 0
        sol = False
        s= list(s)
        t = list(t)
        if len(s) != len(t):
            return sol
        else:
            for letter in s:
                if letter in t:
                    t.remove(letter)
                else:
                    res = res+1

            if res ==0:
                sol = True
            return sol

        