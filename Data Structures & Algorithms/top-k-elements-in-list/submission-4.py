from collections import Counter, defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Save counts
        curr_counts = Counter(nums)
        bucket = [set() for _ in range(len(nums) + 1)]
        
        # Bucket sort
        for num, occur in curr_counts.items():
            bucket[occur].add(num)

        # Enumerate bucket
        res = []
        for i in range(len(bucket) - 1, -1, -1):
            if bucket[i]:
                for val in bucket[i]:
                    res.append(val)
            if len(res) >= k:
                break
        
        return res
        
        # c = Counter(nums)
        # res = sorted(c.keys(), key=lambda x: c[x])[-k:]
        return res