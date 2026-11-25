class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # Sort by start index
        intervals.sort(key=lambda tpl: tpl[0])

        # Merge intervals
        res = [intervals[0]]
        for start, end in intervals:
            if start <= res[-1][1]:
                # Merge
                res[-1][1] = max(res[-1][1], end)
            else:
                # Start new segment
                res.append([start, end])
        return res