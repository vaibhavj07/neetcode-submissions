class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = {}
        for i in nums:
            num_count[i] = 1 + num_count.get(i,0)

        arr = []
        for num,count in num_count.items():
            arr.append([count,num])
        
        arr.sort()

        res = []
        itr = 0
        while itr < k:
            res.append(arr.pop()[1])
            itr+=1
        return res


        