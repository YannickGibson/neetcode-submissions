class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # Sort by start index
        intervals.sort(key=lambda tpl: tpl[0])

        # Merge intervals
        res = [intervals[0]]
        for start, end in intervals:
            curr_end = res[-1][1]
            if start <= curr_end:
                # Merge
                res[-1][1] = max(curr_end, end)
            else:
                # Start new segment
                res.append([start, end])
        return res