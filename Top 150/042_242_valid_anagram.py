class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char = set(s)
        for i in char:
            if s.count(i) != t.count(i):
                return False

        return True