class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp = prices[0]
        maxp = prices[0]
        g = 0
        for p in prices:
            if p > maxp:
                maxp = p
                g = max(g, maxp-minp)
            if p<minp:
                minp = p
                maxp = p
        return g