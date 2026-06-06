class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        set_nums = set(range(1,n+1))

        for num in nums:
            set_nums.discard(num)

        return list(set_nums)