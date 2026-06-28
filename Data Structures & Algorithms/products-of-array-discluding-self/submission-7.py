class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_cnt = 0
        res = [0]*len(nums)
        prod = 1
        
        for num in nums:
            if num == 0:
                zero_cnt+=1
            else:
                prod*=num

        if zero_cnt > 1:
            return res

        for i, v in enumerate(nums):
            if zero_cnt > 0:
                if v == 0:
                    res[i] = prod
                    return res
            else:
                res[i] = prod//v
        return res
        