class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = {}
        for i in nums:
            num_count[i] = 1 + num_count.get(i, 0)

        
        arr = []

        for num, cnt in num_count.items():
            arr.append([cnt, num])

        arr.sort()

        res = []

        while len(res) < k:
            res.append(arr.pop()[1])

        return res