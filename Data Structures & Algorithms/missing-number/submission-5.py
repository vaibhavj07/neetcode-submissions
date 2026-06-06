class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        if 0 not in nums:
            return 0
        num = 1
        for i in nums:
            if num < len(nums):
                if num not in nums:
                    return num
            num+=1
        return num-1