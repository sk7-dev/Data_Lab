class Solution:
    def trap(self, height: List[int]) -> int:
        i , j = 0 , len(height)-1
        left = right = 0 
        water = 0

        while i < j:
            if height[i] < height[j]:
                left = max(left , height[i])
                water += left - height[i]
                i += 1
            else:
                right = max(right , height[j])
                water += right - height[j]
                j -= 1
        return water