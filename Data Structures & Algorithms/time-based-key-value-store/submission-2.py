class TimeMap:
    from collections import defaultdict

    def __init__(self):
        self.sorted_timestamps: dict[str, list[int]] = defaultdict(list)
        self.sorted_values: dict[str, str] = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.sorted_timestamps[key].append(timestamp)
        self.sorted_values[key].append(value)
        # O(1)
        
    def _upperbound(self, key, timestamp):

        t = self.sorted_timestamps[key]
        i, j = 0, len(t) - 1

        res = -1
        while i <= j:
            mid = (i + j) // 2
            if t[mid] <= timestamp:  # VALID
                res = mid
                i = mid + 1
            elif t[mid] > timestamp:
                j = mid - 1

        return res

    def get(self, key: str, timestamp: int) -> str:
        # upperbound O(n)
        index = self._upperbound(key, timestamp)
        return self.sorted_values[key][index] if index != -1 else ""
