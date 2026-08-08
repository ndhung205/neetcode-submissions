class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_sort = sorted(s)
        t_sort = sorted(t)
        if s_sort == t_sort:
            return True;
        return False

        # if len(s) != len(t):
        #     return False

        # count = 0
        # for c in s:
        #     if c in t:
        #         count = count + 1

        # if count == len(s):
        #     return True
        # return False
