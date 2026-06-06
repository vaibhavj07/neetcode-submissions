class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_count = {}
        window_count = {}

        for i in range(len(s1)):
            s1_char = s1[i]
            s2_char = s2[i]

            s1_count[s1_char] = s1_count.get(s1_char, 0) + 1
            window_count[s2_char] = window_count.get(s2_char, 0) + 1

        if s1_count == window_count:
            return True

        l = 0

        for r in range(len(s1), len(s2)):
            # add new right character
            new_char = s2[r]
            window_count[new_char] = window_count.get(new_char, 0) + 1

            # remove old left character
            old_char = s2[l]
            window_count[old_char] -= 1

            if window_count[old_char] == 0:
                del window_count[old_char]

            l += 1

            if s1_count == window_count:
                return True

        return False


