class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a={}
        for i in ransomNote:
            a[i]=ransomNote.count(i)
        for j in a:
            if a[j] > magazine.count(j):
                return False
            
        return True