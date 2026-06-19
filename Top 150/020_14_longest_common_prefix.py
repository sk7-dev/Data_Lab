class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs=sorted(strs)
        n=len(strs)
        first=strs[0]
        last=strs[n-1]
        i=0
        while i< len(first) and i<len(last):
            if first[i]!=last[i]:
                break
            i+=1
        return first[:i]