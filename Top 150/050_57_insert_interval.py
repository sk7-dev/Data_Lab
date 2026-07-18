class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        n_s, n_e = newInterval
        i = 0
        n = len(intervals)
        while i < n and intervals[i][1] < n_s:
            ans.append(intervals[i])
            i += 1
        while i < n and intervals[i][0] <= n_e:
            n_s = min(intervals[i][0], n_s)
            n_e = max(intervals[i][1], n_e)
            i += 1
        ans.append([n_s, n_e])
        while i < n and intervals[i][0] > n_e:
            ans.append(intervals[i])
            i += 1
        return ans