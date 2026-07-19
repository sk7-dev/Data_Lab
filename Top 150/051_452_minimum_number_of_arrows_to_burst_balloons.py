class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        sorted_points = sorted(points, key=lambda point: point[1])
        res = 0
        prev_y = float('-inf')
        for (x, y) in sorted_points:
            if x > prev_y:
                res += 1
                prev_y = y
        return res