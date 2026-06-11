class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero_cnt = 0
        for i in nums:
            if i == 0:
                zero_cnt +=1
            else:
                prod*=i
        
        res = [0]*len(nums)

        if zero_cnt > 1:
            return res

        for i, v in enumerate(nums):
            if zero_cnt > 0:
                if v == 0:
                    res[i] = prod
                else:
                    res[i] = 0
            else:
                res[i] = prod//v

        return res