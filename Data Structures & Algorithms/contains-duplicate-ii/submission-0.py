class Solution:
    def containsNearbyDuplicate(self, nums, k):

        l = 0

        while l < len(nums):
            r = l + 1
            while r < len(nums):
                if nums[l] == nums[r] and abs(l - r) <= k:
                    return True
                r += 1
            l += 1
        return False