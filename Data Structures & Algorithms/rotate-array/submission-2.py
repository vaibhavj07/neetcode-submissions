class Solution:
    def rotate(self, nums, k):
        k = k % len(nums)   # handles k bigger than array length

        nums[:] = nums[-k:] + nums[:-k]