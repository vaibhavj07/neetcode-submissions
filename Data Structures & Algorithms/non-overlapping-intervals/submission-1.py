class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()  # [[1,2],[2,4],[1,4]] ==> [[1,2],[1,4],[2,4]]
        res = 0
        prevEnd = intervals[0][1] # => prevEnd = 2

        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(end, prevEnd)  #prevEnd = 2
        return res