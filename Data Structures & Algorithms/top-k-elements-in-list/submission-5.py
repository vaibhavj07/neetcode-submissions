class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for i in nums:
            counts[i] = 1 + counts.get(i, 0)

        arr = []

        for num, count in counts.items():
            arr.append([count,num])

        arr.sort()
        print(arr)

        res = []

        while len(res) < k:
            res.append(arr.pop()[1])
        
        return res



        