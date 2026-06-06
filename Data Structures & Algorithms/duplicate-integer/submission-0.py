class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unqiue = set(nums)
        if len(nums) != len(unqiue):
            return True
        return False