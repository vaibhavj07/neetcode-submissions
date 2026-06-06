class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        # p1 points to the last REAL number in nums1
        # Ignore the extra 0s at the end
        p1 = m - 1

        # p2 points to the last number in nums2
        p2 = n - 1

        # i points to the last position in nums1
        # This is where we will place the biggest number
        i = m + n - 1

        # Continue until one array is fully processed
        while p1 >= 0 and p2 >= 0:

            # Compare the biggest remaining numbers
            # from both arrays
            if nums1[p1] > nums2[p2]:

                # nums1 value is bigger,
                # so place it at the back
                nums1[i] = nums1[p1]
                # Move nums1 pointer left
                p1 -= 1

            else:

                # nums2 value is bigger (or equal),
                # so place it at the back
                nums1[i] = nums2[p2]

                # Move nums2 pointer left
                p2 -= 1

            # Move the write position left
            # because one position is now filled
            i -= 1

        # If nums2 still has numbers left,
        # copy them into nums1
        # (Remaining nums1 values are already correct)
        while p2 >= 0:

            nums1[i] = nums2[p2]

            p2 -= 1
            i -= 1

        