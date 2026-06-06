class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            print("num: ", num)
            if (num - 1) not in numSet:
                print("inside if", num)
                length = 1
                print("lenght in if:" , length)
                while (num + length) in numSet:
                    length += 1
                    print("lenght in while:" , length)
                longest = max(length, longest)
                print("longest: ", longest)
        return longest