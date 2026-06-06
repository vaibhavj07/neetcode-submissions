class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        tmp = []

        while l <= r:
            mid = l + (r - l) // 2

            if target < matrix[mid][0]:
                r = mid - 1
            elif target > matrix[mid][-1]:
                l = mid + 1
            else:
                tmp = matrix[mid]
                break

        if not tmp:
            return False

        l1 = 0
        r1 = len(tmp) - 1

        while l1 <= r1:
            mid1 = l1 + (r1 - l1) // 2

            if tmp[mid1] < target:
                l1 = mid1 + 1
            elif tmp[mid1] > target:
                r1 = mid1 - 1
            else:
                return True

        return False