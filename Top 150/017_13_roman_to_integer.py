class Solution:
    def romanToInt(self, s: str) -> int:
        d = {"I" : 1, "V" : 5, "X": 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        n = len(s)
        i = 0
        num = 0
        while i < n-1:
            if d[s[i]] < d[s[i+1]]:
                num += d[s[i+1]] - d[s[i]]
                i += 2
            else:
                num += d[s[i]]
                i += 1

        if i == n:
            return num 

        return num + d[s[n-1]]