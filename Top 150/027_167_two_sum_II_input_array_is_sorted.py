class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(numbers, start=1):
            need = target - num
            if need in seen:
                return [seen[need], i]
            seen[num] = i