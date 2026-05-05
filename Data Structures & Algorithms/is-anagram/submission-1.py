class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)==len(t):
            s1 = ''.join(sorted(s))
            l1 = ''.join(sorted(t))
            return s1==l1
        return False