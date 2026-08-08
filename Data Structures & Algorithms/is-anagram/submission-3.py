class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s_sort = sorted(s)
        # t_sort = sorted(t)
        # if s_sort == t_sort:
        #     return True;
        # return False

        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT