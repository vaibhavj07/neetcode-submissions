class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_cnt = 0
        res = [0]*len(nums)
        prod = 1
        
        for i, v in enumerate(nums):
            if v == 0:
                zero_cnt +=1
            else:
                prod*=v
        
        if zero_cnt > 1:
            print(zero_cnt)
            return [0]*len(nums)

        for i, v in enumerate(nums):
            if zero_cnt > 0:
                if v == 0:
                    res[i] = prod
                    return res
            else:
                res[i] = prod//v

        return res