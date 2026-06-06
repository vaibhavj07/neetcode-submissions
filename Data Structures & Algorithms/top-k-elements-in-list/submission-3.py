class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_nums = {}
        for i in nums:
            count_nums[i] = 1 + count_nums.get(i, 0)
        print(count_nums)
        arr = []

        for i, v in count_nums.items():
            arr.append([v, i])

        arr.sort()

        res = []
        while len(res) < k:
            element_to_append = arr.pop()[1]
            res.append(element_to_append)

        return res


        