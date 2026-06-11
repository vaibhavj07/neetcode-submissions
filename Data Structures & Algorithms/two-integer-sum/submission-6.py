class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_map = {}
        res = []
        for index, num in enumerate(nums):
            diff = target - num
            if diff in seen_map.keys():
               res.append(seen_map[diff])
               res.append(index)
            seen_map[num] = index
        print(seen_map)
        return res