class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i, v in enumerate(stones):
            stones[i] = -v
        heapq.heapify(stones) 

        while len(stones) != 1:
            if stones:
                a = heapq.heappop(stones)
                b = heapq.heappop(stones)

                if b > a:
                    diff = a - b
                    heapq.heappush(stones,diff)
                elif b < a:
                    diff = b - a
                    heapq.heappush(stones,diff)
                else:
                    continue
            else:
                return 0
            
  
        return abs(stones[0])

        