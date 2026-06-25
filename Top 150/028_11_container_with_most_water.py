class Solution:
    def maxArea(self, height: List[int]) -> int:
        c = 0
        i = 0
        r = len(height)-1
        max_height = max(height)
        while (i < r):
            c = max(c,(min(height[i],height[r])*(r-i)))
            if height[i] < height[r]:
                i+=1
            else:
                r-=1
            if c > max_height * (r-i):
                break
        return c