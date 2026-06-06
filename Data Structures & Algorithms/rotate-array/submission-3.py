class Solution:
    def rotate(self, nums, k):
        k = k % len(nums)

        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        reverse(0, len(nums) - 1)  # reverse whole array
        reverse(0, k - 1)          # reverse first k part
        reverse(k, len(nums) - 1)  # reverse remaining part