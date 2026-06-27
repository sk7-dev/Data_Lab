class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hm = defaultdict(int)
        search_count = len(t)
        for c in t:
            hm[c] += 1
        start = 0
        ans = ""

        for i in range(len(s)):
            hm[s[i]] -= 1
            if hm[s[i]] >= 0:
                search_count -= 1
            if search_count == 0:
                while hm[s[start]] < 0:
                    hm[s[start]] += 1
                    start += 1
                if not ans or i - start + 1 < len(ans):
                    ans = s[start: i + 1]
                search_count += 1
                hm[s[start]] += 1
                start += 1

        return ans