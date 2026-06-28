class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0
        for i, v in enumerate(nums):
            if (v-1) not in seen:
                length = 1
                while v + length in seen:
                    length +=1
                longest = max(length, longest)
        return longest