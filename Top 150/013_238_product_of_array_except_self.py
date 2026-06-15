class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_no_zero = 1
        zero_ct = 0
        for num in nums:
            if num != 0:
                product_no_zero = product_no_zero * num
            else:
                zero_ct += 1
        if zero_ct >  1:
            return [0] * len(nums)
        if zero_ct == 1:
            return [0 if num !=0 else product_no_zero for num in nums] 
        else:
            return [product_no_zero // num for num in nums]